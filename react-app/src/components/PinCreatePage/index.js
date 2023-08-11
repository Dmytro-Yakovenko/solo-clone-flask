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
  const [description, setDescription] = useState("");
  const [ingredients, setIngredients] = useState("");
  const [time, setTime] = useState("");
  // const [image_url, setImage_url] = useState("https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691726195/bc2d04276b5bfde9bce68c7a91914b7f_mi6kmp.jpg");
  const [image_url, setImage_url] = useState("");
  const [kitchen, setKitchen] = useState(1);
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

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
    if (description.length > 1500 || description.length < 10) {
      errors.description =
        "description should be shorter than 1500 characters and longer than 10 characters ";
    }
    if (ingredients.length > 1500 || ingredients.length < 10) {
      errors.ingredients =
        "ingredients should be shorter than 1500 characters and longer than 10 characters";
    }
    if (time.length > 10 || time.length < 2) {
      errors.time =
        "ingredients should be shorter than 10 characters and longer than 2 characters";
    }
    // if (image_url.length > 255 || image_url.length < 10) {
    //   errors.image_url =
    //     "image url should be longer than 10 characters and shorter than 255";
    // }

    // if (!image_url.match(/(\.jpe?g$)|(\.png$)/g)) {
    //   errors.image_url = "Image URL must end in .png, .jpg, or .jpeg";
    // }

    setErrors(errors);
  }, [setErrors, title, description, ingredients, time, submitted]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitted(true);
    if (
      errors.title ||
      errors.description ||
      errors.ingredients ||
      errors.time
      // errors.image_url
    ) {
      return;
    }
    const formData = {
      title,
      description,
      ingredients,
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
              placeholder="Add description in this format: step1. step2. step3.  ... "
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
              placeholder="Add ingredients in this format: ingredient1. ingredient2. ingredient3. ... "
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
              placeholder="30 min"
            />
            {errors.time && submitted && <span>{errors.time}</span>}
          </label>
          <label>
            Image_url
            <input
              value={image_url}
              onChange={(e) => setImage_url(e.target.value)}
              placeholder="we want you to add your link"
            />
            {errors.image_url && submitted && <span>{errors.image_url}</span>}
          </label>
          <button type="submit">Create Pin</button>
        </form>
      </div>
    </main>
  );
};

export default PinCreatePage;
