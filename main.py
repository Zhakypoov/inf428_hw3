import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# Используем бэкэнд 'Agg'
matplotlib.use('Agg')

# Загрузка данных
data = pd.read_csv('churn_magic.csv', sep=';')

# Проверяем данные
print(data.head())

# Фильтрация по churn_risk_score
churn_0 = data[data['churn_risk_score'] == 0]
churn_1 = data[data['churn_risk_score'] == 1]

# Рассчет описательной статистики
stats = data.describe()
print("Описательная статистика:")
print(stats)

# Анализ конкретного признака
feature = 'magic_feature_0'  # Замените на интересующий признак
sns.kdeplot(churn_0[feature], label='Churn = 0', fill=True)
sns.kdeplot(churn_1[feature], label='Churn = 1', fill=True)
plt.title(f'Распределение {feature}')
plt.legend()

# Сохраняем график в файл
plt.savefig('distribution_plot.png')
