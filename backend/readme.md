## Back-End Setup

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python**: This project requires Python 3.6 or higher. You can download it from the [Python official website](https://www.python.org/downloads/).
- **pip**: pip is a package manager for Python. It is usually installed with Python.

### Installation

1. **Clone the Repository**: First, clone the `litter-detector` repository to your local machine. Open your terminal and run:

git clone https://github.com/Thawshi-Srikanth/litter-detector.git

```
Replace `yourusername` with the actual username of the repository owner.

2. **Navigate to the Back-End Directory**: Change your current directory to the back-end directory of the project:
```

cd litter-detector/backend

```

3. **Install Dependencies**: Install the necessary Python packages by running:
```

pip install -r requirements.txt

```
This command installs Flask, TensorFlow, and other dependencies required by `@main.py`.

### Running the Application

To run the application, execute the following command in your terminal:

```

python main.py

```

This command will start the Flask server defined in `@main.py`, which listens for POST requests on `/predict`. The server uses the MobileNet model to classify images sent in the request.
```
