from io import BytesIO
import numpy as np
import base64
import json
import os 

class Model(object):
    """Handles data preprocess and forward pass of the model"""
    def __init__(self, model_path="models/"):
        self.model_path = model_path
        self.model = None

    def init_model(self):
        """Initializes the machine learning model.

        Returns:
            model (object): Loaded pre-trained model used
                to make predictions.

        """
        raise NotImplementedError()
    
    def decode_data(self, encoded_data):
        """Decodes the encoded data comming from a request.

        Args:
            encoded_data (base64): data comming from the HTTP request.

        Returns:
            array: Data decoded into a usable format.

        """
        # NOTE: This could vary depending on your data
        decoded_data = base64.b64decode(encoded_data)
        return np.frombuffer(decoded_data, dtype=np.float64)

    def preprocess(self, raw_data):
        """Prerocess the data into the right format
        to be feed in to the given model.
        
        Args:
            raw_data (array): Raw decoded data to be processed.

        Returns:
            array: The data ready to use in the given model.

        """
        raise NotImplementedError()

    def model_predict(self, encoded_data):
        """Decodes and preprocess the data, uses the 
        pretrained model to make predictions and 
        returns a well formatted json output.

        Args
            encoded_data (base64): data comming from the HTTP request.

        Returns:
            json: A response that contains the output from 
                the pre-trained model.
        """
        # Decode data
        data = self.decode_data(encoded_data)
        # Preprocess into the right format
        inputs = self.preprocess(data)
        # Compute predictions
        preds = self.model.predict(inputs)
        # Create json response
        output = json.dumps({"outputs":preds})
        
        return output