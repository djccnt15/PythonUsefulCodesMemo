import pandas as pd
import statsmodels.formula.api as smf

dataset = pd.read_csv('dataset.csv')

'''targetting var'''
independ_names = ' + '.join(dataset.columns)
depend_name = "target"

'''modeling'''
model = depend_name + ' ~ ' + independ_names
# print(model)

result = smf.ols(formula=model, data=dataset)
