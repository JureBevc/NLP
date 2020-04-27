import sys
sys.path.append("..")
from common import XMLParser
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
		jar = './stanford/stanford-ner.jar'
		model = './stanford/slovenian-stanford-model.ser.gz'
		ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

		print(ner_tagger.tag(nltk.word_tokenize('Tim Novak se je odločil, da oropa banko')))
		print(ner_tagger.tag(nltk.word_tokenize('Zavod za zaposlovanje Republike Slovenije je izdal odločbo za povečanje socialnega dodatka šibkejšim skupinam.')))
		print(ner_tagger.tag(nltk.word_tokenize('The employment bureau of the Republic of Slovenia has issued an order to increase the social supplement to weaker social groups.')))
		print(ner_tagger.tag(nltk.word_tokenize('V njegovem času so se v Rim preselili številni gnostiki, ki so razlagali krščanstvo v nasprotju z naukom svetega pisma in cerkvenega učiteljstva.')))
		print(ner_tagger.tag(nltk.word_tokenize('Direktor SOVE je dal odpoved.')))
		print(ner_tagger.tag(nltk.word_tokenize('The director of SOVA has announced his resignation.')))
		print(ner_tagger.tag(nltk.word_tokenize('V okolici Bleda se je število ljudi zmanjšalo.')))
		print(ner_tagger.tag(nltk.word_tokenize('Z družino gremo na Triglav')))
		print(ner_tagger.tag(nltk.word_tokenize('Tilen gre iz Nišc v Višce čez cestišče')))
		print(ner_tagger.tag(nltk.word_tokenize('Zazrl se je v Tino, nato pa se s težkim korakom vrnil v svojo klop.')))
		print(ner_tagger.tag(nltk.word_tokenize('Rok, Peter Hodulja in Tim Macesen so se najprej odpeljali do Kranja, nato skozi Posavec do Otoč in se skozi Koritno vrnili na Bled')))
		print(ner_tagger.tag(nltk.word_tokenize('Kranjska Gora, Ilirska Bistrica in Polhov gradec.')))
		print(ner_tagger.tag(nltk.word_tokenize('Ivan Cankar se je rodil na Klancu v Vrhniki.')))
		print(ner_tagger.tag(nltk.word_tokenize('Rok, pridi, gremo k babici Ančki!')))
		print(ner_tagger.tag(nltk.word_tokenize('Josip Vajkard Valvasor je spisal Slavo Vojvodine Kranjske')))
