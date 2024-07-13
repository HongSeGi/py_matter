import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#tip에 관련된 데이터셋을 불러온다.
tips = sns.load_dataset('tips')

plt.figure(figsize=(12, 12))
# sns.scatterplot(x= 'total_bill', y= 'tip', hue='time', data= tips)
sns.scatterplot(x= 'total_bill', y= 'tip', hue='day', style='time', data= tips)
plt.show()