from flask import Blueprint, render_template, request, Response
import cv2, time, os, base64
# from models import products, cropped
# from middlewares.yolo import detect, VideoCamera
# from middlewares.knn import get_neighbors
import pandas as pd
import pickle

# df = pd.read_csv('static/product-data/Sofa bed.csv')
# print(df.head(5))

imagePath = 'static\images\input.jpeg'
image = cv2.imread(imagePath)
print(image.shape[0])