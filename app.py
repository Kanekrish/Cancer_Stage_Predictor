import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Cancer Prediction System",
    page_icon="🧬",
    layout="wide"
)

# =========================
# CUSTOM UI STYLE
# =========================
st.markdown("""
    <style>
    .main { background-color: #f5f7fb; }
    h1, h2, h3 { color: #1f4e79; }
    </style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title(" Breast Cancer Survival Prediction System using SEER dataset by Krish")
st.caption("Upload trained model (.pkl) + dataset (.csv) to generate predictions")

# =========================
# SIDEBAR UPLOADS
# =========================
st.sidebar.title("📂 Upload Section")

model_file = st.sidebar.file_uploader("Upload Model (.pkl)", type=["pkl"])
data_file = st.sidebar.file_uploader("Upload Dataset (.csv)", type=["csv"])

run_btn = st.sidebar.button("🚀 Predict")

# =========================
# MAIN LOGIC
# =========================
if model_file and data_file:

    # LOAD MODEL
    model = joblib.load(model_file)

    # LOAD DATA
    df = pd.read_csv(data_file)

    # CLEAN DATA
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.dropna(axis=1, how='all')
    df.columns = df.columns.str.strip()

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    # =========================
    # PREDICTION BUTTON
    # =========================
    if run_btn:

        # CHECK TARGET COLUMN
        if 'Status' not in df.columns:
            st.error("Dataset must contain 'Status' column for evaluation metrics.")
            st.stop()

        # ENCODE TARGET
        df['Status'] = df['Status'].map({'Alive': 0, 'Dead': 1})

        X = df.drop('Status', axis=1)
        y = df['Status']

        # =========================
        # PREDICTIONS
        # =========================
        predictions = model.predict(X)

        df['Prediction'] = predictions
        df['Prediction Label'] = df['Prediction'].map({0: "Alive", 1: "Dead"})

        # =========================
        # METRICS
        # =========================
        acc = accuracy_score(y, predictions)
        cm = confusion_matrix(y, predictions)

        st.subheader("📈 Model Performance")

        col1, col2, col3 = st.columns(3)
        col1.metric("Accuracy", f"{acc:.2f}")
        col2.metric("Total Patients", len(df))
        col3.metric("Predicted Deaths", (df['Prediction'] == 1).sum())

        # =========================
        # CONFUSION MATRIX
        # =========================
        st.subheader("📊 Confusion Matrix")

        fig, ax = plt.subplots()
        ax.imshow(cm, cmap='Blues')
        ax.set_title("Confusion Matrix")
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        st.pyplot(fig)

        # =========================
        # PIE CHART
        # =========================
        st.subheader("📊 Prediction Distribution")

        fig2, ax2 = plt.subplots()
        df['Prediction Label'].value_counts().plot(
            kind='pie',
            autopct='%1.1f%%',
            ax=ax2
        )
        ax2.set_ylabel("")
        st.pyplot(fig2)

        # =========================
        # RESULTS TABLE
        # =========================
        st.subheader("🧾 Prediction Results")
        st.dataframe(df, use_container_width=True)

        # =========================
        # DOWNLOAD RESULTS
        # =========================
        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            "⬇ Download Predictions",
            data=csv,
            file_name="seer_predictions.csv",
            mime="text/csv"
        )

else:
    st.info("👉 Please upload BOTH a .pkl model file and a .csv dataset in the sidebar")