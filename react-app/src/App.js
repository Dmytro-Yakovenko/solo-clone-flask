import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import AboutPage from "./components/AboutPage";
import BoardsPage from "./components/BoardsPage";
import PinsPage from "./components/PinsPage";
import PinsDetailsPage from "./components/PinsDetailsPage";

import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {isLoaded && (
<>
<Navigation/>

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
  <Route path="/boards/:id/edit">
    {/* <EditFriendPage /> */}
  </Route>
  <Route path="/boards/create">
    {/* <FriendPage /> */}
  </Route>
  <Route path="/pins/create">
    {/* <FriendPage /> */}
  </Route>
  <Route path="/pins/:id/edit">
    {/* <FriendPage /> */}
  </Route>
  <Route path="/boards/:id">
    {/* <FriendPage /> */}
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