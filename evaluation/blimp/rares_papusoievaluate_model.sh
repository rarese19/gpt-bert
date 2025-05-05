python blimp.py \
    --input_path="./data" \
    --output_dir="blimp_results/gptbert-remake-clean-slate" \
    --tokenizer_path="../../tokenizers/tokenizer_10M.json" \
    --model_path_or_name="../../model_checkpoints/small_15-16_babylm_10M_15_16.bin" \
    --config_file="../../configs/small.json" \
    --backend="causal" \
    --batch_size=64 \
    --architecture="extra" \
    --predict
