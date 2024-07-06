import numpy as np

x = np.array([[1.83, 1.76, 1.69, 1.86, 1.77, 1.73],
              [86.0, 74.0, 59.0, 95.0, 80.0, 68.0]])

y = x[0:2, 1:3]
z = x[0:2][1:3]

print('x shape :', x.shape)
print('y shape :', y.shape)
print('z shape :', z.shape)
print('z values = :', z)

bmi = x[0] / x[1]**2
print('BMI data')
print(bmi)

#CNN에서 합성곱시킬 칸이 오른쪽으로 이동시킬때랑 관련있는거.
#CNN하면서도 직접 사용할일은 없겠지만, CNN내부에서 작동되는것을 들여다보면 numpy배열을 슬라이싱으로 이용해서 하는게 들어가있다고한다.