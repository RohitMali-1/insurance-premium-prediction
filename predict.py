import streamlit as st
import pickle
import numpy as np
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv("data/insurance_c.csv")
    return data

df = load_data()

# categories in dataframe
regions  = tuple(df.region.unique())
sex = tuple(df.sex.unique())
childrens = tuple(df.children.unique())
smoker = tuple(df.smoker.unique())

# load model XGBRegressor model pickle file
@st.cache_data
def load_model():
    with open("pkl/xgb_model.pkl", 'rb') as file:
        model = pickle.load(file)
    
    return model

XGBRegressor = load_model()

@st.cache_data
# load transformer pickle file
def load_transformer():
    with open("pkl/transformer.pkl", 'rb') as file:
        ct = pickle.load(file)
    
    return ct

transformer = load_transformer()

#prediction page
def show_predict_page():
    st.title("Health Insurance Premium Prediction")
    st.write("""### select the input for prediction""")

    # select categories from select box
    region = st.selectbox("Region", regions)
    gender = st.selectbox("Gender", sex)
    age = st.slider("Age", df.age.min(), df.age.max())
    smoke = st.selectbox("Smoker", smoker)
    children = st.selectbox("Number of childrens", childrens)
    bmi = st.slider("BMI", df.bmi.min(), df.bmi.max())

    #['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
    # column transformer take dataframe as input
    data = [[age, gender, bmi , children , smoke, region]]
    input = pd.DataFrame(data=data, columns=df.drop(columns="charges").columns)

    boolean = st.button("Calculate charges")

    if boolean:
        charges = XGBRegressor.predict(transformer.transform(input))
        st.subheader(f"Estimated charges ${charges[0]:.2f}")
