### Method1. Attention is all you need


* sinusodial

* original code : https://github.com/jadore801120/attention-is-all-you-need-pytorch/blob/master/transformer/Models.py

* modifications :
  1. torch based converted to tf based
  2. returns 2D without expanding dimension
  3. applied independently, using other Encoder/Decoder models

 
-----

https://heekangpark.github.io/ml-shorts/positional-encoding-vs-positional-embedding
Method 2 and 3 should be integrated as a layer of a trainable model.
Should modify code!

-----

### Method2. Keras NLP


* learnable weight

* original code : https://github.com/keras-team/keras-nlp/blob/v0.7.0/keras_nlp/layers/modeling/position_embedding.py#L20


-----


### Method3. Tensorflow


* sinusodial

* original code : https://github.com/tensorflow/models/blob/master/official/nlp/modeling/layers/position_embedding.py
