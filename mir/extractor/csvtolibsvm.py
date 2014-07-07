#!/usr/bin/python

#expecting label as the last column
import sys
def csvtolibsvm(instrument_label):
	ifile = '/home/anvith/django-workspace/mir/mir/extractor/testinput.csv'
	out= '/home/anvith/django-workspace/mir/mir/extractor/testinput.libsvm'
	instru = instrument_label
	print "i'm in csvtolibsvm"
	fin = open(ifile,'r')
	fout =open(out,'w+')
	line = fin.readline()
	while(line != ''):
		vals=line.strip().split(',')	
		fout.write(str(vals[-1])+' ')
		#print vals

	#	if(instru == str(vals[-1])):
	#		fout.write('+1'+' ')
	#	else:
	#		fout.write('-1'+' ')
		#for i in range(2,len(vals)-1):
		#	fout.write(str(i+1-2)+':'+str(vals[i])+' ')
		#fout.write('\n')
		#line = fin.readline()

		for i in range(len(vals)-1):
			fout.write(str(i+1)+':'+str(vals[i])+' ')
		fout.write('\n')
		line = fin.readline()
