import React from "react";

const Navbar = ({ setActivePage }) => {
  return (
    <nav className="bg-green-100 shadow-md p-4 flex justify-between items-center">
      <h1
        className="text-2xl font-bold text-green-800 cursor-pointer"
        onClick={() => setActivePage("home")}
      >
        Healing Hands
      </h1>
      <ul className="flex gap-6 text-green-700 font-medium">
        <li className="cursor-pointer" onClick={() => setActivePage("home")}>
          Home
        </li>
        <li className="cursor-pointer" onClick={() => setActivePage("about")}>
          About
        </li>
        <li className="cursor-pointer" onClick={() => setActivePage("mudra")}>
          Mudra Detection
        </li>
        <li
          className="cursor-pointer"
          onClick={() => setActivePage("progress")}
        >
          Progress Tracker
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
