import os
from tkinter import *
root = Tk()                   # 클래스의 객체
root.title("제목없음 - Windows 메모장")           # 메소드
root.geometry("450x350")

menu1 = Menu(root)
root.config(menu=menu1)

# 파일
file_menu = Menu(menu1, tearoff=0)
menu1.add_cascade(label="파일", menu=file_menu)

filename = "mynote.txt"
def open_file() :
    if os.path.isfile(filename) :          # os.path.exists도 됨
        with open(filename, "r", encoding="utf8") as file :
            txt.delete("1.0", END)         # 기존 내용 삭제하고 불러오도록
            txt.insert(END, file.read())

file_menu.add_command(label="열기", command=open_file)

def save_file() :
    with open(filename, "w", encoding="utf8") as file :
        file.write(txt.get("1.0", END))      # text 모든 내용 가져와서 file에 기록
file_menu.add_command(label="저장", command=save_file)

file_menu.add_separator()
file_menu.add_command(label="끝내기", command=root.quit)

# 편집 ,서식, 보기, 도움말
menu1.add_cascade(label="편집")
menu1.add_cascade(label="서식")
menu1.add_cascade(label="보기")
menu1.add_cascade(label="도움말")


# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트
txt = Text(root, yscrollcommand=scrollbar.set)  # 창 크기에 맞게 조정되도록
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)



root.mainloop()






