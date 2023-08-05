
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams, Redirect } from "react-router-dom/";
import { editPin, getPinById } from "../../store/pinReducer";
import { boardConfig } from "../../utils/boardConfig";


import "./PinEditPage.css";
const PinEditPage = () => {
  const {id}=useParams()
  const dispatch = useDispatch();
  const pin = useSelector((state)=>state.pins.pin)
  const user = useSelector((state) => state.session.user);
  const [title, setTitle] = useState(pin.title);
  const [description, setDescription] = useState(pin.description);
  const [ingredients, setIngredients] = useState(pin.ingredients);
  const [time, setTime] = useState(pin.time);
  const [image_url, setImage_url] = useState(pin.images);
  const [kitchen, setKitchen] = useState(1);
  const [ errors, setErrors ] = useState({});
 
  const history = useHistory()
  
  useEffect(()=>{
    dispatch(getPinById(id))
  },[dispatch, id])


  useEffect(() => {
    const errors = {};
    if (title?.length > 255) {
      errors.title = "title should be shorter than 255 characters";
    }
    if (description?.length > 1500) {
      errors.description = "title should be shorter than 1500 characters";
    }
    if (ingredients?.length > 1500) {
      errors.description = "ingredients should be shorter than 1500 characters";
    }
    if (time.length > 10) {
      errors.time = "ingredients should be shorter than 10 characters";
    }
    if (image_url?.length > 255) {
      errors.image_url = "ingredients should be shorter than 10 characters";
    }
    setErrors(errors);
  }, [setErrors, title, description, ingredients, time, image_url]);

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(
      editPin(
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
    
history.push("/pins")
    setTitle("");
    setDescription("");
    setIngredients("");
    setTime("");
    setImage_url("");
    setKitchen(1);
    setErrors({})
  };

  if(!user){
    return <Redirect to="/"/>
  } 

  return (
    <main className="main">
      <div className="container pins-edit-page">
        <form 
        className="pins-edit-page-form"
        onSubmit={handleSubmit}>
          <select value={kitchen} onChange={(e) => setKitchen(e.target.value)}>
            {boardConfig.map((item) => (
              <option key={item.id} value={item.id}>
                {item.kitchen}
              </option>
            ))}
          </select>
          <label>Tell everyone what are you going to cook
          <input 
          value={title} 
          onChange={(e)=>setTitle(e.target.value)}
          required
          placeholder="Add title"
            />
          {errors.title && <span>{errors.title}</span>}
          </label>
          <label>Tell everyone how you will cook
          <textarea 
          required  
          value={description} 
          onChange={(e)=>setDescription(e.target.value)}
          rows="5"
          cols="44"
          placeholder="Add description"
          />
          {errors.description && <span>{errors.description}</span>}
          </label>
          <label>Ingredients
          <textarea
           required  
           value={ingredients} 
           onChange={(e)=>setIngredients(e.target.value)}
           rows="5"
           cols="44"
           placeholder="Add ingredients"
           
           />
          {errors.ingredients && <span>{errors.ingredients}</span>}
          </label>
          <label>Time

          <input required value={time} onChange={(e)=>setTime(e.target.value)}/>
          {errors.time && <span>{errors.time}</span>}
          </label>
          <label>Image_url
          <input required  value={image_url} onChange={(e)=>setImage_url(e.target.value)}/>
          {errors.image_url && <span>{errors.image_url}</span>}
          </label>
          <button 
          type="submit"
          disabled={!!errors.title || !!errors.description || !!errors.ingredients || !!errors.time || !!errors.image_url}
          >
            Edit Pin
            </button>
        </form>
      </div>
    </main>
  );
};

export default PinEditPage;