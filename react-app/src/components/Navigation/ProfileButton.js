import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { NavLink } from "react-router-dom/";

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;
    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };
    document.addEventListener("click", closeMenu);
    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);
console.log(user, 444444)
  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };
  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

  return (
    <>
      <ul className="navigation-menu" ref={ulRef}>
        {user ? (
          <>
            <button className="nav-btn" onClick={openMenu}>
              <img src={user.user_image} alt={user.username} />
              <span>{user.username}</span>
            </button>
            <ul className={ulClassName}>
              <li> Hello, </li>
              <li>{user.first_name} {user.last_name}!</li>
              <li>
              <NavLink to="/pins/create" className="navigation-link nav-login">
                Create Pin
              </NavLink>
            </li>

            <li>
              <NavLink to="/boards/create" className="navigation-link nav-login">
                Create Board
              </NavLink>
            </li>
            <li>
              <NavLink to={`/${user.id}/edit`} className="navigation-link nav-login">
                Edit User
              </NavLink>
            </li>
            
              <button className="log-out" onClick={handleLogout}>
                Log Out
              </button>
            </ul>
          </>
        ) : (
          <>
            <li>
              <NavLink to="/login" className="navigation-link nav-login">
                Log in
              </NavLink>
            </li>
            <li>
              <NavLink to="/signup" className="navigation-link nav-signup">
                Sign up
              </NavLink>
            </li>
         
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;