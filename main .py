import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load data and prepare features/labels
df = pd.read_csv("diabetes.csv")
x = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Scale features
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Split data
X_train, X_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Train the model using GaussianNB
nb = GaussianNB()
nb.fit(X_train, y_train)

# Evaluate the model
y_pred = nb.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Function to get user input and predict diabetes outcome
def predict_user_input():
    print("\nEnter the following details for diabetes prediction:")
    features = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    user_data = []
    for feature in features:
        value = float(input(f"{feature}: "))
        user_data.append(value)
    # Scale the user input using the same scaler
    user_data_scaled = scaler.transform([user_data])
    # Predict using the trained model
    prediction = nb.predict(user_data_scaled)[0]
    outcome = "Has Diabetes" if prediction == 1 else "No Diabetes"
    print(f"Predicted Outcome: {outcome}")

# Uncomment the line below to run the interactive prediction
predict_user_input()
