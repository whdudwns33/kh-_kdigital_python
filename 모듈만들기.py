# 모듈이란 코드가 저장된 파일을 모듈.
def add(a,b):
    return a+b

def sub(a,b):
    return a - b

def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
    return password



if __name__ == "__main__":  # 진입 지점. entry point. 현재 파일이 엔트리 포인트인지 확인 할 떄 사용.
                            # 엔트리 포인트가 없으면 다른 파일에서 모듈을 불러 사용하면 원하지 않는 아래 함수가 출력됨
                            # 즉, 진입 지점이 이파일이 아니면 아래 함수를 쓰지 않는다.
    print(add(1,4))
    print(sub(10,4))

