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
	
	def evaluate_model(self):
		tf = open("./results/test.txt", "r")
		rf = open("./results/test_result.txt", "r")
		
		true_tags = [([],[])]
		for line in tf:
			if line == "\n":
				true_tags.append(([],[]))
				continue
			spl = line.split(" ")
			token = spl[0]
			tag = 'O'
			if "LOC" in spl[1]:
				tag = "loc"
			if "ORG" in spl[1]:
				tag = "org"
			if "PER" in spl[1]:
				tag = "per"
			if "MISC" in spl[1]:
				tag = "misc"
			true_tags[-1][0].append(token)
			true_tags[-1][1].append(tag)
		tf.close()
		
		result_tags = [([],[])]
		for line in rf:
			if line == "\n":
				result_tags.append(([],[]))
				continue
			spl = line.split("\t")
			token = spl[0]
			tag = spl[1].strip()
			result_tags[-1][0].append(token)
			result_tags[-1][1].append(tag)
		rf.close()
		
		tags = ["loc", "misc", "org", "per"]
		for t in tags:
			TP = 0
			S = 0
			P = 0
			for i in range(len(result_tags)):
				rt = result_tags[i][1]
				tt = true_tags[i][1]
				for j in range(len(rt)):
					if rt[j] == t and tt[j] == t:
						TP += 1
					if rt[j] == t:
						S += 1
					#print(tt[j])
					if tt[j] == t:
						P += 1

			precision = TP/S
			recall = TP/P
			f1 = 2 * (precision * recall) / (precision + recall)
			print(f"\n{t}:")
			print(f"--Precision: {precision}")
			print(f"--Recall: {recall}")
			print(f"--F1: {f1}")
		
	
	def test_model(self):
		jar = './stanford/stanford-ner.jar'
		model = './stanford/train-test.ser.gz'
		ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

		sentences = [([],[])]
		tf = open("./results/test.txt", "r")
		count = 0
		for line in tf:
			if line == "\n":
				#print(sentences[-1][0])
				sentences.append(([],[]))
				continue
			spl = line.split(" ")
			token = spl[0]
			tag = 'O'
			if "LOC" in spl[1]:
				tag = "loc"
			if "ORG" in spl[1]:
				tag = "org"
			if "PER" in spl[1]:
				tag = "per"
			if "MISC" in spl[1]:
				tag = "misc"
			sentences[-1][0].append(token)
			sentences[-1][1].append(tag)
		tf.close()
		f = open("./results/test_result.txt", "w")
		for s in sentences:
			count += 1
			print(f"Running model {count} / {len(sentences)}")
			#print(s[0])
			result = ner_tagger.tag(s[0])
			for r in result:
				f.write(r[0] + "\t" + r[1] + "\n")
			f.write("\n")
		f.close()

if __name__ == "__main__":
    s = StanfordModel()
    print("Testing model")
    s.test_model()
    print("Running evaluation")
    s.evaluate_model()