#prime factors of 13195
#5 7 13 29

divisors = []
long big_number = 600851475143 
for i in range(1, big_number) :
	if(big_number % i == 0 ) :
		divisors.append(i)

print divisors #the list divisors

prime = []		
for j in divisors:
	for k in range (1,j):
		if(j%k == 0):
			prime.append(k)

			
print prime