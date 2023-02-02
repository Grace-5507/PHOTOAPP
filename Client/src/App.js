import React, { Component } from "react";

import "./App.css";
import Album from "./Components/Album";
import Home from "./Components/Home";
import Login from "./Components/Login";
import LandingPage from "./Components/LandingPage";
import Users from "./Components/Users";
import Photos from "./Components/Photos";


import { Route } from 'react-router-dom';


class App extends Component {
  render() {
    return (
      <div className="App">
        <LandingPage />
        
       
      </div>
      
    );
  }
}
export default App;




