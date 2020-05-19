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

  processPdf = files => {
    const file = files[0]
    var form = new FormData();
    form.append('file', file, file.name)
    console.log(form.entries())
    this.setState({ submit: 'loading' })
    fetch('http://resumatch.andrechek.com/upload', {
      method: 'POST',
      body: form
    })
    .then(res => res.text())
    .then(res => {
      console.log(res)
      this.setState({ submit: false, selected: file.name })
    })
    .catch(err => console.log(err));
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
            <Button variant="primary" size="lg" active style={{ alignSelf: 'center' }} disabled={(this.state.submit === "loading")}>
              Submit
            </Button>
            {
              this.state.submit === true ? (
                <p style={{ width: '800px', textAlign: 'center' }}><i>Identified Charasteristics: Customer Service, Teamwork, Sales, Negotiation, Professionalism</i></p>
              ) : null
            }
          </div>
          <img src={arrow} style={{ flex: 0.5, height: '170px', alignSelf: 'center' }}/>
          <div className="jobs">
            { 
              this.state.submit === true ? (
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
                          <td><a href={job.link} target="_blank">{job.title}</a></td>
                          <td>{job.description}</td>
                        </tr>
                      ))
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

  state = {
    file: '',
    selected: 'None',
    pdf: '',
    submit: false,
    jobs: [
      { title: 'PT - Cashier', description: 'All Lowe’s associates deliver quality customer service while maintaining a store that is clean, safe, and stocked with the products customers need. As a Customer Service Associate – Front End, this means:\nDelivering a checkout experience that is quick, professional, and friendly.\nEnsuring merchandise is accurately accounted, scanned, and meets the needs of customers.\nEngaging in safe work practices and encouraging others to do the same.\nThe Customer Service Associate – Front End is responsible for delivering excellent customer service during the checkout process. This associate is one of the last interactions with our customer before leaving the store and needs to ensure the customer is satisfied and encouraged to come back to Lowe’s. Therefore, engaging with customers as well as attention to detail are extremely important in this role.', link: 'https://www.linkedin.com/jobs/view/1827838103' },
      { title: 'Cashier', link: 'https://www.linkedin.com/jobs/view/1513665368', description: 'Cashiers play a critical customer service role by providing customers with fast, friendly, accurate and safe service. They process Checkout and/or Return transactions, as well as monitor and maintain the Self-Checkout area. They proactively seek product/project knowledge to provide customers with information and identify selling opportunities. They follow all policies and procedures to ensure that shrink is minimized. A Head Cashier will position Cashiers and support them by expediting price checks, approving Point of Sale transactions and markdowns for mainline registers, Self-Checkout, Returns, Pro Desk, Special Services, and Tool Rental. They provide first level escalation for customer issues and assist in the supervision, coaching and training of other Front End Associates by participating in the training of new Cashiers and utilizing all available tools to coach and develop other Cashiers. The preferred qualification for a Head Cashier is 1+ years of Cashier experience.' },
      { title: 'Warehouse Associate', link: 'https://www.linkedin.com/jobs/view/1858824965', description: 'Our Associates work in any variety of warehousing functions, and we are a fun team looking for other amazing associates to join our crew! You will have the opportunity to work in all facets of the warehouse with tasks that may include loading, receiving, order fulfillment, order preparation, and basic inventory function.' },
      { title: 'Logistics and Warehouse Lead', link: 'https://www.linkedin.com/jobs/view/1849575503', description: 'Lime is a smart-mobility provider that offers cities an array of products including Lime-E (e-assist bicycles) and Lime-S (electric scooters). Lime aims to revolutionize mobility in cities and campuses by empowering residents to take charge of their commutes with cleaner, more efficient, and affordable transportation options that improve urban sustainability.\nWe are looking for a Logistics and Warehouse Associate Lead to successfully move materials, supplies and finished goods through the facility which includes unloading product from semis into warehouse and loading from warehouse into delivery trucks.' },
      { title: 'Planner', link: 'https://www.linkedin.com/jobs/view/1840747765', description: 'The Planner position at Celestica, Fremont, CA supports manufacturing by monitoring and managing inventories, sales, and production levels to plan for materials needed to meet production demand.' },
      { title: 'Planner', link: 'https://www.linkedin.com/jobs/view/1863004073', description: 'DESCRIPTION: As a Production Planner, you will be responsible for planning, organizing and controlling the flow of production parts to support scheduling of orders and services for established and scheduled customer commitments; receiving and responding to customer inquiries, communicating potential schedule impacts and escalating issues to the internal Business Manager; working closely with internal departments such as manufacturing, procurement, materials, engineering, quality and the Business Manager to ensure timely communication of lead times, schedule impacts and changes, material shortages, etc. ESSENTIAL DUTIES: Process timely release of shop orders in quantities that support upper level demand Define, monitor and adjust planning as conditions in the processes or demand stream change Generate and respond to various ERP/MRP reporting to ensure in-tact schedules and priorities are properly defined for the shop floor, procurement, business manager, etc. Maintain weekly/monthly production schedule, execute the subsequent MRP cycles where applicable to support the desired schedules' },
      { title: 'Shipping and Receiving Clerk', link: 'https://www.linkedin.com/jobs/view/1864041462', description: <p>· Label bottles, assemble kits, and package shipments\n
      · Ensures all shipments are stocked according to company standards, focusing on organization and safety.<br />
      · Maintains the warehouse, shipping and receiving areas in a clean, organized, and safe manner at all times.<br />
      · Completes all necessary paperwork, and submits in a timely manner.<br />
      · Actively participates in safety training; makes safety a priority each day.<br />
      · Performs a daily key parts inventory and communicates company needs in a timely manner.</p> },
      { title: 'Storeroom Clerk', description: <p>We are looking for experienced candidate to work on a swing shift, Monday thru Friday, as a Storeroom Clerk in the Pleasanton area. <br />
      Responsible for receipt, data entry, and transfer of materials<br />
      Run reports daily on inventory and stock status<br />
      Knowledge of MRP<br />
      Receive and stock parts<br />
      Ability to lift up to 50lbs.</p> },
      { title: 'Human Resources Generalist', link: 'https://www.linkedin.com/jobs/view/1850878698', description: <p>
        Manage and resolve employee relations issues of moderate difficulty through effective, thorough, and objective investigations<br />
        Advise managers on HR policies, their interpretation, and application, and manage involuntary terminations<br />
        Assist in the development and implementation of personnel policies and procedures; help prepare and maintain the employee handbook<br />
        Ability to audit and analyze data, as well as propose methods for continuous improvement<br />
        Participate in the design and implementation of programs that build employee engagement and retention<br />
        Participate in projects as assigned that support broader corporate human resources programs<br />
      </p> },
    ]
  }
}

export default App;
