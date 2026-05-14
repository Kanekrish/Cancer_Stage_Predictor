# 🧬 SEER Breast Cancer Prediction System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-AI-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen?style=for-the-badge)

### Machine Learning-Based Clinical Decision Support System for Breast Cancer Survival Prediction Using the SEER Clinical Dataset

</div>

---

# 📌 Project Overview

The **SEER Breast Cancer Prediction System** is a machine learning-powered healthcare analytics application developed using the **SEER (Surveillance, Epidemiology, and End Results)** clinical dataset.

The system predicts breast cancer survival outcomes using advanced machine learning algorithms and provides an interactive web dashboard for data visualization, prediction analysis, and performance evaluation.

This project combines:

- Machine Learning
- Clinical Data Analysis
- Data Visualization
- Predictive Analytics
- Streamlit Web Development

---

# 🚀 Key Features

✅ Upload trained machine learning models (`.pkl`)  
✅ Upload SEER clinical datasets (`.csv`)  
✅ Predict patient survival outcomes  
✅ Interactive Streamlit web dashboard  
✅ Automatic preprocessing and data cleaning  
✅ Confusion matrix visualization  
✅ Performance metrics evaluation  
✅ Download prediction reports  
✅ Real-time prediction analysis  

---

# 🤖 Machine Learning Algorithms

| Algorithm | Description |
|---|---|
| Logistic Regression | Baseline classification algorithm for survival prediction |
| Random Forest | Ensemble learning algorithm for improved accuracy |
| XGBoost | Advanced gradient boosting algorithm optimized for predictive performance |

---

# 📊 Dataset Features

| Feature | Description |
|---|---|
| Age | Patient age at diagnosis |
| Race | Patient ethnicity/racial background |
| T Stage | Tumor staging classification |
| N Stage | Lymph node staging classification |
| Tumor Size | Measured tumor size |
| Estrogen Status | Hormone receptor status |
| Status | Target variable (Alive / Dead) |

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| Scikit-learn | Machine learning library |
| XGBoost | Gradient boosting framework |
| Pandas | Data processing |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Joblib | Model serialization |

---

# ⚙️ System Workflow

```text
1. Train machine learning model using SEER dataset
2. Save best model as .pkl file
3. Launch Streamlit web application
4. Upload trained model (.pkl)
5. Upload dataset (.csv)
6. Generate predictions
7. Visualize metrics and download reports
```

---

# ▶️ Running the Application

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Streamlit Application

```bash
python -m streamlit run app.py
```

After execution, open the generated localhost URL in your browser.

---

# 📈 Expected Outputs

- Prediction labels (`Alive / Dead`)
- Accuracy metrics
- Confusion matrix visualization
- Prediction distribution charts
- Downloadable prediction reports
- Interactive healthcare analytics dashboard

---

# 📂 Project Structure

```text
SEER-Breast-Cancer-Prediction/
│
├── app.py
├── breast_cancer_best_model.pkl
├── dataset.csv
├── requirements.txt
├── README.md
│
├── models/
├── outputs/
├── visualizations/
└── reports/
```

---

# 📷 Dashboard Preview

```text
✔ Upload Dataset
✔ Upload Model
✔ Generate Predictions
✔ View Metrics
✔ Download Reports
```

---

# 🔬 Research Objective

The objective of this project is to improve breast cancer survival prediction using machine learning techniques and clinical healthcare datasets to support data-driven medical decision-making.

---

# 📌 Future Improvements

- Deep Learning integration (ANN/CNN)
- Real-time clinical API integration
- Cloud deployment
- Advanced healthcare analytics
- Explainable AI (XAI)
- Multi-class cancer prediction

---

# 👨‍💻 Developer

**Krish**  
Software Developer | Cybersecurity Specialist | Machine Learning Enthusiast

---

# 📜 License

This project is developed for educational and research purposes.

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

</div>
