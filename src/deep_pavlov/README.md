## How to set up trained DeepPavlov model

1. Set up Python 3.6.8 virtualenv and activate the virtualenv
2. Install packages from _requirenments.txt_
3. After installed, install ner_ontonotes_bert to deeppavlov

    python -m deeppavlov install ner_ontonotes_bert
4. Download trained DeepPavlov model:
    * NER tags trained only: [under releases](https://github.com/JureBevc/NLP/releases):  ner_ontonotes_bert_mult_samo_TAG.zip  (https://github.com/JureBevc/NLP/releases/download/0.2.0/ner_ontonotes_bert_mult_samo_TAG.zip)
    * NER and morphosyntactic tags: [under releases](https://github.com/JureBevc/NLP/releases): ner_ontonotes_bert_mult_TAG_UPOS.zip (https://github.com/JureBevc/NLP/releases/download/0.2.0/ner_ontonotes_bert_mult_TAG_UPOS.zip)
5. Put in (profile folder, both in Windows or linux, Mac) "~/.deeppavlov/models/" in directory "ner_ontonotes_bert_mult"
    * inside "~/.deeppavlov/models/ner_ontonotes_bert_mult" there must be the checkpoint, tag.dict etc files.

## To evaluate:
1. select which trained model to evaluate and extract the archive into "~/.deeppavlov/models/ner_ontonotes_bert_mult"
2. move dataset to "~/.deeppavlov/downloads/ontonotes/"
    * NER tags trained only: copy over the files from "repo/src/deep_pavlov/training_dataset_NER_tag/"
    * NER and morphosyntactic tags: copy over the files from "repo/src/deep_pavlov/training_dataset_NER_upos_tag/"
3. run pavlov_test_on_dataset.py


## Scripts:

* preprocess_dataset_for_training.py - Preprocess dataset for training of DeepPavlov model. 
   Dataset must exist under src/common/dataset
* pavlov_train.py - starts training pavlov on datasets in ~/.deeppavlov/downloads/ontonotes
as stated in http://docs.deeppavlov.ai/en/master/features/models/ner.html#train-and-use-the-model
* pavlov_test_on_dataset.py - run test on datasets in ~/.deeppavlov/downloads/ontonotes
* pavlov_test.py - run trained model on handmade test strings

## results folder
Contains results of pavlov_test.py of DeepPavlov model trained on ssj500k stripped of  entries without \<seg\> tokens.

## trainingDataset folder
Dataset used in training the model, parsed by
