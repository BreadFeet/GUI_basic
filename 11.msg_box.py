import tkinter.messagebox as msgbox
from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

# 기차 예매 시스템
def info() :          # 버튼의 명령 정의
    msgbox.showinfo('성공',"정상적으로 예매 완료.")  # 팝업 타이틀, 내용
Button(root, text="알림", command=info).pack()      # 버튼 생성

def warn() :
    msgbox.showwarning("실패", '해당 좌석은 매진되었습니다.')
Button(root, text="경고", command=warn).pack()

def error() :
    msgbox.showerror("오류", "결제오류 발생!!")
Button(root, text="오류", command=error).pack()

def okcancel() :
    msgbox.askokcancel("선택여부 확인", "해당 좌석은 유아동반석\
입니다. 예매하시겠습니까?")
Button(root, text="확인/취소", command=okcancel).pack()

def retrycancel() :
    respond = msgbox.askretrycancel("재시도 여부", "일시적인 오류. 다시시도 하겠습니까?")
    print(respond)               # 재시도: True, 취소: False
    if respond == 1 :            # True
        print("재시도 선택")
    elif respond == 0 :          # False
        print("취소 선택")
Button(root, text="재시도/취소", command=retrycancel).pack()





def yesno() :
    msgbox.askyesno("선택확인", "해당좌석은 역방향입니다. 예매하시겠습니까?")
Button(root, text="예/아니오", command=yesno).pack()

def question() :      # 예/아니오와 큰 차이가 없다.
    msgbox.askquestion("질문", "설문조사에 응하시겠습니까?")
Button(root, text="확인질문", command=question).pack()

# 팝업 후 실행 명령 설정
def yesnocancel() :
    response = msgbox.askyesnocancel(None, "예매내역이 저장되지 않았습니다.\n종료 전 예매내역을 저장하시겠습니까?")
    print("응답:", response)    # Terminal에 True/False/None 출력

    if response == 1 :     # True
        print("예")
    elif response == 0 :    # False
        print("아니오")
    else :                  # None
        print("취소")


Button(root, text="예/아니오/취소", command=yesnocancel).pack()








root.mainloop()