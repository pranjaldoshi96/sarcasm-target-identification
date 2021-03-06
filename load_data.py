import pandas as pd

def load_data():
    df1 = pd.read_excel("snippets.xlsx", engine='openpyxl')
    columns = df1.columns

    sentence = df1[columns[0]].to_list()
    label = df1[columns[1]].to_list()

    sentence.append(columns[0])
    label.append(columns[1])

    sentence = [s.lower().replace("<em>", "") for s in sentence]
    label = [l.lower().split(',') for l in label]

    return sentence, label


if __name__ == '__main__':
    sentence, label = load_data()
