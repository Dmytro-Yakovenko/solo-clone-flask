import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createPin } from "../../store/pinReducer";


import "./PinCreatePage.css";
const PinCreatePage = () => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const [title , setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [ingredients, setIngredients] = useState("");
  const [time, setTime] = useState("");
  const [image_url, setImage_url] = useState("");
  const {errors, setErrors}= useState({})
  useEffect(() => {
   
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(
      createPin(
        {
            title,
            description,
            ingredients,
            time,
            image_url,
        },
        
      )
    );
    setTitle("");
    setDescription("");
    setIngredients("");
    setTime("");
    setImage_url("");
    
  };

  return (
    <main className="main">
      <div className="container pins-create-page">
       <form>
        <label>Title</label>
        <input/>
        <label>Description</label>
        <textarea/>
        <label>Ingredients</label>
        <textarea/>
        <label>Time</label>
        <input/>
        <label>Image_url</label>
        <input/>
       </form>
      </div>
    </main>
  );
};

export default PinCreatePage;
