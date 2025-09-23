import React from "react";
import { useNavigate } from "react-router-dom";
import mudra1 from "../Components/jnana mudra.jpg"; // Update paths for your images
import mudra2 from "../Components/chin mudra.jpg";
import mudra3 from "../Components/bhairava mudra.jpg";
import "./Home.css"; // CSS for hover overlay effect

function Home() {
  const navigate = useNavigate();

  const mudras = [
    { img: mudra1, name: "Jnana Mudra", path: "/detect" },
    { img: mudra2, name: "Chin Mudra", path: "/progress" },
    { img: mudra3, name: "Bhairava Mudra", path: "/about" },
  ];

  return (
    <div className="app-main">
      <header className="app-header">
        <h1>Healing Hands</h1>
        <p>Your Yoga Mudra Recognition & Correction App</p>
      </header>

      <section className="welcome">
        <h2>Welcome 🙏</h2>
        <p>Practice yoga mudras and get real-time AI corrections!</p>
        <div className="mudra-gallery">
          {mudras.map(({ img, name, path }, idx) => (
            <div
              className="mudra-item"
              key={idx}
              onClick={() => navigate(path)}
              tabIndex={0}
              role="button"
              onKeyDown={(e) => {
                if (e.key === "Enter") navigate(path);
              }}
            >
              <img src={img} alt={name} />
              <div className="overlay">{name}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default Home;
