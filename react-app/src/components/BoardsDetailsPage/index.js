import React, { useEffect, useState } from "react";
import "./BoardDetailsPage.css";
import { useDispatch, useSelector } from "react-redux";
import { getBoardById } from "../../store/boardReducer";
import { useParams, Link, Redirect} from "react-router-dom";
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

  console.log(board.pins);
  useEffect(() => {
    dispatch(getBoardById(id));
  }, [dispatch, id]);
  if(!user){
    return <Redirect to="/"/>
  } 

  return (
    <main className="main">
      <div className="container">
        <section className="board-details-page-profile">
          <img
            className="board-details-page-image"
            src={user.user_image}
            alt={user.username}
          />
          <h3>
            {user.first_name} {user.last_name}
          </h3>
          <p>{user.email}</p>
          <div className="board-details-page-btn-wrapper">
            <button className="board-detail-btn board-detail-btn-edit">
              Edit Profile
            </button>

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
              alt={board.title}
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
          <ResponsiveMasonry
            columnsCountBreakPoints={{
              350: 1,
              700: 2,
              900: 3,
              1000: colImages,
            }}
          >
            <Masonry columnsCount={5}>
              {board?.pins?.map((item) => (
                <Link className="boards-page-link" to={`/pins/${item.id}`}>
                  <img
                    className="boards-image"
                    src={item.images}
                    alt={item.title}
                  />
                  <h4>{item.title}</h4>
                </Link>
              ))}
            </Masonry>
          </ResponsiveMasonry>
        </section>
      </div>
    </main>
  );
};

export default BoardDetailsPage;
