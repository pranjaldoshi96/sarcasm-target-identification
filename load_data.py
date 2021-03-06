import pandas as pd

def load_data():
    df1 = pd.read_excel("snippets.xlsx", engine='openpyxl')
    columns = df1.columns

    sentence = df1[columns[0]].to_list()
    label = df1[columns[1]].to_list()

    sentence.append(columns[0])
    label.append(columns[1])

    sentence = [s.lower().replace("<em>", "").replace('"',"").replace("?", "").replace(".","").replace(",","") for s in sentence]
    label = [l.lower().split(',') for l in label]

    return sentence, label


def annotate_data():
    sentence, label = load_data()

    for q in zip(sentence, label):
        s,l = q
        tags = [0] * len(s.split())

        words = s.split()
        print("--------")
        for label in l:
            if len(label) == 0:
                continue
            slots = label.split()
            """
            if len(slots) == 1:
                for i in range(len(words)):
                    if words[i] == slots[0]:
                        tags[i] = 1
            else:
                print(slots)
            """
            seqlen = len(slots)
            for i in range(len(words) - seqlen + 1):
                match = True
                for j in range(seqlen):
                    if words[i+j] != slots[j]:
                        match = False
                        break
                if match:
                    tags[i] = 1
                    for k in range(i+1, i + seqlen):
                        tags[k] = 2
                #print(words[i:i+seqlen])
        print(s,l)
        print(tags, l)
        print("--------")

annotate_data()

if __name__ == '__main__':
    sentence, label = load_data()
