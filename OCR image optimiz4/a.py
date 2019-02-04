a=open('calculated.png',mode='r')

for l in a:
	f = open("demofile.txt", mode="a")
	f.write(l) 