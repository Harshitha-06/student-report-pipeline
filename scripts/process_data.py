import pandas as pd

# Read the attendance/marks data
df = pd.read_csv("data/attendance.csv")

# Calculate attendance percentage
df["Attendance%"] = (df["ClassesAttended"] / df["ClassesHeld"] * 100).round(2)

# Calculate marks percentage
df["Marks%"] = (df["MarksObtained"] / df["MaxMarks"] * 100).round(2)

# Flag students with low attendance (<75%) or failing marks (<40%)
df["LowAttendance"] = df["Attendance%"] < 75
df["Failing"] = df["Marks%"] < 40

# Print results to check
print(df)

# Save results as a new report file
df.to_csv("output/report.csv", index=False)
print("\nReport saved to output/report.csv")