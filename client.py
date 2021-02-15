''' Example client sending POST request to server (localhost:8000/detect/)and printing the YOLO results
'''

import requests as r
import json
from pprint import pprint

def send_request(image_file = './images/zidane.jpg', model_name = 'yolov5s'):
	
	files = {'file': open(image_file , "rb")} #pass the files here
	other_form_data = {'model_name': model_name} #pass the other form data here

	res = r.post("http://localhost:8000/detect/", 
					data=other_form_data, 
					files = files)

	pprint(json.loads(res.text))

if __name__ == '__main__':
	send_request()