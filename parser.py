from xml.dom import minidom

class Parser:

	def __init__(self, file_path='ssj500k-sl.TEI/ssj500k-sl.body.xml'):
		print("Prasing " + file_path + "...")
		self.doc = minidom.parse(file_path)
		print("Done")
	
	def words_in_element(self, s):
		elements = s.getElementsByTagName("w")
		return [w.firstChild.nodeValue for w in elements]

	def all_named_entities(self):
		entities = self.doc.getElementsByTagName("seg")
		entity_names = [e.getAttribute("subtype") for e in entities]
		words_in_entity = [self.words_in_element(e) for e in entities]
		return words_in_entity, entity_names
