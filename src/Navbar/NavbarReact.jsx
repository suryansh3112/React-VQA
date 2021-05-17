import React from 'react'
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import {Link, NavLink} from 'react-router-dom';

function NavbarReact() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
  <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
  <Navbar.Toggle aria-controls="basic-navbar-nav" />
  <Navbar.Collapse id="basic-navbar-nav">
    <Nav className="mr-auto">
    <Link to='/'>
      <Nav.Link href="#home">VQA</Nav.Link>
    </Link>
          
    <Link to='/cifar10'>
      <Nav.Link href="#link">Cifar10</Nav.Link>
    </Link>
          
    </Nav>
  </Navbar.Collapse>
</Navbar>
  )
}

export default NavbarReact
