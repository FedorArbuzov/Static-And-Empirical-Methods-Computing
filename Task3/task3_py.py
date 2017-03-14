import pandas as pd
import scipy.stats as stat
import matplotlib.pyplot as plt

data = pd.read_excel('Данные к задаче 3 дз.xls')

x_data = list(data['x9'])
y_data = list(data['y9'])


print(stat.pearsonr(x_data, y_data)[0])

print(stat.spearmanr(x_data, y_data)[0])

plt.scatter(x_data, y_data)
plt.show()





