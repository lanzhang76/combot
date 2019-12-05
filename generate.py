import sys
import gpt_2_simple as gpt2
from keras import backend as K
from flask import jsonify
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def generateOutput(words, len):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    text = gpt2.generate(sess,
                         length=len,
                         temperature=0.7,
                         prefix=words,
                         nsamples=1,
                         batch_size=1,
                         include_prefix=True,
                         return_as_list=True
                         )
    K.clear_session()
    return text

# K.clear_session()
