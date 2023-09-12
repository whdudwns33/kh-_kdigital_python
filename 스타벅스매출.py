file_name = "스타벅스일일매출.txt"
f = open(file_name, "r", encoding="utf-8")
head = f.readline()      # 파일의 첫번째 줄을 읽음
print(head)
head_line = head.split() # 각각의 항목을 공백 기준으로 잘라서 리스트로 변환

espresso = []
americano = []
latte = []
cappucino = []


for line in f: # f는 파일 객체이며 파일의 읽는 위치를 가르키는 식별자, 두번쨰 라인부터 반복처리
    data_list = line.split()    # 각각의 라인을 공백기준으로 구분
    print(data_list)
    espresso.append(int(data_list[1]))
    americano.append(int(data_list[2]))
    latte.append(int(data_list[3]))
    cappucino.append(int(data_list[4]))
f.close()

print(f"{head_line[1]} 전체판매량: {sum(espresso)}, 일 평균 판매량: {sum(espresso)/len(espresso)}")
print(f"{head_line[2]} 전체판매량: {sum(americano)}, 일 평균 판매량: {sum(americano)/len(americano)}")
print(f"{head_line[3]} 전체판매량: {sum(latte)}, 일 평균 판매량: {sum(latte)/len(latte)}")
print(f"{head_line[4]} 전체판매량: {sum(cappucino)}, 일 평균 판매량: {sum(cappucino)/len(cappucino)}")
