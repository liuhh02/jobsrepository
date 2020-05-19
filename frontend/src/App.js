import React, { Component } from 'react';
import logo from './assets/logo.png';
import wave from './assets/wave.png';
import arrow from './assets/arrow.png';
import './App.css';
import Dropzone from 'react-dropzone';
import { Container, InputGroup, FormControl, Button, Table, Form } from 'react-bootstrap';
import { Document, Page } from 'react-pdf';
import PDFViewer from 'pdf-viewer-reactjs';

class App extends Component {

  state = {
    file: '',
    selected: 'None',
    pdf: '',
    submit: false,
    jobs: []
  }

  processPdf = () => {
    const file = this.state.file
    const form = new FormData()
    form.append('file', file, file.name)
    console.log(form.entries())
    this.setState({ submit: 'loading' })
    fetch('https://resumatch.andrechek.com/upload', {
      method: 'POST',
      body: form
    })
    .then(res => res.json())
    .then(res => {
      console.log(res)
      this.setState({ submit: true, selected: file.name, jobs: res })
    })
    .catch(err => console.log(err));
  }

  process = acceptedFiles => {
    this.setState({ file: acceptedFiles[0], selected: acceptedFiles[0].name });
  }

  render(){
    return (
      <Container fluid className="App-container">
        <div className="App-header">
          <div className="title">
            <img src={logo} className="App-logo" alt="logo" />
            <p className="name">
              RESUMATCH
            </p>
            <p style={{ color: 'white', fontSize: 20 }}>
              Find your next job with the power of NLP!
            </p>
          </div>
          <div className="arrow">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <img src={wave} className="wave" />
        </div>
        <div className="content">
          <div className="drop">
            <Dropzone onDrop={acceptedFiles => this.process(acceptedFiles)}>
              {({getRootProps, getInputProps}) => (
                <section className="dropzone">
                  <Container {...getRootProps()} className="drop-inside">
                    <input {...getInputProps()} />
                    <p style={{ fontSize: 20, width: '90%' }}>
                      Drag and Drop your .pdf resume in here! <br />
                      <i>Selected File: {this.state.selected}</i>
                    </p>
                  </Container>
                </section>
              )}
            </Dropzone>
            <Button variant="primary" size="lg" active style={{ alignSelf: 'center' }} onClick={this.processPdf} disabled={(this.state.submit === "loading")}>
              Submit
            </Button>
          </div>
          <img src={arrow} style={{ flex: 0.5, height: '170px', alignSelf: 'center' }}/>
          <div className="jobs">
            { 
              this.state.submit === true ? (
                <Table striped bordered hover className="table">
                  <thead>
                    <th>Similarity</th>
                    <th>Job Title</th>
                    <th>Job Description</th>
                  </thead>
                  <tbody>
                    {
                      Object.keys(this.state.jobs.description).map(i => {
                        return (
                          <tr>
                            <td>{(parseInt(this.state.jobs.similarity[i] * 100)).toString() + "%"}</td>
                            <td><a href={this.state.jobs.link[i]} target="_blank">{this.state.jobs.title[i]}</a></td>
                            <td>{this.state.jobs.description[i]}</td>
                          </tr>
                        )
                      })
                    }
                  </tbody>
                </Table>
              ) : null
            }
          </div>
        </div>
      </Container>
    );
  }
}

export default App;
