
def basicstats():
	import matplotlib.pyplot as p
	x = [8,5,6,8,10,11,14,12,11,20,17,2,6,15,15,12,4,3,18,4,6,4,14,8,10];
	y = 0;
	for N in x:
   		y = y+1
	print("List x is %d" % y + " elements long")
	
	y = 0;
	for N in x:
    		y = y+1
	print("The length of list x is %d" % y)
	z = 0
	for N in x:
    		z = z + N
	print("The sum of list x is %d" %z)
	mean = z/y
	print("The mean is %f" % mean)


	y = 0
	for N in x:
    		y = y+1
	print("The length of list x is %d" % y)

	z = 0
	for N in x:
    		z = z + N
	print("The sum of list x is %d" %z)

	mean = z/y
	print("The mean is %f" % mean)

	s =[]
	for N in x:
    		s.append(N - mean)
	#print(s)

	ssqd = []
	for N in s:
    		ssqd.append(N*N)
	#print(ssqd)

	t = 0
	for N in ssqd:
    		t = t + N
	print("The sum of list ssqd is %d" %t)

	a = t/y
	print(a)

	std = a ** 0.5
	print("The standard deviation is %f" % std)
	print("The average is %f" % mean)

	b = mean + std
	print(b)
	b = int(b)
	print(b)
	c = mean - std
	print(c)
	c = int(c)
	print(c)

	counter = 0
	for N in x:
    		if N in range(c, b):
        		counter = counter + 1
        		print("The number %f" % N + " is between %f" % c + " and %f" %b)
	print("The total number of values within the std is %f" % counter)

	distribution = counter/y
	print(distribution)

	if distribution >= 0.68:
    		print("The list has a normal distribution.")
	elif distribution < 0.68:
    		print("The list does not have a normal distribution.")


	plt.hist(x)
	plt.title("Histogram of List X")
	plt.xlabel("List Values")
	plt.ylabel("Frequency")

	y = 0
	for N in x:
    		y = y+1
	print("The length of list x is %d" % y)

	z = 0
	for N in x:
    		z = z + N
	print("The sum of list x is %d" %z)

	mean = z/y
	print("The mean is %f" % mean)

	s =[]
	for N in x:
    		s.append(N - mean)
	#print(s)

	d = []
	for N in s:
    		d.append(N/std)
	#print(d)

	e = []
	for N in d:
    		e.append(N**3)
	#print(e)

	f = 0
	for N in e:
    		f = f + N
	print("The sum of list e is %d" %f)

	g = f/y
	print("The skewness of list x is %f" % g)

	if f == 0:
    		print("The list has a normal distribution and no skewness.")
	elif f < 0:
    		print("The list does not have a normal distribution and is skewed to the left.")
	elif f > 0:
     		print("The list does not have a normal distribution and is skewed to the right.")

return x, s