# 🏥 Insurance Premium Prediction  

This project aims to predict **health insurance premiums** using machine learning models, helping insurance companies quickly calculate premium charges. The dataset, sourced from **Kaggle**, contains **1,338 rows and 7 columns**.  

## 📌 Features & Workflow  

### 🔹 **1. Data Preprocessing & Analysis**  
- Checked for **duplicate values, missing values, and data types**.  
- Performed **statistical analysis and visualizations** to understand patterns and relationships between features.  
- Key insights were derived from plots, showing how factors like **age and smoking status** impact premium charges.  

### 🔹 **2. Feature Engineering**  
- Applied **Label Encoding** to handle categorical data.  
- Used **Standard Scaling** to normalize numerical features for better model performance.  

### 🔹 **3. Model Development & Evaluation**  
- Implemented multiple machine learning models:  
  - **Linear Regression, Lasso Regression, Ridge Regression, KNN, Decision Tree, Random Forest, XGBoost, and AdaBoost**.  
- Evaluated models using **Mean Squared Error (MSE), Root Mean Squared Error (RMSE),** and **R2 Score**.  
- **XGBoost Regressor** achieved the highest accuracy of **90%** after **hyperparameter tuning** using **Randomized Search CV**.  
- Saved the trained model and transformers as **pickle files** for deployment.  

### 🔹 **4. Web App Development (Streamlit)**  
A web application was developed using **Streamlit**, featuring:  
1. **Prediction Page** – Allows users to input customer details (age, BMI, smoking status, etc.) and receive a predicted premium amount.  
2. **Data Visualization Page** – Displays interactive graphs and insights from data analysis.  

## 🚀 **Live Demo**  
🔗 **Try the Web App Here:** [Insurance Premium Prediction](https://insurance-premium-prediction-kmz7swihxjrnnkbdm3igvn.streamlit.app/)  

## 📂 **Technologies Used**  
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, Streamlit  
- **Model Deployment:** Pickle, Streamlit 

