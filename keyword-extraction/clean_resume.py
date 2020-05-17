def eliminate_bad_chars (string):
    '''

    Replaces unwanted characters with a space.

    Why a space? imagine you have words seperated by a '/'. This prevents the words from being concatenated end to end.

    The '-' symbols are kept for a similar reason. Conjunction words with '-' typically have different meanings from their components.
    
    '''
    bad_chars = "!@#$%^&*()[]{};:,./<>?\|`~-=_•'"
    for char in bad_chars:
        string = string.replace(char, " ")
    return string

def clean(filename):
    '''

    Clean a text file of certain characters and return a set of the words.

    Returns: list of words

    '''
    with open(filename) as f:
        lines = f.readlines()

    lines_new = []
    for line in lines:
        line = eliminate_bad_chars(line.lower()).strip()
        for word in line.split(" "):
            if word != '':
                lines_new.append(word)

    return list(set(lines_new))