import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import pickle

model=pickle.load(open(r"lr.pkl","rb"))
                       
SquareFeet =st.number_input("Enter the size of the house",min_value=1000,max_value=2999,step=50)
Bedrooms=st.number_input("Enter the number of Bedrooms",min_value=2,max_value=5,step=1)
Bathrooms=st.number_input("Enter the number of Bathooms",min_value=1,max_value=3,step=1)
Neighbourhood=st.radio("Enter the Neighbourhood",['Rural','Urban','Suburb'])
neighbour=1 if Neighbourhood=='Rural' else 2 if Neighbourhood=='Urban' else 3
YearBuilt=st.number_input("Enter the Year of Construction",min_value=1950,max_value=2021,step=1)

price=model.predict([[SquareFeet,Bedrooms,Bathrooms,neighbour,YearBuilt]])

st.write("the price of the house for your given details is Rs.",price)

