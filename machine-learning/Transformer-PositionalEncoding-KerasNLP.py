# Keras NLP
# How to apply

import numpy as np
import tensorflow as tf
from keras_nlp.layers import PositionEmbedding



# Given input data "input"...
# input.shape = (#sentences, #words in sentence, #dim of vector for word)



max_sequence_length = input.shape[1]  # maximum sequence length
embedding_dimension = input.shape[-1]  # embedding dimension

position_embedding_layer = PositionEmbedding(
    sequence_length=max_sequence_length,
    input_shape=(max_sequence_length, embedding_dimension),
)

# Apply positional encoding
pos_encoded_data = position_embedding_layer(input)
# FIXME don't quite get how this is applied to all sentences - check source code
