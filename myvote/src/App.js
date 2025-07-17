import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Pages/Login";
import ProfilePage from "./Pages/ProfilePage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />}/>
        <Route path="profile" element={<ProfilePage />}/>
      </Routes>
    </Router>
  );
}

export default App;
