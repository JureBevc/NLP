## How to set up trained Stanford model

1. The model was trained and tested with Python 3.6.1
2. Install the nltk library with `pip install nltk`
3. Download the trained Stanford model: https://drive.google.com/open?id=1nRd3GJQJvOE1IaLspfebmQVZwrMmJ65c
4. Unzip and put the stanford folder in src/stanford

## Scripts:

* stanford.py - runs trained model on the test data and evaluate results

## Results folder
Contains results of stanford.py of the Stanford model trained on ssj500k stripped of entries without \<seg\> tokens.

## Training the model
The model can be trained using the following command in the downloaded `stanford` folder:
`java -cp "*" -Xmx15g edu.stanford.nlp.ie.crf.CRFClassifier -prop prop.txt`
The file `prop.txt` contains configurations and file paths to training data.