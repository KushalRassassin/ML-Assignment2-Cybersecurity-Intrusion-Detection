import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.metrics import confusion_matrix, classification_report
import zipfile

if not os.path.exists("models"):
    with zipfile.ZipFile("models.zip", "r") as zip_ref:
        zip_ref.extractall()

# Page config
st.set_page_config(page_title="Cybersecurity ML App", layout="wide")

# Title
st.title("Cybersecurity Intrusion Detection App")

st.write("""
Upload network traffic dataset to predict whether
connections are normal or malicious attacks.
""")

# Model selection
model_names = [
    "Logistic Regression",
    "Decision Tree",
    "KNN",
    "Naive Bayes",
    "Random Forest",
    "XGBoost"
]

model_choice = st.selectbox("Select ML Model", model_names)

# Load models safely
try:
    MODEL_DIR = "models"
    model_path = os.path.join(MODEL_DIR, f"{model_choice}.pkl")
    scaler_path = os.path.join(MODEL_DIR, "scaler.pkl")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

except Exception as e:
    st.error(f"Models not found: {e}")
    st.stop()

# Upload dataset
uploaded_file = st.file_uploader("Upload CSV dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.divider()
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if "target" in df.columns:
        X = df.drop("target", axis=1)
        y_true = df["target"]
    else:
        X = df
        y_true = None

    try:
        X_scaled = scaler.transform(X)
        predictions = model.predict(X_scaled)
    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.stop()

    st.divider()
    st.subheader("Predictions")
    st.write(predictions[:20])

    if y_true is not None:
        st.divider()
        st.subheader("Confusion Matrix")

        cm = confusion_matrix(y_true, predictions)
        cm_df = pd.DataFrame(
            cm,
            index=["Actual Normal", "Actual Attack"],
            columns=["Pred Normal", "Pred Attack"]
        )
        st.table(cm_df)

        st.divider()
        st.subheader("Classification Report")

        report = classification_report(y_true, predictions, output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df)

        st.divider()
        st.subheader("Prediction Summary")

        label_map = {0: "Normal Traffic", 1: "Attack Traffic"}

        pred_labels = pd.Series(predictions).map(label_map)
        pred_counts = pred_labels.value_counts()

        st.bar_chart(pred_counts)

