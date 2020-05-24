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

        f = open("ssj500k.tsv", "w", encoding="utf-8")
        for d in data:
            print(d)
            f.write(d[0] + "\t" + d[1] + "\t" + d[2] + "\n")
        f.close()

    def evaluate_model(self, using_pos=False):
        tf = open("./results/test.txt", "r", encoding="utf-8") if not using_pos else open("./results/test_pos.txt", "r",
                                                                                          encoding="utf-8")
        rf = open("./results/test_result.txt", "r", encoding="utf-8") if not using_pos else open(
            "./results/test_result_pos.txt", "r", encoding="utf-8")

        true_tags = [([], [])]
        for line in tf:
            if line == "\n":
                true_tags.append(([], []))
                continue
            spl = line.split(" ")
            token = spl[0]
            tag = 'O'
            if "LOC" in spl[-1]:
                tag = "loc"
            if "ORG" in spl[-1]:
                tag = "org"
            if "PER" in spl[-1]:
                tag = "per"
            if "MISC" in spl[-1]:
                tag = "misc"
            true_tags[-1][0].append(token)
            true_tags[-1][1].append(tag)
        tf.close()

        result_tags = [([], [])]
        for line in rf:
            if line == "\n":
                result_tags.append(([], []))
                continue
            spl = line.split("\t")
            token = spl[0]
            tag = spl[1].strip()
            if "LOC" in tag:
                tag = "loc"
            if "ORG" in tag:
                tag = "org"
            if "PER" in tag:
                tag = "per"
            if "MISC" in tag:
                tag = "misc"
            result_tags[-1][0].append(token)
            result_tags[-1][1].append(tag)
        rf.close()

        total_TP = 0
        total_S = 0
        total_P = 0
        tags = ["loc", "misc", "org", "per"]
        for t in tags:
            TP = 0
            S = 0
            P = 0
            for i in range(len(true_tags)):
                rt = result_tags[i][1]
                tt = true_tags[i][1]
                for j in range(len(rt)):
                    if rt[j] == t and tt[j] == t:
                        TP += 1
                        total_TP += 1
                    if rt[j] == t:
                        S += 1
                        total_S += 1
                    # print(tt[j])
                    if tt[j] == t:
                        P += 1
                        total_P += 1

            precision = TP / S
            recall = TP / P
            f1 = 2 * (precision * recall) / (precision + recall)
            print(f"\n{t}:")
            print(f"--Precision: {precision}")
            print(f"--Recall: {recall}")
            print(f"--F1: {f1}")
        precision = total_TP / total_S
        recall = total_TP / total_P
        f1 = 2 * (precision * recall) / (precision + recall)
        print(f"\nTotal:")
        print(f"--Precision: {precision}")
        print(f"--Recall: {recall}")
        print(f"--F1: {f1}")

    def test_model(self):
        jar = './stanford/stanford-ner.jar'
        model = './stanford/train-test.ser.gz'
        ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

        sentences = [([], [], [])]
        tf = open("./results/test.txt", "r", encoding="utf-8")
        count = 0
        for line in tf:
            if line == "\n":
                # print(sentences[-1][0])
                sentences.append(([], [], []))
                continue
            spl = line.split(" ")
            token = spl[0]
            pos = spl[1]
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
            sentences[-1][1].append(pos)
            sentences[-1][2].append(tag)
        tf.close()
        f = open("./results/test_result.txt", "w", encoding="utf-8")
        for s in sentences:
            count += 1
            print(f"Running model {count} / {len(sentences)}")
            # print(s[0])
            result = ner_tagger.tag(s[0])
            for r in result:
                f.write(r[0] + "\t" + r[1] + "\n")
            f.write("\n")
        f.close()


if __name__ == "__main__":
    s = StanfordModel()
    # s.create_training_data()
    print("Testing model")
    # s.test_model()
    print("\nRunning evaluation (without POS tags)")
    s.evaluate_model()
    print("\nRunning evaluation (using POS tags)")
    s.evaluate_model(using_pos=True)
