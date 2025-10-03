import os
import json
from tokenizers import Tokenizer

# Path to the saved tokenizer.json (from Script 1)
tokenizer_path = "/home/gangagyatso/Desktop/stt-bpe-trainer/data/whisper_tokenizer_added_tibetan/tokenizer_added.json"
output_dir = "/home/gangagyatso/Desktop/stt-bpe-trainer/data/whisper_tokenizer_added_tibetan"
os.makedirs(output_dir, exist_ok=True)

# Load tokenizer
tokenizer = Tokenizer.from_file(tokenizer_path)

# Extract vocab (token → id mapping)
vocab = tokenizer.get_vocab()
# sort by id (important!)
sorted_vocab = sorted(vocab.items(), key=lambda x: x[1])

with open(os.path.join(output_dir, "vocab.json"), "w", encoding="utf-8") as f:
    json.dump({token: idx for token, idx in sorted_vocab}, f, ensure_ascii=False, indent=2)

print(f"✅ Saved vocab.json to {output_dir}/vocab.json")

# Extract merges
model = tokenizer.to_str()  # stringified JSON of the whole tokenizer
model_json = json.loads(model)

if "model" in model_json and "merges" in model_json["model"]:
    merges = model_json["model"]["merges"]
    with open(os.path.join(output_dir, "merges.txt"), "w", encoding="utf-8") as f:
        f.write("#version: 0.2\n")
        for merge in merges:
            f.write(" ".join(merge) + "\n")
    print(f"✅ Saved merges.txt to {output_dir}/merges.txt")
else:
    print("⚠️ No merges found in tokenizer.json (check if it's really BPE)")
