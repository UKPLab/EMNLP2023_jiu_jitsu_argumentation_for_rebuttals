import pandas as pd
import os
from variables import all_rebuttals
import pickle

def split_based_on_can_rebuttals(df_extended):
    #return train_aspects
    canonical_rebuttals = df_extended['canonical_rebuttals'].tolist()
    train = canonical_rebuttals[:round(len(canonical_rebuttals)*0.6)]
    rest = list(set(canonical_rebuttals)- set(train))
    dev = rest[:round(len(rest)*0.1)]
    test = list(set(canonical_rebuttals)-set(train+dev))
    train_df = df_extended[df_extended['canonical_rebuttals'].isin(train)]
    dev_df = df_extended[df_extended['canonical_rebuttals'].isin(dev)]
    test_df = df_extended[df_extended['canonical_rebuttals'].isin(test)]
    return train_df, dev_df, test_df

    

parent_path = '../data'
def get_reviews(aspect, section):
    f  = open(os.path.join(parent_path,aspect, 'review', f'{section}.txt'))
    reviews = f.readlines()
    reviews = [rev.strip('\n') for rev in reviews]
    return reviews

def create_joined_dataframe(df):
    aspects = df['aspects'].tolist()
    sections = df['sections'].tolist()
    new_labels = [f'{asp}_{sec}' for asp, sec in zip(aspects, sections)]
    df['new_labels'] = new_labels
    return df

def add_actions(rem_actions, df):
    aspect = list(set(df['aspects'].tolist()))[0]
    sections = list(set(df['sections'].tolist()))[0]
    #action = list(set(df['action'].tolist())) [0]
    new_labels  = list(set(df['new_labels'].tolist()))[0]
    print(new_labels)
    print(rem_actions)
    for action in rem_actions:
        new_row = {'aspects':aspect, 'sections':sections, 'action':action, 'canonical_rebuttal': 'No rebuttal', 'new_labels': new_labels}
        df = df.append(new_row, ignore_index=True)
    return df

def create_new_df(all_labels, new_rebuttal_df):
    all_aspects, all_sections, all_actions, all_canonical_rebuttals, all_new_labels = [],[],[],[],[]
    for label in all_labels:
        new_df = new_rebuttal_df[new_rebuttal_df['new_labels']==label]
        actions = new_df['action'].tolist()
        remaining_actions =  set(all_rebuttals)- set(actions)
        new_df = add_actions(remaining_actions, new_df)
        aspects = new_df['aspects'].tolist()
        sections = new_df['sections'].tolist()
        rebuttals = new_df['canonical_rebuttal'].tolist()
        new_labels  = new_df['new_labels'].tolist()
        avl_actions = new_df['action'].tolist()
        all_aspects.extend(aspects)
        all_sections.extend(sections)
        all_actions.extend(avl_actions)
        all_canonical_rebuttals.extend(rebuttals)
        all_new_labels.extend(new_labels)
        del new_df
    df = pd.DataFrame({'aspects': all_aspects, 'sections':all_sections, 'actions': all_actions, 'canonical_rebuttal': all_canonical_rebuttals, 'new_labels': all_new_labels})
    
    return df


def get_reviews(aspect, section):
    f  = open(os.path.join(parent_path,aspect, 'review', f'{section}.txt'))
    reviews = f.readlines()
    reviews = [rev.strip('\n') for rev in reviews]
    return reviews

def join_revs_with_actons(revs,actions):
    rev_joined_actions =[f"{rev}' [SEP] '{act}" for rev,act in zip(revs, actions)]
    return rev_joined_actions

def join_with_revs(df):
    all_reviews, all_actions, all_aspects, all_secs, all_rebuttals = [],[], [],[], []
    for idx, rows in df.iterrows():
        revs = get_reviews(rows['aspects'], rows['sections'])
        print('reviews')
        aspects = [rows['aspects']]*len(revs)
        sections = [rows['sections']]*len(revs)
        actions = [rows['actions']]*len(revs)
        can_rebs = [rows['canonical_rebuttal']]*len(revs)
        all_reviews.extend(revs)
        all_aspects.extend(aspects)
        all_secs.extend(sections)
        all_actions.extend(actions)
        all_rebuttals.extend(can_rebs)
    
    print(f'Len of revs:{len(set(all_reviews))}')
    revs_joined_actions = join_revs_with_actons(all_reviews, all_actions)
    df = pd.DataFrame({'aspects': all_aspects, 'sections':all_secs, 'reviews': revs_joined_actions, 'actions': all_actions, 'canonical_rebuttals': all_rebuttals})
   
    return df

def main():
    rebuttal_df  = pd.read_csv('../../data/canonical_rebuttals_and_descs/all_canonical_rebuttals.tsv', sep='\t')
   
    new_rebuttal_df = create_joined_dataframe(rebuttal_df)

    all_labels  = set(new_rebuttal_df['new_labels'].tolist())
    df = create_new_df(all_labels, new_rebuttal_df)
    df_extended = join_with_revs(df)
    
   

    #train_df, valid_df = train_test_split(rest_df, test_size=0.1)
    train_df, valid_df, test_df = split_based_on_can_rebuttals(df_extended)
    test_df = test_df [['reviews', 'canonical_rebuttals']]
    
    train_df=train_df[['reviews', 'canonical_rebuttals']]

    valid_df = valid_df[['reviews', 'canonical_rebuttals']]

    train_df.to_csv('can_reb/train.csv', sep = '\t', index=None)
    valid_df.to_csv('can_reb/dev.csv', sep='\t', index=None)
    test_df.to_csv('can_reb/test.csv', sep='\t', index=None)

if __name__=='__main__':
    main()
