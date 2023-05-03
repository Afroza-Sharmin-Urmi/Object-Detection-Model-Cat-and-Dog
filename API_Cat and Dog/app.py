import streamlit as st
import torch
import numpy as np
from PIL import Image

# Load YOLOv5 and our pre-traied model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\User\\Documents\\Object Detection\\ObjectDetection\\best.pt')

# Define function to perform object detection on input image
def predict(image):
    results = model(image)
    return results

# Define Streamlit app
def app():
    st.title('Cat and Dog Detection Model')
    st.write('This app uses a pre-trained YOLOv5 model to recognize cat and dog in an image.')
    
    # Create file uploader
    image_file = st.file_uploader('Upload an image here:', type=['jpg', 'jpeg', 'png'])
    
    if image_file is not None:
        # Load image and perform object detection
        image = Image.open(image_file)
        results = predict(np.array(image))
        
        # Display input image with bounding box detection
        st.image(image, channels="BGR")
        
        # Display list of detected objects and corresponding confidence scores
        st.write('Object Recognition:')
        for obj in results.xyxy[0]:
            if obj[-1] == 0:
                st.write('Cat', obj[-2])
            elif obj[-1] == 1:
                st.write('Dog', obj[-2])
            else:
                st.write('Unknown Object')
          
if __name__ == '__main__':
    app()
