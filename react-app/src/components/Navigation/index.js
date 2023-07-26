

import React from "react";
import { NavLink } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";


function Navigation() {
  const sessionUser = useSelector((state) => state.session.user);
  const headerLogin = sessionUser ? "header-login" : "";
  const titleLogin = sessionUser ? "title-login" : "";
  return (
    <header className={`header ${headerLogin}`}>
		<div className="container">
		<ul className="navigation">
            <li>
              <NavLink
                className="logo"
                exact
                to={sessionUser ? "/pins" : "/"}
              >
                <img
                  id="logo"
                  alt="food-terest icon"
                  src="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690295566/png-clipart-pinterest-logo-pinterest-logo-icons-logos-emojis-tech-companies-thumbnail_qcaaiz.png"
                />
               
                <h1 className={`title ${titleLogin}`}>Foodterest</h1>
              </NavLink>
            </li>
              <li>
                <ProfileButton user={sessionUser} />
              </li>
          </ul>

		</div>
         
    </header>
  );
}

export default Navigation;