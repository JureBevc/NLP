## How to set up trained Stanford model

1. The model was trained and tested with Python 3.6.1
2. Install the nltk library with `pip install nltk`
3. Download and set up the Stanford NER model (https://nlp.stanford.edu/software/CRF-NER.html) in the src/stanford folder 
4. Download the trained Stanford models from the latest release
5. Put the models in the stanford folder in src/stanford

## Scripts:

* stanford.py - runs trained model on the test data and evaluate results

## Results folder
Contains results of stanford.py of the Stanford model trained on ssj500k stripped of entries without \<seg\> tokens.

## Training the model
The model can be trained using the following command in the downloaded `stanford` folder:  
`java -cp "*" -Xmx15g edu.stanford.nlp.ie.crf.CRFClassifier -prop prop.txt`  
The file `prop.txt` contains configurations and file paths to training data.

## Model evaluation
To evaluate the trained Stanford model run the following command in the `stanford` folder:  
`python stanford.py`  
This will print precission, recall and F1 scores for all NER tags and both trained models (one with using POS tags and one without).
