import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, Link, Redirect } from "react-router-dom";
import { createPin, getPinById } from "../../store/pinReducer";
import { BsEmojiSunglasses } from "react-icons/bs";
import {
  createComment,
  deleteComment,
  editComment,
} from "../../store/commentReducer";
import DeletePinModal from "../DeletePinModal";
import OpenModalButton from "../OpenModalButton";

import "./PinsDetailsPage.css";
import CreateBoardPinModal from "../CreateBoardPinModal";
import { getBoardById } from "../../store/boardReducer";
import { ImCross } from "react-icons/im";
import { FiEdit } from "react-icons/fi";
import { useHistory } from "react-router-dom";

const PinsDetailsPage = () => {
  const dispatch = useDispatch();
  const { id } = useParams();

  const pin = useSelector((state) => state.pins.pin);
  const user = useSelector((state) => state.session.user);
  const board = useSelector((state) => state.boards.board);
  const history = useHistory()
  const [comment, setComment] = useState("");
  const [isIngredientsShow, setIngredientsShow] = useState(true);
  const [isCommentsShow, setCommentsShow] = useState(true);
  const [isEditComment, setEditComment] = useState(false);
  const [commentId, setCommentId] = useState(null);
  const [commentEdit, setCommentEdit] = useState("");

  useEffect(() => {
    if (pin?.board_id?.board_id) {
      dispatch(getBoardById(pin?.board_id?.board_id));
    }
  }, [dispatch, pin]);

  useEffect(() => {
    dispatch(getPinById(id));
  }, [dispatch, id]);

  const handleSubmitComment = (e) => {
    e.preventDefault();
    dispatch(
      createComment(
        {
          comment,
          user_id: user.id,
          pin_id: id,
        },
        id
      )
    );
    setComment("");
  };

  const handleEditComment = (id,comment) => {
    setEditComment(true);
    setCommentId(id);
    setCommentEdit(comment)
  };

  const handleSubmitEditComment = (e) => {
    e.preventDefault();
    dispatch(
      editComment({
        pin_id: id,
        id: commentId,
        comment: commentEdit,
      })
    );
    setCommentEdit();
    setEditComment(false);
    setCommentId(null);
  };

  const handleDeleteComment = (commentId) => {
    dispatch(deleteComment(commentId, id));
  };

  if (!user) {
    return <Redirect to="/" />;
  }

  const handleError = (e) => {
    e.target.src =
      "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691812110/776229ef8d0028f88330a492116ab40b_zelqge.jpg";
  };

  const handlePinError = (e) => {
    e.target.src =
      "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691726195/bc2d04276b5bfde9bce68c7a91914b7f_mi6kmp.jpg";
  };


  const handleClick = (e)=> {
    e.preventDefault();
    dispatch(
      createPin({
        title: pin.title,
        description: pin.description,
        time: pin.time,
        ingredients: pin.ingredients,
        user_id: user.id,
        image_url: pin.images,
       
      }, 1)
     
    )
     history.push('/boards')

  }

  return (
    <main className="main">
      <div className="container ">
        <div className="pins-details-page">
          <img
            className="image-page-details"
            src={pin.images}
            alt={pin.title}
            onError={handlePinError}
          />
          <section>
            <h2 className="title-pins-details-page">{pin.title}</h2>
            <p className="title-pins-details-page"> Cooking time: {pin.time}</p>

            <ol className="pins-details-page-order-list">
              {pin?.description?.split(".").map((item, index) => (
                <li className="pins-details-page-text" key={index}>
                  {item}{" "}
                </li>
              ))}
            </ol>

            <div className="user-pins-details-page">
              <img
                className="user-image-pins-details"
                src={pin?.user?.user_image}
                alt={pin?.user?.usarname}
                onError={handleError}
              />
              <p>
                {pin?.user?.first_name} {pin?.user?.last_name}
              </p>
              {pin?.user_id === user.id && (
                <>
                  {!pin.is_saved && (
                    <Link
                      to={`/pins/${id}/edit`}
                      className="pins-details-update"
                    >
                      Update Pin
                    </Link>
                  )}

                  <OpenModalButton
                    modalComponent={<DeletePinModal id={id} />}
                    buttonText="Delete Pin"
                    className="pins-details-delete"
                  />
                </>
              )}

              {pin?.user_id !== user.id && (
                <>
                
                <OpenModalButton
                  modalComponent={
                    <CreateBoardPinModal
                      pins={{
                        title: pin.title,
                        description: pin.description,
                        time: pin.time,
                        ingredients: pin.ingredients,
                        user_id: user.id,
                        image_url: pin.images,
                        is_saved: true,
                        board,
                      }}
                    />
                  }
                  buttonText="Save"
                  className="pins-details-update"
                />
                <button
                  className="pins-details-update"
           
                  onClick ={handleClick}
                >
                  Save
                </button>
                </>
              )}
            </div>
            <div className="pins-details-ingredients-wrapper">
              <h6 className="pins-details-page-subtitle">Ingredients</h6>
              <button
                className="pins-details-primary"
                onClick={() => setIngredientsShow(!isIngredientsShow)}
              >
                {isIngredientsShow ? "hide" : "show"}
              </button>
            </div>
            {isIngredientsShow && (
              <ul>
                {pin?.ingredients?.split(".").map((item, index) => (
                  <li className="pins-details-page-text" key={index}>
                    {item}{" "}
                  </li>
                ))}
              </ul>
            )}
            <div className="pins-details-ingredients-wrapper">
              <h6 className="pins-details-page-subtitle ">Comments</h6>
              <button
                className="pins-details-primary"
                onClick={() => setCommentsShow(!isCommentsShow)}
              >
                {isCommentsShow ? "less..." : "more..."}
              </button>
            </div>

            <ul>
              {isCommentsShow &&
                pin?.comments?.map((item) => (
                  <li className="pins-details-comment-item" key={item.id}>
                    <img
                      className="user-image-pins-details"
                      src={item.user.user_image}
                      alt="item.user.username"
                      onError={handleError}
                    />
                    {isEditComment && commentId === item.id ? (
                      <form
                        className="form-edit"
                        onSubmit={handleSubmitEditComment}
                      >
                        <textarea
                          rows="5"
                          cols="50"
                          required
                          value={commentEdit}
                          onChange={(e) => setCommentEdit(e.target.value)}
                        ></textarea>
                        <div
                        className="form-wrapper-button"
                        >
                          <button
                            type="submit"
                            className=" pins-details-update"
                          >
                            Edit Comment
                          </button>

                          <button
                            className=" pins-details-delete"
                            onClick={() => {
                              setEditComment(false);
                              setCommentEdit(item.comment);
                              setCommentId(null);
                            }}
                          >
                            Cancel
                          </button>
                        </div>
                      </form>
                    ) : (
                      <>
                        <p>
                          <span>{item.user.username}</span>: {item.comment}{" "}
                        </p>
                        {user.id===item.user_id && 
                          <>
                            <FiEdit
                              className="edit-comment"
                              onClick={() => handleEditComment(item.id, item.comment)}
                            />

                            <ImCross
                              className="delete-comment"
                              onClick={(e) => handleDeleteComment(item.id)}
                            />
                          </>
                        }
                      </>
                    )}
                  </li>
                ))}
            </ul>
            <form className="pins-details-form" onClick={handleSubmitComment}>
              <label>
                <img
                  className="user-image-pins-details"
                  src={user?.user_image}
                  alt={user?.username}
                  onError={handleError}
                />
              </label>
              <textarea
                required
                rows="5"
                cols="50"
                placeholder="Add comment"
                value={comment}
                onChange={(e) => setComment(e.target.value)}
              ></textarea>
              <button className="pins-details-emogi-btn" type="submit">
                <BsEmojiSunglasses className="pins-details-emogi" />
              </button>
            </form>
          </section>
        </div>
      </div>
    </main>
  );
};

export default PinsDetailsPage;
