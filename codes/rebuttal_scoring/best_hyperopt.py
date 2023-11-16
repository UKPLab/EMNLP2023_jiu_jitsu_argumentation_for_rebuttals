import glob
import numpy as np
import codecs
import csv


def main():
    # get dev results
    path = '../models'

    all_models =[f'{path}/bert_neg_100', f'{path}/bert_pre_100', f'{path}/bert_all_100',f'{path}/roberta_all_100', f'{path}/roberta_neg_100', f'{path}/scibert_all_100', f'{path}/scibert_neg_100', f'{path}/scibert_pre_100', f'{path}/roberta_pre_100']

    for model in all_models:
        files = glob.glob(f"{model}*/eval_results.txt")
        scores = []
        for file in files:
            with open(file) as f:
                for line in f.readlines():
                    if "overall" in line:
                        scores.append(float(line.split("\'pearsonr\': ")[1].split(", \'pearsonp\'")[0]))
        max_index = np.argmax(scores)
        max_config = files[max_index]
        print("Best dev result: " + max_config)

if __name__=='__main__':
    main()