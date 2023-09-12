#파일 쓰기: 파일을 읽거나 쓰기 위해서는 반드시 open() 필요
#파일 객체 = open(파일명, 파일모드, 인코딩)
#파일명: 파일경로 + 파일명 (파일 경로를 입력하지 않으면 현재 위치에 저장)
#파일 모드: r:읽기,w:쓰기(기존파일이 있으면 지우고 새로씀),a:추가(파일이 없으면 생성하고 추가, 있으면 파일의 마지막에 추가)

#파일 쓰기
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학:85", file=score_file)
# print("영어:70", file=score_file)
# score_file.write("국어:80" + "\n")
# score_file.write("과학:45" + "\n")
# score_file.close()

#파일 읽기
#read(): 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
#readline(): 해당 파일의 내용을 한라인씩 읽어 들여 문자열로 반환, 더 이상 읽을 내용이 없으면 None 반환
#readlines(): 해당 파일의 모든 라인을 순서대로 읽어 각각의 라인을 하나의 요소로 저장하는 리스트를 반환

# score_file = open("score.txt", "r", encoding="utf-8")
# # print(score_file.read())
# # score_file.close()
#
# while True:
#     line = score_file.readline() #한줄씩 읽음.
#     if not line : # None, 0, false 등은 거짓, 즉 여기서 line에 줄이 없으면 None이니까 not line 조건 충족
#         break
#     print(line, end="") # 한줄씩 읽어서 출력하기 때문에 줄바꿈 문자가 포함되어있음.
# score_file.close()

# lines = score_file.readlines()
# for e in lines:
#     print(e, end= "")
# score_file.close()

# with 키워드 사용 하기: open() 이후에 자동으로 close를 호출해주는 기능
# with open("score.txt", "r", encoding="utf-8")as score_file:
#     print(score_file.read()) # with는 들여쓰기가 필요함
#
# print("프로그램 끝")


# pickle: 직렬화 역직렬화
# 객체를 직렬화하여 파일에 저장
import pickle
# data = {"name":"전사", "level":200, "addr":"페리온"}
# with open("data.pickle", "wb")as file :
#     pickle.dump(data, file)

# 역직렬화
# 파일에서 객체를 역직렬화하여 복원하기
with open("data.pickle", "rb") as file :
    # restored_data = pickle.loads(file)
    restored_data = pickle.load(file)
print(restored_data)

