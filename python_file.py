import time

fp3 = open("py_temp.csv","w")

ptime = []
filelist = ['10MB.txt','20MB.txt','30MB.txt','40MB.txt','50MB.txt']
for i in range(0,5):
	start_time = time.time()
	fp = open("python_copy.txt",'w')
	fp1 = open(filelist[i])
	for line in fp1:
		fp.write(line)
	fp1.close()
	fp.close()
	end_time = time.time()
	ptime.append(round(end_time-start_time,2))
	fp3.write(str(ptime[i])+',')
fp3.write('\n')
fp3.close()

# print(ptime)
