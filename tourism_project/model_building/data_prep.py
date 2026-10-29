
# for data manipulation
import pandas as pd
import sklearn

# for data preprocessing and pipeline creation
from sklearn.model_selection import train_test_split

# for converting text data to numerical values
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

tourism_pkg=pd.read_csv("tourism_project/data/tourism_data.csv")

# skipping bad rows of data

df_tourism = pd.read_csv("tourism_project/data/tourism_data.csv", on_bad_lines="skip")
print("Dataset loaded successfully.")

# drop unique identifier columns
df_tourism.drop(['Unnamed: 0', 'CustomerID'], axis=1, inplace=True)

# Encode categorical features
categorical_features = ['TypeofContact', 'Occupation', 'Gender', 'ProductPitched', 'MaritalStatus', 'Designation']
label_encoders = {}
for feature in categorical_features:
    label_encoders[feature] = LabelEncoder()
    df_tourism[feature] = label_encoders[feature].fit_transform(df_tourism[feature])

# Define target variable
target_variable = 'ProdTaken'

#Split into X (features) and y (target)
X = df_tourism.drop(columns=[target_variable])
y = df_tourism[target_variable]

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

X_train.to_csv("tourism_project/data/X_train.csv", index=False)
X_test.to_csv("tourism_project/data/X_test.csv", index=False)
y_train.to_csv("tourism_project/data/y_train.csv", index=False)
y_test.to_csv("tourism_project/data/y_test.csv", index=False)

print("Data preparation complete: train/test splits written.")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
