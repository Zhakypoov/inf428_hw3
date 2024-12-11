import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print('--------------------------------------------------')
print('----------- First 5 rows from csv file -----------')
print('--------------------------------------------------')

data = pd.read_csv('churn_magic.csv', sep=';', encoding='ISO-8859-1')
magic_features = [col for col in data.columns if col.startswith('magic_feature')]

print('-----------------------------------------')
print('----------- mean, median, std -----------')
print('-----------------------------------------')

descriptive_stats = data.groupby('churn_risk_score')[magic_features].agg(['mean', 'median', 'std'])
print(descriptive_stats)

print('------------------------------------------')
print('----------- Correlation matrix -----------')
print('------------------------------------------')

correlation_matrix = data[magic_features + ['churn_risk_score']].corr()
print(correlation_matrix)

print('-------------------------------')
print('----------- Sorting -----------')
print('-------------------------------')

correlation_with_churn_abs = correlation_matrix['churn_risk_score'].drop('churn_risk_score').abs()
sorted_features_abs = correlation_with_churn_abs.sort_values(ascending=False)

print(sorted_features_abs.head(5))
