import pandas as pd

print("Student Performance Data Analysis")
print("----------------------------------")

# Load CSV file
data = pd.read_csv("student_data.csv")

print("\nOriginal Data:")
print(data)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Clean missing values
data["Marks"] = data["Marks"].fillna(data["Marks"].mean())
data["Attendance"] = data["Attendance"].fillna(data["Attendance"].mean())

print("\nCleaned Data:")
print(data)

# Filter students with marks 80 or above
high_marks = data[data["Marks"] >= 80]

print("\nStudents with Marks 80 or Above:")
print(high_marks)

# Group data by subject
subject_average = data.groupby("Subject")["Marks"].mean()

print("\nAverage Marks by Subject:")
print(subject_average)

# Summary statistics
print("\nSummary Statistics:")
print(data["Marks"].describe())
