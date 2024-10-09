from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from objRelation import Repository

screen = Tk()

screen.geometry("%dx%d+%d+%d" % (600, 420, 250, 150))
screen.title("فرم ثبت نام باشگاه")
screen.iconbitmap("img/icon.ico")

repository = Repository()


# functions

def register(User):
    if int(User["Age"]) >= 18:
        col = "prsl_name,prsl_family,prsl_age"
        val = "'" + User["Name"] + "','" + User["Family"] + "','" + User["Age"] + "' "
        result = repository.Create('personal', col, val)
        if result:
            messagebox.showinfo("ثبت گردید", "ثبت نام شما با موفقیت انجام شد")
        else:
            messagebox.showerror(" خطا", "ثبت عملیات با خطا مواجه شد")
        return result
    else:
        messagebox.showwarning("توجه", "سن شما برای باشگاه کافی نیست")
        return False


def OnClickRegister():
    name = Name.get()
    family = Family.get()
    age = Age.get()
    us = {"Name": name, "Family": family, "Age": age}
    result = register(us)
    if result:
        Load()
        txtName.focus_set()


def Clear(ListVal):
    for item in ListVal:
        item.set("")


def InsertData(value):
    tbl.insert('', "end", text="1", values=[value[2].get(), value[1].get(), value[0].get()])


def GetSelection(e):
    btnDelete.place(x=370, y=110)
    selection_row = tbl.selection()
    if selection_row != ():
        btnEdit.place(x=450, y=110)
        ListItem = [Name, Family, Age]
        Clear(ListItem)
        Id.set(tbl.item(selection_row)["values"][3])
        Name.set(tbl.item(selection_row)["values"][2])
        Family.set(tbl.item(selection_row)["values"][1])
        Age.set(tbl.item(selection_row)["values"][0])


def OnClickSearch():
    if txtSearch.get() != "":
        search = txtSearch.get()
        result = Search(search)
    else:
        CleanTable()
        Load()


def Search(value):
    where = (
                "prsl_name LIKE '%" + value + "%' OR prsl_family LIKE '%" + value + "%' OR prsl_age LIKE '%" + value + "%' ")
    result = repository.Search("personal", "*", where)
    CleanTable()
    for item in result:
        tbl.insert('', "end", values=[item[3], item[2], item[1], item[0]])


def CleanTable():
    for item in tbl.get_children():
        sel = (str(item),)
        tbl.delete(sel)


def Load():
    result = repository.Read("personal", "*")
    CleanTable()
    for item in result:
        tbl.insert('', "end", values=[item[3], item[2], item[1], item[0]])


def OnClickDelete():
    result = messagebox.askquestion("هشدار", "آیا از حذف این رکورد مطمئن هستید؟")
    if result == "yes":
        Delete()


def Delete():
    select_row = tbl.selection()
    if select_row != ():
        selectItem = tbl.item(select_row)["values"]
        where = "prsl_id= '" + str(selectItem[3]) + "' "
        result = repository.Delete("personal", where)
        print(selectItem[3])
        if result:
            messagebox.showinfo("عملیات موفق", "حذف اطلاعات با موفقیت انجام شد")
            Load()
        else:
            messagebox.showerror("خطا", "حذف انجام نشد")
        btnDelete.place_forget()


def OnClickEdit():
    select_row = tbl.selection()
    selectItem = tbl.item(select_row)["values"]
    where = " prsl_id='" + Id.get() + "'"
    col = " prsl_name='" + Name.get() + "', prsl_family= '" + Family.get() + "', prsl_age= '" + Age.get() + "' "
    result = repository.Update('personal', col, where)
    if result:
        Load()
        btnEdit.place_forget()
        ListItem = [Name, Family, Age, Id]
        Clear(ListItem)
        messagebox.showinfo("ثبت گردید", "ویرایش انجام شد")
    else:
        messagebox.showwarning("خطا ", "ویرایش انجام نگردید")


def OnClickShowSearch():
    frmSearch.place(x=0, y=0)
    btnSearchShow.place_forget()


def OnClickClose():
    frmSearch.place_forget()
    btnSearchShow.place(x=180, y=110)


def GetValue():
    counter = []
    for item in range(1, 130):
        counter.append(item)
    return counter


