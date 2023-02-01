import React from "react";
import { ReactDOM } from "react-dom";
import classes from "../Styles/LandingPage.module.css";



const Landing = () => {
  return (
    <div className="landing">
      <h1>Welcome to the Album App</h1>
      <p>
        The Album App is a platform where you can view and manage your albums
        and photos.
      </p>
      <button>Login</button>
    </div>
  );
};

export default Landing;