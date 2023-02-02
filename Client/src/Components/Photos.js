//import classes from "../Styles/Photos.module.css";
import React, { useState, useEffect } from "react";
import { Form, FormGroup, Label, Input, Button } from "reactstrap";
import axios from "axios";

const Photos = (props) => {
  const [photo, setPhoto] = useState({});
  const [title, setTitle] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`/photos/${props.match.params.id}`);
        setPhoto(response.data);
        setTitle(response.data.title);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, [props.match.params.id]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.patch(`/photos/${photo.id}`, { title });
      setTitle(title);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="photo-page">
      <img src={photo.url} alt={photo.title} />
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for="title">Title</Label>
          <Input
            type="text"
            name="title"
            id="title"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
          />
        </FormGroup>
        <Button type="submit">Save</Button>
      </Form>
    </div>
  );
};

export default Photos;

