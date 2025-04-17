import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from scipy import stats


df = pd.read_csv(r"/Users/alexkochu/Downloads/archive/nasa.csv")
df.head(10)

df.tail()

df.isnull().sum()

df.info()

df.describe()

df.shape()




hazardous = df[df['Hazardous'] == True]
non_hazardous = df[df['Hazardous'] == False]

columns_to_test = [
    'Absolute Magnitude',
    'Est Dia in KM(max)',
    'Relative Velocity km per sec',
    'Miss Dist.(kilometers)'
]

t_test_results = {}
z_test_results = {}

for col in columns_to_test:
    t_stat, t_p = ttest_ind(hazardous[col], non_hazardous[col], equal_var=False)
    t_test_results[col] = (t_stat, t_p)

    mean1, mean2 = hazardous[col].mean(), non_hazardous[col].mean()
    std1, std2 = hazardous[col].std(), non_hazardous[col].std()
    n1, n2 = len(hazardous[col]), len(non_hazardous[col])
    pooled_se = np.sqrt((std1**2 / n1) + (std2**2 / n2))
    z_stat = (mean1 - mean2) / pooled_se
    z_test_results[col] = z_stat

print("T-Test Results:")
for col, (t, p) in t_test_results.items():
    print(f"{col}: t-statistic = {t:.2f}, p-value = {p:.4e}")

print("\nZ-Test Results:")
for col, z in z_test_results.items():
    print(f"{col}: z-statistic = {z:.2f}")



plt.style.use("dark_background")
for col in columns_to_test:
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue='Hazardous', kde=True, bins=30, palette='inferno')
    plt.title(f'Distribution of {col} by Hazardous Status')
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.grid(linestyle='--',color='gray')
    plt.tight_layout()
    plt.show()







for col in columns_to_test:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Hazardous', y=col, data=df, palette='inferno',hue='Hazardous')
    plt.title(f'Boxplot of {col} by Hazardous Status')
    plt.xlabel("Hazardous")
    plt.ylabel(col)
    plt.grid(linestyle='--',color='gray')
    plt.tight_layout()
    plt.show()






sns.pairplot(df[columns_to_test + ['Hazardous']], hue="Hazardous", palette='inferno')
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()





numerical_cols = df.select_dtypes(include=np.number).columns.tolist()

plt.figure(figsize=(14, 10))
corr = df[numerical_cols].corr()
sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.show()









scatter_pairs = [
    ('Est Dia in KM(max)', 'Relative Velocity km per sec'),
    ('Absolute Magnitude', 'Miss Dist.(kilometers)')
]

for x, y in scatter_pairs:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y, hue='Hazardous', alpha=0.6, palette='inferno')
    plt.title(f'{y} vs {x} by Hazardous Status')
    plt.tight_layout()
    plt.grid(linestyle='--',color='gray')
    plt.show()







for col in columns_to_test:
    plt.figure(figsize=(8, 5))
    sns.violinplot(x='Hazardous', y=col, data=df, palette='coolwarm', inner='quartile',hue='Hazardous')
    plt.title(f'Violin Plot of {col} by Hazardous Status')
    plt.tight_layout()
    plt.grid(linestyle='--',color='gray')
    plt.show()







if 'Close Approach Date' in df.columns:
    df['Close Approach Date'] = pd.to_datetime(df['Close Approach Date'], errors='coerce')

    plt.figure(figsize=(12, 5))
    df.set_index('Close Approach Date').resample('M')['Hazardous'].sum().plot()
    plt.title("Monthly Count of Hazardous NEOs")
    plt.xlabel("Date")
    plt.ylabel("Hazardous NEOs Count")
    plt.tight_layout()
    plt.grid(linestyle='--',color='gray')
    plt.show()








sns.countplot(x='Hazardous', data=df, palette='inferno',hue='Hazardous')
plt.title("Count of Hazardous vs Non-Hazardous NEOs")
plt.xlabel("Hazardous")
plt.ylabel("Count")
plt.tight_layout()
plt.grid(linestyle='--',color='gray')
plt.show()






for col in columns_to_test:
    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=hazardous[col], label='Hazardous', shade=True)
    sns.kdeplot(data=non_hazardous[col], label='Non-Hazardous', shade=True)
    plt.title(f'KDE Plot of {col}')
    plt.xlabel(col)
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.show()






scatter_combos = [
    ('Est Dia in KM(max)', 'Miss Dist.(kilometers)'),
    ('Relative Velocity km per sec', 'Miss Dist.(kilometers)'),
    ('Absolute Magnitude', 'Est Dia in KM(max)'),
    ('Absolute Magnitude', 'Relative Velocity km per sec')
]

for x, y in scatter_combos:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y, hue='Hazardous', palette='hsv', alpha=0.7)
    plt.title(f'Scatter Plot: {y} vs {x}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.show()






for col in columns_to_test:
    plt.figure(figsize=(10, 5))
    sns.histplot(hazardous[col], kde=True, color="blue", label="Hazardous", bins=30, alpha=0.6)
    sns.histplot(non_hazardous[col], kde=True, color="green", label="Non-Hazardous", bins=30, alpha=0.6)
    plt.title(f'Overlay Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()






for col in columns_to_test:
    g = sns.FacetGrid(df, hue="Hazardous", height=5, aspect=2)
    g.map(sns.histplot, col, bins=30, kde=True, alpha=0.6)
    g.add_legend()
    plt.title(f'Facet Histogram of {col} by Hazardous Status')
    plt.show()






subset = df[[*columns_to_test, 'Hazardous']]
sns.pairplot(subset, hue="Hazardous", palette='Set1')
plt.suptitle("Scatter Matrix of Key Features", y=1.02)
plt.show()


































