import React from "react";
import mudra1 from "./Components/jnana mudra.jpg";
import mudra2 from "./Components/chin mudra.jpg";
import mudra3 from "./Components/bhairava mudra.jpg";
import "./MudraGallery.css"; // create this CSS file

const mudras = [
  { image: mudra1, name: "Mudra One" },
  { image: mudra2, name: "Mudra Two" },
  { image: mudra3, name: "Mudra Three" },
];

function MudraGallery() {
  return (
    <div className="mudra-gallery">
      {mudras.map((mudra, index) => (
        <div className="mudra-item" key={index}>
          <img src={mudra.image} alt={mudra.name} />
          <div className="overlay">{mudra.name}</div>
        </div>
      ))}
    </div>
  );
}

export default MudraGallery;
