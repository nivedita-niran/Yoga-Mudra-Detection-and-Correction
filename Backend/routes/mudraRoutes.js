import express from "express";
import { saveMudra, getMudras } from "../controller/mudracontroller.js";

const router = express.Router();

router.post("/", saveMudra); // Save detection
router.get("/", getMudras); // Fetch all detections

export default router;
