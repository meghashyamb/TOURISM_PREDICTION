import pandas as pd

TOURISM_DATA = "tourism_project/data/tourism_data.csv"

rows_before = sum(1 for _ in open(TOURISM_DATA, encoding="utf-8", errors="replace")) - 1
df = pd.read_csv(TOURISM_DATA, on_bad_lines="skip")
rows_skipped = rows_before - df.shape[0]
if rows_skipped:
    print(f"Skipped {rows_skipped} malformed row(s) while parsing {TOURISM_DATA}.")

# Validate that the expected columns are present before registering it
expected_columns = [
'Unnamed: 0', 'CustomerID', 'ProdTaken', 'Age', 'TypeofContact',
       'CityTier', 'DurationOfPitch', 'Occupation', 'Gender',
       'NumberOfPersonVisiting', 'NumberOfFollowups', 'ProductPitched',
       'PreferredPropertyStar', 'MaritalStatus', 'NumberOfTrips', 'Passport',
       'PitchSatisfactionScore', 'OwnCar', 'NumberOfChildrenVisiting',
       'Designation', 'MonthlyIncome'
]
missing = [c for c in expected_columns if c not in df.columns]
if missing:
    raise ValueError(f"Dataset is missing expected columns: {missing}")

print("Dataset registered successfully.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("Columns:", list(df.columns))
