from flask import Flask, request
import numpy as np
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger
#from werkzeug.datastructures import FileStorage

# create flask app and wrap it in Swagger
app = Flask(__name__)
Swagger(app)

# load the model
pickle_in = open('logreg.pkl', 'rb')
model = pickle.load(pickle_in)

# use get request for single prediction and post request for grouop prediction
@app.route('/predict', methods=['Get'])
def predict_class():
    """
    Predict if customer would by the product or not
    ---
    Parameters:
    - name: age
      in: query
      type: number
      required: true
    - name : new_user
      in: query
      type: number
      required: true
    - name: total_pages_visited
      in: query
      type: number
      required: true
    responses:
        500:
            description: Prediction
    """
    age = int(request.args.get('age'))
    new_user = int(request.args.get('new_user'))
    total_pages_visited = int(request.args.get('total_pages_visited'))
    prediction = model.predict([[age, new_user, total_pages_visited]])
    print(prediction[0])
    return "The prediction is " + str(prediction)


@app.route('/predict_file', methods=['POST'])
def predict_file():
    """
    Predict if customer would by the product or not
    ---
    Parameters:
    - name: file
      in: formData
      type: file
      required: true
    responses:
        500:
            description: Prediction
    """
    #file = request.files.get('file')
    #if not file:
    #    return "No file found", 400
    df_test = pd.read_csv(request.files.get('file'))
    prediction = model.predict(df_test)
    return str(list(prediction))

if __name__ == '__main__':
    app.run(debug=True)
