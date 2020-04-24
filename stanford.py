from xml_parser import XMLParser

class StanfordModel:
	
	def create_training_data(self, file_path=None):
		if file_path is None:
			self.parser = XMLParser()
		else:
			self.parser = XMLParser(file_path)
		data = self.parser.all_words_and_tags()
		
		f = open("ssj500k.tsv", "w")
		for d in data:
			f.write(d[0] + "\t" + d[1] + "\n")
		f.close()
	