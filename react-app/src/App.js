import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Route, Switch, Link } from "react-router-dom";
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

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
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
            <Link to="/pins/create" className="btn_fix btn_fix_right">
              <TiPlus className="plus-icon plus-icon_right" />
            </Link>
          )}
            {user && (
            <Link to="/boards/create" className="btn_fix btn_fix_left">
              <TiPlus className="plus-icon plus-icon_left" />
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
            <Route path="/boards">
              <BoardsPage />
            </Route>

            <Route path="/boards/:id/edit">{/* <EditFriendPage /> */}</Route>
            <Route path="/boards/create"><BoardCreatePage/></Route>
            <Route path="/pins/create">{<PinCreate />}</Route>
            <Route path="/pins/:id/edit">{<PinEditPage />}</Route>
            <Route path="/boards/:id"></Route>
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
