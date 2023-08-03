import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Route, Switch, Link, Redirect } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import AboutPage from "./components/AboutPage";
import BoardsPage from "./components/BoardsPage";
import PinsPage from "./components/PinsPage";
import PinsDetailsPage from "./components/PinsDetailsPage";
import { TiPlus } from "react-icons/ti";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import PinCreate from "./components/PinCreatePage";
import PinEditPage from "./components/PinEditPage";
import BoardCreatePage from "./components/BoardCreatePage";
import BoardEditPage from "./components/BoardEditPage";
import BoardDetailsPage from "./components/BoardsDetailsPage";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const [isShowPopUpBoard, setIsShowPopUpBoard] = useState(false);
  const [isShowPopUpPin, setIsShowPopUpPin] = useState(false);
  const user = useSelector((state) => state.session.user);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);
  
  return (
    <>
      {isLoaded && (
        <>
          <Navigation />
          {user && (
            <Link
              onMouseOver={() => setIsShowPopUpPin(true)}
              onMouseLeave={() => setIsShowPopUpPin(false)}
              to="/pins/create"
              className="btn-fix btn-fix-right"
            >
              <TiPlus className="plus-icon plus-icon-right" />
              {isShowPopUpPin && (
                <span className="btn-fix-span btn-fix-span-right">
                  Create Pin
                </span>
              )}
            </Link>
          )}
          {user && (
            <Link
              onMouseOver={() => setIsShowPopUpBoard(true)}
              onMouseLeave={() => setIsShowPopUpBoard(false)}
              to="/boards/create"
              className="btn-fix btn-fix-left"
            >
              <TiPlus className="plus-icon plus-icon-left" />
              {isShowPopUpBoard && (
                <span className="btn-fix-span">Create Board</span>
              )}
            </Link>
          )}

          <Switch>
            <Route exact path="/">
              <AboutPage />
            </Route>
            <Route path="/login">
              <LoginFormPage />
            </Route>
            <Route path="/signup">
              <SignupFormPage />
            </Route>
            <Route exact path="/pins">
              <PinsPage />
            </Route>
            <Route exact path="/boards">
              <BoardsPage />
            </Route>

            <Route path="/boards/:id/edit">
              <BoardEditPage />
            </Route>
            <Route path="/boards/create">
              <BoardCreatePage />
            </Route>
            <Route path="/pins/create">
              <PinCreate />
            </Route>
            <Route path="/pins/:id/edit">
              <PinEditPage />
            </Route>
            <Route path="/boards/:id">
              <BoardDetailsPage/>
            </Route>
            <Route path="/pins/:id">
              <PinsDetailsPage />
            </Route>
          </Switch>
        </>
      )}
    </>
  );
}

export default App;
