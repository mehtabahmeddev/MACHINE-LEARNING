import pandas as pd 

#PART 0
#1
df = pd.read_csv("healthcare-dataset-stroke-data_1.csv")
print (df.head())
df.info()
df.describe()
df.isnull().sum()
# 2. Shape of the dataset (Rows, Columns)
print("=== Dataset Shape ===")
print(df.shape)

#. Columns with missing values and their counts
print("\n=== Missing Values per Column ===")
missing_val = df.isnull().sum()
print(missing_val)

#  Value counts of 'gender'
print("\n=== Gender Value Counts ===")
print(df["gender"].value_counts(dropna=False))

# Stroke counts and percentage (stroke = 1 vs stroke = 0)
print("\n=== Stroke Count & Percentage ===")
stroke_counts = df["stroke"].value_counts()
stroke_percent = df["stroke"].value_counts(normalize=True) * 100

stroke_summary = pd.DataFrame(
    {"Count": stroke_counts, "Percentage (%)": stroke_percent.round(2)}
)
print(stroke_summary)



#3
df=df.drop('id', axis=1)
print("\n=== Dataset after dropping 'id' column ===")
print(df.head())    
print(df["gender"].value_counts())
c=df[df["gender"]=="Other"]
print(c)
df=df[df["gender"]!="Other"]
print(df["gender"].value_counts())

df=pd.get_dummies(df,drop_first=True)
print(df.head()) 


#4
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
df_encoded = pd.get_dummies(df, drop_first=True, dtype=int)


X = df_encoded.drop(columns=["stroke"])
y = df_encoded["stroke"]

SEED = 42

# 2. Stratified 80/20 Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y
)

# 3. Simple Missing Value Fill (Train ke median se)
train_medians = X_train.median()
X_train = X_train.fillna(train_medians)
X_test = X_test.fillna(train_medians)

# 4. Scaling for Logistic Regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 1. Train set me stroke cases
print("=== Train Set Stroke Counts ===")
print(y_train.value_counts())
print("\nTrain Set Stroke Percentages:")
print(y_train.value_counts(normalize=True) * 100)

# 2. Test set me stroke cases
print("\n=== Test Set Stroke Counts ===")
print(y_test.value_counts())
print("\nTest Set Stroke Percentages:")
print(y_test.value_counts(normalize=True) * 100)



