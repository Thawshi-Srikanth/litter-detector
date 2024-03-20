### Installation

1. **Clone the Repository**: First, clone the `litter-detector` repository to your local machine. Open your terminal and run:

   ```
   git clone https://github.com/Thawshi-Srikanth/litter-detector.git
   ```

2. **Navigate to the Front-End Directory**: Change your current directory to the front-end directory of the project:

   ```
   cd litter-detector/front-end
   ```

3. **Install Dependencies**: Install the necessary Node.js packages by running:
   ```
   npm install
   ```
   This command installs `axios` for making HTTP requests, `form-data` for handling form data, and `fs` for file system operations, as specified in `@app.js`.

### Running the Application

To run the application, execute the following command in your terminal:

```
node app.js
```

This command will start the script in `@app.js`, which sends an image (`band.png`) to the back-end server running on `http://localhost:5000/predict`. The server is expected to process the image and return the prediction results, which are then logged to the console.

### Note

- Ensure that the back-end server is running and accessible at `http://localhost:5000/predict` before executing `app.js`.
- The image `band.png` used in this example is hardcoded in `@app.js`. You can replace it with any other image file you wish to analyze.
