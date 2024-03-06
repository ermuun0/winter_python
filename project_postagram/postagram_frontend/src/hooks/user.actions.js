import { useNavigate } from "react-router-dom";
import axios from "axios";

function useUserActions() {
  const navigate = useNavigate();
  const baseURL = "http://localhost:8000/api";
  return {
    login,
    register,
    logout,
  };
  function login(data) {
    return axios.post(`${baseURL}/auth/login/`, data).then((res) => {
      // Registering the account and tokens in the
      // store
      setUserData(res);
      navigate("/");
    });
  }
  function register(data){
    return axios.post(`${baseURL}/auth/register/`, data).then((res) => {
      setUserData(res);
      navigate("/")
    })
  }
  // Logout the user
  function logout() {
    localStorage.removeItem("auth");
    navigate("/login");
  }


}

// Get the user
function getUser() {
  const auth = JSON.parse(localStorage.getItem("auth"));
  if (auth){
    return auth.user
  }else{
    null;
  }
}
// Get the access token
function getAccessToken() {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth.access;
}
// Get the refresh token
function getRefreshToken() {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth.refresh;
}
// Set the access, token and user property
function setUserData(data) {
  localStorage.setItem(
    "auth",
    JSON.stringify({
      access: data.access,
      refresh: data.refresh,
      user: data.user,
    })
  );
  
}

export {useUserActions, getUser, getAccessToken, getRefreshToken}