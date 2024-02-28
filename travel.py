import random
import time
transport=["차","대중교통"]

#여행지 결정 함수
def choices():
    print("여행지 선정 프로그램을 실행해 주셔서 감사합니다.")
    print("여행 후보지를 띄어쓰기로 구분해서 입력해 주세요")
    huboji = list(input().split())
    place_pick=random.choice(huboji)
    print(f"축하합니다. {place_pick} 지역이 당첨되었습니다.")
    return place_pick

#이동수단 결정함수.
def transport_choice():
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(f"축하드립니다. {place_to_go}을 가되, {random.choice(transport)}를 이용하시면 됩니다")

#실행부
place_to_go=choices()
while True:
    print("다음은 이동수단 결정입니다. 이동 수단은 차와 버스 중 하나입니다.")
    print("확인하시겠습니까?(y/n)")
    check_transport=input()
    if check_transport=='y':
        transport_choice()
        break

    

#반복 시켜주는 코드.
'''
again="y"
while again!="n":
    if again=='y':
        choices()
        print("다시할래?")
        again=input()
    else:
        print("다시 입력해 주세요")
        again=input() 
print("이용해주셔서 감사합니다.")'''    

    