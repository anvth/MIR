#!/usr/bin/python
#SVM Predictions from pre-computed model
from svmutil import *
import operator

def predict():
	count = {}
	inst={1:'FLUTE', 2:'GUITAR', 3:'VIOLIN', 4:'PIANO'}
	model = svm_load_model('/home/anvith/django-workspace/mir/mir/extractor/models/fourinstru.model')
	y, x = svm_read_problem('/home/anvith/django-workspace/mir/mir/extractor/testinput.libsvm')
#	print model
	p_labels, p_acc, p_vals = svm_predict(y, x, model)
	print 'Printing Results!!'
	for i in range(1,5,1):
		count[i]=p_labels.count(i)
	predicted_inst =sorted(count.iteritems(), key=operator.itemgetter(1))
	predicted_inst.reverse()
	confidence = predicted_inst[0][1]/len(p_labels)
	return inst[predicted_inst[0][0]]+' with a confidence of ' + str(confidence*100)+'%'
	#print 'Max occ' +str(max(count))
	#print p_acc
	#print p_vals
	


if __name__ == '__main__':
    predict()


