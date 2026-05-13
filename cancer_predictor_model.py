

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_curve,
    auc
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("seer_breast_cancer.csv")

# REMOVE BROKEN COLUMNS (IMPORTANT FIX)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.dropna(axis=1, how='all')

# Clean column names
df.columns = df.columns.str.strip()

# Clean text values
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

# =========================
# 2. TARGET VARIABLE
# =========================
df['Status'] = df['Status'].map({'Alive': 0, 'Dead': 1})

# =========================
# 3. SPLIT FEATURES/TARGET
# =========================
X = df.drop('Status', axis=1)
y = df['Status']

# =========================
# 4. COLUMN TYPES
# =========================
categorical_cols = X.select_dtypes(include='object').columns
numerical_cols = X.select_dtypes(exclude='object').columns

# =========================
# 5. PREPROCESSING PIPELINE
# =========================
num_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, numerical_cols),
    ('cat', cat_pipeline, categorical_cols)
])

# =========================
# 6. TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 7. MODELS (BALANCED)
# =========================
models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight='balanced'
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight='balanced'
    ),

    "XGBoost": XGBClassifier(
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=682/123,  # handles imbalance
        eval_metric='logloss',
        random_state=42
    )
}

# =========================
# 8. STORAGE FOR GRAPHS
# =========================
results = {}
roc_data = {}

# =========================
# 9. TRAIN MODELS
# =========================
for name, model in models.items():

    clf = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    results[name] = acc
    roc_data[name] = (fpr, tpr, roc_auc)

    print("\n==============================")
    print(f"MODEL: {name}")
    print("==============================")
    print("Accuracy:", acc)
    print("\nConfusion Matrix:\n", cm)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # -------------------------
    # CONFUSION MATRIX PLOT
    # -------------------------
    plt.figure()
    plt.title(f"Confusion Matrix - {name}")
    plt.imshow(cm, cmap='Blues')
    plt.colorbar()
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.xticks([0, 1])
    plt.yticks([0, 1])
    plt.show()

# =========================
# 10. ROC CURVE PLOT
# =========================
plt.figure()
for name, (fpr, tpr, roc_auc) in roc_data.items():
    plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.2f})")

plt.plot([0, 1], [0, 1], 'k--')
plt.title("ROC Curve Comparison")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()

# =========================
# 11. ACCURACY COMPARISON BAR CHART
# =========================
plt.figure()
plt.bar(results.keys(), results.values())
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.xticks(rotation=20)
plt.show()