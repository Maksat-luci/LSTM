import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime



# Чтение таблицы из CSV файла
df = pd.read_csv('5minute.csv')

# Преобразование столбцов 'Open time' и 'Close time' в значения типа datetime
df['Open time'] = pd.to_datetime(df['Open time'], unit='s')
df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')

# Построение графика
plt.plot(df['Open time'], df['Close'])
plt.xlabel('Time')
plt.ylabel('Close')
plt.title('Close Price Over Time')
plt.xticks(rotation=45)
plt.show()