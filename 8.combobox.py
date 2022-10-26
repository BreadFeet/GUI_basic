import tkinter.ttk as ttk   # tkinter.ttk를 짧게 ttk로 호출가능
from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

value = [str(i) + '일' for i in range(1, 32)]   # 1~31 까지의 날짜
cbbox = ttk.Combobox(root, height=5, values=value)  # 클래스 객체값
cbbox.pack()            # 메소드 값 출력
cbbox.set("카드 결제일")

cbbox_readonly = ttk.Combobox(root, height=10, values=value, state="readonly")  # state 설정: 읽기 전용
cbbox_readonly.current(0)    # index: 0번째 값을 목록 제목으로 설정
cbbox_readonly.pack()            


def btncmd() :
    print(cbbox.get())    # 선택한 값을 그대로 출력
    print(cbbox_readonly.get())
btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()