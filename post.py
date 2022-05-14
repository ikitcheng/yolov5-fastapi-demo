import requests
import utils
import threading

def load_files(filenames):
    files = []
    for filename in filenames:
        imgfile = open(filename, "rb")
        # imgfile is the same as the element in st.file_uploader()
        files.append(("file_list",imgfile))
    
    return files

def postreq(filesIO):
    params = {"model_name":"yolov5s", "img_size":640, "conf":0.5, "iou":0.5, "download_image":True}
    url = "https://foodwasteyolov5.herokuapp.com/detect/"
    res = requests.post(url, files=filesIO, data=params)
    print(res)
    data = res.json()
    for i in range(len(data)):
        imgname = filesIO[i][1].name.split('/')[-1]
        im = utils.openb64image(data[i][-1]['image_base64'], output=f"./output/detect/{imgname}")
        json_name = imgname.split('.')[0] + '.json'
        utils.save_json(data[i][0:-1], output=f"./output/detect/labels/{json_name}")

def fire_and_forget(target, kwargs={}):
    """ Fire a target (i.e. a function) and continue running the rest of the program.

    Args:
        target (callable): callable object to be invoked.
        kwargs (dict, optional): Dictionary of keyword arguments for the target invocation. Defaults to {}.

    """
    threading.Thread(target=target, kwargs=kwargs).start()

if __name__ == "__main__":
    img_filenames = ["../pi/output/images/20220422T162743.png"]
    filesIO = load_files(img_filenames)
    #post(filesIO) # running in sequential
    fire_and_forget(target=post, kwargs={'filesIO':filesIO})
    print('Im still running... Thread is running in parallel.')