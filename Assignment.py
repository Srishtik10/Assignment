# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Data.csv')
plt.figure(figsize=(7, 5))
plt.subplot(1, 2, 1)
plt.hist(df['Income'], bins=6, edgecolor='black', alpha=0.6, color='Cyan')
plt.xlabel('Income')


plt.tight_layout()
plt.show()