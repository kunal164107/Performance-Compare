import os,sys,time

class outofrangeerror(Exception):
	def __init__(self,message):
		self.message = message
		
class notavailablelanguageerror(Exception):
	def __init__(self,message):
		self.message = message;

try:
	print("\nAvailable Languages are: ")
	print("1.) Python\n2.) C++\n3.) C\n4.) Java\n5.) Perl\n")
	print('------------------------------------------------------------------------------------------------------------------------')

	l=[] 
	m=['first','second','third','fourth','fifth']
	
	x=input(">>> How many number of Languages You Want to Compare? ")
	x=x.strip();
	if(x.lower() == 'one' or x.lower()=='two' or x.lower()=='three' or x.lower()=='four' or x.lower()=='five' or int(x)>5 or int(x)<1):
		raise outofrangeerror(">>> #### Error!! Choose only number between 1 to 5 ")
		
	for i in range(1,int(x)+1):
		x = input(">>> Choose "+m[i-1]+" Language: ")
		while(x.lower() in l):
			print('>>> #### Error: Languages already choosen... Choose another language')
			x = input(">>> Choose "+m[i-1]+" Language: ")
		if(x.lower()!='python' and x.lower()!='c++' and x.lower()!='c' and x.lower()!='java' and x.lower()!='perl' ):
			raise notavailablelanguageerror('>>> #### Error: Choose Between the Available Languages only')
		l.append(x.lower())

	print('\n')
	for i in l:
		if(i=='python'):
			print(">>> Hold on Working on "+i+" File...\n")
			os.system('python ptime.py')
			
		elif(i=='c++'):
			print(">>> Hold on Working on "+i+" File...\n")
			os.system('cppfile.exe')
			
		elif(i=='c'):
			print(">>> Hold on Working on "+i+" File...\n")
			os.system('cfile.exe')
			
		elif(i=='java'):
			print(">>> Hold on Working on "+i+" File...\n")
			os.system('java jtime')
			
		elif(i=='perl'):
			print(">>> Hold on Working on "+i+" File...\n")
			os.system('perl perltime.pl')

	print('------------------------------------------------------------------------------------------------------------------------')
	fp1 = open("graph_temp.csv",'w')
	for i in l:
		fp1.write(i+',')
	fp1.close();

		
	print(">>> Opening The Result...")
	cmd = 'octave-cli graph.m'
	os.system(cmd)

	os.system('plot.jpg')
	
except outofrangeerror as e:
	print(e.message)
except notavailablelanguageerror as e:
	print(e.message)	
except Exception:
	print("error!")
