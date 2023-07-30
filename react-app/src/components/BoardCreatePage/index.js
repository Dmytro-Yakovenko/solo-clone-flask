import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom/";
import { createBoard } from "../../store/boardReducer";
import { boardConfig } from "../../utils/boardConfig";

import "./BoardCreatePage.css";
const BoardCreatePage = () => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const [kitchen, setKitchen] = useState(1);
  const [title, setTitle] = useState(boardConfig[0].kitchen);
  const [description, setDescription] = useState(boardConfig[0].description);
  const [boardImageUrl, setBoardImageUrl] = useState(boardConfig[0].board_image_url);
  const history = useHistory()
  
  

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(
      createBoard(
        {
            title,
            description,
            board_image_url:boardImageUrl,
            user_id:user.id,
        },
        kitchen

      )
    );
    
history.push("/boards")
 
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
          
          <button 
          type="submit"
        //   disabled={!!errors.title || !!errors.description || !!errors.ingredients || !!errors.time || !!errors.image_url}
          >
            Create Board
            </button>
        </form>
      </div>
    </main>
  );
};

export default BoardCreatePage;