import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams, Redirect } from "react-router-dom/";
import { editPin, getPinById } from "../../store/pinReducer";
import { boardConfig } from "../../utils/boardConfig";
import { createBoard } from "../../store/boardReducer";

import "./PinEditPage.css";
import { getBoardById } from "../../store/boardReducer";
const PinEditPage = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const pin = useSelector((state) => state.pins.pin);
  const user = useSelector((state) => state.session.user);
  const board = useSelector((state) => state.boards.board);
  const finded = boardConfig.find((item) => item.kitchen === board.title);
  const [title, setTitle] = useState(pin.title);
  const [description, setDescription] = useState(pin.description);
  const [ingredients, setIngredients] = useState(pin.ingredients);
  const [time, setTime] = useState(pin.time);
  const [image_url, setImage_url] = useState(pin.images);
  const [kitchen, setKitchen] = useState(finded?.id);
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const history = useHistory();

  useEffect(() => {
    if(pin?.board_id?.board_id){
      dispatch(getBoardById(pin?.board_id?.board_id));
    }
    
  }, [dispatch, pin]);

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
      errors.time = "ingredients should be shorter than 10 characters";
    }
    if (image_url && image_url?.length > 255) {
      errors.image_url = "ingredients should be shorter than 10 characters";
    }
    setErrors(errors);
  }, [
    setErrors,
    title,
    description,
    ingredients,
    time,
    image_url,
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
      errors.time ||
      errors.image_url
    ) {
      return;
    }
    const formData =   {
      title,
      description,
      ingredients,
      time,
      image_url,
      user_id: user.id,
    } 

    if (board.id) {
      dispatch(
        editPin(
          formData,
          pin.id
        )
      );
      setSubmitted(false);
      history.push(`/pins/${id}`);
      setTitle("");
      setDescription("");
      setIngredients("");
      setTime("");
      setImage_url("");
      setKitchen(1);
      setErrors({});
      return
    }

    if (!board.id) {
      const boardId = await dispatch(
        createBoard({
          title:boardConfig[kitchen-1].kitchen,
          description:boardConfig[kitchen-1].description,
          board_image_url: boardConfig[kitchen-1].board_image_url,
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
            {errors.title && submitted && <span>{errors.title}</span>}
          </label>
          <label>
            Tell everyone how you will cook
            <textarea
              required
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              rows="5"
              cols="44"
              placeholder="Add description"
            />
            {errors.description && submitted && (
              <span>{errors.description}</span>
            )}
          </label>
          <label>
            Ingredients
            <textarea
              required
              value={ingredients}
              onChange={(e) => setIngredients(e.target.value)}
              rows="5"
              cols="44"
              placeholder="Add ingredients"
            />
            {errors.ingredients && submitted && (
              <span>{errors.ingredients}</span>
            )}
          </label>
          <label>
            Time
            <input
              required
              value={time}
              onChange={(e) => setTime(e.target.value)}
            />
            {errors.time && submitted && <span>{errors.time}</span>}
          </label>
          <label>
            Image_url
            <input
              required
              value={image_url}
              onChange={(e) => setImage_url(e.target.value)}
            />
            {errors.image_url && submitted && <span>{errors.image_url}</span>}
          </label>
          <button type="submit">Edit Pin</button>
        </form>
      </div>
    </main>
  );
};

export default PinEditPage;
