try:
    print("나눗셈 계산기 입니다.")
    num1 = int(input("첫 번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("에러!!! 잘못된 값을 입력 하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
else :      # 정상실행되었을 때 호출 조건 분기 되는 위치
    print("정상 처리 되었습니다.")
finally:    # 오류 여부 없이 무조건 실행
    print("프로그램 실행 완료!!")






