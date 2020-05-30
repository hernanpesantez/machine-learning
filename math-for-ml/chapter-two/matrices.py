# here we will do some baisc matrices operation to
# make sure all concepts of linear algebra are well understood
# do not forget to init your virtual environment in my case is pipenv shell
import numpy as np

b = np.array([[0, 2], [1, -1], [0, 1]])
a = np.array([[1, 2, 3], [3, 2, 1]])


print('dot product: '+a.dot(b))

c = np.einsum('il, lj', a, b)

print(c)
