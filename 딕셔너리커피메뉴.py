menu_dic = { # 키와 값으로 구성되며, 값을 리스트로 만들어 여러가지 정보를 포함시킴.
    # 메뉴이름 : [카테고리(분류), 가격, 설명]
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Espresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}

while True :
    print("메뉴를 선택하세요 : ")
    menu = input("[1]메뉴 보기 [2]메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]종료 : ") # 문자열을 기본으로 입력받음
    if menu == "1":
        for key in menu_dic: # key값만 출력
            print(key, ":", menu_dic[key])
    elif menu == "2":
        name_menu == input("조회 할 메뉴 선택 : ")
        if name_menu in menu_dic:
            print(menu_dic[name_menu])
        else :
            print("찾는 메뉴가 없습니다.")

    elif menu == "3":
        add_munu = input("추가할 메뉴 :")
        if add_munu not in menu_dic:
            category = input("카테고리 :")
            price = int(input("갸격 :"))
            description = input("제품설명 :")
            menu_dic[add_munu] = [category, price, description] #추가 : 딕셔너리[키] = 값 새로운 키와 값을 추가 할 수 있습니다.
            for key in menu_dic:
                print(key, ":", menu_dic[key])  # 메뉴가 추가되어 리스트(딕셔너리)가 변경되었음을 보여줌
        else:
            print("메뉴가 존재합니다.")

    elif  menu == "4":
        del_menu = input("삭제할 메뉴를 입력하세요 :")
        if del_menu in menu_dic:
            del menu_dic[del_menu] # 삭제: del 딕셔너리[키] 형식으로 써 주면 됩니다.
            for key in menu_dic:
                print(key, ":", menu_dic[key]) # 메뉴가 삭제되면 변경된 리스트 출력.
        else:
            print("삭제할 메뉴가 없습니다.")

    elif menu == "5":
        print("종료")
        break

    else :
        print("다시 입력하시오.")





