import TileMap from "./TileMap.js";

const tileSize = 32;
const canvas = document.getElementById("gameCanvas"); // Fix ID typo
const ctx = canvas.getContext("2d");
const tileMap = new TileMap(tileSize); // Rename to tileMap for consistency

function gameLoop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas before redrawing
  tileMap.draw(ctx); // Pass the context to the draw method
}

tileMap.setCanvasSize(canvas); // Set the canvas size based on the map dimensions and tile size
setInterval(gameLoop, 1000 / 60); // Adjust frame rate if needed (60 FPS)

