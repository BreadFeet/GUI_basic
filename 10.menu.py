from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")

menu1 = Menu(root)
root.config(menu=menu1) 

# File 메뉴
menu_file = Menu(menu1, tearoff=0)  
menu1.add_cascade(label="File", menu=menu_file)  

def creat_new_file() :       # 클릭 명령 설정하는 경우
    print("새 파일을 만듭니다.")
menu_file.add_command(label="New File", command=creat_new_file)  

menu_file.add_command(label="New Window")  # 클릭 명령 설정 안함
menu_file.add_separator()    # 구분선 추가
menu_file.add_command(label="Open File...")
menu_file.add_separator() 
menu_file.add_command(label="Save All", state="disable")  # 버튼 비활성화
menu_file.add_separator() 
menu_file.add_command(label="Exit", command=root.quit)  # 클릭 시, 프로그램 종료

# Edit 메뉴
def txt() :
    print("아래 하위 메뉴가 없습니다.")
menu1.add_cascade(label="Edit", command=txt)

# Language - 라디오버튼 삽입
menu_lang = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Language", menu=menu_lang)

menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")

# View - 체크박스 삽입
menu_view = Menu(menu1, tearoff=0)
menu1.add_cascade(label="View", menu=menu_view)

menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show Breadcrumps")
menu_view.add_checkbutton(label="Render Whitespace")




root.mainloop()