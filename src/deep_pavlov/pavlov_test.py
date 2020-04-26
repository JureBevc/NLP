from deeppavlov import configs, build_model
from deeppavlov.core.commands.utils import parse_config
 
ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=False)
 
print("testiranje slovenščine:")
print(ner_model(['Tim Novak se je odločil, da oropa banko']))
print(ner_model(['Zavod za zaposlovanje Republike Slovenije je izdal odločbo za povečanje socialnega dodatka šibkejšim skupinam.']))
print(ner_model(['The employment bureau of the Republic of Slovenia has issued an order to increase the social supplement to weaker social groups.']))
print(ner_model(['V njegovem času so se v Rim preselili številni gnostiki, ki so razlagali krščanstvo v nasprotju z naukom svetega pisma in cerkvenega učiteljstva.']))
print(ner_model(['Direktor SOVE je dal odpoved.']))
print(ner_model(['The director of SOVA has announced his resignation.']))
print(ner_model(['V okolici Bleda se je število ljudi zmanjšalo.']))
print(ner_model(['Z družino gremo na Triglav']))
print(ner_model(['Tilen gre iz Nišc v Višce čez cestišče']))
print(ner_model(['Zazrl se je v Tino, nato pa se s težkim korakom vrnil v svojo klop.']))
print(ner_model(['Rok, Peter Hodulja in Tim Macesen so se najprej odpeljali do Kranja, nato skozi Posavec do Otoč in se skozi Koritno vrnili na Bled']))
print(ner_model(['Kranjska Gora, Ilirska Bistrica in Polhov gradec.']))
print(ner_model(['Ivan Cankar se je rodil na Klancu v Vrhniki.']))
print(ner_model(['Rok, pridi, gremo k babici Ančki!']))
print(ner_model(['Josip Vajkard Valvasor je spisal Slavo Vojvodine Kranjske']))