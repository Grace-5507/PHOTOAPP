
//import classes from "../Styles/Navbar.module.css";



import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth ,logout} from '../auth'




const LoggedInLinks = () => {
    return (
        <>
            <li className="nav-item">
                <Link className="nav-link active" to="/">Home</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link  active" to="/users">Users</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link  active" to="/albums">Album</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link  active" to="/photos">Photos</Link>
            </li>
            <li className="nav-item">
                <a className="nav-link active" href="#" onClick={()=>{logout()}}>Log Out</a>
            </li>
        </>
    )
}


const LoggedOutLinks = () => {
    return (
        <>
            <li className="nav-item">
                <Link className="nav-link active" to="/">Home</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link active" to="/signup">SignUp</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link active" to="/login" >Login</Link>
            </li>

        </>
    )
}
const NavbarPage = () => {
  return (
    <div className="NavbarPage">
      <h1>Welcome to the Album App</h1>
      <p>
        The Album App is a platform where you can view and manage your albums
        and photos.
      </p>
     
    </div>
  );
};
const NavBar = () => {

    const [logged] = useAuth();

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container-fluid">
                <Link className="navbar-brand" to="/">Users</Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        {logged?<LoggedInLinks/>:<LoggedOutLinks/>}
                    </ul>
                </div>
            </div>
        </nav>
    )
}

export default NavBar




