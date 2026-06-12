import numpy as np

arr1 =np.array([1,2,3,4,5])
arr2 = np.array([[85,67,88],[23,45,6],[12,15,19]])

print(arr2.shape)
print(arr2.dtype)
print(arr2.ndim)

#methods in Numpy

#zeroes 
Zeros = np.zeros((3,4))  #give all 0 in 3 *4 array
print(Zeros)

#Ones 
Ones= np.ones((2,5)) #give all 1 in 2 * 5 array
print(Ones)

#range 
rng = np.arange(0,50,5)  #give array of range from 0 to 45 with step of 5
print(rng)

#linespace
lin = np.linspace(0,1,11)  # give 11 sequence from 0 to 1 (0.0,0.1,----1.0)
print(lin)

#random
random = np.random.randint(40,100,(5,3)) #random no. from 40 to 100 in form of 5 *3 array
print(random)

#vectorized math
arr = np.array([10,20,30,40,50])
print(arr *2)
print(arr+5)
print(arr**2)

mark2 = np.array([[85,90,78],[72,88,95],[91,76,83]])

print(np.mean(mark2))

print(np.mean(mark2,axis =1))  #mean per student (row)

print(np.mean(mark2,axis=0))  #mean per subject (column)

print(np.max(mark2))

print(np.std(mark2)) #standard deviation

#boolean indexing (data filteering)
arr = np.array([55,82,43,91,67,78,35,88])
print(arr[arr>70])  #only value greater than 70 