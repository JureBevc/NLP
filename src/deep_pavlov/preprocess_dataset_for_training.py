import codecs
import math
import os
import random
from common import XMLParser

"""
Workdir must be "src" folder
"""
print("Workdir: " + os.getcwd() + ", file:" + __file__)
parser = XMLParser("./common/dataset/ssj500k-sl_merged_samoSeg.xml")
parsed = parser.list_all_tags_for_deepPavlov()
sentences = {
    "training": [],
    "validation": [],
    "test": []
}
sUnseg = [[]]
cursentence = []
i = 0
for line in parsed:
    if line[0] == "0" and line[1] == "0":
        sUnseg[i].append("\n")
        sUnseg.append([])
        i += 1
        continue
    sUnseg[i].append(line[0] + " " + line[1] + "\n")

nSentences = len(sUnseg)
nValidation = math.ceil(nSentences * 0.1)
nTesting = nValidation
nTrening = nSentences - nValidation - nTesting

random.shuffle(sUnseg)
for sentence in sUnseg:
    nTreningRi = len(sentences["training"])
    nValidationRi = len(sentences["validation"])
    nTestingRi = len(sentences["test"])
    if (nTreningRi < nTrening):
        sentences["training"].append(sentence)
    elif (nValidationRi < nValidation):
        sentences["validation"].append(sentence)
    else:
        sentences["test"].append(sentence)
del nTreningRi
del nValidationRi
del nTestingRi

nSentencesR = len(sentences["training"]) + len(sentences["validation"]) + len(sentences["test"])
nTreningR = len(sentences["training"])
nValidationR = len(sentences["validation"])
nTestingR = len(sentences["test"])

print("Sizes ([calculated, real]): ")
print([nTrening, nTreningR])
print([nValidation, nValidationR])
print([nTesting, nTestingR])

deepPavlovfolder = str(__file__[:-len("preprocess_dataset_for_training.py")])
print("Split dataset will be saved to: " + deepPavlovfolder)

ftr = codecs.open(deepPavlovfolder + "all_words_with_subtypes_training.txt", "w", "utf-8")
fval = codecs.open(deepPavlovfolder + "all_words_with_subtypes_validation.txt", "w", "utf-8")
ftest = codecs.open(deepPavlovfolder + "all_words_with_subtypes_test.txt", "w", "utf-8")
for sentence in sentences["training"]:
    for word in sentence:
        ftr.write(word)
for sentence in sentences["validation"]:
    for word in sentence:
        fval.write(word)
for sentence in sentences["test"]:
    for word in sentence:
        ftest.write(word)
