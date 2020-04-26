from xml.dom import minidom


class XMLParser:

    def __init__(self, file_path='../ssj500k-sl.TEI/ssj500k-sl.body.xml'):
        print("Parsing " + file_path + "...")
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

    def list_all_tags(self):
        sen = self.doc.getElementsByTagName("s")
        tags = []
        for s in sen:
            for c in s.childNodes:
                if c.nodeType != c.TEXT_NODE:
                    if c.tagName == "pc" or c.tagName == "w":
                        word_tag = "O"
                        word = c.firstChild.nodeValue;
                        tags.append((word, word_tag))
                    elif c.tagName == "seg":
                        word_tag = c.getAttribute("subtype")
                        for word in self.words_in_element(c):
                            tags.append((word, word_tag))
        return tags

    def list_all_tags_for_deepPavlov(self):
        """
        same as "list_all_tags", but different format: UPPERCASE an B- or I- prepended.

        :return: Array of two element array [word, tag]
        """

        all_words_with_subtypes = []
        for sentence in self.doc.getElementsByTagName("s"):
            # flatnames = {
            #
            # }
            # for link in sentence.getElementsByTagName("link"):
            #    if(link.getAttribute("ana") == "ud-syn:flat_name"):
            #        n = 0
            #        for target in link.getAttribute("target").split(" "):
            #            pot=target.split(".")
            #            idx =int(pot[len(pot)-1].split("t")[1])-1
            #            selected =  all_words_with_subtypes[idx]
            #            if(n == 0):
            #                selected=[selected[0], "B-"+selected[1]]
            #            else:
            #                selected=[selected[0], "I-"+selected[1]]
            #            n+=1
            #    #ud-syn:flat_name
            for node in sentence.childNodes:
                subtype = "O"
                if node.nodeName == "w":
                    msd = node.getAttribute("msd")
                    if "UposTag=PROPN|Case=Loc|" in msd:
                        subtype = "LOC"
                    elif "UposTag=PROPN|Case=Nom|" in msd:
                        if node.getAttribute("lemma").isupper():
                            subtype = "ORG"
                        else:
                            subtype = "PER"
                    all_words_with_subtypes.append([node.firstChild.nodeValue, subtype.upper()])
                elif node.nodeName == "seg":
                    subtype = node.getAttribute("subtype")
                    if subtype == "per":
                        subtype = "PERSON"
                    wordinSeg = 0
                    for w in node.getElementsByTagName("w"):
                        prepend = "B-"
                        if wordinSeg > 0:
                            prepend = "I-"
                        wordinSeg += 1
                        all_words_with_subtypes.append([w.firstChild.nodeValue, prepend + subtype.upper()])
                elif node.nodeName == "pc":
                    all_words_with_subtypes.append([node.firstChild.nodeValue, subtype.upper()])
                elif node.nodeName == "linkGrp":

                    all_words_with_subtypes.append(["0", "0"])
                    break
        return all_words_with_subtypes
