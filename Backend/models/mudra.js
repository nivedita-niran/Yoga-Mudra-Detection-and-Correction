import mongoose from "mongoose";

const mudraSchema = new mongoose.Schema({
  mudraName: { type: String, required: true },
  status: { type: String, enum: ["correct", "incorrect"], required: true },
  feedback: { type: String },
  createdAt: { type: Date, default: Date.now },
});

export default mongoose.model("Mudra", mudraSchema);
