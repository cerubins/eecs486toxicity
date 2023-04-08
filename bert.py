from transformers import BertTokenizer
import glob

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')


for file in glob.glob('comments/*'):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            # preprocessing here
            bert_input = tokenizer(line, padding='max_length', max_length = 10, truncation=True, return_tensors="pt")
