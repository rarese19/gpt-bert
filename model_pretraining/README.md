TODO: Add files from old folder
TODO: Modify files (remove scare code, cleanup, add descriptions)
TODO: Create single GPU training
TODO: Finish README


## Training

After preprocessing your data, creating your tokenizer, and caching the data with your tokenizer, you are ready to train your ELC BERT model. To this extent, you can run:

```bash
python train_single_gpu.py \
    --input_path="PATH_TO_CACHED_DATA" \
    --config_file="PATH_TO_CONFIG_FILE" \
    --output_dir="PATH_TO_OUTPUT_DIR" \
    --vocab_path="PATH_TO_TOKENIZER_FILE" \
    --checkpoint_path="PATH_TO_MODEL_CHECKPOINT" \ # (Optional, to continue training)
    --optimizer="NAME_OF_OPTIMIZER" \ # Options: lamb, adamw
    --scheduler="NAME_OF_SCHEDULER" \ # (Not implemented) Options: cosine
    --seq_length=MAX_SEQUENCE_LENGTH \
    --batch_size=TRAINING_BATCH_SIZE \
    --learning_rate=MAX_TRAINING_LAEARNING_RATE \
    --max_steps=NUMBER_OF_TRAINING_STEPS \
    --long_after=FRACTION_AFTER_WHICH_TO_4x_SEQUENCE_LENGTH \
    --warmup_proportion=FRACTION_OF_TRAINING_STEPS_FOR_WARMUP \
    --seed=RANDOMIZATION_SEEd \
    --log_freq=LOSS_LOGGING_FREQUENCY \ # For WANDB, unused
    --mask_p=TOKEN_MASKING_PROBABILITY \
    --short_p=PROBABILITY_OF_SHORTENING_SEQUENCE \
    --weight_decay=FRACTION_OF_WEIGHT_DECAY \
    --max_gradient=MAX_GRADIENT_BEFORE_CLIPPING \
    --gradient_accumulation=NUMBER_GRADIENT_ACCUMULATION_STEPS \
    --label_smoothing=CROSS_ENTROPY_LABEL_SMOOTHING \
    --wandb_entity="WANDB_ENTITY_NAME" \
    --wandb_name="WANDB_RUN_NAME" \
    --wandb_project="WANDB_PROJECT_NAME"
```

A few things to note:
 - In the dataset (look up `pre_training/dataset.py`) you can pass a `random_p` and `keep_p` representing the probability of a masked token being replaced by either a random token or the original token. In the code they are both set to 0.1 by default, but this can be changed.
 - Our code assumes the usage of wandb but this can be removed. In general, before calling wandb we do a check for `is_main_process()` (when running multiple GPUs/CPUs, it makes sure only one process (the main) executes the code) to make sure to not have multiple wandb runs for the same model.
 - We assume the usage of SLURM at the start of the code (to import wandb) (lines 31-32), if you do not use SLURM remove line 31 (and line 32 if you do not use wandb).