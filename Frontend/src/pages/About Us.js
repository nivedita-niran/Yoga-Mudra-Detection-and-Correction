// src/pages/About.js
import React from "react";

function About() {
  return (
    <div className="app-main">
      <header className="app-header">
        <h1>About Healing Hands</h1>
      </header>
      <main>
        <section>
          <h2>Our Mission</h2>
          <p>
            Healing Hands is dedicated to helping yoga practitioners perfect
            their mudras using AI-powered recognition and real-time corrections.
          </p>
        </section>

        <section>
          <h2>Our Team</h2>
          <p>
            We are a team of developers, yoga enthusiasts, and AI researchers
            committed to bridging technology and wellness.
          </p>
        </section>

        <section>
          <h2>Contact</h2>
          <p>Email: contact@healinghands.com</p>
        </section>
      </main>
    </div>
  );
}

export default About;
