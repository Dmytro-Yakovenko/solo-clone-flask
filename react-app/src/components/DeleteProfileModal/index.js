import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./DeleteProfileModal.css";

function DeleteProfileModal() {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  
  const handleDelete = async (e) => {
    e.preventDefault();
    alert("this feature coming soon");
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
      <h2>Are you sure you want to delete your profile?</h2>
      <div className="modal-button-wrapper">
        <button className="modal-btn confirm" onClick={handleDelete}>Delete</button>
        <button className="modal-btn  cancel" onClick={closeModal}>Cancel</button>
      </div>
    </div>
  );
}

export default DeleteProfileModal;
