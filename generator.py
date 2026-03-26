import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Set the number of rows to 500
num_rows = 500
start_date = datetime(2025, 1, 1)

# 2. Define products and logic (Price and Material usage)
# 6 inch: $1.5 price, 0.02kg material
# 7 inch: $2.0 price, 0.025kg material
# 12 inch: $4.5 price, 0.05kg material
# 13 inch: $5.5 price, 0.06kg material
products = {
    '6 inch': {'price': 1.5, 'material_per_unit': 0.02},
    '7 inch': {'price': 2.0, 'material_per_unit': 0.025},
    '12 inch': {'price': 4.5, 'material_per_unit': 0.05},
    '13 inch': {'price': 5.5, 'material_per_unit': 0.06}
}

# 3. Generate random data for 500 entries
data_list = []
for i in range(num_rows):
    random_date = start_date + timedelta(days=np.random.randint(0, 365))
    size = np.random.choice(list(products.keys()))
    quantity = np.random.randint(100, 1000)
    
    price_per_unit = products[size]['price']
    raw_material_kg = round(quantity * products[size]['material_per_unit'], 2)
    total_revenue = round(quantity * price_per_unit, 2)
    
    data_list.append([random_date.strftime('%Y-%m-%d'), size, quantity, raw_material_kg, price_per_unit, total_revenue])

# 4. Create DataFrame and Export to CSV
columns = ['Date', 'Product_Size', 'Quantity', 'Raw_Material_Used_kg', 'Price_Per_Unit', 'Total_Revenue']
df = pd.DataFrame(data_list, columns=columns)

# Save the file
df.to_csv('Paper_Plate_Business_Data.csv', index=False)

print("Success! 'Paper_Plate_Business_Data.csv' with 500 rows has been created.")