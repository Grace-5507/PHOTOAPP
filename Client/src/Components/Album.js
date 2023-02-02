import React, { useState, useEffect } from "react";
import axios from "axios";

//import classes from "../Styles/Album.module.css";

function Album({ match }) {
  const [album, setAlbum] = useState({});
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    const fetchAlbum = async () => {
      const res = await axios.get(`/Album/${match.params.id}`);
      setAlbum(res.data);
    };
    fetchAlbum();
  }, [match.params.id]);

  useEffect(() => {
    const fetchPhotos = async () => {
      const res = await axios.get(`/albums/albums${match.params.id}/photos`);
      setPhotos(res.data);
    };
    fetchPhotos();
  }, [match.params.id]);

  return (
    <div className="album-page-container">
      <h2>Album: {album.title}</h2>
      <h3>Photos:</h3>
      <ul>
        {photos.map((photo) => (
          <li key={photo.id}>{photo.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Album;
