from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

def btncmd() :
  print(chkvar.get())   # 0: 체크 해제(기본값), 1: 체크 설정
  print(chkvar2.get())
btn = Button(root, text="click", command=btncmd)
btn.pack()

chkvar = IntVar()     #chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.pack()

chkvar2 = IntVar()    # IntVar는 저장된 함수라 이름변경X
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()





root.mainloop()