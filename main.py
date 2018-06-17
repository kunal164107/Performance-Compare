import os
import sys
import time
# import matplotlib.pyplot as plt


fp2 = open("result.csv",'w')
fp2.write("  File Size  "+ ","+"                                    Time Taken(sec)                                    "+'\n')
fp2.write(','+"Python"+','+'C++'+','+'C'+','+'Java'+','+'Perl'+'\n')


print("Calling Python File ")
cmd = 'python ptime.py'
os.system(cmd)

print("Calling Cpp File ")
cmd = 'cppfile.exe'
os.system(cmd)

print("Calling C File ")
cmd = 'cfile.exe'
os.system(cmd)

print("Calling Java File ")
cmd = 'java jtime'
os.system(cmd)

print("Calling Perl File ")
cmd = 'perl perltime.pl'
os.system(cmd)

l=[]
i=0
fp1 = open("ptemp.csv")
for line in fp1:
	l.append(line.split(","))
	del l[i][5]
	i+=1
# print(l)
# print (l[0][0])
fp1.close()

filelist = ['10MB.txt','20MB.txt','30MB.txt','40MB.txt','50MB.txt']
for i in range(0,5):
	fp2.write(filelist[i]+',')
	for j in range(0,5):
		fp2.write(l[j][i]+',')
	fp2.write('\n')
fp2.close()

# fp3 = open("octave.csv",'a')
# for i in range(0,5):
	# for j in range(0,5):
		# fp3.write(l[j][i]+',')
	# fp3.write('\n')
# fp3.close()



# plt.plot(filelist,l[0])
# plt.plot(filelist,l[1])
# plt.plot(filelist,l[2])
# plt.plot(filelist,l[3])
# plt.plot(filelist,l[4])

# plt.show()

print("Plotting The Graph...")

cmd = 'octave-cli graph.m'
os.system(cmd)