// Define a class named TileMap
export default class TileMap {
    // Constructor takes a parameter tileSize
    constructor(tileSize) {
        // Initialize the tileSize property with the provided value
        this.tileSize = tileSize;

        // Load images for tiles (yellowDot and wall)
        this.yellowDot = new Image();
        this.yellowDot.src = "images/yellowdot.png"; // Adjust the image paths

        this.wall = new Image();
        this.wall.src = "images/wall.png"; // Adjust the image paths
    }

    // 2D array representing the map layout
    map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ];

    // Method to draw the map on the canvas
    draw(ctx) {
        // Iterate through each row in the map
        for (let row = 0; row < this.map.length; row++) {
            // Iterate through each column in the current row
            for (let column = 0; column < this.map[row].length; column++) {
                // Get the value of the current tile in the map
                let tile = this.map[row][column];

                // Check if the current tile is a wall (value of 1)
                if (tile === 1) {
                    // If it is a wall, call the private #drawWall method to draw it
                    this.drawWall(ctx, column, row, this.tileSize);
                } else if (tile === 0) {
                    // If it is a dot (value of 0), call the private #drawDot method to draw it
                    this.drawDot(ctx, column, row, this.tileSize);
                }
            }
        }
    }

    // Private method to draw a yellow dot on the canvas
    drawDot(ctx, column, row, size) {
        ctx.drawImage(this.yellowDot, column * this.tileSize, row * this.tileSize, size, size);
    }

    // Private method to draw a wall on the canvas
    drawWall(ctx, column, row, size) {
        // Use the canvas 2D rendering context to draw the wall image at the specified position
        ctx.drawImage(
            this.wall,                  // Image to be drawn (wall image in this case)
            column * this.tileSize,    // X-coordinate of the top-left corner of the image
            row * this.tileSize,       // Y-coordinate of the top-left corner of the image
            size,                      // Width of the image
            size                       // Height of the image
        );
    }

    // Set the canvas size based on the map dimensions and tile size
    setCanvasSize(canvas) {
        // Set the width of the canvas to the total width of the tile map
        canvas.width = this.map[0].length * this.tileSize;

        // Set the height of the canvas to the total height of the tile map
        canvas.height = this.map.length * this.tileSize;
    }
}
