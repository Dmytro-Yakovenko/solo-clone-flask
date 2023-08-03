import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, Redirect } from "react-router-dom/";
import { createBoard } from "../../store/boardReducer";
import { boardConfig } from "../../utils/boardConfig";

import "./BoardCreatePage.css";
const BoardCreatePage = () => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const [kitchen, setKitchen] = useState(1);
  const [title, setTitle] = useState(boardConfig[0].kitchen);
  const [description, setDescription] = useState(boardConfig[0].description);
  const [boardImageUrl, setBoardImageUrl] = useState(
    boardConfig[0].board_image_url
  );
  const history = useHistory();

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(
      createBoard(
        {
          title,
          description,
          board_image_url: boardImageUrl,
          user_id: user.id,
        },
  
      )
    );

    history.push("/boards");
  };
  if(!user){
    return <Redirect to="/"/>
  } 
  return (
    <main className="main">
      <div className="container board-create-page">
        <form className="board-create-page-form" onSubmit={handleSubmit}>
          <select
            value={kitchen}
            onChange={(e) => {
              setKitchen(e.target.value);
              setTitle(boardConfig[e.target.value-1].kitchen)
              setBoardImageUrl(boardConfig[e.target.value-1].board_image_url)
              setDescription(boardConfig[e.target.value-1].description)
            }}
          >
            {boardConfig.map((item) => (
              <option key={item.id} value={item.id}>
                {item.kitchen}
              </option>
            ))}
          </select>
          <img 
          className="board-create-page-image"
          src={boardImageUrl} alt={title} />
          <p>{description}</p>
          <button
          
          type="submit">Create Board</button>
        </form>
      </div>
    </main>
  );
};

export default BoardCreatePage;
