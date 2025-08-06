import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import *
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import *
from sklearn.preprocessing import *

# Load data
df = pd.read_csv('fraud.csv')  # Replace with actual file path
print(df.shape)
print(df.info())
print(df.head())
# Check for class imbalance
df.columns = df.columns.str.strip()
print(df.columns)

# Now retry
print(df['isFraud'].value_counts(normalize=True))
 #Visualize feature distributions
sns.countplot(x='isFraud',data=df)
plt.title('Fraud vs Non-Fraud Distribution')
plt.show()



# Separate features and target
X =df.drop("isFraud",axis=1)
y =df['isFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

X_train = X_train.select_dtypes(include=['number'])
X_test = X_test.select_dtypes(include=['number'])



# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# Evaluation
print(classification_report(y_test, y_pred))
print("AUC Score:", roc_auc_score(y_test, y_proba))

