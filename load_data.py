import pandas as pd

df1 = pd.read_excel("snippets.xlsx", engine='openpyxl')
columns = df1.columns

sentence = df1[columns[0]].to_list()
label = df1[columns[1]].to_list()

sentence.append(columns[0])
label.append(columns[1])

sentence = [s.lower().replace("<em>", "") for s in sentence]
label = [l.lower().split(',') for l in label]
count = 1
for s in zip(sentence, label):
    print(count, s)
    count += 1
