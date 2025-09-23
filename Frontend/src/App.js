import React, { useState } from "react";
import "./App.css";
import Navbar from "./Components/Navbar";
import Home from "./pages/Home";
import About from "./pages/About Us";
import MudraDetection from "./pages/MudraDetection";
import ProgressTracker from "./pages/Progress";

function App() {
  const [activePage, setActivePage] = useState("home");

  const renderPage = () => {
    switch (activePage) {
      case "about":
        return <About />;
      case "mudra":
        return <MudraDetection />;
      case "progress":
        return <ProgressTracker />;
      default:
        return <Home />;
    }
  };

  return (
    <div className="min-h-screen bg-green-50 text-gray-800">
      <Navbar setActivePage={setActivePage} />
      <main className="p-6">{renderPage()}</main>
    </div>
  );
}

export default App;
