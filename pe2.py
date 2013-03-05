i = 0 
j = 1
even_sum = 0
sum = 0

while ( i < 4000000 ) : # itterate till 4 million

	sum = i + j #1

	if (sum%2 == 0) :
		even_sum = even_sum + sum
		print even_sum #print the sum
		
	i = j #1
	j = sum #1
