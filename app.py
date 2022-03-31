# frontend/main.py

import requests
import json
import streamlit as st
from fastapi import Form

MODELS = {
    "small": "yolov5s",
    "medium": "yolov5m",
    "large": "yolov5l",
    "xlarge": "yolov5x",
}
CONF = 0.5
IOU = 0.45

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Plate Waste Detection Web App")

# displays a file uploader widget
imgfiles = st.file_uploader("Choose an image", accept_multiple_files=True)

# displays the select widget for the models
model_name = st.selectbox("Select YOLO model", [i for i in MODELS.keys()])
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        iou = st.slider("IOU", 0., 1., IOU)
    with col2:
        conf = st.slider("CONF", 0., 1., CONF)

# displays a button
if st.button("Detect"):
    if imgfiles is not None and model_name is not None:
        files = [("file_list",f) for f in imgfiles] # multifile upload: https://stackoverflow.com/questions/18179345/uploading-multiple-files-in-a-single-request-using-python-requests-module
        params = {"model_name":MODELS[model_name], "img_size":640, "conf":conf, "iou":iou, "download_image":False}
        st.write(files, params)
        # with open('/storage/test.txt', 'w') as f:
        #     f.write('hi') # file should be mapped to local storage
        res = requests.post(f"http://localhost:8000/detect/", files=files, data=params)
        st.write(res)
        st.write(res.text)
        # img_path = res.json()
        # image = Image.open(img_path.get("name"))
        # st.image(image, width=500)

if st.button("Test backend"):
    res = requests.get("http://localhost:8000/")
    st.write('Test GET request to server:', res)
    valid_book = {'book': 'Clean Code: A Handbook of Agile Software Craftsmanship'}
    res = requests.post('http://localhost:8000/test/', data=valid_book)
    st.write(res.json())