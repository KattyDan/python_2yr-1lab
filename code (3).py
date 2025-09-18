import pandas as pd
import matplotlib.pyplot as plt

# Создание DataFrame с тестовыми данными
data = {
    'Товар': ['Клубника', 'Малина', 'Манго'],
    'Цена': [None, 350, 100],
    'Количество': [200, 70, 400]
}

df = pd.DataFrame(data)
print("Исходные данные:")
print(df)

# Заполнение пропусков медиан.зн
median_price = df['Цена'].median()
df['Цена'].fillna(median_price, inplace=True)

# Удаление выбросов
df = df[(df['Количество'] >= 1) & (df['Количество'] <= 1000)]

# Новый столбец
df['Общая_стоимость'] = df['Цена'] * df['Количество']

# Группировка
revenue_by_product = df.groupby('Товар')['Общая_стоимость'].sum()

print("\nВыручка по товарам:")
print(revenue_by_product)

# График
plt.figure(figsize=(7, 3))
revenue_by_product.plot(kind='bar', color=['red', 'blue', 'orange', 'yellow'])
plt.title('Выручка по товарам')
plt.xlabel('Товар')
plt.ylabel('Выручка (руб)')
plt.tight_layout()
plt.show()
