def isprime(num):
	num = abs(int(num))
	if num < 2:
		return False
	if num == 2: 
		return True
	if not num & 1:
		return False
	for x in range(3, int(num**0.5)+1, 2):
		if num % x == 0:
			return False
	return True

testprime = input("How high do you want to check for primes? ")
n = int(testprime)
	
with open('Results.txt','w') as a:
	a.write("Every prime less than " + str(n) + ':' + '\n' + '\n')
	for m in range(1,n):
		if isprime(m):
			a.write("True " + str(m) + '\n')
		if not isprime(m):
			pass

print("Done")