import React, { useState } from "react";
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

  if (sessionUser) return <Redirect to="/pins" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
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
            </div>

            <div className="input-wrapper" >
              <label>Password</label>
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
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
