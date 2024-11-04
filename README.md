# Exam_Projcet_NLP
We found two popular and easy-to-use models on HuggingFace for machine translation task, specifically from Japanese to English :
Helsinki-NLP/opus-mt-ja-en (https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) and facebook/mbart-large-50-many-to-many-mmt (https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt). 

Furthermore, we hope to compare their performance on translation benchmark. Here, I will detail the frameworks, tokenizers, configurations, and other relevant aspects of both models. Usage demonstrations are provided in the notebook.

### MarianMT Model

**1. Overview**

- **Framework**: MarianMT is a series of translation models developed using the Marian NMT framework, which are known for their efficiency and performance in neural machine translation.
- **Specific Model**: The `Helsinki-NLP/opus-mt-ja-en` model is specifically trained to translate from Japanese to English. It is trained on OPUS.
- **Tokenizer**: The model uses SentencePiece for tokenization, a popular choice for handling diverse scripts and languages efficiently. SentencePiece models (source.spm and target.spm) are typically used for both the source language (Japanese) and the target language (English), enabling subword tokenization that balances the vocabulary size with the granularity of language representation.
- **Configuration:** Files can be found on https://huggingface.co/Helsinki-NLP/opus-mt-ja-en/tree/main

 `config.json`: This file contains the main settings for the model. This model incorporates 6 layers of encoders and decoders with 8 attention heads each. Each transformer layer uses a self-attention mechanism and has a model dimension of 512, with a feed-forward dimension of 2048.
`tokenizer_config.json` :This file includes specific settings for the tokenizer, such as the source and target languages.spécifiques au tokenizer, comme les langues source et cible.

`generation_config.json` These settings collectively define the structure, operational dynamics, and optimization approaches of the model. It's configured as an encoder-decoder model. For example, parameters related to text generation, such as maximum length, using beam search fixed at 6.

**2. Key Features**

- **Model Design**: MarianMT models are designed for specific language pairs, which can limit their use to the languages they were trained on but optimize their performance for those specific translation tasks. For example, here we use`Helsinki-NLP/opus-mt-ja-en` for translation from Japanese to English, but if we want to translate English to Japanese, we ned to use another model, which is `Helsinki-NLP/opus-mt-en-ja`.
- **Efficiency**: Generally, MarianMT models are smaller and faster, making them suitable for environments where resources are limited or quick translations are necessary.

### mBART Model

**1. Overview**

- **Framework**: mBART is a multilingual sequence-to-sequence model designed by Facebook, which extends the BART architecture to multiple languages. It is pre-trained on a large corpus covering 50 different languages.
- **Specific Model**: This model is a fine-tuned checkpoint of [**mBART-large-50**](https://huggingface.co/facebook/mbart-large-50). `mbart-large-50-many-to-many-mmt` is fine-tuned for multilingual machine translation. It is pre-trained on a large-scale corpus covering 50 different languages. This model uses a multilingual setup to handle translations across various language pairs, not just from Japanese to English.
- **Tokenizer**: `MBart50TokenizerFast`is also based on SentencePiece, supporting fast tokenization for 50 different languages.
- **Configuration:** Files can be found on https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt/tree/main.  `config.json`:gives  a comprehensive look at the configuration parameters of the mBART-50 model, particularly tailored for multilingual machine translation. The model follows an encoder-decoder structure with each consisting of 12 layers. Both the encoder and decoder feature 1024 units per layer with 16 attention heads, enabling the model to capture various aspects of language through multiple focus points. For sequence handling, the model supports sequences up to 1024 tokens long, and It uses predefined token IDs to mark the beginning and end of sequences (BOS: 0, EOS: 2) and for padding (PAD: 1).

**2. Key Features**

- **Model Design**: mBART models are built to handle translation, text generation, and fine-tuning for various NLP tasks across multiple languages, not limited to specific language pairs. When using the mBART-large-50-many-to-many-mmt model for translating from Japanese to English, it also involves setting specific parameters to direct the model's attention towards the correct language pair during translation.
- **Size and Performance**: These models are larger in size, which may lead to slower inference times but generally better translation quality and versatility across many languages.

### Comparison

- **Library Utilization**: Both models are available through the `transformers` library, offering easy integration into Python-based projects with robust support for NLP tasks.
- **Language Support**: MarianMT is limited to specific language pairs (in this case, Japanese to English), making it less versatile than mBART, which supports translation between 50 languages.
- **Usage:** When using an mBART model for translation, such as translating from Japanese to English, there are specific parameters that need to be set to correctly guide the model's translation process. For example, we need to specify the source (`src_lang`) and target (`tgt_lang`) languages, as well as update the tokenizer's language settings, `tokenizer.src_lang = src_lang` . This contrasts with using a language-specific model like `Helsinki-NLP/opus-mt-ja-en` from MarianMT, which is pre-configured for its language pairs and generally does not require the setting of additional parameters for the language direction.
- **Tokenisers:** Both tokenizers are  based on the SentencePiece model. However, MarianMT's tokenizer is optimized for specific language pairs, ensuring efficient and effective translation within those bounds, while mBART's tokenizer supports a much broader range of languages, suitable for a multilingual context. Also, in the small script which is for demonstration of usagae, we can see `MBart50TokenizerFast` performs faster than the MarianMT's tokenizer.
- **Model Size and Runtime**: MarianMT models are smaller and faster, suited for quicker translation tasks with limited resources. mBART models, being larger, are generally slower but can handle a wider variety of languages and more complex translation tasks.

Based on these aspects, we will  performance the translation task on a benmark corpus using these two models and further compare the quality of both results.