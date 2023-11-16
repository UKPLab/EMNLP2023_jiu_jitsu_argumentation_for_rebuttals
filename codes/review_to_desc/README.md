# README
We use the same file main.py to train different models:
* T5
* BART
* Pegasus

The data can be created in multiple forms. You need to do the following to generate different splits on the data:
1. Split on attitude roots. This will save the data in ```data``` folder
``` python
python create_data.py
```

2. For finetuning, change the train test and dev files as needed for each of the folders
For BART/PEGASUS ((google/pegasus-large)), we use the command,
``` python    
python main.py \
--model_name_or_path facebook/bart-large \ 
--do_train \
--do_eval \
--do_predict \
--seed 42 \
--num_beams 5 \
--train_file  'train.csv'\
--validation_file 'dev.csv'\
--test_file  'test.csv'\
--output_dir bart/$epochs/$learning_rate \
--overwrite_output_dir \
--per_device_train_batch_size=8 \
--per_device_eval_batch_size=8 \
--gradient_accumulation_steps 4 \
--num_train_epochs $epochs \
--learning_rate $learning_rate \
--save_steps -1 \
--report_to 'none' \
--predict_with_generate
```

For T5, we use the command,
``` python    
python main.py \
--model_name_or_path t5-large \
--do_train \
--do_eval \
--do_predict \
--num_beams 5 \
--prefix "Generate Description" \
--train_file  'train.csv'\
--validation_file 'dev.csv'\
--test_file  'test.csv'\
--output_dir bart/$epochs/$learning_rate \
--overwrite_output_dir \
--per_device_train_batch_size=8 \
 --per_device_eval_batch_size=8 \
--gradient_accumulation_steps 4 \
--num_train_epochs $epochs \
--learning_rate $learning_rate \
--save_steps -1 \
 --report_to 'none' \
--predict_with_generate
```

3. We change the train and validation file for few-shot setups from the folder ```few_shot```. We use the test set created in Step 2.
* ```1_shot``` (contains 1 shot train,valid files)
* ```2_shot``` (contains 2_shot train,valid files)

We run the same finetuning codes as in Step 2.

