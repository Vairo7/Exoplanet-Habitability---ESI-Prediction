from flask import Flask, request, jsonify
from xgboost import XGBRegressor
import pickle
from db import engine
import numpy as np
import pandas as pd


app = Flask(__name__)

model = XGBRegressor()
model.load_model('model.json')

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

@app.route('/ayy', methods = ['POST'])
def lmao():
    planet = request.get_json()  

    if not planet or "features" not in planet:
        return jsonify({"error": "Invalid input format. Expected {'features': [values]}"})

    features = np.array(planet["features"]).reshape(1, -1) 
    feat_scaled_arr  = scaler.transform(features)

    prediction = model.predict(feat_scaled_arr)[0]

    return jsonify({"ESI_Score": float(prediction)})

@app.route('/exoplanets', methods=['GET'])
def exoplanets():
    try:
        query = 'SELECT * FROM planet;'
        df = pd.read_sql(query, engine)

        if df.empty:
            return jsonify([]) 
        
        return jsonify(df.to_dict(orient='records')) 
    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)
