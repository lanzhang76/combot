import sys
import gpt_2_simple as gpt2

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

#print(gpt2.generate(sess))
def generateOutput(words,len):
	text = gpt2.generate(sess,
	              length=200,
	              temperature=0.7,
	              prefix=words,
	              nsamples=1,
	              batch_size=1,
	              include_prefix = True,
	              return_as_list = True
	              )
	return text
