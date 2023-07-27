import React, { useEffect } from "react";
import Navigation from "../Navigation";
import "./PinsPage.css";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";
import { useDispatch, useSelector } from "react-redux";
import { getAllPins } from "../../store/pinReducer";
import { NavLink } from "react-router-dom";
const PinsPage = () => {
  const pins = useSelector((state) => Object.values(state.pins.pins));
  console.log(pins, 33333333);
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllPins());
  }, [dispatch]);

  return (
    <>
      <Navigation />
      <div className="container pins-page">
        <h1 className="pins-page-title">Get your next dinner idea </h1>

        <ResponsiveMasonry columnsCountBreakPoints={{ 350: 1, 750: 3, 900: 5 }}>
          <Masonry columnsCount={5}>
            {pins.map((item) => (
              <NavLink to={`/pins/${item.id}`} key={item.alt} className="pins-page-link">
           
    <img className="pins-images" src={item.images} alt={item.title} />
           
              
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
