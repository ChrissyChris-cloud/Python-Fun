import pandas as pd

# Step 1: Create a CSV file (you can manually create this or use Python to generate it)
data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
    ["David", 40, "New York"],
    ["Eve", 28, "Los Angeles"]
]

# Write data to a CSV file
with open('people.csv', 'w') as file:
    file.write("Name,Age,City\n")
    for row in data:
        file.write(",".join(map(str, row)) + "\n")

# Step 2: Load the CSV file into a Pandas DataFrame
df = pd.read_csv('people.csv')

# Display the DataFrame
print("Data Loaded into DataFrame:")
print(df)

# Step 3: Filter data for people older than 30
older_than_30 = df[df['Age'] > 30]
print("\nPeople older than 30:")
print(older_than_30)

# Step 4: Group by city and calculate the average age in each city
average_age_by_city = df.groupby('City')['Age'].mean()
print("\nAverage age by city:")
print(average_age_by_city)
