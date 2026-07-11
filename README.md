# 🚗 Road Accident Severity and Safety Hotspot Analyzer

## 📌 Project Overview

Road accidents are one of the leading causes of injuries and fatalities worldwide. Understanding the factors that contribute to accident severity can help governments and transportation authorities take preventive actions.

This project uses **Machine Learning** to predict the severity of road accidents based on factors such as weather conditions, road surface, driver information, vehicle details, and environmental conditions. It also analyzes accident patterns to identify high-risk conditions and provides safety recommendations for decision-makers.

---

## 🎯 Problem Statement

Develop a machine learning-based system that:

- Predicts the severity of a road accident.
- Identifies high-risk accident patterns.
- Analyzes important accident factors.
- Provides actionable safety recommendations.

The system is designed to support traffic authorities, road safety departments, and policymakers in improving road safety.

---

## 🌍 Real-World Impact

This project can help:

- 🚦 Traffic Police
- 🛣 Road Safety Authorities
- 🏛 Government Agencies
- 🚑 Emergency Response Teams
- 🚗 Transportation Departments

by identifying accident-prone conditions and supporting data-driven road safety planning.

---

## 📂 Dataset

**Dataset Name:** Road Accident Severity Dataset

**Source:** Kaggle

https://www.kaggle.com/datasets/kanuriviveknag/road-accidents-severity-dataset

### Dataset Summary

- Records: **12,316**
- Features: **32**
- Target Variable: **Accident_severity**

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Git & GitHub

---

# 📁 Project Structure

```
Road_Accident_Severity_Analyzer/
│
├── data/
│   └── RTA Dataset.csv
│
├── docs/
│   ├── Project_Report.pdf
│   └── Presentation.pdf
│
├── models/
│   └── random_forest_model.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Model_Training.ipynb
│   └── 03_Hotspot_Analysis.ipynb
│
├── outputs/
│   ├── safety_recommendations.csv
│   └── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 Project Workflow

```
Understand Problem
        ↓
Download Dataset
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Machine Learning Model
        ↓
Model Evaluation
        ↓
Hotspot Analysis
        ↓
Safety Recommendations
        
```

---

# 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Accident Severity Distribution
- Driver Age Analysis
- Driver Experience Analysis
- Weather Condition Analysis
- Road Surface Analysis
- Light Condition Analysis
- Vehicle Type Analysis
- Cause of Accident Analysis
- Day-wise Accident Analysis

These visualizations helped identify important accident patterns and influential factors.

---

# 🤖 Machine Learning Models

The following classification models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The best-performing model was selected based on evaluation metrics.

---

# 📈 Model Evaluation

The trained model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report
- Feature Importance Analysis

These metrics ensured that the model performs reliably across different accident severity classes.

---

# 📍 Safety Hotspot Analysis

The project identifies high-risk accident patterns based on:

- Weather Conditions
- Road Surface Conditions
- Light Conditions
- Driver Age Group
- Driver Experience
- Cause of Accident

The analysis helps identify scenarios where road accidents are more likely to be severe.

---

# 💡 Safety Recommendations

Based on the analysis, the system provides recommendations such as:

- Install additional street lighting in poorly lit areas.
- Improve road maintenance, especially on wet or damaged roads.
- Conduct awareness campaigns for high-risk driver groups.
- Increase traffic monitoring in high-risk conditions.
- Promote defensive driving practices.

---

# 🚀 How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/KomalKumari27/Road_Accident_Severity_Analyzer.git
```

### Navigate to the Project

```bash
cd Road_Accident_Severity_Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Jupyter Notebook

```bash
jupyter notebook
```

---

# 📸 Sample Outputs

Include screenshots of:

- Dataset Overview
- EDA Visualizations
- Model Evaluation Results
- Feature Importance
- Prediction Output

---

# 📌 Key Insights

- Most accidents resulted in slight injuries.
- Driver-related factors significantly influence accident severity.
- Weather and road surface conditions affect accident outcomes.
- Random Forest achieved the best performance among the tested models.
- Safety recommendations can support better road safety planning.

---

# ⚠ Limitations

- Based on historical accident data.
- Does not use real-time traffic information.
- Does not include GPS-based hotspot mapping.
- Performance depends on data quality and completeness.
- Predictions should support, not replace, expert decision-making.

---

# 🔮 Future Scope

Future improvements may include:
- Streamlit Dashboard
{ Enter accident-related information.
 Predict accident severity.
 View safety recommendations.
 Demonstrate the trained machine learning model.}

- Integration with live traffic APIs.
- GPS-based hotspot visualization.
- Weather API integration.
- Deep Learning models.
- XGBoost or LightGBM implementation.
- Cloud deployment.
- Mobile application support.

---

# Team Members:
- Komal Kumari
- Pallavi
- Shruti Saini

---

# 📚 References

1. Kaggle Road Accident Severity Dataset
2. Scikit-learn Documentation
3. Streamlit Documentation
4. Pandas Documentation
5. Matplotlib Documentation
6. Seaborn Documentation

---

# 📜 License

This project is developed for academic and educational purposes.

---

# ⭐ Acknowledgements

Special thanks to:

- IIT Mandi – Himshikhar Project Program
- Kaggle Dataset Contributors
- Open-source Python Community

---

GitHub: https://github.com/KomalKumari27

---

⭐ **If you found this project useful, consider giving the repository a star!**