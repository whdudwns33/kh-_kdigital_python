# 딕셔너리를 사용해 학생의 인적사항 등록 , 검색, 저장, 불러오기 기능 구현
# 저장한 Rest Api의 기본형태인 Jason으로 저장 및 불러오기.    (웹에서 API의 기본 포맷)
# 함수로 구현

import json # Json 형식으로 데이터를 저장하고 불러오기 위해서 json 모듈을 import
student_dic ={} # 빈 딕셔너리. 학생정보를 저장하기 위한 딕셔너리.

# 함수만들기
# 1. 학생정보 등록을 위한 함수
def reg_student() :
    student_id = input("학번 :")
    student_name = input("이름 :")
    student_addr = input("주소 :")
    student_dic[student_id] = {"이름" : student_name, "주소" : student_addr}
    print(f"학생 {student_name}님의 정보가 등록되었습니다.")

# 학생정보 검색
def search_student():
    student_id = input("검색할 학번 입력 :")
    student_info = student_dic.get(student_id) # get(key) 함수로 학번을 입력하여 정보를 출력함
    if student_info : #student_info가 있으면 정보 출력
        print(f"학번 : {student_id} \n"
              f"이름 : {student_info['이름']} \n"
              f"주소 : {student_info['주소']}")
    else:
        print("다시 입력하시오")

# 학생정보 변경
def modify_student() :
    student_id = input("수정할 학생의 학번을 입력하세요")
    student_info = student_dic.get(student_id)
    if student_info :
        student_name = input("이름 :")
        student_addr = input("주소 :")
        student_info["이름"] = student_name
        student_info["주소"] = student_addr
        print(f"{student_name}님의 정보 수정")
    else:
        print("해당 학생의 정보를 찾을 수 없음")

# 학생정보 삭제
def del_student():
    student_id = input("삭제할 학생의 학번을 입력하시오")
    if student_dic.get(student_id) : #get() True or False
        del student_dic[student_id]  #해당 키로 딕셔너리 삭제
        print("학생 정보 삭제")
    else:
        print("해당 정보가 없음")

# 학생정보 보기
def view_all_student() :
    for student_id in student_dic:
        student_info = student_dic[student_id] # .get(key)로 해도 됨
        print(f"학번 : {student_id} \n"
              f"이름 : {student_info['이름']} \n"
              f"주소 : {student_info['주소']}")
# 학생 정보 저장
def save_student() :
    with open("student.json", "w", encoding='utf-8')as file: # with는 close를 생략할 수 있음.
        json.dump(student_dic, file, ensure_ascii=False)     # ensure_ascii=False 이걸 해줘야 한글로 저장할 수 있음. 제이슨 형식을 쓸때는.
    print("학생 정보가 저장 되었습니다.")

# 제이슨 파일을 불러들임
def load_student() :
    try :
        with open("student.json", "r", encoding='utf-8')as file:
            student_dic.clear() # 현재 메모리에 있는 데이터 초기화
            student_dic.update(json.load(file))
        print("학생정보를 불러왔습니다.")
    except FileExistsError:
        print("저장된 파일을 찾을 수 없습니다.")

while True:
    print("="*5, "학생정보 관리", "="*5)
    choice = input("[1] 등록 [2] 검색 [3] 수정 [4] 삭제 [5] 전체 보기 [6] 저장 [7] 불러오기 [8] 종료 : ")
    if choice == "1":
        reg_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        modify_student()
    elif choice == "4":
        del_student()
    elif choice == "5":
        view_all_student()
    elif choice == "6":
        save_student()
    elif choice == "7":
        load_student()
    elif choice == "8":
        print("종료")
        break
    else:
        print("다시 입력 하시오")


