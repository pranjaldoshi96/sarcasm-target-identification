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


def annotate_data():
    sentence, label = load_data()

    for q in zip(sentence, label):
        s,l = q
        tags = ' '.join(['O'] * len(s.split()))

        print("--------")
        print(s)
        for label in l:
            slots = label.split()
            print(slots)
        print("--------")
        #print(s)
        #print(tags, l)

annotate_data()

if __name__ == '__main__':
    sentence, label = load_data()
