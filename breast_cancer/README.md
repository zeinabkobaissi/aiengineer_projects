Breast Cancer Classification and Feature Analysis

This project demonstrates a complete machine learning pipeline for breast cancer classification using feature selection, feature engineering, model comparison, and hyperparameter tuning.

The goal is to identify the most important features and evaluate different machine learning algorithms to predict whether a tumor is malignant or benign.

Project Overview

This project includes:

Loading and exploring the Breast Cancer dataset

Feature selection using Mutual Information

Feature engineering by creating new combined features

Training multiple classification models

Comparing model performance

Hyperparameter tuning using GridSearchCV

Evaluating the best model using classification metrics

Dataset

The dataset used is the Breast Cancer Wisconsin dataset from scikit-learn.

It contains:

569 samples

30 numerical features

Binary target:

0 → Malignant

1 → Benign

Features include measurements such as:

Mean radius

Mean texture

Mean perimeter

Mean area

Mean smoothness

Technologies Used

Python

NumPy

Pandas

Seaborn

Matplotlib

Scikit-learn

Project Pipeline
1. Data Loading
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer(as_frame=True)


The dataset is converted into a Pandas DataFrame and prepared for analysis.

2. Feature Selection using Mutual Information

Mutual Information is used to measure how important each feature is for predicting the target.

mutual_info_classif(X, y)


Visualization is done using Seaborn bar plots.

This helps identify the most relevant features.

3. Feature Engineering

A new feature was created by combining two existing features:

Combined_radius_texture = mean radius × mean texture


Feature engineering can improve model performance by introducing meaningful relationships.

4. Train-Test Split

The dataset is split into training and testing sets:

train_test_split(X, y, random_state=42)


This allows proper evaluation on unseen data.

5. Model Training and Comparison

Multiple machine learning models were trained and compared:

LinearSVC

KNeighborsClassifier

Support Vector Machine (SVC)

Logistic Regression

Random Forest Classifier

Example:

model.fit(X_train, y_train)
model.score(X_test, y_test)

Model Performance Results
Model	Accuracy
Linear SVC	93.4%
KNeighborsClassifier	92.0%
Logistic Regression	92.4%
SVC	89.9%
Random Forest	93.1%
6. Hyperparameter Tuning using GridSearchCV

GridSearchCV was used to find the best parameters for the SVC model.

GridSearchCV(SVC(), param_grid=params, cv=5, scoring='recall')


Best parameters found:

C = 0.01
max_iter = 1000

7. Model Evaluation

Classification report includes:

Precision

Recall

F1-score

Accuracy

Example:

Accuracy: 63%
Recall for class 1: 100%


This shows the model prioritizes detecting benign cases.

Project Structure
breast-cancer-classification/
│
├── breast_cancer_classification.ipynb
├── README.md
└── requirements.txt

How to Run
1. Clone the repository
git clone https://github.com/zeinabkobaissi/breast-cancer.git
cd breast-cancer-classification

2. Install dependencies
pip install -r requirements.txt

3. Run the notebook
jupyter notebook

Key Machine Learning Concepts Demonstrated

Feature selection (Mutual Information)

Feature engineering

Model training and evaluation

Model comparison

Hyperparameter tuning

Classification metrics analysis

Key Learning Outcomes

How to analyze feature importance

How to compare different ML models

How to improve performance with hyperparameter tuning

How to build a complete ML pipeline

Future Improvements

Add cross-validation for all models

Add feature scaling

Add ROC curve analysis

Deploy the model using FastAPI or Streamlit

