import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams, Redirect } from "react-router-dom/";
import { editPin, getPinById } from "../../store/pinReducer";
import { boardConfig } from "../../utils/boardConfig";
import { createBoard } from "../../store/boardReducer";
import { RiEditLine } from "react-icons/ri";
import "./PinEditPage.css";
import { getBoardById } from "../../store/boardReducer";
const PinEditPage = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const pin = useSelector((state) => state.pins.pin);
  const user = useSelector((state) => state.session.user);
  const board = useSelector((state) => state.boards.board);
  const finded = boardConfig.find((item) => item.kitchen === board.title);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState([]);
  const [ingredients, setIngredients] = useState([]);
  const [time, setTime] = useState("");
  const [image_url, setImage_url] = useState("");
  const [kitchen, setKitchen] = useState(finded?.id);
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [descriptionOneStep, setDescriptionOneStep] = useState("");
  const [ingridientOneStep, setIngridientOneStep] = useState("");
  const [stepSubmitted, setStepSubmitted] = useState(false);
  const [indexStep, setIndexStep] = useState(null);

  const history = useHistory();

  useEffect(() => {
    if (id) {
      dispatch(getBoardById(id));
    }
   
    setDescription(pin?.description?.split(". "));
    setIngredients(pin?.ingredients?.split(". "))
    if(pin.time){
      setTime(pin.time)
    }
    if(pin.images){
      setImage_url(pin.images)
    }
    if(pin.title){
      setTitle(pin.title)
    }
   
  }, [dispatch, pin, id]);

  useEffect(() => {
    const errors = {};
    if (title && title?.length > 255) {
      errors.title = "title should be shorter than 255 characters";
    }
    if (description && description?.length > 1500) {
      errors.description = "title should be shorter than 1500 characters";
    }
    if (ingredients && ingredients?.length > 1500) {
      errors.description = "ingredients should be shorter than 1500 characters";
    }
    if (time && time.length > 10) {
      errors.time = "Time should be shorter than 10 characters";
    }
  
    setErrors(errors);
  }, [
    setErrors,
    title,
    description,
    ingredients,
    time,
    
    submitted,
    pin,
  ]);
  useEffect(() => {
    dispatch(getPinById(id));
  }, [dispatch, id]);

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
    const formData = {
      title,
      description: description.join(". "),
      ingredients: ingredients.join(". "),
      time,
      is_saved: pin.is_saved,

      user_id: user.id,
    };
    if (image_url) {
      formData["image_url"] = image_url;
    }
    if (board.id) {
      dispatch(editPin(formData, pin.id));
      setSubmitted(false);
      history.push(`/pins/${id}`);
      setTitle("");
      setDescription([]);
      setIngredients([]);
      setTime("");
      setImage_url("");
      setKitchen(1);
      setErrors({});
      return;
    }

    if (!board.id) {
      const boardId = await dispatch(
        createBoard({
          title: boardConfig[kitchen - 1].kitchen,
          description: boardConfig[kitchen - 1].description,
          board_image_url: boardConfig[kitchen - 1].board_image_url,
          user_id: user.id,
        })
      );

      if (boardId) {
        dispatch(editPin(formData, pin.id));
      }
    }

    setSubmitted(false);
    history.push(`/pins/${id}`);
    setTitle("");
    setDescription([]);
    setIngredients([]);
    setTime("");
    setImage_url("");
    setKitchen(1);
    setErrors({});
  };

  const handleEditIngredient = (index) => {
    const elem = ingredients[index];
    setIngridientOneStep(elem);
    setIndexStep(index);
  };

  const handleClickIngredient = (e) => {
    e.preventDefault();
    setIngridientOneStep(true);
    if (errors.ingridientOneStep) {
      return;
    }
    if (indexStep !== null) {
      const updateIngredient = [...ingredients];
      updateIngredient.splice(indexStep, 1, ingridientOneStep);

      setIngredients(updateIngredient);
      setStepSubmitted(false);
      setIngridientOneStep("");
      setIndexStep(null);
      return;
    }

    setIngredients([...ingredients, ingridientOneStep]);
    setStepSubmitted(false);
    setIngridientOneStep("");
  };

  const handleDeleteIngredient = (index) => {
    const deleted = [...ingredients];
    deleted.splice(index, 1);
    setIngredients(deleted);
  };

  const handleEditDescription = (index) => {
    const elem = description[index];
    setDescriptionOneStep(elem);
    setIndexStep(index);
  };

  const handleClickDescription = (e) => {
    e.preventDefault();
    setStepSubmitted(true);
    if (errors.descriptionOneStep) {
      return;
    }
    if (indexStep !== null) {
      const updatedDescription = [...description];
      updatedDescription.splice(indexStep, 1, descriptionOneStep);

      setDescription(updatedDescription);

      setStepSubmitted(false);
      setDescriptionOneStep("");
      setIndexStep(null);
      return;
    }
    const updated = [...description]
    updated.push(descriptionOneStep)
 
    setDescription(prev=>[...prev, descriptionOneStep]);
    
    setStepSubmitted(false);
    setDescriptionOneStep("");
  };

  const handleDeleteDescription = (index) => {
    const deleted = [...description];
    deleted.splice(index, 1);
    setDescription(deleted);
  };

  if (!user) {
    return <Redirect to="/" />;
  }

  return (
    <main className="main">
      <div className="container pins-edit-page">
        <form className="pins-edit-page-form" onSubmit={handleSubmit}>
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
            {errors.title && submitted && (
              <span className="pins-edit-error-span">{errors.title}</span>
            )}
          </label>
          <label>
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
                {indexStep !== null ? "Update your step" : "Add next step"}
              </button>

              {errors.descriptionOneStep && stepSubmitted && (
                <span className="pin-create-span">
                  {errors.descriptionOneStep}
                </span>
              )}
            </div>
            <ul>
              {description?.map((item, index) => (
                <li className="pin-update-step-item" key={item}>
                  {item}
                  <span
                    onClick={() => handleEditDescription(index)}
                    className="pin-update-step-edit-span"
                  >
                    <RiEditLine />
                  </span>
                  <span
                    onClick={() => handleDeleteDescription(index)}
                    className="pin-update-step-span"
                  >
                    {" "}
                    X{" "}
                  </span>
                </li>
              ))}
            </ul>
          </label>
          <label>
            <div className="input-wrapper-step">
              <input
                className="steps"
                value={ingridientOneStep}
                onChange={(e) => {
                  setIngridientOneStep(e.target.value);
                }}
                placeholder="ingredient"
              />
              <button className="steps-btn" onClick={handleClickIngredient}>
                {indexStep !== null ? "Update ingredient" : "Add ingredient"}
              </button>
              {errors.ingridientOneStep && stepSubmitted && (
                <span className="pin-create-span">
                  {errors.ingridientOneStep}
                </span>
              )}
            </div>

            <ul>
              {ingredients?.map((item, index) => (
                <li className="pin-update-step-item" key={item}>
                  {item}
                  <span
                    onClick={() => handleEditIngredient(index)}
                    className="pin-update-step-edit-span"
                  >
                    <RiEditLine />
                  </span>
                  <span
                    onClick={() => handleDeleteIngredient(index)}
                    className="pin-update-step-span"
                  >
                    X
                  </span>
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
            />
            {errors.time && submitted && (
              <span className="pins-edit-error-span">{errors.time}</span>
            )}
          </label>
          <label>
            Image_url
            <input
              value={image_url}
              onChange={(e) => setImage_url(e.target.value)}
            />
            {errors.image_url && submitted && (
              <span className="pins-edit-error-span">{errors.image_url}</span>
            )}
          </label>
          <button type="submit">Edit Pin</button>
        </form>
      </div>
    </main>
  );
};

export default PinEditPage;
