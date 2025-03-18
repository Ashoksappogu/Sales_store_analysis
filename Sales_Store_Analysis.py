import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("============== Data Exploration with Pandas =========================")
# Load the data
data = pd.read_csv(r"C:\Users\user\Downloads\Salesstore.csv")
print('top records:',data.head())
print('bottom records:',data.tail())
print('===============================================')
# Data Exploration
# Check the shape of the data
data_shape=data.shape
print('data shape:',data_shape)
print('===============================================')
# Check the data types
dt=data.dtypes
print('checking the datatype:',dt)
print('===============================================')
# Check for missing values
mv=data.isnull().sum()
print('missing values;==',mv)
print('===============================================')
# Check for duplicate values    
dv=data.duplicated().sum()
print('to know the duplicate values:==',dv)
print('===============================================')
# Discribe the dataset
print('Discribe the table :====',data.describe())
print('===============================================')
# Check the columns
print('columns:',data.columns)
print('===============================================')
# 1. Most selling Product_category
most_selling_p=data['Product_Category'].value_counts().idxmax()
print(most_selling_p)
print('===============================================')
# 2. Which product_category given more profits
cat_profit=data.groupby('Product_Category')['Profit'].sum()
print(cat_profit)
print('===============================================')
# 3. which segment peoples buying the goods
cust_profit=data.groupby('Customer_Segment')['Profit'].sum()
print(cust_profit)
print('===============================================')
# 4. Which region peoples are purchase more times 
rig_sales=data.groupby('Region')['Sales'].sum()
print(rig_sales)
print('===============================================')
# 5. Know the Product_category and its Oredr_quantity
cust_cat=data.groupby('Product_Category')['Order_Quantity'].sum()
print(cust_cat)
print('===============================================')
# 6. To know the total sales of Product_category and Profit
total_profit=data.groupby(['Sales','Product_Category'])['Profit'].sum()
print(total_profit)
print('===============================================')

# Data_Analysis using Pandas
print('================= Data_Analysis with matplotlib =========================')
# Most selling Product_category
most_selling_p=data['Product_Category'].value_counts()
df=pd.DataFrame(most_selling_p)
c='g','y','r'
ax=df.plot(kind='bar',color=c)
# 1. Customizing the plot
plt.title("1. Category and its members")
plt.xlabel("Category")
plt.ylabel("members_count")
plt.xticks(rotation=25)
plt.legend(title="Product Category")
# Adding profit value labels on the bars
for i, value in enumerate(df.values):
    ax.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=10)
# Show plot
plt.tight_layout()
plt.show()

print('=====================================================')
# 2. Which product_category given more profits
cat_profit=data.groupby('Product_Category')['Profit'].sum()
df=pd.DataFrame(cat_profit)
c='r','y','g'
ax=df.plot(kind='bar',color=c)
# Customizing the plot
plt.title(" 2. Profit by Product_Category wise")
plt.xlabel("Category")
plt.ylabel("Profit(in $)")
plt.xticks(rotation=25)
plt.legend(title="Product_Category profit")
# Adding profit value labels on the bars
for i, value in enumerate(df.values):
    ax.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=10)
# Show plot
plt.tight_layout()
plt.show()
print('================================================')
#3. which segment peoples buying the goods
cust_profit=data.groupby('Customer_Segment')['Profit'].sum()
df=pd.DataFrame(cust_profit)
c='y','g','orange','r'
ax=df.plot(kind='bar',color=c)
# Customizing the plot
plt.title(" 3. Profit genareted by Customer_Segmentwise")
plt.xlabel("Customer_Segment")
plt.ylabel("Profit(in $)")
plt.xticks(rotation=25)
plt.legend(title="Product_Category profit")
# Adding profit value labels on the bars
for i, value in enumerate(df.values):
    ax.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=10)
# Show plot
plt.tight_layout()
plt.show()
print('=======================================================')
# 4. Which region peoples are purchase more times 
rig_sales=data.groupby('Region')['Sales'].sum()
df=pd.DataFrame(rig_sales)
c='blue','yellow','red','maroon','orange','green'
ax=df.plot(kind='bar',color=c)
# Customizing the plot
plt.title(" 4. Region wise sales")
plt.xlabel("Regions")
plt.ylabel("Sales(in $)")
plt.xticks(rotation=25)
plt.legend(title="Region sales")
# Adding profit value labels on the bars
for i, value in enumerate(df.values):
    ax.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=8)
# Show plot
plt.tight_layout()
plt.show()
print('====================================================')
 #5. Know the Product_category and its Oredr_quantity
cust_cat=data.groupby('Product_Category')['Order_Quantity'].sum()
df=pd.DataFrame(cust_cat)
c='r','g','y'
ax=df.plot(kind='bar',color=c)
# Customizing the plot
plt.title(" 5. Product_category and its Oredr_quantity ")
plt.xlabel("Product_category")
plt.ylabel("Order_quantity")
plt.xticks(rotation=25)
plt.legend(title="Product_quantity")
# Adding profit value labels on the bars
for i, value in enumerate(df.values):
    ax.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=8)
# Show plot
plt.tight_layout()
plt.show()
print('=======================================================')
# 6. To know the total sales of Product_category and Profit

# Reset index to turn groupby result into a DataFrame
total_profit = data.groupby(['Sales','Product_Category'])['Profit'].sum().reset_index()

# Line Chart
plt.figure(figsize=(10, 6))
sns.lineplot(x='Sales', y='Profit', hue='Product_Category', marker='o', data=total_profit)

plt.title('6. Total Profit vs Sales by Product Category')
plt.xlabel('Sales')
plt.ylabel('Total Profit')
plt.legend(title='Product Category')
plt.grid(True)
plt.show()
print('==========Successfuly Completed=====================')
