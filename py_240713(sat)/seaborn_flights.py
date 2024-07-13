import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#seaborn에서 제공하는 flights 데이터 셋을 사용
flights = sns.load_dataset('flights')

plt.figure(figsize=(12, 3))
sns.barplot(data=flights, x= 'year', y='passengers', palette="Blues")
plt.show()