from flask import Flask, request, jsonify
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
from tensorflow.keras.applications.mobilenet import decode_predictions


app = Flask(__name__)

# Load the MobileNet model
model = MobileNet(weights='imagenet')


@app.route('/predict', methods=['POST'])
def predict():
    # Get image data from the request
    image_file = request.files['image']
    img = Image.open(io.BytesIO(image_file.read()))

    # Convert the image to RGB mode
    img = img.convert('RGB')

    # Resize the image to 224x224 pixels (the size that MobileNet expects)
    img = img.resize((224, 224))

    # Convert the image to a numpy array and preprocess it
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Perform prediction
    prediction = model.predict(img_array)

    # You may need to post-process the prediction based on your model output

    predicted_class = decode_predictions(prediction, top=1)
    predicted_class_name = predicted_class[0][0][1]

    return jsonify({'predicted_class': predicted_class_name})


if __name__ == '__main__':
    app.run(debug=True)
