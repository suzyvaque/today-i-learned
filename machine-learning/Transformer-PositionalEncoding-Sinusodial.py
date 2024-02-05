'''
original torch-based code from jadore801120/attention-is-all-you-need-pytorch/transformer/Models.py

1. pytorch converted to tensorflow
2. class PositionalEncoding only, independently applicable before model training

(x = batch size) number of (y = sequence length, z = hidden dim)
equals x number of sentences, where each sentence has y words, and each word is encoded to a z sized vector

Apply positional encoding for each (y, z) shaped input, total x times

Refer to https://www.blossominkyung.com/deeplearning/transfomer-positional-encoding for sinusodial encoding
'''



# Should be ipynb

import tensorflow as tf
import numpy as np



class PositionalEncoding(tf.keras.layers.Layer):
    def __init__(self, d_hid, n_position):
        super(PositionalEncoding, self).__init__()

        # Not a parameter
        self.pos_table = self._get_sinusoid_encoding_table(n_position, d_hid)

    def _get_sinusoid_encoding_table(self, n_position, d_hid):
        ''' Sinusoid position encoding table '''

        def get_position_angle_vec(position):
            return [position / np.power(10000, 2 * (hid_j // 2) / d_hid) for hid_j in range(d_hid)]

        sinusoid_table = np.array([get_position_angle_vec(pos_i) for pos_i in range(n_position)], dtype=np.float32)
        sinusoid_table[:, 0::2] = np.sin(sinusoid_table[:, 0::2])  # dim 2i
        sinusoid_table[:, 1::2] = np.cos(sinusoid_table[:, 1::2])  # dim 2i+1

        return sinusoid_table
        # FIXME The original code adds one dimension when returning... What is the point of it?
        # return tf.expand_dims(sinusoid_table, axis=0)

    def call(self, x):
        return x + self.pos_table[:, :x.shape[1]]



'''
Sample Input Below
'''



batch_size = 30 # number of sentences
n_position = 500  # number of words in sentence - to be accurate, max length of sequence for input
d_hid = 16 # word encoding vector size
pos_enc = PositionalEncoding(d_hid, n_position)

for i in range(batch_size):
  input_tensor = tf.random.normal((n_position, d_hid))  # Example input with n_position words, each represented by a d_hid-sized vector
  output_tensor = pos_enc(input_tensor)

  print('\n\n\n#', i)
  print(input_tensor)
  print(output_tensor)
