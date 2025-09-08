import pandas as pd  # used for working like Excel 
import matplotlib.pyplot as plt # Used for plotting graphs 
import seaborn as sns # used for statistical data visualization 

df = pd.read_csv("sales_data.csv")  # open the CSV file
# PART A - DATA EXPLORATION 
print(df.head(10))  # prints the first 10 rows
print("Shape:", df.shape)  # number of rows and columns
print("Columns:", df.columns)  # column names
print("Missing values:\n", df.isnull().sum())  # check missing values
print("Statistical summary:\n", df.describe())  # mean, std, min, max, etc.

# PART B - DATA ANALYSIS
print("Total Sales:", df["Sales"].sum())  # total sales
print("Total Profit:", df["Profit"].sum())  # total profit

print("\nTop 5 highest sales orders:")
print(df.nlargest(5, "Sales"))  # top 5 rows with highest sales

region_sales = df.groupby("Region")["Sales"].sum()  # sales by region
print("\nSales by Region:\n", region_sales)

category_profit = df.groupby("Category")["Profit"].mean()  # avg profit by category
print("\nAverage Profit by Category:\n", category_profit)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract month names
df["Month"] = df["Date"].dt.month_name()

# Monthly sales trend
monthly_sales = df.groupby("Month")["Sales"].sum().sort_values(ascending=False)
print("\nTop 4 Months with Highest Sales:\n", monthly_sales.head(4))


# PART C - DATA VISUALIZATION (All charts together)

fig, axes = plt.subplots(3, 2, figsize=(14, 12))  # 3 rows, 2 cols grid

# 1. Sales by Region (Bar Chart)
region_sales.plot(kind="bar", color="Red", edgecolor="black", ax=axes[0,0])
axes[0,0].set_title("Total Sales by Region")
axes[0,0].set_xlabel("Region")
axes[0,0].set_ylabel("Total Sales")

# 2. Monthly Sales Trend (Line Chart)
monthly_sales.plot(kind="line", marker="o", color="green", ax=axes[0,1])
axes[0,1].set_title("Monthly Sales Trend")
axes[0,1].set_xlabel("Month")
axes[0,1].set_ylabel("Total Sales")

# 3. Profit Distribution by Category (Boxplot)
sns.boxplot(x="Category", y="Profit", data=df, ax=axes[1,0])
axes[1,0].set_title("Profit Distribution by Category")
axes[1,0].set_xlabel("Category")
axes[1,0].set_ylabel("Profit")

# 4. Sales vs Profit Scatterplot
sns.scatterplot(x="Sales", y="Profit", data=df, hue="Region", alpha=0.7, ax=axes[1,1])
axes[1,1].set_title("Sales vs Profit (colored by Region)")

# 5. Correlation Heatmap
corr = df[["Sales","Profit","Quantity"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=axes[2,0])
axes[2,0].set_title("Correlation Matrix")

# Hide the last empty cell (bottom-right)
axes[2,1].axis("off")

# Adjust layout so titles/labels don’t overlap
plt.tight_layout()
plt.show()


