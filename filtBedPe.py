#!/usr/bin/python
import sys
import argparse

parser = argparse.ArgumentParser(description='Parse bedpe and get it ready to read into diffloop')

parser.add_argument('-input', action="store", dest="input")
parser.add_argument('-prefix', action="store", dest="prefix")
parser.add_argument('-mindist', action="store", dest="mindist")

results = parser.parse_args()
file1 = results.input
prefix = results.prefix
mindist = results.mindist
file2 = prefix + ".intra.loop_counts.bedpe"
file3 = prefix + ".inter.loop_counts.bedpe"

with open(file1, 'r') as in1:
	with open(file2, 'w') as out2:
		with open(file3, 'w') as out3:
			while True:
				dat1=in1.readline()
				if not dat1: break #End of file; should be same number of lines for paired end read
				dat2=in1.readline()
				ss1=dat1.split("\t")
				ss2=dat2.split("\t")
				chr1=ss1[10]
				start1=ss1[11]
				stop1=ss1[12].strip()
				chr2=ss2[10]
				start2=ss2[11]
				stop2=ss2[12].strip()
				mid1 = (int(start1) + int(stop1))/2
				mid2 = (int(start2) + int(stop2))/2
				dist = abs(mid2 - mid1)
				if(chr1 == chr2):
					if(dist > int(mindist)):
						out2.write(chr1+" "+start1+" "+stop1+" "+chr2+" "+start2+" "+stop2+" "+"."+" "+"1"+"\n")
				else:
					out3.write(chr1+" "+start1+" "+stop1+" "+chr2+" "+start2+" "+stop2+" "+"."+" "+"1"+"\n")

			

