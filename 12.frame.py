from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")


# 버거 프레임
fr_bg = Frame(root, relief="solid", bd=10)    # relief: 테두리, bd: 외곽선
fr_bg.pack(side="top", fill="both", expand=True)                    # 설정만 되고 출력 안됨

Button(fr_bg, text="햄버거").pack()   
Button(fr_bg, text="치즈버거").pack()
Button(fr_bg, text="치킨버거").pack()

# 음료 레이블 프레임
lfr_dr = LabelFrame(root, text="음료", bd=10)  # 다른 모양 테두리
lfr_dr.pack(side="right", fill="both", expand=True)         # 출력은 안됨

Button(lfr_dr, text="coke").pack()
Button(lfr_dr, text="sprite").pack()


root.mainloop()