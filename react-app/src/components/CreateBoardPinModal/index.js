import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from "react-router-dom";
import "./CreateBoardPinModal.css";
import { useState } from "react";
import { createBoard } from "../../store/boardReducer";
import { boardConfig } from "../../utils/boardConfig"
import { createPin } from "../../store/pinReducer";


function CreateBoardPinModal({pins}) {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const history = useHistory()
  const[kitchen, setKitchen]= useState("");
  const [title, setTitle] = useState(boardConfig[0].kitchen);
  const [description, setDescription] = useState(boardConfig[0].description);
  const [boardImageUrl, setBoardImageUrl] = useState(
    boardConfig[0].board_image_url
  );

  const handleSubmit = async (e) => {
    e.preventDefault();
    const boardId= await dispatch(
        createBoard(
          {
            title,
            description,
            board_image_url: boardImageUrl,
            user_id: user.id,
          },
    
        )
      );
  
      if(boardId){
        dispatch(createPin(pins, boardId))
        closeModal();
        history.push("/boards")
      }
  
   
  };


  return (
    <div className="modal-body">

      <img
        className="modal-logo"
        id="logo"
        alt="food-terest icon"
        src="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690295566/png-clipart-pinterest-logo-pinterest-logo-icons-logos-emojis-tech-companies-thumbnail_qcaaiz.png" />
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
          className="modal-btn confirm"
          type="submit">Create Board</button>
           <button className="modal-btn  cancel" onClick={closeModal}>Cancel</button>
        </form>
      <div className="modal-button-wrapper">
        
       
      </div>
    </div>
  );
}

export default CreateBoardPinModal;
