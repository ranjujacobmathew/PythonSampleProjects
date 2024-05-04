 import pandas as pd
data=pd.read_csv("/content/comprehensive_mutual_funds_data.csv")
df=pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
cat=df.category
val=df.fund_size_cr
fig,ax= plt.subplots()
ax.pie((val),labels=cat)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Assuming df has 'category' and 'fund_size_cr' columns
data = pd.read_csv("/content/comprehensive_mutual_funds_data.csv")
df = pd.DataFrame(data)

# Extracting data
cat = df['category']
val = df['fund_size_cr']

# Plotting
fig, ax = plt.subplots()
ax.pie(val, labels=cat, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

plt.title('Distribution of Fund Size by Category')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize']=[15,6]
df = pd.read_csv('/content/comprehensive_mutual_funds_data.csv')
df.head()
df.info()
df['returns_5yr'].fillna(df['returns_5yr'].median(),inplace=True)
for i in df.columns:
    print(i,': ',df.loc[:,i].nunique())
sns.countplot(x=df['category'])
plt.show()
ns.countplot(x=df['sub_category'])
plt.xticks(rotation=90)
plt.show()
pd.crosstab(df['sub_category'],df['category']).plot(kind='barh')
sns.kdeplot(data=df,x='returns_1yr')
sns.kdeplot(data=df,x='returns_3yr')
sns.kdeplot(data=df,x='returns_5yr')
plt.legend()
plt.grid()
plt.show()
sns.kdeplot(data=df,x='returns_1yr')
sns.kdeplot(data=df,x='returns_3yr')
sns.kdeplot(data=df,x='returns_5yr')
plt.legend()
plt.grid()
plt.show()
sns.countplot(x='category',data=df,hue='rating')
plt.show()
fig,ax=plt.subplots()
ax.pie(df['expense_ratio'].head(),labels=df['fund_manager'].head())
ax.set_title('expense_ratio')
plt.show()
