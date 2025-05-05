import random

input_file = "babycosmofine_10M.jsonl" 

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

random.seed(42)
random.shuffle(lines)

n_valid = int(len(lines) * 0.1 + 0.5)
valid, train = lines[:n_valid], lines[n_valid:]

with open("babycosmofine_10M_validation.jsonl", "w", encoding="utf-8") as f:
    f.writelines(valid)
with open("babycosmofine_10M_train.jsonl", "w", encoding="utf-8") as f:
    f.writelines(train)

print(f"Total records:     {len(lines)}")
print(f" → Train:          {len(train)}")
print(f" → Validation:     {len(valid)}")
