from flask import Flask, request
import numpy as np
import utils

# Initialize the flask app
app = Flask(__name__)

# Loads the given model
model = utils.Model("models/")
model.init_model()


<<<<<<< HEAD
# The model runs in the /predict route
@app.route('/predict', methods=['POST'])
=======
@app.route('/predict/', methods=['GET', 'POST'])
>>>>>>> 7c4c5a9f80ca19a2024f33718e7f93d73dca4445
def predict():
    # Obtain the data from the request
    data = request.get_data()
    # Runs the model and returns the outputs in a json format
    output = model.model_predict(data)
    return output

if __name__ == "__main__":
    # Running the Flask app on the url http://0.0.0.0:7000/
    # Use 0.0.0.0 to run in any IP available
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=7000)
=======
    app.run(host='0.0.0.0', port=7000, threaded=True)
>>>>>>> 7c4c5a9f80ca19a2024f33718e7f93d73dca4445
