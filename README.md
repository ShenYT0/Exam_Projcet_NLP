# Model evaluation
This branch is the model evaluation for translation task
## Model choice
We evaluated two seq2seq model for Japanese to English translation: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian) and [facebook mbart](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt).
## Translation scripts
- Two notebooks are presented in the `script` directory. These two notebooks use the corresponding model to translate the corpus presented in `data/ryo0634__bsd_ja_en`. 
- The reason that we used two notebooks instead of a `.py` file is that each model requires some minor modifications to the script, which excludes the possibility to use the `argparse` module.
- We basically used these models to translate a portion of `bsd` dataset (where the original sentence is in Japanese) on a server. We then output the translated dataset, with three columns: `['ja_sentence', 'translations', 'en_sentence']`. Needless to say, `en_sentence` serves as the golden corpus for model performance evaluation.
- These notebooks output two datasets saved in `.parquet` format in the `data` directory.
## Evaluation
- We used `data/evaluation.py` script to evaluate the datasets with translation.
- For usage of the script, use `python evaluation.py -h` in the command line.
- In general
- `evaluation.py` output a `results/result.json` file.
## Quantitative test
- We notice that the `facebook_mbart` model produces a higher bleu score of 0.143 (vs. 0.138 by MarianMT), it yields better results for n-gram precision as well.
## Qualitative test
- It might be difficult to interpret the quantitative test just by itself as differences in bleu score seem quite small between the two models. 
- We also conducted a few qualitative test in the `.ipynb` file. From a human reader's point of view, the `facebook_mbart` model's translations are significantly better. `MarianMT`'s sentences are quite often grammatically incorrect and they correspond poorly to the Japanese sentences' original meaning. The facebook model's sentences are intuitively more readable.
## Further improvements
- After these first tests and discussion with colleagues, we conducted a more thorough evaluation [here](https://github.com/ShenYT0/Parallel-corpus-evaluation-for-translation-tasks/blob/main/model_evaluate.ipynb).
