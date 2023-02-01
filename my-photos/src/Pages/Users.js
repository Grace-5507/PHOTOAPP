import React, { useState, useEffect } from "react";
import classes from "../Styles/Users.module.css";

const UserInfo = ({ match }) => {
  const [user, setUser] = useState({});
  const [albums, setAlbums] = useState([]);

  useEffect(() => {
    const fetchUser = async () => {
      const response = await fetch(
        `https://jsonplaceholder.typicode.com/users/${match.params.id}`
      );
      const data = await response.json();
      setUser(data);
    };
    fetchUser();
  }, [match.params.id]);

  useEffect(() => {
    const fetchAlbums = async () => {
      const response = await fetch(
        `https://jsonplaceholder.typicode.com/albums?userId=${match.params.id}`
      );
      const data = await response.json();
      setAlbums(data);
    };
    fetchAlbums();
  }, [match.params.id]);

  return (
    <div className="user-info">
      <h1>{user.name}</h1>
      <p>Email: {user.email}</p>
      <p>Phone: {user.phone}</p>
      <h2>Albums:</h2>
      <ul>
        {albums.map((album) => (
          <li key={album.id}>{album.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserInfo;
