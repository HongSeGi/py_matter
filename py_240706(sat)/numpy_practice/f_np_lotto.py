# link : https://dhlottery.co.kr/gameResult.do?method=statByNumber
# selenium > 자동화 모듈 중 하나로, 웹에서 정보를 가져오는 역할을 수행한다.
# pip install selenium webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import numpy as np
import time as t

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://dhlottery.co.kr/gameResult.do?method=statByNumber")
driver.implicitly_wait(10) #브라우저를 불러오기 위해 잠시 대기 #>없어도 동작하는데 문제없다.

lotto_lst = []
for i in range(1, 46):
    #웹 사이트의 정보를 이용해 데이터를 가져옴.
    xpath = f'//*[@id="printTarget"]/tbody/tr[{i}]/td[3]'   #//*[@id="printTarget"]/tbody/tr[1]/td[3] 데이터형태.
    row_element = driver.find_element(By.XPATH, xpath)

    # 각 행의 정보를 가져오기
    lotto_lst.append(int(row_element.text))
# print(lotto_lst)
#a = input() #브라우저 종료 방지 #데이터 잘 받아와지는거 확인했으니, 웹브라우저종료방지는 이제 지워도 상관없다.

lst_to_array = np.array(lotto_lst)
total = np.sum(lst_to_array)
p = lst_to_array/total

# print(f"합: {total}")
# print(f"각 위치별 확률: {p}")

np.random.seed(int(t.time())) # 토요일 8시로 고정시킬수있다.(datetime으로)
a = np.arange(1, 46)
for i in range(5):
    b = np.random.choice(a, 6, replace=False, p=p)
    b = np.sort(b)
    print(b)



