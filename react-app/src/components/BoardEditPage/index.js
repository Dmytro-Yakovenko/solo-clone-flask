import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams, Redirect } from "react-router-dom/";
import { editBoard, getAllBoards, getBoardById } from "../../store/boardReducer";
import { boardConfig } from "../../utils/boardConfig";

import "./BoardEditPage.css";
const BoardEditPage = () => {
  const dispatch = useDispatch();
  const { id } = useParams();
  const board = useSelector((state) => state.boards.board);
  const user = useSelector((state) => state.session.user);
  const findedIndex =
    boardConfig.findIndex((item) => item.kitchen === board.title) + 1;
  const boards= useSelector(state=>Object.values(state.boards.boards))
  const boardsTitles =boards.map(item=>item.title)
  const boardTitlesWithoutCurrent = boardsTitles.filter(item=>item!==board.title)

  const filteredBoards=boardConfig.filter(item=>!boardTitlesWithoutCurrent.includes(item.kitchen))

  const [kitchen, setKitchen] = useState(1);
 
  const [title, setTitle] = useState("");
  
  const [description, setDescription] = useState("");
  const [boardImageUrl, setBoardImageUrl] = useState("");
  const history = useHistory();

  useEffect(() => {
    dispatch(getBoardById(id));
    
  }, [dispatch, id]);

  useEffect(() => {
    dispatch(getAllBoards(user.id));
    
  }, [dispatch, user.id]);


  useEffect(() => {
    setKitchen(findedIndex);
    setTitle(board.title);
    setDescription(board.description);
    setBoardImageUrl(board.board_image_url);
  }, [findedIndex, board]);

  const handleChange = (e)=> {
    const finded = filteredBoards.find(item=>item.id=== +e.target.value)
    setKitchen(+e.target.value);
    setTitle(finded.kitchen)
    setBoardImageUrl(finded.board_image_url);
    setDescription(finded.description);
  }

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
  if (!user) {
    return <Redirect to="/" />;
  }

  return (
    <main className="main">
      <div className="container board-edit-page">
        <form className="board-edit-page-form" onSubmit={handleSubmit}>
          <select
            value={kitchen}
            onChange={handleChange}
          >
            {filteredBoards.map((item) => (
              <option key={item.id} value={item.id}>
                {item.kitchen}
              </option>
            ))}
          </select>
          <img
            className="board-edit-page-image"
            src={boardImageUrl}
            alt={title}
          />
          <p>{description}</p>
          <button type="submit">Edit Board</button>
        </form>
      </div>
    </main>
  );
};

export default BoardEditPage;
