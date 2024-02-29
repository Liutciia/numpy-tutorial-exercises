import numpy as np

#exercises:2-3
#print(np.__version__)

#exercise:4
#null_vector = np.zeros(10)
#print(null_vector)

#exercise:5
#null_vector = np.zeros(10)
#item_size = null_vector.itemsize
#num_elements = null_vector.size
#memory_size = item_size * num_elements
#print(memory_size)

#exercise:6
#print(np.info(np.add))

#exercise:7
#null_vector = np.zeros(10)
#null_vector[4] = 1
#print(null_vector)

#exercise:8
#arr=np.arange(10,50, dtype=int)
#print(arr)

#exercise:9
#arr=np.arange(0,10, dtype=int)
#reversed_arr=arr[::-1]
#print(reversed_arr)

#exercise:10
#arr = np.arange(9).reshape((3, 3))
#print(arr)

#exercise:11
#arr = np.nonzero([1,2,0,0,4,0])
#print(arr)

#exercise:12
#identity_matrix=np.eye(3)
#print(identity_matrix)

#exercise:13
#arr=np.random.random(3)
#print(arr) 

#exercise:14
#arr = np.array([1, 5, 3, 7, 2, 9, 2, 3, 4, 8])
#max_value = np.max(arr)
#print(max_value)

#exercise:15
#arr = np.array([1, 5, 3, 7, 2, 9, 2, 3, 4, 8])
#mean_value = np.mean(arr)
#print(mean_value)

#exercise:16
#matrix = np.ones((5,5))
#matrix[1:-1,1:-1] = 0
#print(matrix)

#exercise:17
#matrix = np.ones((5,5))
#modified_matrix=np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
#print(modified_matrix)

#exercise:18
#result = 0 * np.nan
#print(result)  #NaN#
#result = np.nan == np.nan
#print(result) #False#
#result = np.inf > np.nan
#print(result) #False#
#result = np.nan - np.nan
#print(result)  #NaN#
#result = np.nan in set([np.nan])
#print(result)  #True#
#result = 0.3 == 3 * 0.1
#print(result)  #False#

#exercise:19
#matrix = np.arange(0,9).reshape((3, 3))
#matrix_diagonal = np.diag(matrix)
#print(matrix_diagonal)

#exercise:20
#matrix = np.ones((8, 8))
#matrix[::2,::2] = 0
#matrix[1::2, 1::2] = 0
#print(matrix)