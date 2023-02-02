import React, { useState, useEffect } from "react";
//import classes from "../Styles/Home.module.css";


const Home = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Make a GET request for the users
    fetch("/Users")
      .then((res) => res.json())
      .then((data) => setUsers(data));
  }, []);

  return (
    <ul className="users-list">
      {users.map((user) => (
        <li key={user.id}>
          {user.name} ({user.albums.length} albums)
        </li>
      ))}
    </ul>
  );
};

export default Home;

