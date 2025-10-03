from pathlib import Path

def create_corpus():
    """
    Merges Garchen Rinpoche's transcripts with a general Tibetan dataset
    to create a single corpus file for tokenizer training.
    """
    # 1. Define file paths
    gr_text_path = Path("/home/gangagyatso/Desktop/stt-bpe-trainer/data/corpus/gr_submitted_text.txt")
    corpus_path = Path("/home/gangagyatso/Desktop/stt-bpe-trainer/data/corpus/generalcorpus.txt")
    merged_corpus_path = Path("/home/gangagyatso/Desktop/stt-bpe-trainer/data/corpus/mergedcorpus.txt")
    # Check if the Garchen Rinpoche file exists
    if not gr_text_path.exists():
        print(f"Error: The file '{gr_text_path}' was not found.")
        print("Please make sure the transcript file is in the same directory.")
        return

    # 2. Load Garchen Rinpoche transcripts from the local text file
    print(f"Loading Garchen Rinpoche transcripts from '{gr_text_path}'...")
    with open(gr_text_path, "r", encoding="utf-8") as f:
        gr_texts = [line.strip() for line in f.readlines() if line.strip()]
    print(f"-> Loaded {len(gr_texts)} lines.")

    # 3. Load general Tibetan transcripts from the local text file
    print(f"Loading general Tibetan transcripts from '{corpus_path}'...")
    with open(corpus_path, "r", encoding="utf-8") as f:
        general_texts = [line.strip() for line in f.readlines() if line.strip()]
    print(f"-> Loaded {len(general_texts)} lines.")

    # 4. Combine the two text sources
    all_texts = 20 * gr_texts + general_texts
    
    # 5. Report on the composition of the corpus
    total_lines = len(all_texts)
    if total_lines > 0:
        gr_ratio = 20 * len(gr_texts) / total_lines
        print(f"\nGarchen Rinpoche transcripts make up {gr_ratio:.2%} of the total combined lines.")

    # 6. Write the combined corpus to a single file
    print(f"Writing {len(all_texts)} total lines to '{merged_corpus_path}'...")
    with open(merged_corpus_path, "w", encoding="utf-8") as f:
        for line in all_texts:
            f.write(line + "\n")

    print(f"\nSuccessfully created '{merged_corpus_path}'.")

if __name__ == "__main__":
    create_corpus()
