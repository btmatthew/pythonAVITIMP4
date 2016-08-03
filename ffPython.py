#!/usr/bin/python
import os
import subprocess
import re
import time

def ffcomand():
	content_list= []
	for content in os.listdir("."):
		if "ff" not in content:
			if "dur" not in content:
				process = subprocess.Popen(['ffmpeg',  '-i', content], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				stdout, stderr = process.communicate()
				matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()

				x = int(float(matches['seconds']))/6
				start=0
				end=6
				for i in range(x):
					fileName = content.split(".")[0]
					h = ""
					seq = (fileName,"_",str(i),".","mp4")
					fullFileName = h.join(seq) 
					timeseq=""
					endTimeSeq=""
					if start == 0:
						timeseq=("00:00:0",str(start))
						endTimeSeq=("00:00:0",str(end))
					elif start == 6:
						timeseq=("00:00:0",str(start))
						endTimeSeq=("00:00:",str(end))
					else:
						timeseq=("00:00:",str(start))
						endTimeSeq=("00:00:",str(end))

					startTime = h.join(timeseq)
					endTime = h.join(endTimeSeq)
					commseq =("ffmpeg -i ",content," -vcodec copy -acodec copy -ss  ",startTime," -t ",endTime," /home/matthew/dataSet1/round2/",fullFileName)
					command = h.join(commseq)
					print command
					os.system(command)
					start=start+6
					end=end+6
				
ffcomand()
	
