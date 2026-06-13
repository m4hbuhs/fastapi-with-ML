# Loan Approval Prediction using Machine Learning

## Overview

This project predicts whether a loan application will be **Approved** or **Rejected** using machine learning algorithms. The goal is to build an accurate classification model by analyzing an applicant's financial information, credit score, and asset details.

The project includes:

* Data preprocessing and cleaning
* Feature engineering
* Model training and evaluation
* Comparison of multiple machine learning models
* Feature importance analysis
* Performance visualization using confusion matrices and evaluation metrics

---

## Dataset

The dataset used in this project is the **Loan Approval Dataset** by Rohit Grewal, available on Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/rohitgrewal/loan-approval-dataset

The dataset contains information related to loan applicants including income, assets, credit score, education, employment status, and loan details.

### Features

* Number of Dependents
* Education
* Self Employed Status
* Annual Income
* Loan Amount
* Loan Term
* CIBIL Score
* Residential Asset Value
* Commercial Asset Value
* Luxury Asset Value
* Bank Asset Value

### Target Variable

* Approved
* Rejected

---

## Project Workflow

### 1. Data Preprocessing

* Loaded dataset using Pandas
* Cleaned column names and categorical values
* Removed unnecessary whitespace
* Applied One-Hot Encoding to categorical features
* Split dataset into training and testing sets

### 2. Feature Engineering

Categorical features:

* Education
* Self Employed Status

Numerical features:

* Annual Income
* Loan Amount
* Loan Term
* CIBIL Score
* Residential Asset Value
* Commercial Asset Value
* Luxury Asset Value
* Bank Asset Value
* Number of Dependents

---

## Machine Learning Models

### Logistic Regression

Used as the baseline classification model.

#### Results

* Accuracy: 91.16%
* Weighted F1 Score: 91.18%

---

### Random Forest Classifier

An ensemble learning model that combines multiple decision trees to improve prediction accuracy.

#### Results

* Accuracy: 97.25%
* Weighted F1 Score: 97.24%

---

### XGBoost Classifier

Gradient boosting-based ensemble model that achieved the best overall performance.

#### Results

* Accuracy: 97.72%
* Weighted F1 Score: 97.71%

---

## Model Comparison

| Model               | Accuracy | Weighted F1 Score |
| ------------------- | -------: | ----------------: |
| Logistic Regression |   91.16% |            91.18% |
| Random Forest       |   97.25% |            97.24% |
| XGBoost             |   97.72% |            97.71% |

### Best Performing Model

**XGBoost** achieved the highest accuracy and F1 Score among all evaluated models.

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Random Forest Results

Confusion Matrix:

|                 | Predicted Approved | Predicted Rejected |
| --------------- | -----------------: | -----------------: |
| Actual Approved |               1033 |                 21 |
| Actual Rejected |                 26 |                628 |

Accuracy:

97.25%

---

## Feature Importance Analysis

Feature importance extracted from the Random Forest model showed:

1. CIBIL Score
2. Loan Term
3. Loan Amount
4. Annual Income
5. Residential Asset Value

The analysis revealed that **CIBIL Score** is the most influential factor in determining loan approval status.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* XGBoost
* Jupyter Notebook

---

## Project Structure

```text
Loan-Approval-Prediction/
│
├── loan_approval_dataset.csv
├── main.ipynb
├── README.md
└── requirements.txt
```

---

## Key Results

* Built and evaluated multiple classification models.
* Improved accuracy from **91.16% (Logistic Regression)** to **97.72% (XGBoost)**.
* Reduced classification errors significantly using ensemble learning techniques.
* Identified CIBIL Score as the most important predictor for loan approval decisions.
* Achieved strong performance on unseen test data with excellent precision and recall.

---

## Future Improvements

* Hyperparameter tuning using Grid Search and Random Search
* Cross-validation for more robust evaluation
* Real-time prediction system
* Model deployment and monitoring
* Explainable AI techniques for prediction interpretation

---

## Author

**Shubham**

Machine Learning | Data Science | Backend Development
