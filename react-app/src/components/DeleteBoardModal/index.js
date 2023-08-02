import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteBoard } from "../../store/boardReducer";
import { useHistory } from "react-router-dom";
// import "./DeleteProfileModal.css";

function DeleteBoardModal({id}) {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  const history = useHistory()
  const handleDelete = async (e) => {
    e.preventDefault();
    dispatch(deleteBoard(id));
    history.push("/boards")
    closeModal();
  };

  return (
    <div className="modal-body">

      <img
        className="modal-logo"
        id="logo"
        alt="food-terest icon"
        src="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690295566/png-clipart-pinterest-logo-pinterest-logo-icons-logos-emojis-tech-companies-thumbnail_qcaaiz.png"
      />
      <h2>Are you sure you want to delete your board?</h2>
      <div className="modal-button-wrapper">
        <button className="modal-btn confirm" onClick={handleDelete}>Delete</button>
        <button className="modal-btn  cancel" onClick={closeModal}>Cancel</button>
      </div>
    </div>
  );
}

export default DeleteBoardModal;
