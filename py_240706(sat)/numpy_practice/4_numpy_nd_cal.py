import numpy as np

x = np.array([['a', 'b', 'c', 'd'],
              ['c', 'c', 'g', 'g']])

mat_a = np.array([[10, 20, 30], [10, 20, 30]])
mat_b = np.array([[2, 2, 2], [1, 2, 3]])

print(x[x == 'c'])  #조건에부합하는거 가져오는거임. #[]에서 끝나게되면 있는지 없는지정도만 아는거. 값을 직접 가져오려면 앞에 x붙어야함.(아마 객체를 의미하는거겠지.)
print(mat_a - mat_b)    #얘는 다차원배열에 대해 계산할수있다는걸 보여주는거.

