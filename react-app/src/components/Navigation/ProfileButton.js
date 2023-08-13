import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { NavLink, useHistory, Link } from "react-router-dom/";


function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const history =useHistory()
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

  const handleError=(e)=>{
    e.target.src="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691812110/776229ef8d0028f88330a492116ab40b_zelqge.jpg"
  }

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push("/")
  };
  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

  return (
    <>
      <ul className="navigation-menu" ref={ulRef}>
        {user ? (
          <>
            <Link to ="/boards" className="nav-profile-btn" >
            All my boards
             
            </Link>
            <button
            onClick={openMenu}
            className="nav-btn"
            >
              <img 
              src={user.user_image} 
              alt={user.username}
              onError={handleError}
              />
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
              <NavLink to={`/users/${user.id}/edit`} className="navigation-link nav-login">
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