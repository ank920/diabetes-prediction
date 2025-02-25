# 🚀 Diabetes Prediction Project

Welcome to the **Diabetes Prediction Project**, where AI meets healthcare to make early diabetes detection easier and more accessible. This project employs a **Gaussian Naive Bayes classifier** to predict diabetes based on medical data. It provides both a **command-line interface (CLI)** and a **Flask-based REST API** for easy testing and deployment.

---

## 🔍 Overview

📊 **Dataset:** Pima Indians Diabetes Dataset (`diabetes.csv`)

🧠 **Model:** Gaussian Naive Bayes classifier (scikit-learn)

⚙️ **Preprocessing:** Data is normalized using `StandardScaler`

💻 **Interfaces:**
   - **CLI:** Enter patient data manually and get instant predictions.
   - **Flask API:** Send JSON data via API and receive predictions programmatically.

---

## 🛠 Installation

Follow these steps to set up the project on your system:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows users: venv\Scripts\activate
   ```

3. **Install Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 📌 Command-Line Interface (CLI)

Run the CLI-based prediction tool:
   ```bash
   python cli.py
   ```
You'll be prompted to enter patient details manually, and the model will return a **diabetes prediction** instantly.

### 🌍 Flask API

1. **Start the Flask Server:**
   ```bash
   python app.py
   ```

2. **Make an API Request:**
   Send a POST request to `http://127.0.0.1:5000/predict` with patient data in JSON format:
   ```json
   {
     "Pregnancies": 2,
     "Glucose": 120,
     "BloodPressure": 70,
     "SkinThickness": 20,
     "Insulin": 85,
     "BMI": 28.5,
     "DiabetesPedigreeFunction": 0.5,
     "Age": 30
   }
   ```
   ✅ The API will return a JSON response with the **prediction result**.

---

## 📂 Project Structure
```
📂 diabetes-prediction
│-- 📂 data                # Contains the dataset
│-- 📂 models              # Saved trained models (if applicable)
│-- 📜 cli.py              # Command-line interface script
│-- 📜 app.py              # Flask API script
│-- 📜 requirements.txt    # List of dependencies
│-- 📜 README.md           # Project documentation
```

---

## 🌱 Future Improvements

✨ Experiment with different machine learning models.
✨ Enhance data preprocessing and feature engineering.
✨ Deploy the model using **cloud services** like AWS, GCP, or Azure.

---

## 📜 License

📄 This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

💡 **Let's use AI for better healthcare!** 🏥🔬
