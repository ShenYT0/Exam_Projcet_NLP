# Exam_Projcet_NLP
Exam project for [TALA540A - Documents structures](https://github.com/RimeAB/TALA540A-24-25/blob/main/Examen_Projet_NLP.md)

We chose a parallel corpus of translation tasks and used it to evaluate the translation model.
## Groupe Member
> [Siman CHEN] (https://github.com/simannnc)
> 
> [Weiqi ZHANG] (https://github.com/CourantEnCourant)
> 
> [Yuntian SHEN] (https://github.com/ShenYT0)
>

## Selected Corpus
**Japanese-English Business Scene Dialogue parallel corpus**

https://paperswithcode.com/dataset/business-scene-dialogue

## Selected Model
https://huggingface.co/Helsinki-NLP/opus-mt-ja-en (For evaluation)

https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt (For comparison)

## Corpus analysis

For more details, please refer to branch [corpus_analysis](https://github.com/ShenYT0/Exam_Projcet_NLP/tree/corpus_analysis)

A detailed account of the description and analysis of various aspects of our chosen corpus is given here.

## Introducing the model

For more details, please refer to branch [model_comparison](https://github.com/ShenYT0/Exam_Projcet_NLP/tree/model_comparison)

The features used in our chosen model are described here, and a comparison of the performance of two different models is presented, with their advantages and disadvantages shown.

## Evaluating the model by corpus

For the script of evalution, please refer to branch [model_evaluation](https://github.com/ShenYT0/Exam_Projcet_NLP/tree/model_evaluation)

We used two models to translate the Japanese portion of the corpus, and compared the machine translation results of the models with the original human translation results of the parallel corpus to calculate the BLEU scores and thus evaluate the models. The results obtained are [here](https://github.com/ShenYT0/Exam_Projcet_NLP/blob/model_evaluation/results/result.json)

As a complement, here [notebook](model_evaluate.ipynb) uses the `Helsinki-NLP/opus-mt-ja-en` model to compute BLEU scores for different sub-corpora.

## Difficulties Encountered
The difficulties encountered come mainly from the lack of computing performance, which causes the model to run abnormally slow.

## Avenues for Improvement
If other algorithms for evaluating the level of translation can be found, the results can be evaluated more comprehensively.


## Results
The results indicate that although `opus-mt-ja-en` operates faster, the larger model, `mbart-large-50-many-to-many-mmt`, which is trained on a more extensive dataset, achieves higher scores and performs better.
In [notebook](model_evaluate.ipynb), the results show that the `opus-mt-ja-en` model is better at spoken text with short sentences, which is evidenced by the fact that the category "general chatting" with shorter sentences have achieved higher bleu scores than other categories.  

![<# alt text #>](../../../../var/folders/zf/pddfgzln54z8s3jv_bd136wm0000gn/T/TemporaryItems/NSIRD_screencaptureui_HHEUNh/Screenshot%202024-11-07%20at%2000.13.01.png "Screenshot")
