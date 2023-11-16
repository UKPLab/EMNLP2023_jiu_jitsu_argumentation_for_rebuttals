#!/bin/bash


export model_name='roberta-base'
export model_prefix = 'roberta_pre'

for EPOCHS in 1.0 2.0 3.0 4.0 5.0; do
    for LEARNING_RATE in 2e-4 1e-4 ; do
        DATA_DIR=data
        SEED=100
        BATCH_SIZE=32
        OUTPUT_DIR=models/${model_prefix}_all_${SEED}_${LEARNING_RATE}_${EPOCHS}/

        python main.py \
            --model_name_or_path ${model_name} \
            --train_file ${DATA_DIR}/train.csv \
            --validation_file ${DATA_DIR}/dev.csv \
            --task_name jitsupeer \
            --do_train \
            --do_eval \
            --report_to "none" \
            --do_predict \
            --max_seq_length 128 \
            --per_device_train_batch_size ${BATCH_SIZE} \
            --learning_rate ${LEARNING_RATE} \
            --num_train_epochs ${EPOCHS} \
            --output_dir ${OUTPUT_DIR} \
            --seed ${SEED} \
            --overwrite_cache \
            --overwrite_output_dir \
            --save_steps -1 
    done;
done;
