import { Link, useNavigate } from "react-router-dom";
import useGlobalReducer from "../hooks/useGlobalReducer";

export const Navbar = () => {
  const { store, dispatch } = useGlobalReducer();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch({ type: "logout" });
    navigate("/login");
  };

  return (
    <nav className="navbar navbar-light bg-light px-4">
      <Link className="navbar-brand" to="/">My App</Link>
      <div className="d-flex gap-3">
        {store.token ? (
          <>
            <Link className="btn btn-outline-secondary" to="/private">Private</Link>
            <button className="btn btn-outline-danger" onClick={handleLogout}>Logout</button>
          </>
        ) : (
          <>
            <Link className="btn btn-outline-primary" to="/login">Login</Link>
            <Link className="btn btn-primary" to="/signup">Signup</Link>
          </>
        )}
      </div>
    </nav>
  );
};
