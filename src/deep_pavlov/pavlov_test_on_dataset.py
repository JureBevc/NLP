from deeppavlov import configs, build_model, evaluate_model
from deeppavlov.core.commands.utils import parse_config
 
ner_model = evaluate_model(configs.ner.ner_ontonotes_bert_mult, download=False)
 
