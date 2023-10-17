import pandas as pd
data = pd.DataFrame({'Name':['Alvin', 'Chris'], 'Age':[24, 28]})
data.to_csv('panda_output.csv', index=False)