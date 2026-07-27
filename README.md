# Customer Churn Prediction App

A Machine Learning web application built with Python and Streamlit that identifies Frauds based on transactions. The project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and deployment.


![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)


## Overview

This application detects Fraud using the following input features:

- Transaction Type
- Old Balance ( SENDER )
- New Balance ( SENDER )
- Old Balance ( RECEIVER )
- New Balance ( RECEIVER )

The trained model processes the input and predicts whether the transaction is likely to be a  **Fraud** or not

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Project Structure

```
Fraud-Detection-App/
│
├── app.py
├── main.ipynb
├── fraud-detection-pipeline.pkl
├── dataset.csv
├── requirements.txt
└── README.md
```

## Dataset

Dataset: Fraud Detection Dataset

https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download

## Machine Learning Workflow

- Data cleaning and preprocessing
- Train-test split
- Model training and comparison
- Model evaluation using accuracy score
- Exporting the pipeline using Joblib

## Running the Application

Clone the repository:

```bash
git clone https://github.com/riyasehgal-codes/Fraud-Detection-App.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```



