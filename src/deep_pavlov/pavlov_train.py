from deeppavlov import configs, build_model, train_model
from deeppavlov.core.commands.utils import parse_config

config_dict = parse_config(configs.ner.ner_ontonotes_bert_mult)
reader = config_dict['dataset_reader']
print(config_dict['dataset_reader']['data_path'])
ner_model = train_model(configs.ner.ner_ontonotes_bert_mult, download=False)
