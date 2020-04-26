## How to set up trained DeepPavlov model

1. Set up Python 3.6.8 virtualenv and activate the virtualenv
2. Install packages from _requirenments.txt_
3. After installed, install ner_ontonotes_bert to deeppavlov

    python -m deeppavlov install ner_ontonotes_bert
4. Download trained DeepPavlov model from --url--
5. Put in ~/.deeppavlov/models/ in directory "ner_ontonotes_bert_mult"


##Scripts:

* preprocess_dataset_for_training.py - Preprocess dataset for training of DeepPavlov model. 
   Dataset must exist under src/common/dataset
* pavlov_train.py - starts training pavlov on datasets in ~/.deeppavlov/downloads/ontonotes
as stated in http://docs.deeppavlov.ai/en/master/features/models/ner.html#train-and-use-the-model
* pavlov_test.py - run trained model on handmade test strings

## results folder
Contains results of pavlov_test.py of DeepPavlov model trained on ssj500k stripped of  entries without \<seg\> tokens.

## trainingDataset folder
Dataset used in training the model, parsed by