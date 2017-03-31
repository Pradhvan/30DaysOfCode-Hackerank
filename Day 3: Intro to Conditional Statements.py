import sys

N = int(raw_input().strip())

E = ['0','2','4','6','8']

O = ['1','3','5','7','9']

if N in range (0,10):

    n = str(N)
    
    A1 = n in E
    
    
    if A1 == False:
		print "Weird"

    if A1 == True :
    	if N in range (2,7):
    		print "Not Weird"
    	elif N in range (7,21):
    		print "Weird"
	else:
		print "Weird"
		
elif N >9:
	num = N%10

	NUM = str(num)

	Ans = NUM in E

	if Ans == True:
		if N in range(2,7):
			print "Not Weird"
		elif N in range (7,21):
			print "Weird"
		elif (N>20) == True:
			print "Not Weird"
	else:
		print "Weird"
     