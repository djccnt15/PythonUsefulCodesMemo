'''targetting var'''
# independ var
names = train.columns[:]
independ_names = ""

for i in names:
    if independ_names == "": independ_names = i
    else: independ_names = independ_names + " + " + i
# print(independ_names)

# depend var
depend_name = "EF07ExpectMatuLevel"

'''modeling'''
model = depend_name + " ~ " + independ_names
# print(model)

result = sm.ols(formula=model, data=train)
