import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import VQA from './VQA'
import Cifar10 from './Cifar10/Cifar10'
import NavbarReact from './Navbar/NavbarReact'

function App() {
  return (
    <div>
      <Router>
        <NavbarReact/>
        <Switch>     
          <Route path="/" exact component={VQA} />
          <Route path="/cifar10" component={Cifar10} />    
        </Switch>
      </Router>
    </div>
  )
}

export default App
