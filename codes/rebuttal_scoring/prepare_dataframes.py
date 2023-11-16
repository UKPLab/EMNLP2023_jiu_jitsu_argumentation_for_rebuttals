import pandas as pd
import random
import pickle

random.seed(42)

def split_based_on_aspects():
    #return train_aspects
    with open('train_aspects.pkl', 'rb') as f:
        train_aspects = pickle.load(f)
    with open('dev_aspects.pkl', 'rb') as f:
        dev_aspects = pickle.load(f)
    with open('test_aspects.pkl', 'rb') as f:
        test_aspects = pickle.load(f)
    print(train_aspects)
    print(test_aspects)
    print(dev_aspects)
    all_aspects_train = train_aspects+ dev_aspects

    return all_aspects_train, train_aspects, dev_aspects, test_aspects

def create_row_bert_style(desc, row):
    text = desc + " [SEP] " + row['action']+ " [SEP] " +row['canonical_rebuttal']
    return text

def merge_dataframes():
    data_path_can_reb = '../../data/canonical_rebuttals_and_descs/rebuttals_scores_with_out_page_rank.tsv'
    data_path_descs = '../../data/canonical_rebuttals_and_descs/all_cluster_descs.txt'
    df = pd.read_csv(data_path_can_reb, sep='\t')
    desc_df = pd.read_csv(data_path_descs, sep='\t')
    all_descs = []

    for idx, rows in df.iterrows():
        new_df = desc_df[(desc_df['aspects']==rows['aspects']) & (desc_df['sections']==rows['sections'])] 
        all_descs.append(create_row_bert_style(new_df['descs'].tolist()[0], rows))
        #print(new_df['descs'].tolist()[0])
        del new_df
    df['descs']= all_descs
    print(f'Len of descs:{len(all_descs)}')
    print(f'Len of can df: {len(df)}')

    train_aspects, topics_train, topics_dev, topics_test = split_based_on_aspects()
    train_df = df[df['aspects'].isin(topics_train)]
    valid_df =  df[df['aspects'].isin(topics_dev)]
    test_df =  df[df['aspects'].isin(topics_test)]
    #test_df = df[~df['aspects'].isin(train_aspects)]
    test_df_with_aspects = test_df
    test_df = test_df [['descs','scores']]
    
    #rest_df = df[df['aspects'].isin(train_aspects)]
    #topics_train = random.sample(list(set(rest_df['aspects'].tolist())), 4)

    #train_df = rest_df[rest_df['aspects'].isin(topics_train)]
    train_df_with_aspects = train_df
    train_df=train_df[['descs','scores']]

    #valid_df = rest_df[~rest_df['aspects'].isin(topics_train)]
    valid_df_with_aspects = valid_df
    valid_df = valid_df[['descs','scores']]

    train_df.to_csv('data/train.csv', sep = '\t', index=None)
    valid_df.to_csv('data/dev.csv', sep='\t', index=None)
    test_df.to_csv('data/test.csv', sep='\t', index=None)



#def add_other_rebuttals(df):
if __name__=='__main__':
    merge_dataframes()
