import os
import json 
from PIL import Image
from io import BytesIO
import base64
import hashlib

def save_json(data, output, encoding="utf-8"):
    """Save data in json format.

    Args:
        data (list or dict): Data to be saved.
        output (str): Path of the output file (including its filename).
        encoding (str, optional): Format encoding. Defaults to "utf-8".
    """
    output_path = "/".join(output.split("/")[0:-1])
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
        print("Created folder : ", output_path)
    with open(output, "w", encoding=encoding) as outfile:
        outfile.write(json.dumps(data, indent=4, ensure_ascii=False))
        print("Data saved to folder : ", output)

def load_json(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def openb64image(b64image, output=None, show=False):
    """ Open base64 image.

    Args:
        b64image (str): Image as base64 string. 
        output (str, optional): Path to save the image as jpeg. 
        show (bool, optional): Show the image in window.
    """
    im = Image.open(BytesIO(base64.b64decode(b64image)))
    if show:
        im.show()
    if output:
        im.save(output)
        print(f"Image saved to {output}")
    return im

