from io import BytesIO
import numpy as np
import base64
import json
import os 

class Model(object):
    def __init__(self, model_path):
        """Model Class"""
        self.model_path = model_path
        self.model = self.init_model()

    def init_model(self):
        """
        Initializes the machine learning model.

        Returns
        -------
        model: object
            Pre-trained model used
            to make predictions.
        """
        pass
    
    def decode_data(self, encoded_data):
        """
        Decodes the encoded data comming from a request.

        Parameters
        ----------
        encoded_data : bytes
            Base64 data comming from request.

        Returns
        -------
        decoded_data: optional
            Data decoded into a usable format.
        """
        # NOTE: This could vary depending on your data
        decoded_data = base64.b64decode(encoded_data)
        return np.frombuffer(decoded_data, dtype=np.float64)

    def preprocess(self, raw_data):
        """
        Prerocess the data into the right format
        to be feed in to the given model.

        Parameters
        ----------
        raw_data: optional
            Raw data to be processed.

        Returns
        -------
        inputs: optional
            Data ready to use in the given model.
        """
        pass

    def model_predict(self, encoded_data):
        """
        Decodes and preprocess the data, uses the 
        pretrained model to make predictions and 
        returns a well formatted json output.

        Parameters
        ----------
        encoded_data: bytes
            Base64 data comming from request.

        Returns
        -------
        outputs: json
            A json response that contains the output
            from the pre-trained model.
        """
        pass
        