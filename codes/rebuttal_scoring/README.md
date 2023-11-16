We use different versions of models for training on this task:
* Pretrained BERT (bert-base-uncased)
* Prerained RoBERTa (roberta-base)
* Pretrained SciBERT (allenai/scibert_scivocab_uncased)  

The rest of the models have been domain specialized (available here). We use some abbreviations within parentheses that are used as model prefixes laters for better naming conventions:
* BERT_all [bert_all]
* RoBERTa_all [roberta_all]
* SciBERT_all [scibert_all]
* BERT_neg [bert_neg]
* RoBERTa_neg [roberta_neg]
* SciBERT_neg [scibert_neg]

We also use some abbreviations for the pre-trained models as well:
* Pretrained BERT (bert-base-uncased) [bert_pre]
* Prerained RoBERTa (roberta-base) [roberta_pre]
* Pretrained SciBERT (allenai/scibert_scivocab_uncased) [scibert_pre]

We can first create the data in the format required for scoring.
``` python
        python prepare_dataframes.py
```
The data used in our work is provided in the data folder. You can change the train, dev and test aspects used for splitting the data initially (which we load from pkl files).

We first do hyper-parameter search using following:
``` python
        ./hyperparameter_tuning.sh
```
We change the model names to do the hyper-parameter tuning. The script requires model_name and model_prefix. For eg., in the shell script, the model_name is 'roberta-base' for pre-trained roberta and the model_prefix is 'roberta_pre'. 

We then run the following script to get the best hyper-parameters on the validation set.

``` python
python best_hyperopt.py
```

We then take finetune the models with best hyper-parameters found in the previous step.

``` python
./finetune_models.sh
```
We change the model names and hyper-parameters based on the grid-search before. 

----------------------------------------------------------------------------------------------------------------------------------
To run the other baselines:
* For majorty baseline
    ```python
    python majority_baseline.py
    ```
* For random baseline
    ```python
    python random_baseline.py
    ```