import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createPin } from "../../store/pinReducer";
import { boardConfig } from "./boardConfig";

import "./PinCreatePage.css";
const PinCreatePage = () => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [ingredients, setIngredients] = useState("");
  const [time, setTime] = useState("");
  const [image_url, setImage_url] = useState("");
  const [kitchen, setKitchen] = useState(1);
  const [ errors, setErrors ] = useState({});
  useEffect(() => {
    const errors = {};
    if (title.length > 255) {
      errors.title = "title should be shorter than 255 characters";
    }
    if (description.length > 1500) {
      errors.description = "title should be shorter than 1500 characters";
    }
    if (ingredients.length > 1500) {
      errors.description = "ingredients should be shorter than 1500 characters";
    }
    if (time.length > 10) {
      errors.time = "ingredients should be shorter than 10 characters";
    }
    if (image_url.length > 255) {
      errors.image_url = "ingredients should be shorter than 10 characters";
    }
    setErrors(errors);
  }, [setErrors, title, description, ingredients, time, image_url]);

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
            user_id:user.id,
        },
        kitchen

      )
    );
    

    setTitle("");
    setDescription("");
    setIngredients("");
    setTime("");
    setImage_url("");
    setKitchen(1);
    setErrors({})
  };

  return (
    <main className="main">
      <div className="container pins-create-page">
        <form 
        className="pins-create-page-form"
        onSubmit={handleSubmit}>
          <select value={kitchen} onChange={(e) => setKitchen(e.target.value)}>
            {boardConfig.map((item) => (
              <option key={item.id} value={item.id}>
                {item.kitchen}
              </option>
            ))}
          </select>
          <label>Tell everyone what are you going to cook</label>
          <input 
          value={title} 
          onChange={(e)=>setTitle(e.target.value)}
          required
          placeholder="Add title"
            />
          {errors.title && <span>{errors.title}</span>}

          <label>Tell everyone how you will cook</label>
          <textarea 
          required  
          value={description} 
          onChange={(e)=>setDescription(e.target.value)}
          rows="5"
          cols="50"
          placeholder="Add description"
          />
          {errors.description && <span>{errors.description}</span>}

          <label>Ingredients</label>
          <textarea
           required  
           value={ingredients} 
           onChange={(e)=>setIngredients(e.target.value)}
           rows="5"
           cols="50"
           placeholder="Add ingredients"
           />
          {errors.ingredients && <span>{errors.ingredients}</span>}
          <label>Time</label>

          <input required value={time} onChange={(e)=>setTime(e.target.value)}/>
          {errors.time && <span>{errors.time}</span>}
          <label>Image_url</label>
          <input required  value={image_url} onChange={(e)=>setImage_url(e.target.value)}/>
          {errors.image_url && <span>{errors.image_url}</span>}
          
          <button 
          type="submit"
          disabled={!!errors.title || !!errors.description || !!errors.ingredients || !!errors.time || !!errors.image_url}
          >
            Create Pin
            </button>
        </form>
      </div>
    </main>
  );
};

export default PinCreatePage;
