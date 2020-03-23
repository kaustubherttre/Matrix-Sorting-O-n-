import numpy as np
def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap  
        heapify(arr, n, largest) 
def heapSort(arr): 
    n = len(arr) 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 
def printmatrix(array):
    data= np.array(array)
    data.reshape(3,3)
    print(data)
    
if __name__=='__main__':
    r=len(mat)
    c=len(mat[0])
    mat=[[5,4,3],[2,9,7],[1,6,8]]
    matrix= np.matrix(mat).flatten()
    mat1=str(matrix)
    badchar= ['[',']']


    for i in badchar:
        mat1=mat1.replace(i,'')
    y=mat1.strip().replace(' ','')

    array= list(y)
    for i in range(len(array)):
        array[i]=int(array[i])
    heapSort(array)
    print(np.array(array).reshape(r,c))