# Radio & Check buttons

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
btnCheck1 = Checkbutton(screen, text="استانی", variable=check1).place(x=170, y=250)
btnCheck2 = Checkbutton(screen, text="کشوری", variable=check2).place(x=170, y=280)
btnCheck3 = Checkbutton(screen, text="بین المللی", variable=check3).place(x=170, y=310)
sex = IntVar()
btnRadioFemale = Radiobutton(screen, text="خانم", variable=sex, value=0).place(x=170, y=170)
btnRadioMale = Radiobutton(screen, text="آقا", variable=sex, value=1).place(x=170, y=200)

# Search

frmSearch = Frame(screen, width=260, height=400, background="gray")
frmSearch.place(x=0, y=0)
frmSearch.place_forget()

bgSearch = PhotoImage(file="img/backCard.png")
bgBack = PhotoImage(file="img/back.png")

# labels

lblName = Label(screen, text="نام").place(x=440, y=20)
lblFamily = Label(screen, text="نام خانوادگی").place(x=440, y=50)
lblAge = Label(screen, text="سن").place(x=440, y=80)

# Vars

Name = StringVar()
Family = StringVar()
Age = StringVar()
Id = StringVar()

# Inputs

txtId = Entry(screen, textvariable=Id, justify="right")
txtId.place_forget()
txtName = Entry(screen, textvariable=Name, justify="right")
txtName.place(x=290, y=20)
txtFamily = Entry(screen, textvariable=Family, justify="right")
txtFamily.place(x=290, y=50)
cmbAge = ttk.Combobox(screen, state="readonly", textvariable=Age, justify="right", width=17)
cmbAge["value"] = GetValue()
cmbAge.current(24)
cmbAge.place(x=290, y=80)

# Buttons

btnRegister = Button(screen, text="ثبت نام", width=6, command=OnClickRegister).place(x=290, y=110)
btnDelete = Button(screen, text="حذف", bg="red", fg="white", width=6, command=OnClickDelete)
btnDelete.place_forget()
btnEdit = Button(screen, text="ویرایش", bg="green", fg="white", width=6, command=OnClickEdit)
btnEdit.place_forget()
btnSearchShow = Button(screen, text="نمایش جستجو", command=OnClickShowSearch)
btnSearchShow.place(x=180, y=110)

# Table

colms = ("c1", "c2", "c3", "c4")
tbl = ttk.Treeview(screen, columns=colms, show="headings", height=10)
tbl.place(x=290, y=150)
tbl.column("# 4", width=40, anchor=N)
tbl.heading("# 4", text="ردیف")
tbl.column("# 3", width=80, anchor=N)
tbl.heading("# 3", text="نام")
tbl.column("# 2", width=120, anchor=N)
tbl.heading("# 2", text="نام خانوادگی")
tbl.column("# 1", width=50, anchor=N)
tbl.heading("# 1", text="سن")
tbl.bind("<Button-1>", GetSelection)

# Search Area

lblBG = Label(frmSearch, text="*", image=bgSearch).place(x=0, y=0)

lblSearch = Label(frmSearch, text="مقدار جستجو")
lblSearch.place(x=90, y=50)
txtSearch = Entry(frmSearch, )
txtSearch.place(x=60, y=70)
btnSearch = Button(frmSearch, text="جستجو", command=OnClickSearch)
btnSearch.place(x=100, y=100)
btnCloseFrame = Button(frmSearch, command=OnClickClose, text="*", image=bgBack, bg="white").place(x=225, y=0)


# Menu
def part():
    print("کلیک شد")


def close():
    exit()


menuBar = Menu(screen)

userMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="کاربران", menu=userMenu)
userMenu.add_command(label="افزودن کاربر", command=part)
userMenu.add_command(label="نمایش کاربران", command=part)

settingMenu = Menu(menuBar, tearoff=1)
menuBar.add_cascade(label="تنظیمات", menu=settingMenu)
settingMenu.add_command(label="شهریه", command=part)
settingMenu.add_command(label="بدهی", command=part)
settingMenu.add_separator()
settingMenu.add_command(label="خروج", command=close, foreground="red")

screen.config(menu=menuBar)

Load()

screen.mainloop()
