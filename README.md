# Containerized Machine Learning
A simple and ready to use template to create and deploy a machine learning model using Docker and Flask.

## Setup:

In order to build your Docker API, you must make a few changes in the following files:
#### `Dockerfile` 
This is a text document that contains all the commands a user could call on the command line to assemble an image: 
  1. Depending on the Machine Learning framework that you're using you'd have to choose an optimal image for it. I'd recommend you to use the official framework images on [Docker Hub](https://hub.docker.com/). Here is an example using pytorch:
  ```dockerfile
  FROM pytorch/pytorch 
  ```
  2. Is always good practice to add a label with instructions on how to run your docker container, so I'd recommend you to add a label like the following:
  ```dockerfile
  LABEL run="docker run --name=model-service --rm -dit -v <PATH>:/app -p 7001:7000 modelimage"
  ```

#### `utils.py` 
The utils file contains a template of the `Model` class that you'll use to manage requests, data preprocessing, model predictions, and responses, inside this class you'd have to implement the following methods:
  1. `init_model` Initializes the machine learning model. Here is an example using Keras:
  ```python
  model = load_model("model/path/model.h5")
  ```
  2. `decode_data` Decodes the encoded data comming from a request. e.g.
  ```python
  decoded_data = Image.open(BytesIO(base64.b64decode(data)))
  ```
  3. `preprocess` Prerocess the data into the right format to be feed in to the given model.
  4. `model_predict` Decodes and preprocess the data, uses the pretrained model to make predictions and returns a well formatted json output.
  ```python
  # Decode data
  data = self.decode_data(data)
  # Preprocess into the right format
  inputs = self.preprocess(data)
  # Compute predictions
  preds = self.model.predict(inputs)
  # Create json response
  output = json.dumps({"outputs":preds})
  ```

#### `requirements.txt` 
this file is used to force pip to properly resolve dependencies:
  1. Add the extra libraries you'd need to run the model or preprocess your data.

## Run:

There are a few ways to run a docker container, I'll give a couple of examples using `docker-compose` and the `docker run` command. Here are the steps you'll need to follow:

#### Build the image:
With your `Docker` file ready you just have to run:
```bash
docker build -t imagename .
```

#### Run container:
Using the `docker` commands:
```bash
docker run docker run --name=conainername --rm -dit -v <PATH>:/app -p 7001:7000 imagename
```
Using `docker-compose`:
```bash
docker-compose up -d
```

## Usage:
Here are a few examples on how to call the API using different methods. Note that you can change `localhost` for the private or public IP address of your computer.

### Python:
```python
import requests
import base64

data = base64.b64encode(array)
r = requests.get("http://localhost:7000/predict/", params={"data":data})
out = r.json()
```

### URL:
```
http://localhost:7000/predict/?data=<data-in-base64>
```
