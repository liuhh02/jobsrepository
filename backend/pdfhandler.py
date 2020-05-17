import os
import sys
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar

from collections import Counter

import json

def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    filepath.close()
    device.close()
    retstr.close()
    return text


def getlines(fname):
    # Open a PDF file.
    fp = open(fname, 'rb')
    # Create a PDF parser object associated with the file object.
    parser = PDFParser(fp)
    # Create a PDF document object that stores the document structure.
    # Supply the password for initialization.
    document = PDFDocument(parser, password='')
    # Check if the document allows text extraction. If not, abort.
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    # Create a PDF device object.
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    textlines = []
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        # receive the LTPage object for this page
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox):
                for lines in lt_obj:
                    textlines.append(lines)
            elif isinstance(lt_obj, LTTextLine):
                textlines.append(lt_obj)
    textdict = {}
    for i, value in enumerate(textlines):
        textdict[i] = textline(value)
    return textdict


class textline():
    def __init__(self, line):
        self.og = line
        self.totalchars = 0
        total_characters = 0
        totalsize = 0
        self.string = ""
        fontlist = []
        for pos, char in enumerate(line):
            if isinstance(char, LTChar):
                totalsize += char.fontsize
                self.totalchars += 1
                fontlist.append(char.fontname)
            total_characters += 1
            self.string += char.get_text()
        self.avgsize = round((totalsize / total_characters)*2)/2
        newstr = self.string.replace("\n", " ").encode('utf-8').replace(b'\xe2\x80\x8b', b" ").decode('utf-8')
        if newstr.isspace():
            self.string = False
        else:
            self.string = newstr
        self.font = max(fontlist, key=Counter(fontlist).get)

def sections(fname):
    lines = getlines(fname)
    sorted = {}
    cpar = 0
    for branch, line in lines.items():
        if line.string is not False:
            if 'bold' in line.font.lower():
                try:
                    if line.avgsize >= sorted[cpar][0].avgsize:
                        sorted[branch] = [line, []]
                        cpar = branch
                    else:
                        sorted[cpar][1].append({branch: line})
                except KeyError:
                    sorted[branch] = [line, []]
                    cpar = branch
    return sorted, printable(sorted)

def printable(lst):
    prntable = {}
    for key, value in lst.items():
        if isinstance(value, list):
            newlist = []
            for i in value:
                if isinstance(i, textline):
                    newlist.append(i.string)
                else:
                    for x in i:
                        print(x)
                        newlist.append(printable(x))
            prntable[key] = newlist
        else:
            prntable[key] = value.string
    return prntable

def gettxt(fname):
    full, pretty = sections(fname)
    text_output = pdf_to_text(fname)
    text1_output = text_output.decode("utf-8")
    return json.dumps(pretty, indent=4)