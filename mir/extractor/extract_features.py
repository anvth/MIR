from yaafelib import *
import sys
import os
sys.path.append(os.path.abspath("/home/anvith/libsvm-3.18/python"))
from svmutil import *
import itertools
from yaafefeatures import *

def extract_feature(name):
	#1 -flute 2-guitar 3- violin 4-piano
	ins='3'
	fp=FeaturePlan(sample_rate=44100, normalize=None, resample=True)

	fp.addFeature('flat:SpectralFlatness FFTLength=0  FFTWindow=Hanning  blockSize=1024  stepSize=512')
	fp.addFeature('flux:SpectralFlux FFTLength=0  FFTWindow=Hanning  FluxSupport=All  blockSize=1024  stepSize=512')
	fp.addFeature('roll:SpectralRolloff FFTLength=0  FFTWindow=Hanning  blockSize=1024  stepSize=512')
	fp.addFeature('sss: SpectralShapeStatistics FFTLength=0  FFTWindow=Hanning  blockSize=1024  stepSize=512')

	df = fp.getDataFlow()
	df.display()
	engine = Engine();
	engine.load(df);
	directory = '/home/anvith/django-workspace/mir/uploads/'
	#out=sys.argv[2]
	ins='1'
	#name = directory+'.csv'
	file_list = os.listdir(directory)
	#f =open(out,'w')
	print directory
	f =open('/home/anvith/django-workspace/mir/mir/extractor/testinput.csv','w+')
	afp = AudioFileProcessor()
	#b=afp.setOutputFormat('csv','output',{'Precision':'8'})
	
	afp.processFile(engine,directory+str(name))
	feats = engine.readAllOutputs()
	zipped = zip(feats['flat'],feats['flux'],feats['roll'],feats['sss'])
	list(zipped)
	#print zipped

	for i in zipped:
		for val,j in enumerate(i):
			for k in j:
				f.write(str(k)+',')

		f.write(ins)
		f.write('\n')
	
	f.close()
	print "hello"
	return zipped

if __name__ == '__main__':
    extract_feature()

