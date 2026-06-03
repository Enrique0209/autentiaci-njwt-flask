export const initialStore = () => {
  return {
    message: null,
    token: sessionStorage.getItem("token") || null,
    user: null,
  };
};

export default function storeReducer(store, action = {}) {
  switch (action.type) {
    case "set_hello":
      return { ...store, message: action.payload };

    case "login":
      sessionStorage.setItem("token", action.payload.token);
      return {
        ...store,
        token: action.payload.token,
        user: action.payload.user,
      };

    case "logout":
      sessionStorage.removeItem("token");
      return { ...store, token: null, user: null };

    default:
      return store;
  }
}
