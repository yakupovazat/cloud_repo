import numpy as np

my_list = [1,2,3]
#print(type(my_list))

a=np.array(my_list)
#print(type(a))

my_list = [[1,2,3], 
           [4,5,6], 
           [7,8,9]]

#print(type(my_list))
#print(my_list[1][1])

a=np.array(my_list)
#print(a)
#print(type(a))
#print(a[1][1])

#print(a.shape)

a=np.arange(0,10)
#print(a)

a=np.arange(0,10,2)
#print(a)

a=np.zeros(3)
#print(a)

a=np.zeros((2,4))
#print(a)

a=np.zeros((2,4,3))
#print(a)

#a=np.ones(3)
a=np.ones((2,4))
#print(a)

a=np.linspace(0,5,40)
#print(a)

a=np.eye(5)
#print(a)

#a=np.random.rand()
#a=np.random.rand(3)
#a=np.random.rand(3,2)

#a=np.random.randn(250)
#print(a)

#a=np.random.randint(1,100,8)
#print(a)

#np.random.seed(100)
#a=np.random.randint(1,100,8)
#print(a)

b=np.random.randint(1,100,8)
#print(b)
#print(b.shape)

#c=b.reshape(4,2)
#c=b.reshape(2,4)
#c=b.reshape(2,2,2)
#c=b.reshape(4,2,1)
#c=b.reshape(3,2)
#c=b.reshape(2,-1)
##ошибка ниже
#c=b.reshape(3,-1)
#print(c)
#print(c.shape)

#np.random.seed(100)
b=np.random.randint(1,100,8)
#print(b.shape) #(8,1)
#print(b)

#c=b.reshape(1,8)
#print(c)
#print(c.shape == b.shape)
#print(b)
#print(b.max())
#print(b.argmax())

#print(b.min())
#print(b.argmin())

#print(b.dtype)
#c=np.eye(5)
#print(c.dtype)

###работа с выборками из массивов
arr=np.arange(0,11)
#print(arr)
#print(arr[8])

#print(arr[1:5])
#print(arr[6:])

#s=arr*3
#print(s)

#s=arr/10
#print(s)

#print(arr)

y=arr[0:6]
#print(y)
y[:]=100
#print(y)

#матрицы
arr=np.arange(0,9)
arr=arr.reshape(3,3)
#print(arr)
#print('-----')
#print(arr[1][1])
#print(arr[1:][1:])
#print(arr[:,1])

##условные выборки
arr=np.arange(0,9)
arr=arr.reshape(-1)
#print(arr)
#print(arr > 4)

x=arr[arr>4]
#print(x)

#print((arr<2) | (arr>4))
y=arr[(arr<2) | (arr>4)]
#print(arr)
#print(y)

q=arr[:4]
#print(x+q)
#print(x*q)
#print(x/q)
#print(q/q)
#print(q**3)
#print(np.sqrt(q))

##статистика
arr=np.arange(0,11)
#print(arr.mean())
#print(arr.std())
#print(arr.var())

arr2=np.arange(0,11)
arr2=arr2.reshape(11,-1)

#print(arr+arr2)
mat=arr+arr2
#print(mat.shape)
#print(mat.sum())
mat[4]=0.0
print(mat)
print('------')
print(mat.sum(axis=0))
print(mat.sum(axis=1))
print(mat.mean(axis=1))
