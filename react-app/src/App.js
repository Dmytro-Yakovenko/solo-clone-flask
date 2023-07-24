import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import { createPin, deletePin, editPin, getAllPins, getPinById } from "./store/pinReducer";
import { getAllBoards, createBoard, deleteBoard, getBoardById, editBoard } from "./store/boardReducer";
import { getAllComments, createComment, deleteComment, getCommentById, editComment } from "./store/commentReducer";
function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);
  useEffect(()=>{
    // dispatch(deleteBoard(2))
  },[dispatch])
  useEffect(()=>{
    dispatch(getAllComments())
    // dispatch(getCommentById(25))
    // dispatch(editBoard({id:1, title:"American", description:"Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
    // user_id:1,
    dispatch(editComment({comment:"hello test", user_id:1, pin_id:60, id:119}))
    // image_url:"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690067475/pexels-kamila-bairam-12123657_bplmhe.jpg" }, 1))
  // dispatch(createBoard({ title:"American", user_id:1, description:"mexican street dogs"}))
  },[dispatch])

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
