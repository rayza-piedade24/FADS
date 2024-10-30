import pandas as pdf

cancer_data = pd.read_csv('./raw-data/data.csv')
pd.options.display.max_columns = len(cancer_data)
print(f'Number of entries: {cancer_data.shape[0]:,}\n'
      f'Number of features: {cancer_data.shape[1]:,}\n\n'
      f'Number of missing values: {cancer_data.isnull().sum().sum()}\n\n'
      f'{cancer_data.head(2)}')