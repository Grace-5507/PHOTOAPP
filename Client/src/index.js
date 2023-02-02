import "bootstrap/dist/css/bootstrap.min.css";
import "./Styles/main.css";
import React from "react";
import ReactDOM from "react-dom";
import NavBar from "./Components/Navbar";

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./Components/Home";
import SignUp from "./Components/SignUp";
import Login from "./Components/Login";
import Users from "./Components/Users";
import Albums from "./Components/Album";
import Photos from "./Components/Photos";

const App = () => {
  return (
    <Router>
      <div className="container">
        <NavBar />
        <Switch>
          <Route path="/Users">
            <Users />
          </Route>
          <Route path="Album">
            <Albums/>
          </Route>
          <Route path="/Photos">
            <Photos />
          </Route>
          <Route path="/Login">
            <Login />
          </Route>
          <Route path="/SignUp">
            <SignUp />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));
