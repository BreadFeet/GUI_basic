from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

txt = Text(root, width=30, height=5)
txt.insert(END, "글자를 입력해주세요")  # END(대문자): 글자 넣는 위치
txt.pack()

e = Entry(root, width=50)
e.insert(0, "한줄만 입력하세요")   # 0: index 값, 0의 자리에 문구 삽입
e.pack()

def bellybutton() :
    print(txt.get("1.0", "1.3"))
    print(e.get())  

btn = Button(root, text="click", command=bellybutton)
btn.pack()

root.mainloop()