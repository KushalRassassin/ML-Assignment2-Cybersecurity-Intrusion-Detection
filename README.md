# ML Assignment 2 – Cybersecurity Intrusion Detection

## Student Details
Student Name: Kushal R  
BITS ID: 2025AA05518  
Course: M.Tech AIML  
Assignment: Machine Learning Assignment 2  

---

## Problem Statement
The objective of this assignment is to build multiple machine learning classification models for cybersecurity intrusion detection and deploy an interactive web application using Streamlit.

---

## Dataset Description
The NSL-KDD cybersecurity dataset is used for intrusion detection.  
It contains network traffic features that help classify connections as either normal or malicious attacks.

---

## Models Implemented
The following classification models were trained and evaluated:

- Logistic Regression  
- Decision Tree  
- K-Nearest Neighbors (KNN)  
- Naive Bayes  
- Random Forest  
- XGBoost  

### Evaluation Metrics Used
- Accuracy  
- AUC Score  
- Precision  
- Recall  
- F1 Score  
- Matthews Correlation Coefficient (MCC)

---

## Observations
- Random Forest and XGBoost provided the best overall performance.  
- Logistic Regression served as a stable baseline model.  
- Naive Bayes showed relatively lower performance due to feature independence assumptions.

---

## Streamlit Application Features
- Dataset upload option (optional default dataset included)  
- Model selection dropdown  
- Prediction results display  
- Confusion matrix visualization  
- Classification report summary  

---

## Deployment
The application is deployed using Streamlit Cloud and the source code is available in this GitHub repository.
