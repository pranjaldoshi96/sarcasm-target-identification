import pandas as pd

df1 = pd.read_excel("snippets.xlsx", engine='openpyxl')
columns = df1.columns

sentence = df1[columns[0]].to_list()
label = df1[columns[1]].to_list()

sentence.append(columns[0])
label.append(columns[1])

count = 1
for s in zip(sentence, label):
    print(count, s)
    count += 1
    print()
