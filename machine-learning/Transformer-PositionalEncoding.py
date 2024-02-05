'''
# original torch-based code from jadore801120/attention-is-all-you-need-pytorch/transformer/Models.py
# pytorch converted to tensorflow
# class PositionalEncoding only, independently applicable before model training

# (x = batch size) number of (y = sequence length, z = hidden dim)
# equals x number of sentences, where each sentence has y words, and each word is encoded to a z sized vector
# apply positional encoding for each (y, z) shaped input, total x times
'''

