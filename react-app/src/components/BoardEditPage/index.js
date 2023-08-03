import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams, Redirect } from "react-router-dom/";
import { editBoard, getBoardById } from "../../store/boardReducer";
import { boardConfig } from "../../utils/boardConfig";

import "./BoardEditPage.css";
const BoardEditPage = () => {
  const dispatch = useDispatch();
  const {id}=useParams();
  const board = useSelector((state)=>state.boards.board)
  const user = useSelector((state) => state.session.user);
  const findedIndex=boardConfig.findIndex(item=>item.kitchen===board.title)+1
  const [kitchen, setKitchen] = useState(1);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [boardImageUrl, setBoardImageUrl] = useState('');
  const history = useHistory();

useEffect(()=>{
    dispatch(getBoardById(id))
},[dispatch, id])

useEffect(()=>{
  setKitchen(findedIndex)
  setTitle(board.title)
  setDescription(board.description)
  setBoardImageUrl(board.board_image_url)
},[findedIndex,board])

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(
      editBoard(
        {
          title,
          description,
          board_image_url: boardImageUrl,
          user_id: user.id,
        },
  id
      )
    );

    history.push("/boards");
  };
  if(!user){
    return <Redirect to="/"/>
  } 

  return (
    <main className="main">
      <div className="container board-edit-page">
        <form className="board-edit-page-form" onSubmit={handleSubmit}>
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
          className="board-edit-page-image"
          src={boardImageUrl} alt={title} />
          <p>{description}</p>
          <button type="submit">Edit Board</button>
        </form>
      </div>
    </main>
  );
};

export default BoardEditPage;