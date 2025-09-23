import Mudra from "../models/mudra.js";

// Save mudra detection
export const saveMudra = async (req, res) => {
  try {
    const mudra = new Mudra(req.body);
    const saved = await mudra.save();
    res.status(201).json(saved);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Get all records
export const getMudras = async (req, res) => {
  try {
    const mudras = await Mudra.find().sort({ createdAt: -1 });
    res.json(mudras);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
