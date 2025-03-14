# Project Overview
This project is a Flask-based web application that allows users to upload images of pharmaceutical drugs and detects whether they are authentic or counterfeit using a pre-trained YOLOv8 model via the Roboflow API. 
It helps in preventing the circulation of fake medicines in the market.

# Features
Upload drug images for analysis
Detect counterfeit drugs with confidence scores
Highlight detected drugs using bounding boxes
OCR-based label verification (optional)
User-friendly web interface

# Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript (Jinja templates)
Machine Learning: YOLOv8 (via Roboflow API)
OCR (Optional): Tesseract OCR
Storage: Local file system
 
# Project Structure
📁 fake-drug-detection
│── 📁 uploads/            # Stores uploaded images  
│── 📁 templates/          # HTML files for UI  
│── 📄 app.py              # Flask application  
│── 📄 requirements.txt    # Dependencies  
│── 📄 README.md           # Project documentation  

# How to Run the Project
git clone https://github.com/your-username/fake-drug-detection.git
cd fake-drug-detection

# Install Dependencies
pip install -r requirements.txt

# Set Up API Key (Secure Method) Create an environment variable for the Roboflow API Key:
export ROBOFLOW_API_KEY="your_api_key"

# Run the Flask App
python app.py

Open http://127.0.0.1:5000/ in your browser.

# How It Works
1. Upload an image of a drug package or pill.
2. The system analyzes the image using the YOLOv8 model via Roboflow API.
3. If a drug is detected, it returns:

Class: "Authentic" or "Fake"
Confidence Score (e.g., 95%)

4. The result is displayed on the webpage.
