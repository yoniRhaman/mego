import express from "express";
import bodyParser from "body-parser";
import mongoose from "mongoose";
import cors from "cors";
import multer from "multer";
import helmet from "helmet";
import morgan from "morgan";
import Path from "mongoose";
import { fileURLToPath } from "url";
import path from "path";
import dotenv from "dotenv";
import authRoutes from "./routes/auth.js";
import userRoutes from "./routes/users.js";
import postRoutes from "./routes/posts.js";

/* CONFIGURATIONS */
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment variables from .env file
dotenv.config();

// Create an Express application instance
const app = express();

// Middleware setup
// Parse incoming JSON requests
app.use(express.json());

// Helmet middleware for securing HTTP headers
app.use(helmet());

// Set Cross-Origin Resource Sharing policy to allow cross-origin requests
app.use(helmet.crossOriginResourcePolicy({ policy: "cross-origin" }));

// Morgan middleware for logging HTTP requests
app.use(morgan("common"));

// Parse URL-encoded requests with body-parser
app.use(bodyParser.json({ limit: "30mb", extended: true }));
app.use(bodyParser.urlencoded({ limit: "30mb", extended: true }));

// Enable CORS for all routes
app.use(cors());

// Serve static files from the 'public/assets' directory
app.use("/assets", express.static(path.join(__dirname, "public/assets")));

/* FILE STORAGE */

// Define storage settings using multer's diskStorage
const storage = multer.diskStorage({
  // Set the destination directory where uploaded files will be stored
  destination: function (req, file, cb) {
    cb(null, "public/assets");
  },
  // Set the filename for the uploaded file
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  },
});

// Create an instance of multer with the defined storage settings
const upload = multer({ storage });

/* ROUTES WITH FILES */
app.post("/auth/register", upload.single("picture"), register);
app.post("/posts", verifyToken, upload.single("picture"), createPost);


/* ROUTES */
app.use("/auth", authRoutes);
app.use("/users", userRoutes);
app.use("/posts", postRoutes);

/* MONGOOSE SETUP */

// Define the port number for the server
const PORT = process.env.PORT || 6001;

// Connect to MongoDB using Mongoose
mongoose
  .connect(process.env.MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    // Once connected to the database, start the Express server
    app.listen(PORT, () => console.log(`Server Port: ${PORT}`));
  })
  .catch((error) => {
    // If there's an error connecting to the database, log the error
    console.error("Error connecting to MongoDB:", error.message);
  });
