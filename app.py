# # from flask import Flask,request,render_template
# # import pandas as pd 
# # import pickle
# # import numpy as np 

# # model=pickle.load(open('breast_model.pkl','rb'))

# # ## flask app
# # app=Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/predict',methods=['POST'])
# # def predict():
# #     breast = request.form.get('breast')
# #     breast_lst=breast.split(',')
# #     np_breast=np.asarray(breast_lst,dtype=np.float32)
# #     pred=model.predict(np_breast.reshape(1,-1))
# #     output=['cancrous' if pred[0] == 1 else 'not cancrous']

# #     return render_template('index.html',message=output)










# # ## python main

# # if __name__== '__main__':
# #     app.run(debug=True)


# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# import pickle

# # loading model
# model = pickle.load(open('breast_model.pkl', 'rb'))

# # flask app
# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/predict', methods=['POST'])
# def predict():
#     features = request.form.get('feature')
#     print('form get data',request.form)
#     features = features.split(',')
#     np_features = np.asarray(features, dtype=np.float32)

#     # prediction
#     pred = model.predict(np_features.reshape(1, -1))
#     message = ['Cancrouse' if pred[0] == 1 else 'Not Cancrouse']
#     # print(message[0])
#     return render_template('index.html', message=message)


# if __name__ == '__main__':
#     app.run(debug=True)


import streamlit as st
import numpy as np
import joblib  # or any other method to load your model

# Load your model
model = joblib.load('breast_model.pkl')  # Update with your model file path

# Streamlit App
def main():
    st.title('Machine Learning Model Prediction')

    # Input from user
    features_input = st.text_input('Enter features separated by commas')

    if st.button('Predict'):
        if features_input:
            try:
                # Convert input string to list of floats
                features = [float(x) for x in features_input.split(',')]
                np_features = np.asarray(features, dtype=np.float32)
                
                # Prediction
                pred = model.predict(np_features.reshape(1, -1))
                
                # Display the result
                result = 'Cancrouse' if pred[0] == 1 else 'Not Cancrouse'
                st.write(f'Prediction: {result}')
            except Exception as e:
                st.error(f'Error processing input: {str(e)}')
        else:
            st.error('Please enter the features')

if __name__ == "__main__":
    main()
