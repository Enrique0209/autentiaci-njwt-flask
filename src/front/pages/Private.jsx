import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useGlobalReducer from "../hooks/useGlobalReducer";

export const Private = () => {
  const { store } = useGlobalReducer();
  const navigate = useNavigate();

  useEffect(() => {
    if (!store.token) {
      navigate("/login");
    }
  }, [store.token]);

  if (!store.token) return null;

  return (
    <div className="container mt-5 text-center">
      <div className="card p-5">
        <h1>🔒 Private Page</h1>
        <p className="text-muted mt-3">You are authenticated! Only logged in users can see this.</p>
        <p><strong>Token:</strong> {store.token.substring(0, 20)}...</p>
      </div>
    </div>
  );
};
