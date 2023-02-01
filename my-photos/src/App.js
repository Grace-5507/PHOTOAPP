import React, { Component } from "react";

import "./App.css";
import Album from "./Pages/Album";
import Home from "./Pages/Home";
import Login from "./Pages/Login";
import LandingPage from "./Pages/LandingPage";
import Users from "./Pages/Users";
import Photos from "./Pages/Photos";


import { Route } from 'react-router-dom';


class App extends Component {
  render() {
    return (
      <div className="App">
        <Album />
         <Photos />
        <Login />
        <LandingPage />
        <Route exact path="/" component={Home} />
        <Route path="/users/:id" component={Users} />
       
      </div>
      
    );
  }
}
export default App;




