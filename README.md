# yolov5-fastapi-demo

This is a demo FastAPI app that allows a user to upload image(s), perform inference using a pretrained YOLOv5 model, and receive results in JSON format. This repo also includes Jinja2 HTML templates, so you can access this interface through a web browser at localhost:8000

<img src="https://user-images.githubusercontent.com/47000850/107603157-e05aae00-6bf9-11eb-8c1a-2715fdc27066.png" alt="image" width="630"/>

## Requirements
Python 3.8 or later with all requirements.txt dependencies installed, including torch>=1.7 (per https://github.com/ultralytics/yolov5).

To install run:
```
pip install -r requirements.txt
```

## Inference

You can initialize the server with `python server.py` or `uvicorn server:app --reload`

You can test the server a couple of ways:
1. Using `client.py` - this is a basic example of using the Requests library to upload a batch of images + model name to `localhost:8000/detect/` and receive JSON inference results. 
1. Open `localhost:8080` in your web browser, use the web form to upload image(s) and select a model, then click submit. You should see inference results displayed in the web browser shortly. 
1. Open `localhost:8080/docs` in your web browser, clicking on "POST /detect/ Detect Via API" and then click the "Try It Out" button. You should be able to upload files and enter a YOLOv5 model here as well.

Models will automatically be downloaded the first time they are used and are cached on disc.

<img src="https://user-images.githubusercontent.com/47000850/107911503-bae7e000-6f2a-11eb-8be4-cf662608546e.png" alt="image" width="630"/>

### Docker 
* To run the server with docker , `cd` into directory of this readme file and run `docker-compose up -d --build`
* Navigate to `http://localhost:8080`in browser.
* To kill all containers, run `docker-compose down`
* Build errors: 
	- If container failed after build due to module not found error, add the required module into `requirements.txt` file. Rerun `docker-compose up -d --build`.

## API Documentation
Full Swagger API endpoint documentation is auto-generated in `localhost:8000/docs`. The general idea is that humans use the "/" route (HTML form + inference results displayed in the browser) and programs use the "/detect/" API route to receive JSON inference results.

## Credits

This repository is a wrapper around a custom YOLOv5 from Ultralytics: https://github.com/ultralytics/yolov5

Also grabbed some code/ideas from: https://gist.github.com/decent-engineer-decent-datascientist/81e04ad86e102eb083416e28150aa2a1
