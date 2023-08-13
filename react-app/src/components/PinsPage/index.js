import React, { useEffect } from "react";
import "./PinsPage.css";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";
import { useDispatch, useSelector } from "react-redux";
import { getAllPins } from "../../store/pinReducer";
import { NavLink, Redirect} from "react-router-dom";



const PinsPage = () => {
  const user = useSelector(state=>state.session.user)
 
  const pins = useSelector((state) => Object.values(state.pins.pins));
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllPins());
  }, [dispatch]);
  if(!user){
    return <Redirect to="/"/>
  } 


const handleError=(e)=>{
e.target.src ="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691726195/bc2d04276b5bfde9bce68c7a91914b7f_mi6kmp.jpg"
}

  return (
    <>
      <div className="container pins-page">
        <h1 className="pins-page-title">Get your next dinner idea </h1>

        <ResponsiveMasonry
          columnsCountBreakPoints={{ 350: 1, 700: 2, 900: 3, 1000: 5 }}
        >
          <Masonry columnsCount={5}>
            {pins.map((item) => (
              <NavLink
                to={`/pins/${item.id}`}
                key={item.id}
                className="pins-page-link"
              >
                <img
                  className="pins-images"
                  src={item.images}
                  alt={item.title}
                  onError={handleError}
                />

                <h4>{item.title}</h4>
              </NavLink>
            ))}
          </Masonry>
        </ResponsiveMasonry>
      </div>
    </>
  );
};

export default PinsPage;
