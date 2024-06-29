import time

def sample_function():
    total = 0
    for i in range(1000):
        total += i
    return total
# for문은 선형 연산, AI 알고리즘 특히 LLM 같은 경우는 매트릭스 연산을 수행
# LLM에서 하나의 토큰(단어)를 뽑아내기 위해서는 10^9만큼의 연산을 수행(일반적으로 GPT-3에서는 한번의 토큰 생성에 10^12만큼의 연산을 수행)
# 10^12승은 1조

# 함수 사용한 경우 시간 측정
start_time_with_function = time.time()
for _ in range(10000):
    sample_function()
end_time_with_function = time.time()
time_with_function = end_time_with_function - start_time_with_function

# 함수 사용하지 않은 경우 시간 측정
start_time_without_function = time.time()
for _ in range(10000):
    # 함수 내용을 직접 포함
    total = 0
    for i in range(1000):
        total += i
end_time_without_function = time.time()
time_without_function = end_time_without_function - start_time_without_function

# 시간 차이 계산
time_difference = time_with_function - time_without_function

print(f"Time with function: {time_with_function:.4f} seconds")
print(f"Time without function: {time_without_function:.4f} seconds")
print(f"Time difference: {time_difference:.4f} seconds")