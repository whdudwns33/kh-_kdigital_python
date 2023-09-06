# 각 사이트 비밀번호 만들기
# 규칙1 : http//naver.com 앞의 http// 잘라내기
# 규칙2 : 처음 만나는 점 이후 제거.
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자에 포함된 o의 갯수 + 글자에 포함된 k의 갯수 + ! + 자신의 이니셜
#

file_name = "password.txt"
fd = open(file_name, "wt") # wt: write text. 써라
while True :
 url = input("입력 :")
 if url == "exit" :
  break
 my_str = url.replace("http//", "")
 my_str = my_str[:my_str.index(".")]  # 슬라이싱. '.' 미만의 배열 추출, 이후 삭제. 여기서는 index는 5겠지, 왜냐/ http는 제거되니까
 password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "jyj"
 print("비밀번호 : " + password)
 fd.write(password + "\n") # write: open한 파일에 매개변수 혹은 입력값 저장
fd.close() # 저장된 파일 닫기.








