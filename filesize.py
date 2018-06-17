fp = open("20MB.txt")
fp1 = open("40MB.txt",'a')
for line in fp:
	fp1.write(2*line)
fp.close()
print("Writing Done ")