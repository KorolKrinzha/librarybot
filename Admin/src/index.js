import React from "react";
import ReactDOM from "react-dom/client";
import { Home, CreateQuiz, ShowQuizes } from "./pages";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/Header";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <>
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={<CreateQuiz />} />
        <Route path="/show" element={<ShowQuizes />} />
      </Routes>
    </Router>
  </>
);

reportWebVitals();
