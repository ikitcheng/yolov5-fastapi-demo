import requests

def load_files(filenames):
    files = []
    for filename in filenames:
        imgfile = open(filename, "rb")
        # imgfile is the same as the element in st.file_uploader()
        files.append(("file_list",imgfile))
    
    return files

if __name__ == "__main__":
    filenames = ["../pi/output/images/20220422T162743.png"]
    files = load_files(filenames)
    params = {"model_name":"yolov5s", "img_size":640, "conf":0.5, "iou":0.5, "download_image":False}
    url = "http://localhost:8000/detect/"
    res = requests.post(url, files=files, data=params, server_ip='202.86.174.130')
    print(res)
    print(res.text)