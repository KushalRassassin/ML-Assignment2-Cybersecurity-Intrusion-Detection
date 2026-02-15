# ML Assignment 2 – Cybersecurity Intrusion Detection

## Student Details
- **Student Name:** Kushal R  
- **BITS ID:** 2025AA05518  
- **Course:** M.Tech AIML  
- **Assignment:** Machine Learning Assignment 2  

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

---

## Evaluation Metrics Used
- Accuracy  
- AUC Score  
- Precision  
- Recall  
- F1 Score  
- Matthews Correlation Coefficient (MCC)  

### Comparison Table

| Model               | Accuracy | AUC      | Precision | Recall   | F1 Score | MCC     |
|---------------------|----------|----------|-----------|----------|----------|---------|
| Logistic Regression | 0.972177 | 0.996372 | 0.976736  | 0.963159 | 0.969900 | 0.944116|
| Decision Tree       | 0.998452 | 0.998486 | 0.997700  | 0.998977 | 0.998338 | 0.996890|
| KNN                 | 0.996745 | 0.999616 | 0.997267  | 0.995736 | 0.996501 | 0.993460|
| Naive Bayes         | 0.840683 | 0.978025 | 0.997548  | 0.659304 | 0.793900 | 0.711069|
| Random Forest       | 0.999008 | 0.999994 | 0.999488  | 0.998380 | 0.998933 | 0.998006|
| XGBoost             | 0.999325 | 0.999989 | 0.999318  | 0.999232 | 0.999275 | 0.998644|

---

## Observations

| ML Model Name        | Observation about model performance |
|-----------------------|-------------------------------------|
| Logistic Regression   | Stable baseline, strong generalization with high accuracy. |
| Decision Tree         | Very high accuracy but prone to overfitting; excellent recall. |
| KNN                   | Strong performance, slightly lower than ensemble methods. |
| Naive Bayes           | Lower recall due to independence assumptions; weaker overall. |
| Random Forest         | Outstanding performance, robust and reliable across metrics. |
| XGBoost               | Best overall performance, near-perfect accuracy and MCC. |

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
