import pytesseract
import cv2
import matplotlib.pyplot as plt
import glob
import os

file_path = os.getcwd() + "/cars_data/images.Cars0.png"

NP_list = []
predicted_NP = []

for file_path in glob.glob(file_path, recursive = True):
    NP_list = file_path.split("/")[-1]
    