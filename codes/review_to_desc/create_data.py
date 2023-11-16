import pandas as pd
import os
import random
from sklearn.model_selection import train_test_split
random.seed(42)
import json

parent_path = '../../data'

from imblearn.over_sampling import RandomOverSampler


def get_reviews(aspect, section):
    f  = open(os.path.join(parent_path,aspect, 'review', f'{section}.txt'))
    reviews = f.readlines()
    reviews = [rev.strip('\n') for rev in reviews]
    return reviews




def main():
    desc_df  = pd.read_csv('../../data/canonical_rebuttals_and_descs/all_cluster_descs.txt', sep='\t')
    all_reviews, all_descs, all_aspects, all_secs = [],[], [],[]
    for idx, rows in desc_df.iterrows():
        revs = get_reviews(rows['aspects'], rows['sections'])
        print('reviews')
        descs = [rows['descs']]*len(revs)
        aspects = [rows['aspects']]*len(revs)
        sections = [rows['sections']]*len(revs)
        all_reviews.extend(revs)
        all_descs.extend(descs)
        all_aspects.extend(aspects)
        all_secs.extend(sections)
    df = pd.DataFrame({'aspects': all_aspects, 'sections':all_secs, 'descs': all_descs, 'reviews': all_reviews})
    print(len(df))

    label_list = set(df['descs'].tolist())
    label_to_id = {v: i for i, v in enumerate(label_list)}


    rest_df, test_df = train_test_split(df, test_size=0.2)

    train_df, valid_df = train_test_split(rest_df, test_size=0.1)

    test_df = test_df [['reviews', 'descs']]
    
    train_df=train_df[['reviews', 'descs']]

    valid_df = valid_df[['reviews', 'descs']]


    train_df.to_csv('data/train.csv', sep = '\t', index=None)
    valid_df.to_csv('data/dev.csv', sep='\t', index=None)
    test_df.to_csv('data/test.csv', sep='\t', index=None)




if __name__=='__main__':
    main()

