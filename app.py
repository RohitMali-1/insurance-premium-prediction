import streamlit as st
from predict import show_predict_page
from plots import univariate_analysis, bivariate_analysis, multivariate_analysis
st.sidebar.write("#### Select the analysis type or Prediction")
page = st.sidebar.selectbox(
    "Choose an option",  # This is the label
    ["Prediction", "Univariate", "Bivariate", "Multivariate"]  # These are the options
)


if page == "Univariate":
    univariate_analysis()
elif page == "Bivariate":
    bivariate_analysis()
elif page == "Multivariate":
    multivariate_analysis()
elif page == "Prediction":
    show_predict_page()