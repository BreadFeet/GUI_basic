from tkinter import *

root = Tk()     # 대소문자 중요
root.title("Nado GUI")    # 창 이름 설정
root.geometry("350x450")

btn1 = Button(root, text="button 1")   # 설정
btn1.pack()         # 버튼이 실제 프로그램에 포함됨

btn2 = Button(root, padx=5, pady=10, text="button 2")
btn2.pack()         

btn4 = Button(root, width=10, height=3, text="button 4")
btn4.pack()

btn5 = Button(root, fg="skyblue", bg="dark blue", text="button 5")
btn5.pack()       # fg: foreground(글자색), bg: background

photo = PhotoImage(file="gui_basic/image for button.png")   # 파일 경로 지정
btn6 = Button(root, image=photo)    # 지정한 photo 불러옴
btn6.pack()

def btncmd() :
    print("버튼이 클릭되었어요")    # 버튼이 클릭되면 나오는 문구
    
btn7 = Button(root, text="working button 7", command=btncmd)
btn7.pack()        # 터미널에 print 내용 출력됨


root.mainloop()