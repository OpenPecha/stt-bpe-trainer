# Tibetan Whisper Tokenizer Trainer

<h1 align="center">
  <br>
  <a href="https://openpecha.org"><img src="https://avatars.githubusercontent.com/u/82142807?s=400&u=19e108a15566f3a1449bafb03b8dd706a72aebcd&v=4" alt="OpenPecha" width="150"></a>
  <br>
</h1>

## Tibetan Whisper Tokenizer Trainer
Train and adapt Whisper tokenizers for Tibetan language speech recognition, enabling better tokenization of Tibetan text with specialized handling of syllables and tsek markers.

## Owner(s)

_Change to the owner(s) of the new repo. (This template's owners are:)_
- [@ngawangtrinley](https://github.com/ngawangtrinley)
- [@mikkokotila](https://github.com/mikkokotila)
- [@evanyerburgh](https://github.com/evanyerburgh)


## Table of contents
<p align="center">
  <a href="#project-description">Project description</a> •
  <a href="#who-this-project-is-for">Who this project is for</a> •
  <a href="#project-dependencies">Project dependencies</a> •
  <a href="#instructions-for-use">Instructions for use</a> •
  <a href="#contributing-guidelines">Contributing guidelines</a> •
  <a href="#additional-documentation">Additional documentation</a> •
  <a href="#how-to-get-help">How to get help</a> •
  <a href="#terms-of-use">Terms of use</a>
</p>
<hr>

## Project description
With Tibetan Whisper Tokenizer Trainer, you can train OpenAI's Whisper tokenizer on Tibetan text corpora to enhance speech recognition for Tibetan language content.

This toolkit helps you create specialized tokenizers that understand Tibetan syllable patterns and produce more efficient tokenization for Tibetan speech recognition tasks.


## Who this project is for
This project is intended for NLP researchers, linguists, and speech recognition developers who want to improve Whisper's tokenization performance on Tibetan language content.


## Project dependencies
Before using Tibetan Whisper Tokenizer Trainer, ensure you have:
* Python 3.8 or higher
* transformers library (with Whisper support)
* tokenizers library 
* tqdm (for progress bars)
* Internet connection (for downloading base Whisper models)


## Instructions for use
Get started with Tibetan Whisper Tokenizer Trainer by preparing your Tibetan text corpus and selecting a training mode.

### Install Dependencies
1. Install required Python packages:

   ```bash
   pip install transformers tokenizers tqdm
   ```

### Prepare Your Corpus
1. Create a directory for your Tibetan text corpus:

   ```bash
   mkdir -p data/corpus
   ```

2. Add Tibetan text files (with .txt extension) to this directory. Each file should contain Tibetan text, with one sentence or utterance per line.

### Train a Tibetan-Enhanced Tokenizer
1. Use the main training script with your preferred options:

   ```bash
   python train_tibetan_whisper_tokenizer.py \
      --model_name openai/whisper-small \
      --corpus_dir data/corpus \
      --output_dir data/tokenizer_whisper_tibetan \
      --mode hybrid \
      --vocab_size 55000
   ```

2. Available modes:
   - `train`: Complete retraining of tokenizer (slowest but most comprehensive)
   - `augment`: Only add new tokens to existing tokenizer (fastest)
   - `hybrid`: Combined approach (recommended)

### Test Your Tokenizer
1. Test the trained tokenizer on Tibetan text samples:

   ```bash
   python test_tibetan_tokenizer.py \
      --tokenizer_path data/tokenizer_whisper_tibetan \
      --sample_text "བྱང་ཆུབ་ཀྱི་སེམས་རྣམ་པ་གཉིས་ཡོད་རེད།"
   ```


### Troubleshooting

<table>
  <tr>
   <td>
    Issue
   </td>
   <td>
    Solution
   </td>
  </tr>
  <tr>
   <td>
    Cannot download Whisper model
   </td>
   <td>
    Check your internet connection and try using a smaller model first (e.g., whisper-tiny).
   </td>
  </tr>
  <tr>
   <td>
    Training is very slow
   </td>
   <td>
    Use the 'augment' mode for faster results, or use a smaller corpus size.
   </td>
  </tr>
  <tr>
   <td>
    Tokenizer is not handling tseks correctly
   </td>
   <td>
    Try different tsek_behavior settings: 'with_previous', 'with_next', or 'separate'.
   </td>
  </tr>
</table>

For Whisper model specific issues, refer to the Hugging Face documentation.


## Contributing guidelines
If you'd like to help out, check out our [contributing guidelines](/CONTRIBUTING.md).


## Additional documentation

For more information:
* [Whisper on Hugging Face](https://huggingface.co/docs/transformers/model_doc/whisper)
* [Tokenizers library documentation](https://huggingface.co/docs/tokenizers/)
* [BPE tokenization explanation](https://huggingface.co/docs/transformers/tokenizer_summary#bytepair-encoding-bpe)


## How to get help
* File an issue.
* Email us at openpecha[at]gmail.com.
* Join our [discord](https://discord.com/invite/7GFpPFSTeA).


## Terms of use
Tibetan Whisper Tokenizer Trainer is licensed under the [MIT License](/LICENSE.md).
