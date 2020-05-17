import React, { Component } from 'react';
import logo from './assets/logo.png';
import wave from './assets/wave.png';
import './App.css';
import Dropzone from 'react-dropzone';
import { Container, InputGroup, FormControl, Button } from 'react-bootstrap'
import { FaBriefcase } from 'react-icons/fa'

class App extends Component {

  state = {
    file: '',
    selected: 'None'
  }

  processPdf = files => {
    const file = files[0]
    if(file.name.includes(".pdf")) {
      console.log(file)
      this.setState({ file, selected: file.name })
    }
  }

  render(){
    return (
      <Container fluid className="App-container">
        <div className="App-header">
          <div className="title">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
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
            <InputGroup className="mb-3" style={{ width: '30vw', paddingLeft: '30px' }}>
              <InputGroup.Prepend>
                <InputGroup.Text id="basic-addon2"><FaBriefcase size={22} /></InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl
                placeholder="Job Title"
                aria-label="Job Title"
                aria-describedby="basic-addon1"
                inputRef={node => this.title = node}
              />
            </InputGroup>
            <InputGroup className="mb-3" style={{ width: '30vw', paddingLeft: '30px' }}>
              <InputGroup.Prepend>
                <InputGroup.Text id="basic-addon2"><FaBriefcase size={22} /></InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl
                placeholder="Zip Code"
                aria-label="Zip Code"
                aria-describedby="basic-addon1"
                inputRef={node => this.zip = node}
              />
            </InputGroup>

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
            <Button variant="primary" size="lg" active style={{ alignSelf: 'center', marginTop: '10px' }}>
              Submit
            </Button>
          </div>
          <div className="jobs">
          </div>
        </div>
      </Container>
    );
  }
}

export default App;
