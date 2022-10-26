from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

frame = Frame(root, relief="sunken", bd=5)
frame.pack()

scrollbar = Scrollbar(frame)  
scrollbar.pack(side="right", fill="y")   

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)  
for i in range(1,32) :          # 1~31일 리스트박스 설정
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)






root.mainloop()