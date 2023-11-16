import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score, classification_report
import random
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy.stats import pearsonr, spearmanr

def compute_metrics(labels, preds):
    preds = np.squeeze(preds.reshape(len(preds),1))
    labels = np.squeeze(labels.reshape(len(preds),1))
    print(preds.shape)
    print(labels.shape)
    mae = mean_absolute_error(labels, preds)
    mse = mean_squared_error(labels, preds)
    pearson, p = pearsonr(labels, preds)
    spearman, sp = spearmanr(labels, preds)

    return {
        "mae": mae,
        "mse": mse,
        "pearsonr": pearson,
        "pearsonp": p,
        "spearmanr": spearman,
        "spearmanp": sp
    }

def random_uniform_nos(seed, l):
    random.seed(seed)
    all_rand_nos=[]
    for j in range(l):
        n = random.uniform(0,1)
        all_rand_nos.append(n)
    return np.array(all_rand_nos)

def main():
    df = pd.read_csv('data/test.csv', sep='\t')
    all_scores = df.loc[:, df.columns != 'descs']
    all_scores = all_scores.to_numpy()
    #all_scores = all_scores.astype(int)
    mic_f1, rmse= [], []
    for seed in [21, 42, 45, 53, 67]:
        random_predictions = random_uniform_nos(seed, len(all_scores))
        scores = compute_metrics(all_scores, random_predictions)
        mic_f1.append(scores["pearsonr"])
        rmse.append(scores["mse"])
    print(f'Average pearson:{np.mean(mic_f1)}')
    print(f'STD:{np.std(mic_f1)}')
    print(f'Average rmse:{np.mean(mic_f1)}')
    print(f'STD:{np.std(mic_f1)}')


if __name__=='__main__':
    main()
