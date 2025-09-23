import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import dotenv from "dotenv";
import mudraRoutes from "./routes/mudraRoutes.js";

dotenv.config();
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use("/api/mudras", mudraRoutes);

// Test route
app.get("/", (req, res) => {
  res.send("Healing Hands backend is running ✅");
});

// Connect to MongoDB and start server
const PORT = process.env.PORT || 5000;
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => {
    app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
    console.log("MongoDB connected ✅");
  })
  .catch((err) => console.error(err));
