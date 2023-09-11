import random

nums = set()
while True :
    num = random.randrange(1, 46) # 2번째 매개변수는 끝 수로 미만의 개념이 존재
    nums.add(num)
    if len(nums) == 6:
        break
print(nums)