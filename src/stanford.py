from xml_parser import XMLParser
import nltk
from nltk.tag.stanford import StanfordNERTagger

class StanfordModel:
	
	def create_training_data(self, file_path=None):
		if file_path is None:
			self.parser = XMLParser()
		else:
			self.parser = XMLParser(file_path)
		data = self.parser.list_all_tags()
		
		f = open("ssj500k.tsv", "w")
		for d in data:
			f.write(d[0] + "\t" + d[1] + "\n")
		f.close()

	def test_model(self):
		sentence = u"V torek okrog pol desetih zjutraj se je na Partizanski ulici v Litiji ponesrečila 81-letna domačinka."

		jar = './stanford/stanford-ner.jar'
		model = './stanford/slovenian-stanford-model.ser.gz'

		ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

		words = nltk.word_tokenize(sentence)
		print(ner_tagger.tag(words))