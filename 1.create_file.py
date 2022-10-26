from tkinter import *

root = Tk()     # 대소문자 중요
root.title("Nado GUI")    # 창 이름 설정
root.geometry("320x480+300+100")   # 가로*세로 + x좌표 + y좌표 (붙여쓰기)
root.resizable(False, False)    # x축(너비), y축(높이) 크기 변경 불가


root.mainloop()