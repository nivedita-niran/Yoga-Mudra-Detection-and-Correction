import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import DepthwiseConv2D

# Define a custom version of DepthwiseConv2D that ignores 'groups'
def custom_depthwise_conv2d(*args, **kwargs):
    kwargs.pop('groups', None)  # Remove 'groups' if it exists
    return DepthwiseConv2D(*args, **kwargs)

# Manually load the model with custom objects
model_path = "/Users/niveditaniran/Desktop/Model/keras_model.h5"
labels_path = "/Users/niveditaniran/Desktop/Model/labels.txt"
model = load_model(model_path, custom_objects={'DepthwiseConv2D': custom_depthwise_conv2d})

# Assuming Classifier uses the model for prediction
class Classifier:
    def __init__(self, model):
        self.model = model
        with open(labels_path, 'r') as f:
            self.labels = f.read().splitlines()

    def getPrediction(self, img, draw=True):
        img = cv2.resize(img, (224, 224))  # Adjust input size as per your model
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        img = img / 255.0  # Normalize if needed (depends on model)
        
        prediction = self.model.predict(img)
        predicted_class = np.argmax(prediction)
        confidence = prediction[0][predicted_class]
        
        if draw:
            return self.labels[predicted_class], confidence
        return self.labels[predicted_class], confidence  # Ensure confidence is always returned

# Instantiate Classifier with the manually loaded model
classifier = Classifier(model)

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300
counter = 0

labels = ["JnanaMudra", "ChinMudra", "BhairavaMudra"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Ensure the crop region is valid
        if x - offset >= 0 and y - offset >= 0 and x + w + offset <= img.shape[1] and y + h + offset <= img.shape[0]:
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        else:
            continue  # Skip this frame if the crop region is invalid

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, confidence = classifier.getPrediction(imgWhite, draw=False)  # Now returning label and confidence
            print(prediction)

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            
            # Resize the imgResize to fit exactly within imgWhite dimensions (300x300)
            if hCal > imgSize:
                imgResize = cv2.resize(imgResize, (imgSize, imgSize))  # Resize to fit 300x300
            else:
                imgResize = cv2.resize(imgResize, (imgSize, hCal))  # Resize maintaining aspect ratio

            # Ensure imgResize fits into imgWhite (300x300) without broadcasting error
            imgWhite[hGap:hGap + imgResize.shape[0], :] = imgResize
            prediction, confidence = classifier.getPrediction(imgWhite, draw=False)  # Now returning label and confidence

        # Drawing the background for the text
        cv2.rectangle(imgOutput, (x - offset, y - offset - 70), (x - offset + 400, y - offset + 60 - 50), (0, 255, 0), cv2.FILLED)
        
        # Convert confidence to percentage and display it
        confidence_percentage = confidence * 100
        text = f'{prediction} ({confidence_percentage:.2f}%)'
        cv2.putText(imgOutput, text, (x - 10, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        
        # Draw the bounding box around the hand
        cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (0, 255, 0), 4)

        cv2.imshow('ImageCrop', imgCrop)
        cv2.imshow('ImageWhite', imgWhite)

    cv2.imshow('Image', imgOutput)
    cv2.waitKey(1)
