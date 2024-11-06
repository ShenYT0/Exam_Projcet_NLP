import evaluate
from datasets import load_dataset

from pathlib import Path
import json


def evaluate_dataset(tran, metric):
    tran = str(tran)  # Need to ameliorate this
    datadict = load_dataset('parquet', data_files=tran)
    ds = datadict['train']
    references = [[sentence['en_sentence']] for sentence in ds]
    predictions = [sentence['translations'] for sentence in ds]

    return metric.compute(predictions=predictions, references=references)


def main(translations, output):
    metric = evaluate.load("bleu")
    results = {}
    for tran in translations:
        results[str(tran)] = evaluate_dataset(tran, metric)

    with open(output, "w") as json_file:
        json.dump(results, json_file, indent=4)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Calculate bleu from input translation datasets.")
    parser.add_argument('-t', '--translations', nargs='+', required=True, type=Path, help="List of corpus.")
    parser.add_argument('-o', '--output', required=True, type=Path, help="Output file.")
    args = parser.parse_args()

    if args.output.suffix != '.json':
        raise ValueError('Output file must have .json extension.')
    for translation in args.translations:
        if translation.suffix != '.parquet':
            raise ValueError('Translation file must have .parquet extension.')
        if not translation.exists():
            raise ValueError('Translation file does not exist.')

    main(translations=args.translations,
         output=args.output)
