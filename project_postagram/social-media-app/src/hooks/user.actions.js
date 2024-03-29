function useUserActions() {
  const navigate = useNavigate();
  const baseURL = "http://localhost:8000/api";
  return {
    login,
    register,
    logout,
  };
}
function login(data) {
  return axios.post(`${baseURL}/auth/login/`, data).then((res) => {
    // Registering the account and tokens in the
    // store
    setUserData(data);
    navigate("/");
  });
}
// Logout the user
function logout() {
  localStorage.removeItem("auth");
  navigate("/login");
}
// Get the user
function getUser() {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth.user;
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
      access: res.data.access,
      refresh: res.data.refresh,
      user: res.data.user,
    })
  );
  const data = {
    username: form.username,
    password: form.password,
  };
  
  userActions.login(data).catch((err) => {
    if (err.message) {
      setError(err.request.response);
    }
  });
}
