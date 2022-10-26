from tkinter import *

root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

label1 = Label(root, text="Hello World")  # 글자 설정
label1.pack()            # 실행 명령

photo = PhotoImage(file="gui_basic/img1.png")  # 버튼과 같은 방식
label2 = Label(root, image=photo)
label2.pack()

def change() :     # 명령 내용 정의
    label1.config(text="see you again!") 

    global photo2      # 전역 변수 지정
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)
   
btn = Button(root, text="click", command=change)   # 명령내용 -> command
btn.pack()



root.mainloop()