# Steganalysis-System Using CNN
Introduction
This project is a web-based application designed to classify images as either Steganographic or Clean. By leveraging the power of Convolutional Neural Networks (CNNs), the system detects hidden messages embedded in images using steganography techniques.

Features
-User-friendly interface for uploading images.
-Automated classification of uploaded images into Steganographic or Clean.
-Real-time prediction results displayed on the web application.
-Built using Flask for backend integration and TensorFlow for model inference.
-Responsive design with enhanced user experience.


Technologies Used
-Frontend: HTML5, CSS3, JavaScript
-Backend: Flask, Python
-Machine Learning: TensorFlow, Keras
-Web Server: Flask Development Server


Installation Guide
Pre-requisites
-Python 3.8 or higher
-Pip package manager
-Git installed on your system


Steps to Set Up Locally
-Clone the Repository

git clone https://github.com/your-username/steganlysis-classifier.git
cd steganalysis-classifier

Set Up a Virtual Environment
python -m venv env
env\Scripts\activate      # For Windows

Install Dependencies

pip install -r requirements.txt

Place Your Model File
Place the pre-trained CNN model (steganography_cnn_model.h5) in the saved_model/ directory.

Run the Application
python app.py

Access the Application
Open your browser and navigate to: http://127.0.0.1:5000


Folder Structure

├── static/
│   ├── css/
│   │   └── style.css
│   ├── uploads/
│   └── images/
├── templates/
│   └── index.html
├── saved_model/
│   └── steganography_cnn_model.h5
├── app.py
├── requirements.txt
└── README.md
