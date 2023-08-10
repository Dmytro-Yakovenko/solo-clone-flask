import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [userImage, setUserImage] = useState("");

  const [errors, setErrors] = useState([]);
  const [frontErrors, setFrontErrors] = useState({});
  const [isSubmitted, setIsSubmitted]= useState(false)

  useEffect(() => {
    const errors = {};
    if (email.length < 6 || email.length>50) {
      errors.email = "At least 6 characters in email but less than 50 characters";
    }
    if (username.length < 2 || username.length >50) {
      errors.username = "At least 2 characters in username but less than 50 characters";
    }
    if (password.length < 6 || password.length >50) {
      errors.password = "At least 6 characters in password but less than 50 characters";
    }
    if (confirmPassword.length < 6 || confirmPassword.length >50) {
      errors.confirmPassword= "At least 6 characters in confirm password but less than 50 characters";
    }
    if (firstName.length < 2 || firstName.length>50) {
      errors.firstName = "At least 6 characters in first name but less than 50 characters";
    }
    if (lastName.length < 2 || lastName.length > 50){
      errors.lastName = "At least 2 characters in last name but less than 50 characters";
    }
    if (userImage.length < 2){
      errors.userImage = "2 characters in user image";
    }



    setFrontErrors(errors);
  }, [email, password, confirmPassword, userImage, firstName, lastName, username]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitted(true)
      if(frontErrors.email || frontErrors.password || frontErrors.confirmPassword || frontErrors.userImage || frontErrors.lastName || frontErrors.firstName || frontErrors.username ){
        return 
      }
    
    if (password === confirmPassword) {
      const data = await dispatch(signUp(username, email, password, firstName, lastName, userImage));
      if (data) {
        setErrors(data);
      }
    } else {
      setErrors([
        "Confirm Password field must be the same as the Password field",
      ]);
    }
  };

  return (
    <>
      <div className="container form-wrapper-signup">
        <div className="signup-form-container">
          <form className="signup-form" onSubmit={handleSubmit}>
            <div className="form-logo-wrapper">
              <img
                className="form-logo"
                id="logo"
                alt="food-terest icon"
                src="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690295566/png-clipart-pinterest-logo-pinterest-logo-icons-logos-emojis-tech-companies-thumbnail_qcaaiz.png"
              />
            </div>

            <h1>Sign up to see more</h1>
            <ul>
              {errors.map((error, idx) => (
                <li key={idx}>{error}</li>
              ))}
            </ul>

            <div className="input-wrapper">
              <label>Username</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
               {frontErrors.username && isSubmitted && <span className="error">{frontErrors.username}</span>}
            </div>

            <div className="input-wrapper">
              <label>Email</label>
              <input
                type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
               {frontErrors.email && isSubmitted && <span className="error">{frontErrors.email}</span>}
            </div>

            <div className="input-wrapper">
              <label>First name</label>
              <input
                type="text"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                required
              />
               {frontErrors.firstName && isSubmitted && <span className="error">{frontErrors.firstName}</span>}
            </div>

            <div className="input-wrapper">
              <label>Last name</label>
              <input
                type="text"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                required
              />
               {frontErrors.lastName && isSubmitted && <span className="error">{frontErrors.lastName}</span>}
            </div>

            <div className="input-wrapper">
              <label>User Image</label>
              <input
                type="text"
                value={userImage}
                onChange={(e) => setUserImage(e.target.value)}
                required
              />
               {frontErrors.userImage && isSubmitted && <span className="error">{frontErrors.userImage}</span>}
            </div>

            <div className="input-wrapper">
              <label>Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
               {frontErrors.password && isSubmitted && <span className="error">{frontErrors.password}</span>}
            </div>

            <div className="input-wrapper">
              <label>Confirm Password</label>
              <input
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
              />
               {frontErrors.confirmPassword && isSubmitted && <span className="error">{frontErrors.confirmPassword}</span>}
            </div>

            <button className="btn primary" type="submit">Sign Up</button>
          </form>
        </div>
      </div>
    </>
  );
}

export default SignupFormPage;
