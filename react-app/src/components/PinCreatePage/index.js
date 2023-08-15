import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, Redirect } from "react-router-dom/";
import { createPin } from "../../store/pinReducer";
import { boardConfig } from "../../utils/boardConfig";
import { getBoardByTitle } from "../../store/boardReducer";
import { createBoard } from "../../store/boardReducer";
import "./PinCreatePage.css";
const PinCreatePage = () => {
  const dispatch = useDispatch();
  const board = useSelector((state) => state.boards.board);
  const user = useSelector((state) => state.session.user);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState([]);
  const [ingredients, setIngredients] = useState([]);
  const [time, setTime] = useState("");
  const [image_url, setImage_url] = useState("");
  const [kitchen, setKitchen] = useState(1);
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [descriptionOneStep, setDescriptionOneStep] = useState("");
  const [ingridientOneStep, setIngridientOneStep] = useState("");
  const [stepSubmitted, setStepSubmitted] = useState(false);

  const history = useHistory();

  useEffect(() => {
    dispatch(getBoardByTitle(user.id, title));
  }, [dispatch, kitchen, user.id]);

  useEffect(() => {
    const errors = {};
    if (title.length > 255 || title.length < 5) {
      errors.title =
        "title should be shorter than 255 characters and longer than 5 characters";
    }
    if (time.length > 10 || time.length < 2) {
      errors.time =
        "time should be in format  10 min  and length of characters and longer than 2 characters and less than 10";
    }
 
    setErrors(errors);
  }, [setErrors, title, time, submitted]);

  useEffect(() => {
    const error = {};
    if (descriptionOneStep.length < 5 || descriptionOneStep > 50) {
      error.descriptionOneStep =
        "description should be shorter than 50 characters and longer than 5 characters";
    }
    setErrors(error);
  }, [descriptionOneStep]);

  useEffect(() => {
    const error = {};
    if (ingridientOneStep.length < 5 || ingridientOneStep > 50) {
      error.ingridientOneStep =
        " ingredient should be shorter than 50 characters and longer than 5 characters";
    }
    setErrors(error);
  }, [ingridientOneStep]);

  useEffect(()=>{
    const errors={}
    
    if(description.length<1 ){
      
      errors.description="description can not be empty"
    }

    setErrors(errors)
  },[description, descriptionOneStep])


  useEffect(()=>{
    const errors={}
    if(ingredients.length<1 ){
      errors.ingredients="ingredients can not be empty"
    }
    setErrors(errors)
  },[ingredients, ingridientOneStep])


  const handleClickIngredient = (e) => {
    e.preventDefault();
    setStepSubmitted(true);
    if (errors.ingridientOneStep) {
      return;
    }
    setIngredients([...ingredients, ingridientOneStep]);
    setStepSubmitted(false);
    setIngridientOneStep("");
  };


  const handleDeleteIngredient=(index)=>{
    const deleted = [...ingredients]
    deleted.splice(index,1)
  
    setIngredients(deleted)
  }

  const handleDeleteDescription=(index)=>{
    const deleted = [...description]
    deleted.splice(index,1)
    setDescription(deleted)
  }



 
  const handleClickDescription = (e) => {
    e.preventDefault();
    setStepSubmitted(true);
    if (errors.descriptionOneStep) {
      return;
    }
    setDescription([...description, descriptionOneStep]);
    setStepSubmitted(false);
    setDescriptionOneStep("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitted(true);
    if (
      errors.title ||
      errors.description ||
      errors.ingredients ||
      errors.time 
    ) {
      return;
    }
    if(description.length<1 || ingredients.length<1){
      alert("add description and ingredients")
      return 
    }
  
    const formData = {
      title,
      description: description.join("."),
      ingredients: ingredients.join("."),
      time,
      user_id: user.id,
    };
    if (image_url) {
      formData["image_url"] = image_url;
    }
    if (board) {
      const id = await dispatch(createPin(formData, board.id));

      history.push(`/pins/${id}`);
    }
    if (!board) {
      const boardId = await dispatch(
        createBoard({
          title: boardConfig[kitchen - 1].kitchen,
          description: boardConfig[kitchen - 1].description,
          board_image_url: boardConfig[kitchen - 1].board_image_url,
          user_id: user.id,
        })
      );

      if (boardId) {
        const id = await dispatch(createPin(formData, boardId));

        history.push(`/pins/${id}`);
      }
    }
    setSubmitted(false);
    setTitle("");
    setDescription("");
    setIngredients("");
    setTime("");
    setImage_url("");
    setKitchen(1);
    setErrors({});
  };

  if (!user) {
    return <Redirect to="/" />;
  }

  return (
    <main className="main">
      <div className="container pins-create-page">
        <form className="pins-create-page-form" onSubmit={handleSubmit}>
          <select value={kitchen} onChange={(e) => setKitchen(e.target.value)}>
            {boardConfig.map((item) => (
              <option key={item.id} value={item.id}>
                {item.kitchen}
              </option>
            ))}
          </select>
          <label>
            Tell everyone what are you going to cook
            <input
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
              placeholder="Add title"
            />
            {errors.title && submitted && <span className="pin-create-span">{errors.title}</span>}
          </label>
          <label className="label">
            Tell everyone how you will cook
            <div className="input-wrapper-step">
              <input
                className="steps"
                value={descriptionOneStep}
                onChange={(e) => {
                  setDescriptionOneStep(e.target.value);
                }}
                placeholder="Step"
              />
              <button className="step-btn" onClick={handleClickDescription}>
                Add next step
              </button>

              {errors.descriptionOneStep   && stepSubmitted && (
                <span className="pin-create-span" >{errors.descriptionOneStep }</span>
              )}
            </div>
            <ul>
              <li className="step-item" >Prepare your kitchen for the art of cooking</li>
              {description.map((item, index) => (
                <li className="step-item" key={index}>{item}
                <span className="step-span" onClick={()=>handleDeleteDescription(index)}> X </span>
                </li>
              ))}
            </ul>
          </label>
          <label>
            Tell everyone your ingredients
            <div className="input-wrapper-step">
              <input
                className="steps"
                value={ingridientOneStep}
                onChange={(e) => {
                  setIngridientOneStep(e.target.value);
                }}
                placeholder="Ingredient"
              />
              <button className="step-btn" onClick={handleClickIngredient}>
                Add next ingredient
              </button>

              {errors.ingridientOneStep && stepSubmitted && (
                <span className="pin-create-span" >{errors.ingridientOneStep}</span>
              )}
            </div>
            <ul>
              <li className="step-item">Prepare your ingredients</li>
              {ingredients.map((item, index) => (
                <li className="step-item" key={index}>
                  {item}
                  <span className="step-span" onClick={()=>handleDeleteIngredient(index)}> X </span>
                </li>
              ))}
            </ul>
          </label>
          <label>
            Time
            <input
              required
              value={time}
              onChange={(e) => setTime(e.target.value)}
              placeholder="30 min"
            />
            {errors.time && submitted && <span className="pin-create-span">{errors.time}</span>}
          </label>
          <label>
            Image_url
            <input
              value={image_url}
              onChange={(e) => setImage_url(e.target.value)}
              placeholder="we want you to add your link"
            />
            {errors.image_url && submitted && <span className="pin-create-span">{errors.image_url}</span>}
          </label>
          <button type="submit">Create Pin</button>
        </form>
      </div>
    </main>
  );
};

export default PinCreatePage;
