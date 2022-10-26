from tkinter import *
root = Tk()
root.title("Sori's GUI")
root.geometry("450x350")


listbox = Listbox(root, selectmode="extended", height=0) 
listbox.insert(0, "사과")      # 0: 위치 index (사실 첨부터 END로 모두 지정해도 됨!)
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")    # 리스트박스는 순서대로 입력 -> 가장 뒤에 붙는 경우, index는 END
listbox.insert(END, "포도")
listbox.pack()

def bellybutton() :
    print("선택항목:", listbox.curselection())
    # 또는
    print("선택항목: {}입니다.".format(listbox.curselection()))

btn = Button(root, text="click", command=bellybutton)
btn.pack()

root.mainloop()