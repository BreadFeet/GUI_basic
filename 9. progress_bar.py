import time
import tkinter.ttk as ttk   # tkinter.ttk를 짧게 ttk로 호출가능
from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

# pgbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
# pgbar.pack()
# pgbar.start(10)
        
# def btncmd() :
#     pgbar.stop()      # 작동 멈추고 값이 사라짐
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

pgbar2_var = DoubleVar()    # 소수점도 출력되도록 설정
pgbar2 = ttk.Progressbar(root, maximum=100, length=300, variable=pgbar2_var)
pgbar2.pack()

def btncmd2() :
    for i in range(1, 101) :    # 바가 채워지는 범위: 1~100 까지 증가하도록
        pgbar2_var.set(i)        # set: 바가 채위지는 범위   
        pgbar2.update()
        time.sleep(0.01)        # 0.01 초 대기 설정
     
                
  
btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()


root.mainloop()