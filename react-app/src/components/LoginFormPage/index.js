import React, { useState, useEffect } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { useHistory } from "react-router";
import "./LoginForm.css";

function LoginFormPage() {
  const dispatch = useDispatch();
  const history = useHistory();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const [frontErrors, setFrontErrors] = useState({});
  const [isSubmitted, setIsSubmitted]= useState(false)

  useEffect(() => {
    const errors = {};
    if (email.length < 6) {
      errors.email = "6 characters in email";
    }
    if (password.length < 6) {
      errors.password = "6 characters in password";
    }
    setFrontErrors(errors);
  }, [email, password]);

  if (sessionUser) return <Redirect to="/pins" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitted(true)
    if(frontErrors.email || frontErrors.password){
      return 
    }
  
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      history.push("/pins");
    }
  };

  return (
    <>
      <div className="container form-wrapper">
        <div className="login-form-container">
          <form className="login-form" onSubmit={handleSubmit}>
            <div className="form-logo-wrapper">
              <img
                className="form-logo"
                id="logo"
                alt="food-terest icon"
                src="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690295566/png-clipart-pinterest-logo-pinterest-logo-icons-logos-emojis-tech-companies-thumbnail_qcaaiz.png"
              />
            </div>

            <h1>Log in to see more</h1>
            {errors.length > 0 && (
              <ul>
                {errors.map((error, idx) => (
                  <li key={idx}>{error}</li>
                ))}
              </ul>
            )}
            <div className="input-wrapper">
              <label>Email address</label>
              <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
              {frontErrors.email && isSubmitted && <span className="error">{frontErrors.email}</span>}
            </div>

            <div className="input-wrapper">
              <label>Password</label>
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />

              {frontErrors.password && isSubmitted && (
                <span className="error">{frontErrors.password}</span>
              )}
            </div>

            <button className=" btn primary" type="submit">
              Log in
            </button>
            <button
              className="btn secondary"
              onClick={(e) => {
                setEmail("demo@aa.io");
                setPassword("password");
              }}
            >
              Log In as Demo User
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

export default LoginFormPage;
