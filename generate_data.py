import pandas as pd
import random

# Original dataset
data = "data.csv"

# Create a DataFrame from the original data
df = pd.read_csv(data)

# Create list of rows
row_list = []

# Expand the dataset to 200 rows
for i in range(16, 501):
    # Generate random data for each row
    row = {
        "id": i,
        "name": f"Product {chr(65 + i % 26)}",
        "price": random.randint(50, 300),
        "quantity": random.randint(10, 100),
        "category": random.choice(["Electronics", "Apparel", "Home & Kitchen"])
    }
    # df = df.append(row, ignore_index=True)
    row_list.append(row)

df_extension = pd.DataFrame(row_list)

df = pd.concat([df, df_extension])
# Introduce outliers and data anomalies
# For example, randomly set some prices to negative values
for i in range(random.randint(26, 75)):
    idx = random.randint(0, 450)
    df.loc[idx, "price"] = -df.loc[idx, "price"]

# Save the expanded dataset to a CSV file
df.to_csv("expanded_dataset.csv", index=False)

# Print a success message
print("Expanded dataset with outliers and data anomalies saved as expanded_dataset.csv")