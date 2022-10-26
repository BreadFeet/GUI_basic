from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

Label(root, text="메뉴를 선택하세요!").pack()     # 코드 줄이기 위해서

bg_var = IntVar()    # Radiobutton 선택값을 int로 반환해서 저장
btn_bg1 = Radiobutton(root, text="햄버거", value=0, variable=bg_var)
btn_bg1.select()
btn_bg2 = Radiobutton(root, text="치즈버거", value=1, variable=bg_var)
btn_bg3 = Radiobutton(root, text="치킨버거", value=2, variable=bg_var)
btn_bg1.pack()
btn_bg2.pack()
btn_bg3.pack()

Label(root, text="음료를 선택하세요!").pack()

dr_var = StringVar()    # value가 문자이기 때문
btn_dr1 = Radiobutton(root, text="콜라", value="콜라", variable=dr_var)
btn_dr1.select()      # 콜라를 기본값으로 선택함
btn_dr2 = Radiobutton(root, text="사이다", value="사이다", variable=dr_var)
btn_dr1.pack()
btn_dr2.pack()

def btncmd() :
    print(bg_var.get())   # 선택된 햄버거의 값(value)을 보여줌
    print(dr_var.get())   # 선택된 음료의 값을 문자로 보여줌
btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()