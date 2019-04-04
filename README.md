# Conteinerized Machine Learning
A simple and ready to use template to create and deploy a machine learning model using Docker and Flask.

### Setup:

In order to build your Docker API, you must make a few changes in the following files:
* `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image: 
  1. Depending on the Machine Learning framework that you're using you'd have to choose an optimal image for it. I'd recommend you to use the official framework images on [Docker Hub](https://hub.docker.com/). Here is an example using pytorch:
  ``` 
  FROM pytorch/pytorch 
  ```
  2. Is always good practice to add a label with instructions on how to run your docker container, so I'd recommend you do add a label like the following:
  ``` 
  LABEL run="docker run --name=model-service --rm -dit -v <PATH>:/app -p 7001:7000 modelimage"
  ```

* `utils.py` this file contains a template of the `Model` class that you'll use to manage requests, data preprocessing, model predictions, and responses, inside this class you'd have to implement the following methods:
  1. `init_model` Initializes the machine learning model.
  2. `decode_data` Decodes the encoded data comming from a request.
  3. `preprocess` Prerocess the data into the right format to be feed in to the given model.
  4. `model_predict` Decodes and preprocess the data, uses the pretrained model to make predictions and returns a well formatted json output.

* `requirements.txt` is used to force pip to properly resolve dependencies:
  1. Add the extra libraries you'd need to run the model or preprocess your data.