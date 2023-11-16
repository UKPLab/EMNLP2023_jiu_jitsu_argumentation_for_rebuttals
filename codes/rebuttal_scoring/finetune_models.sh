#!/bin/bash
export LEARNING_RATE=1e-4
export EPOCHS=5
export model_name='roberta-base'
export model_prefix = 'roberta_pre'

for EPOCHS in 5.0; do
    for SEED in 23 31 42 53 61 ; do
        DATA_DIR=data
        BATCH_SIZE=32
        LEARNING_RATE=1e-4
        OUTPUT_DIR=finetuned_models/${model_prefix}_${SEED}_${LEARNING_RATE}_${EPOCHS}/

        python main.py \
            --model_name_or_path ${model_name} \
            --train_file ${DATA_DIR}/train.csv \
            --validation_file ${DATA_DIR}/dev.csv \
            --task_name jitsupeer \
            --do_train \
            --do_eval \
            --do_test \
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