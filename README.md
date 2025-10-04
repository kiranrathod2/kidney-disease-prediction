# 🩺 **Kidney Disease Prediction**

A machine learning project to predict whether a patient is at risk of **kidney disease**, built with Python and deployed via Streamlit.

---

## 🚀 **Project Overview**

This repository hosts the full pipeline for kidney disease prediction:
- Data ingestion and preprocessing  
- Model training and evaluation  
- Deployment via a web app using Streamlit  

Users can input patient health metrics and get a prediction: **positive** (has kidney disease) or **negative** (no kidney disease).

---

## 🧠 **Model & Artifacts**

Included in this repository:

- `classifier_kidney.pkl` — trained classification model  
- `scaler_kidney.pkl` — scaler used to preprocess numeric features  
- `kidney_disease_deploy.py` — Streamlit app for prediction  
- `kidney_disease.ipynb` — notebook with data exploration & modeling  
- `kidney_disease.csv` — the dataset used  
- `data_description_kidney_disease.txt` — description of dataset features  

---

## 💻 **Tech Stack**

- Python  
- pandas, NumPy  
- scikit-learn  
- Streamlit  
- Jupyter Notebook  

---

## 🗂️ **Project Structure**

.
├── kidney_disease_deploy.py
├── classifier_kidney.pkl
├── scaler_kidney.pkl
├── kidney_disease.ipynb
├── kidney_disease.csv
├── data_description_kidney_disease.txt
└── README.md

---

## 🛠️ **How to Run Locally**

### **1️⃣ Clone the repo**
```bash
git clone https://github.com/kiranrathod2/kidney-disease-prediction.git
cd kidney-disease-prediction

---

### **🧩 Usage (What to Input)**

In the app, provide the patient’s health metrics such as:

Age, Blood pressure, Specific gravity, Albumin, Sugar, etc.

Key lab measurements and indicators

(Refer to data_description_kidney_disease.txt for detailed feature descriptions)

Click Predict to see if the patient is at risk of kidney disease or not.

---

### **📈 Potential Applications**

Early screening and risk assessment for kidney disease

Healthcare decision support systems

Education and research tool

---

### **🙌 Acknowledgements & References**

Based on publicly available kidney disease datasets

Built using Scikit-learn and Streamlit

Many thanks to dataset contributors and open-source ecosystem

---

## 📬 **Contact**

GitHub: https://github.com/kiranrathod2

LinkedIn / Email: (add your contact info here)
