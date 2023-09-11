# 딕셔너리는 키와 값이 한쌍으로 이루어진 구조. 자바의 맵과 동일.
# 중괄호로 선언, ","로 구분한다.
# 키와 값은 콜론":"으로 구분한다.

coffee_menu = {"Americano": 2500, "Espresso" : 2000, "Latte" : 4000, "Moca" : 4500} # 키와 밸류 입력
tea_menu = {"Black" : 4000, "Green" : 4000, "Milk" : 3500}
food_menu = {"Cake" : 5000, "Bakery" : 6000, "Ice Cream" : 7000}

print(coffee_menu)
print(tea_menu)
print(food_menu)
print(coffee_menu["Americano"]) # Americano 키값을 넣어 밸류값 결과 출력
print(coffee_menu.get("Latte")) # get 메서드(함수)로 키값을 넣어 결과값을 출력하는 방법


# update 함수. 딕셔너리의 데이터를 한번에 변경
dict = {"전사" : 90, "도적" : 88, "마법사" : 80}
dict.update({"전사" : 100, "도적" : 95, "마법사" : 120})
print(dict)

# 정보 얻기. keys(), values(), items()
dict1 = {"Java": 80, "JavaScript": 88, "HTML": 84}
print(dict1.keys())     # 딕셔너리에 포함된 key만 출력.
print(dict1.values())   # 딕셔너리의 values값만 출력
print(dict1.items())    # 키와 값을 한묶음으로 확인.

# 포함여부 확인. 키의 포함 여부 확인.
print("HTML" in dict1) # 해당 딕셔너리에 키가 포함되어 있는지 확인. True
print("파이썬" in dict1)
print(dict1.get("파이썬")) # None
print(dict1.get("Java"))  # 있으면 해당 키값의 결과값 출력

# 반복문에 키를 사용해 값을 가져오기.
for key in coffee_menu: # 향상된 for문. 딕셔너리의 요소의 키값을 순회하고 결과를 자동으로 출력.
    print(key, ":", coffee_menu[key])

# 


