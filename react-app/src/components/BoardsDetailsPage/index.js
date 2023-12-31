import React, { useEffect, useState } from "react";
import "./BoardDetailsPage.css";
import { useDispatch, useSelector } from "react-redux";
import { getBoardById } from "../../store/boardReducer";
import { useParams, Link, Redirect } from "react-router-dom";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";
import { RiDeleteBin6Line } from "react-icons/ri";
import { LuEdit } from "react-icons/lu";
import DeleteProfileModal from "../DeleteProfileModal";
import OpenModalButton from "../OpenModalButton";
import DeleteBoardModal from "../DeleteBoardModal";
const BoardDetailsPage = () => {
  const dispatch = useDispatch();
  const { id } = useParams();
  const board = useSelector((state) => state.boards.board);
  const user = useSelector((state) => state.session.user);
  const colImages = board?.pins?.length < 5 ? board?.pins?.length : 5;
  const [shadow, setShadow] = useState(false);
  useEffect(() => {
    dispatch(getBoardById(id));
  }, [dispatch, id]);
  if (!user) {
    return <Redirect to="/" />;
  }
  const handleError=(e)=>{
    e.target.src="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691812110/776229ef8d0028f88330a492116ab40b_zelqge.jpg"
  }

  const handlePinError=(e)=>{
    e.target.src ="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691726195/bc2d04276b5bfde9bce68c7a91914b7f_mi6kmp.jpg"
    }
  return (
    <main className="main">
      <div className="container">
        <section className="board-details-page-profile">
          <img
            className="board-details-page-image"
            src={user.user_image}
            alt={user.username}
            onError={handleError}
          />
          <h3>
            {user.first_name} {user.last_name}
          </h3>
          <p>{user.email}</p>
          <div className="board-details-page-btn-wrapper">
            <Link
              to={`/users/${user.id}/edit`}
              className="board-detail-btn board-detail-btn-edit"
            >
              Edit Profile
            </Link>

            <OpenModalButton
              modalComponent={<DeleteProfileModal />}
              buttonText="Delete Profile"
              className="board-detail-btn board-detail-btn-delete"
            />
          </div>
        </section>

        <div className="board-details-wrapper">
          <h2>{board.title}</h2>
          <div
            className="board-details-shadow"
            onMouseOver={() => setShadow(true)}
            onMouseLeave={() => setShadow(false)}
          >
            <img
              className="board-details-page-board"
              src={board.board_image_url}
              alt={board?.title}
            />
            {shadow && (
              <div className="wrapper">
                <OpenModalButton
                  modalComponent={<DeleteBoardModal id={id} />}
                  buttonText={<RiDeleteBin6Line className="icon" />}
                  className="board-details-page-delete-btn"
                />
                <Link to={`/boards/${id}/edit`}>
                  <LuEdit className="icon" />
                </Link>
              </div>
            )}
          </div>
        </div>
        <h4 className="board-details-page-subtitle">Your dinner ideas</h4>

        <section className="board-details-page-section">
        {!!board?.pins?.length &&   <ResponsiveMasonry
          
          columnsCountBreakPoints={{
            350: 1,
            700: 2,
            900: 3,
            1000: colImages,
          }}
        >
          <Masonry columnsCount={colImages}>

            {board?.pins?.map((item) => (
              <Link
                key={item.id}
                className="boards-page-link"
                to={`/pins/${item.id}`}
              >
                <img
                  className="boards-image"
                  src={item.images}
                  alt={item.title}
                  onError={handlePinError}
                />
                <h4>{item.title}</h4>
              </Link>
            ))}
          </Masonry>
        </ResponsiveMasonry>}
        
        </section>
      </div>
    </main>
  );
};

export default BoardDetailsPage;
