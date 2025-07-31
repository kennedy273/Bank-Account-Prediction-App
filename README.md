# 💡 Project Overview

The **Bank Account Prediction Streamlit App** allows users to:

* Predict whether a person is likely to have a bank account based on personal and demographic data
* Interact with an intuitive form for input
* Receive instant ML-based feedback

This app is perfect for those new to Python, machine learning, and Streamlit. It also serves as a simple deployment example for binary classification models.

---

## 🚀 Features

✅ **Prediction Based on User Input**
→ Enter personal and demographic information (age, job, education, etc.) and get a real-time prediction

✅ **Categorical Encoding**
→ Automatically encodes features using the same format as during model training

✅ **ML Model Integration**
→ Loads a pre-trained Decision Tree Classifier to make predictions

✅ **User-Friendly UI**
→ Powered by Streamlit with dropdowns, number inputs, and validation button

✅ **Success & Error Feedback**
→ Green success messages and warnings for predictions

---

## 🛠️ Tech Stack

* **Python 3.8+** – Core programming language
* **Streamlit** – UI framework for deploying ML apps
* **Scikit-learn** – For model training
* **Pandas** – For data manipulation
* **Joblib** – For saving/loading ML models

---

## 📦 Installation

### 🔧 Prerequisites

* Python 3.8 or higher
* Streamlit installed (`pip install streamlit`)

### 📥 Steps

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/bank-account-prediction-app.git
cd bank-account-prediction-app

# 2. (Optional) Create a Virtual Environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

> Visit the app in your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Example Workflow

1. Select country, gender, marital status, job, etc.
2. Input age and household size
3. Click "Validate"
4. View result: ✅ Likely / ❌ Unlikely to own a bank account

---

## 🌐 Deployment (Streamlit Community Cloud)

1. Push your code to GitHub:

   * `app.py`
   * `bank_account_model.pkl`
   * `requirements.txt`
   * `README.md`
2. Sign up at [streamlit.io/cloud](https://streamlit.io/cloud)
3. Link your GitHub repo
4. Deploy with one click!

---

## 📁 File Structure

```
bank-account-prediction-app/
├── app.py                   # Streamlit app
├── bank_account_model.pkl
```
