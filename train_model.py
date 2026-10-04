import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# --------------------------------------------------
# 1. CREATE DATASET
# --------------------------------------------------

np.random.seed(42)

n = 1000

data = {
    "CGPA": np.round(np.random.uniform(5.0, 10.0, n), 2),
    "10th_Percentage": np.round(np.random.uniform(50, 100, n), 2),
    "12th_Percentage": np.round(np.random.uniform(50, 100, n), 2),
    "Backlogs": np.random.randint(0, 6, n),
    "Internships": np.random.randint(0, 4, n),
    "Projects": np.random.randint(0, 6, n),
    "Certifications": np.random.randint(0, 8, n),
    "Coding_Score": np.random.randint(30, 101, n),
    "Communication_Score": np.random.randint(30, 101, n),
    "Aptitude_Score": np.random.randint(30, 101, n),
    "Attendance": np.round(np.random.uniform(50, 100, n), 2)
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 2. CREATE TARGET
# --------------------------------------------------

score = (
    df["CGPA"] * 10
    + df["10th_Percentage"] * 0.10
    + df["12th_Percentage"] * 0.10
    - df["Backlogs"] * 8
    + df["Internships"] * 5
    + df["Projects"] * 3
    + df["Certifications"] * 2
    + df["Coding_Score"] * 0.15
    + df["Communication_Score"] * 0.10
    + df["Aptitude_Score"] * 0.10
    + df["Attendance"] * 0.05
)

# Convert score into placement label
threshold = score.median()

df["Placed"] = (score >= threshold).astype(int)

# Save dataset
df.to_csv("student_placement.csv", index=False)

print("Dataset created successfully.")

# --------------------------------------------------
# 3. FEATURES AND TARGET
# --------------------------------------------------

X = df.drop("Placed", axis=1)
y = df["Placed"]

# --------------------------------------------------
# 4. TRAIN / TEST SPLIT
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# 5. FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --------------------------------------------------
# 6. TRAIN RANDOM FOREST MODEL
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train_scaled, y_train)

# --------------------------------------------------
# 7. EVALUATE MODEL
# --------------------------------------------------

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("--------------------------------")
print("MODEL PERFORMANCE")
print("--------------------------------")
print("Accuracy:", round(accuracy * 100, 2), "%")
print()
print(classification_report(y_test, y_pred))

# --------------------------------------------------
# 8. SAVE MODEL
# --------------------------------------------------

joblib.dump(model, "placement_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("--------------------------------")
print("Model saved successfully!")
print("--------------------------------")