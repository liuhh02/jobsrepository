import React, { Component } from 'react';
import logo from './assets/logo.png';
import wave from './assets/wave.png';
import arrow from './assets/arrow.png';
import './App.css';
import Dropzone from 'react-dropzone';
import { Container, InputGroup, FormControl, Button, Table } from 'react-bootstrap';
import { Document, Page } from 'react-pdf';
import PDFViewer from 'pdf-viewer-reactjs';

class App extends Component {

  state = {
    file: '',
    selected: 'None',
    pdf: '',
    jobs: [
      { title: 'Wannabe Rockstar', description: 'IF YOU ARE A TIER 1 BUFFOON, PLEASE APPLY' },
      { title: 'Gamer', description: 'Just bring a soda.' },
      { title: 'Brogrammer', description: 'Hey bruh, wanna write some jUiCy coDe?' },
      { title: 'McDonalds employee', description: 'No, our chicken nuggets are NOT chicken! Learn more secrets in this unbelievably boring job.' },
      { title: 'T-shirt man', description: 'Need a PhD in fashion for this, please :D' },
      { title: 'Wannabe Rockstar', description: 'IF YOU ARE A TIER 1 BUFFOON, PLEASE APPLY' },
      { title: 'Gamer', description: 'Just bring a soda.' },
      { title: 'Brogrammer', description: 'Hey bruh, wanna write some jUiCy coDe?' },
      { title: 'McDonalds employee', description: 'No, our chicken nuggets are NOT chicken! Learn more secrets in this unbelievably boring job.' },
      { title: 'T-shirt man', description: 'Need a PhD in fashion for this, please :D' },
      { title: 'Wannabe Rockstar', description: 'IF YOU ARE A TIER 1 BUFFOON, PLEASE APPLY' },
      { title: 'Gamer', description: 'Just bring a soda.' },
      { title: 'Brogrammer', description: 'Hey bruh, wanna write some jUiCy coDe?' },
      { title: 'McDonalds employee', description: 'No, our chicken nuggets are NOT chicken! Learn more secrets in this unbelievably boring job.' },
      { title: 'T-shirt man', description: 'Need a PhD in fashion for this, please :D' },
      { title: 'Wannabe Rockstar', description: 'IF YOU ARE A TIER 1 BUFFOON, PLEASE APPLY' },
      { title: 'Gamer', description: 'Just bring a soda.' },
      { title: 'Brogrammer', description: 'Hey bruh, wanna write some jUiCy coDe?' },
      { title: 'McDonalds employee', description: 'No, our chicken nuggets are NOT chicken! Learn more secrets in this unbelievably boring job.' },
      { title: 'T-shirt man', description: 'Need a PhD in fashion for this, please :D' },
    ]
  }

  processPdf = files => {
    const file = files[0]
    if(file.name.includes(".pdf")) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const uint = new Uint8Array(event.target.result)
        this.setState({ pdf: uint })
        console.log(this.state.pdf);
      };
      const base64 = reader.readAsArrayBuffer(file);  
      this.setState({ file, selected: file.name })
    }
  }

  render(){
    return (
      <Container fluid className="App-container">
        <div className="App-header">
          <div className="title">
            <img src={logo} className="App-logo" alt="logo" />
            <p style={{ color: 'white' }}>
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
            <Dropzone onDrop={acceptedFiles => this.processPdf(acceptedFiles)}>
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
            <Button variant="primary" size="lg" active style={{ alignSelf: 'center' }}>
              Submit
            </Button>
          </div>
          <img src={arrow} style={{ flex: 0.7, height: '170px', alignSelf: 'center' }}/>
          <div className="jobs">
            <Table striped bordered hover className="table">
              <thead>
                <th>#</th>
                <th>Job Title</th>
                <th>Job Description</th>
              </thead>
              <tbody>
                {
                  this.state.jobs.map((job, i) => (
                    <tr>
                      <td>{i + 1}</td>
                      <td>{job.title}</td>
                      <td>{job.description}</td>
                    </tr>
                  ))
                }
              </tbody>
            </Table>
          </div>
        </div>
      </Container>
    );
  }
}

export default App;
