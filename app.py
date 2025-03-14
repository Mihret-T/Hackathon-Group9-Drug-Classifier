from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_cors import CORS
import os
from inference_sdk import InferenceHTTPClient

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
# Initialize the Roboflow API client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="vJdFKoktJ9xzGQ6ID5wO"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    try:
        # Perform inference using Roboflow API
        result = CLIENT.infer(image_path, model_id="conterfeitdrugdetection/1")

        # Extract confidence and class
        if result.get("predictions"):
            prediction = result["predictions"][0]  # Get the first detected object
            confidence = round(prediction["confidence"] * 100, 1)  # Convert to percentage
            classification = prediction["class"]  # "authentic" or "fake"

            # Create a simple result message
            result_message = f"This drug is {confidence}% {classification}."

            return render_template('result.html', 
                                   result_message=result_message, 
                                   result=result, 
                                   image_url=f"/uploads/{image.filename}")

        else:
            return render_template('result.html', error="No classification detected.")

    except Exception as e:
        return render_template('result.html', error=f"Prediction failed: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
