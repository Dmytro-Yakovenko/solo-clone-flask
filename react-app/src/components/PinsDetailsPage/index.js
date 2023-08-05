import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, Link, Redirect } from "react-router-dom";
import { getPinById } from "../../store/pinReducer";
import { BsEmojiSunglasses } from "react-icons/bs";
import { createComment } from "../../store/commentReducer";
import DeletePinModal from "../DeletePinModal";
import OpenModalButton from "../OpenModalButton";
import "./PinsDetailsPage.css";
import CreateBoardPinModal from "../CreateBoardPinModal";

const PinsDetailsPage = () => {
  const dispatch = useDispatch();
  const { id } = useParams();

  const pin = useSelector((state) => state.pins.pin);
  const user = useSelector((state) => state.session.user);
  const [comment, setComment] = useState("");
  const [isIngredientsShow, setIngredientsShow] = useState(true);
  const [isCommentsShow, setCommentsShow] = useState(true);
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

  if (!user) {
    return <Redirect to="/" />;
  }

  return (
    <main className="main">
      <div className="container ">
        <div className="pins-details-page">
          <img
            className="image-page-details"
            src={pin.images}
            alt={pin.title}
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
              />
              <p>
                {pin?.user?.first_name} {pin?.user?.last_name}
              </p>
              {pin?.user_id === user.id && (
                <>
                  <Link to={`/pins/${id}/edit`} className="pins-details-update">
                    Update Pin
                  </Link>

                  <OpenModalButton
                    modalComponent={<DeletePinModal id={id} />}
                    buttonText="Delete Pin"
                    className="pins-details-delete"
                  />
                </>
              )}

              {pin?.user_id !== user.id && (
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
                      }}
                    />
                  }
                  buttonText="Save"
                  className="pins-details-update"
                />
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
                    />

                    <p>
                      <span>{item.user.username}</span>: {item.comment}{" "}
                    </p>
                  </li>
                ))}
            </ul>
            <form className="pins-details-form" onClick={handleSubmitComment}>
              <label>
                <img
                  className="user-image-pins-details"
                  src={user?.user_image}
                  alt={user?.username}
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
