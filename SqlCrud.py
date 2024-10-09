from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from objRelashen import *

# lbl ha

screen = Tk()
screen.geometry("%dx%d+%d+%d" % (800, 400, 500, 400))
screen.title("پیام خوش آمد گویی")
screen.iconbitmap("img/icon.ico")

repository=Repository()
# def
def Register(User):
    if int(User["age"]) >= 18:

        col = "prs_name , prs_family , prs_age "
        val = " '" + User["Name"] + "','" + User["family"] + "','" + User["age"] + "'  "
        result = repository.Create("personel", col, val)
        if result == True:
            messagebox.showinfo("انجام شد", "خوش امدید ثبت نام شما انجام شد")
        else:
            messagebox.showerror("   خطا", "  انجام نشد")

        return result

    else:
        messagebox.showwarning("توجه", "هنوز بچه ای برا باشگاه رفتن")
        return False;


def OnCkickRegister( ):
    name = Name.get()
    family = Family.get()
    age = Age.get()
    us = {"Name": name, "family": family, "age": age}
    result = Register(us)
    if result == True:
        ListItem = [Name, Family, Age]
        insertData(ListItem)
        cleare(ListItem)
        txtName.focus_set()


def cleare(Listval):
    for item in Listval:
        item.set("")


def insertData(value):
    tbl.insert('', "end", text="1", value=[value[2].get(), value[1].get(), value[0].get()])


def GetSelction(e):
    btnDelet.place(x=410, y=160)


    selection_row = tbl.selection()
    print(selection_row)
    if selection_row != ():
        btnEdit.place(x=460, y=160)
    ListItem = [Name, Family, Age]
    cleare(ListItem)
    Name.set(tbl.item(selection_row)["values"][2])
    Family.set(tbl.item(selection_row)["values"][1])
    Age.set(tbl.item(selection_row)["values"][0])
    Id.set(tbl.item(selection_row)["values"][3])


def OnclickSearch( ):
    query = txtSearch.get()
    Search(query)


def Search(value):
    where = " prs_name Like '%" + value + "%' or prs_family Like '%" + value + "%' "
    result = repository.Search("personel", "*", where)
    CleanTable()
    for item in result:
        tbl.insert('', "end", value=[item[3], item[2], item[1], item[0]])


def Load( ):
    repository = Repository()
    result = repository.Read("personel", "*")
    CleanTable()
    for item in result:
        tbl.insert('', "end", value=[item[3], item[2], item[1], item[0]])


def CleanTable( ):
    for item in tbl.get_children():
        sel = (str(item),)
        tbl.delete(sel)


def OnclickDelet( ):
    result = messagebox.askquestion("هشدار", "آیا مطمعن هستید میخواهید این داده را حذف کنید")

    if result == "yes":
        Delate()


def Delate( ):
    repository = Repository()
    select_row = tbl.selection()

    if select_row != ():
        SelectItem = tbl.item(select_row)["values"]
        where = " prs_id='" + str(SelectItem[3]) + "' "
        result = repository.Delet("personel", where)
        if result:
            messagebox.showinfo("انجام شد ", "حذف اطلاعات با موفقیت انجام شد")
            Load()
    else:
        messagebox.showerror("خطا", "حذف انجام نشد")
    btnDelet.place_forget()


def OnclickEdit( ):
    repository = Repository()
    select_row = tbl.selection()
    SelectItem = tbl.item(select_row)["values"]

    where = " prs_id= '" + Id.get() + "' "
    col = "  prs_name='" + Name.get() + "',prs_family='" + Family.get() + "' , prs_age='" + Age.get() + "' "
    result = repository.Update("personel", col, where)
    if result:
        Load()
        btnEdit.place_forget()
        ListItem = [Name, Family, Age, Id]
        cleare(ListItem)
        messagebox.showinfo("انجام شد", "ویرایش انجام شد")
    else:
        messagebox.showerror("   خطا", "  انجام نشد")


def OnClickShowSearch( ):
    frmSearch.place(x=0, y=0)


def OnclickCloseSearch( ):
    frmSearch.place_forget()


def GetValue():
    counter = []
    for item in range(1, 130):
        counter.append(item)

    return counter


def prt(self):
    print("click shod")
    # end def


bgSearch = PhotoImage(file="img/backCard.png")
iconClose = PhotoImage(file="img/close.png")

lblName = Label(screen, text="نام").place(x=500, y=40)
lblFamily = Label(screen, text="نام خانوادکی").place(x=500, y=80)
lblage = Label(screen, text="سن").place(x=500, y=120)

# var ha

Name = StringVar()
Family = StringVar()
Age = StringVar()
Id = StringVar()

# input

txtName = Entry(screen, textvariable=Name, justify="right")
txtName.place(x=350, y=40)
txtFamily = Entry(screen, textvariable=Family, justify="right")
txtFamily.place(x=350, y=80)
txtId = Entry(screen, textvariable=Id, justify="right")
txtId.place_forget()

comobText = ttk.Combobox(screen, state="readonly", textvariable=Age, justify="right")
valuesCombo = GetValue()
comobText["value"] = valuesCombo
comobText.current(23)
comobText.place(x=350, y=120)

# frame

frmSearch = Frame(screen, width=300, height=400, background="black")
frmSearch.place(x=0, y=0)
frmSearch.place_forget()

# btns

btnRegester = Button(screen, text="ثبت نام", command=OnCkickRegister).place(x=350, y=160)
btnDelet = Button(screen, text="حذف", bg="red", fg="white", command=OnclickDelet)
btnDelet.place_forget()
btnEdit = Button(screen, text="ویرایش", bg="#00ff37", fg="#000000", command=OnclickEdit)
btnEdit.pack_forget()
btnSearchShow = Button(screen, text="نمایش جستجو", command=OnClickShowSearch).place(x=350, y=190)

cols = ("c1", "c2", "c3", "c4")
tbl = ttk.Treeview(screen, columns=cols, show="headings", height=50)

tbl.column("# 4", anchor=E, width=50)
tbl.heading("# 4", text="شماره سطر")

tbl.column("# 3", anchor=E, width=50)
tbl.heading("# 3", text="نام")

tbl.column("# 2", width=50)
tbl.heading("# 2", text="نام خانوادگی")

tbl.column("# 1", width=100)
tbl.heading("# 1", text="سن")
tbl.bind("<Button-1>", GetSelction)

tbl.place(x=300, y=220)

lblBg = Label(frmSearch, text="*", image=bgSearch).place(x=0, y=0)
lblsarch = Label(frmSearch, text="مقدار جستجو").place(x=140, y=10)
txtSearch = Entry(frmSearch)
txtSearch.place(x=10, y=10)
btnSearch = Button(frmSearch, text="جستجو کن", command=OnclickSearch).place(x=40, y=40)
btnClose = Button(frmSearch, text="*", command=OnclickCloseSearch, image=iconClose, bg="white").place(x=250,
                                                                                                      y=0)

menobar = Menu(screen)

userMeno = Menu(menobar, tearoff=0)

userMeno.add_command(label="افزودن کاربر", command=prt)
userMeno.add_command(label="نمایش کاربران  ", command=prt)

menobar.add_cascade(label="کابران", menu=userMeno)

SettingMnu = Menu(menobar, tearoff=0)
SettingMnu.add_command(label="شهریه", command=prt)
SettingMnu.add_command(label="بدهی", command=prt)
SettingMnu.add_separator()
SettingMnu.add_command(label="خروج", command=prt, foreground="red")

menobar.add_cascade(label="تنظیمات", menu=SettingMnu)

screen.config(menu=menobar)

Load()
screen.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from objRelashen import *

# lbl ha


screen = Tk()
screen.geometry("%dx%d+%d+%d" % (800, 400, 500, 400))
screen.title("پیام خوش آمد گویی")
screen.iconbitmap("img/icon.ico")


# def
def Register(User):
    if int(User["age"]) >= 18:

        col = "prs_name , prs_family , prs_age "
        val = " '" + User["Name"] + "','" + User["family"] + "','" + User["age"] + "'  "
        result = repository.Create("personel", col, val)
        if result == True:
            messagebox.showinfo("انجام شد", "خوش امدید ثبت نام شما انجام شد")
        else:
            messagebox.showerror("   خطا", "  انجام نشد")

        return result

    else:
        messagebox.showwarning("توجه", "هنوز بچه ای برا باشگاه رفتن")
        return False;


def OnCkickRegister():
    name = Name.get()
    family = Family.get()
    age = Age.get()
    us = {"Name": name, "family": family, "age": age}
    result = Register(us)
    if result == True:
        ListItem = [Name, Family, Age]
        insertData(ListItem)
        cleare(ListItem)
        txtName.focus_set()


def cleare(Listval):
    for item in Listval:
        item.set("")


def insertData(value):
    tbl.insert('', "end", text="1", value=[value[2].get(), value[1].get(), value[0].get()])


def GetSelction(e):
    btnDelet.place(x=410, y=160)


    selection_row = tbl.selection()
    print(selection_row)
    if selection_row != ():
        btnEdit.place(x=460, y=160)
    ListItem = [Name, Family, Age]
    cleare(ListItem)
    Name.set(tbl.item(selection_row)["values"][2])
    Family.set(tbl.item(selection_row)["values"][1])
    Age.set(tbl.item(selection_row)["values"][0])
    Id.set(tbl.item(selection_row)["values"][3])


def OnclickSearch():
    query = txtSearch.get()
    Search(query)


def Search(value):
    where = " prs_name Like '%" + value + "%' or prs_family Like '%" + value + "%' "
    result = repository.Search("personel", "*", where)
    CleanTable()
    for item in result:
        tbl.insert('', "end", value=[item[3], item[2], item[1], item[0]])


def Load():
    repository = Repository()
    result = repository.Read("personel", "*")
    CleanTable()


    for item in result:
        tbl.insert('', "end", value=[item[3], item[2], item[1], item[0]])


def CleanTable():
    for item in tbl.get_children():
        sel = (str(item),)
        tbl.delete(sel)


def OnclickDelet():
    result = messagebox.askquestion("هشدار", "آیا مطمعن هستید میخواهید این داده را حذف کنید")

    if result == "yes":
        Delate()


def Delate():
    repository = Repository()
    select_row = tbl.selection()

    if select_row != ():
        SelectItem = tbl.item(select_row)["values"]
        where = " prs_id='" + str(SelectItem[3]) + "' "
        result = repository.Delet("personel", where)
        if result:
            messagebox.showinfo("انجام شد ", "حذف اطلاعات با موفقیت انجام شد")
            Load()
    else:
        messagebox.showerror("خطا", "حذف انجام نشد")
    btnDelet.place_forget()


def OnclickEdit():
    repository = Repository()
    select_row = tbl.selection()
    SelectItem = tbl.item(select_row)["values"]

    where = " prs_id= '" + Id.get() + "' "
    col = "  prs_name='" + Name.get() + "',prs_family='" + Family.get() + "' , prs_age='" + Age.get() + "' "
    result = repository.Update("personel", col, where)
    if result:
        Load()
        btnEdit.place_forget()
        ListItem = [Name, Family, Age, Id]
        cleare(ListItem)


        messagebox.showinfo("انجام شد", "ویرایش انجام شد")
    else:
        messagebox.showerror("   خطا", "  انجام نشد")


def OnClickShowSearch():
    frmSearch.place(x=0, y=0)


def OnclickCloseSearch():
    frmSearch.place_forget()


def GetValue():
    counter = []
    for item in range(1, 130):
        counter.append(item)

    return counter


def prt(self):
    print("click shod")
    # end def


bgSearch = PhotoImage(file="img/backCard.png")
iconClose = PhotoImage(file="img/close.png")

lblName = Label(screen, text="نام").place(x=500, y=40)
lblFamily = Label(screen, text="نام خانوادکی").place(x=500, y=80)
lblage = Label(screen, text="سن").place(x=500, y=120)

# var ha

Name = StringVar()
Family = StringVar()
Age = StringVar()
Id = StringVar()

# input

txtName = Entry(screen, textvariable=Name, justify="right")
txtName.place(x=350, y=40)
txtFamily = Entry(screen, textvariable=Family, justify="right")
txtFamily.place(x=350, y=80)
txtId = Entry(screen, textvariable=Id, justify="right")
txtId.place_forget()

comobText = ttk.Combobox(screen, state="readonly", textvariable=Age, justify="right")
valuesCombo = GetValue()
comobText["value"] = valuesCombo
comobText.current(23)
comobText.place(x=350, y=120)

# frame

frmSearch = Frame(screen, width=300, height=400, background="black")
frmSearch.place(x=0, y=0)
frmSearch.place_forget()

# btns

btnRegester = Button(screen, text="ثبت نام", command=OnCkickRegister).place(x=350, y=160)
btnDelet = Button(screen, text="حذف", bg="red", fg="white", command=OnclickDelet)
btnDelet.place_forget()
btnEdit = Button(screen, text="ویرایش", bg="#00ff37", fg="#000000", command=OnclickEdit)
btnEdit.pack_forget()
btnSearchShow = Button(screen, text="نمایش جستجو", command=OnClickShowSearch).place(x=350, y=190)

cols = ("c1", "c2", "c3", "c4")
tbl = ttk.Treeview(screen, columns=cols, show="headings", height=50)

tbl.column("# 4", anchor=E, width=50)
tbl.heading("# 4", text="شماره سطر")

tbl.column("# 3", anchor=E, width=50)
tbl.heading("# 3", text="نام")

tbl.column("# 2", width=50)
tbl.heading("# 2", text="نام خانوادگی")

tbl.column("# 1", width=100)
tbl.heading("# 1", text="سن")
tbl.bind("<Button-1>", GetSelction)

tbl.place(x=300, y=220)
lblBg = Label(frmSearch, text="*", image=bgSearch).place(x=0, y=0)
lblsarch = Label(frmSearch, text="مقدار جستجو").place(x=140, y=10)
txtSearch = Entry(frmSearch)
txtSearch.place(x=10, y=10)
btnSearch = Button(frmSearch, text="جستجو کن", command=OnclickSearch).place(x=40, y=40)
btnClose = Button(frmSearch, text="*", command=OnclickCloseSearch, image=iconClose, bg="white").place(x=250,
                                                                                                      y=0)

menobar = Menu(screen)

userMeno = Menu(menobar, tearoff=0)

userMeno.add_command(label="افزودن کاربر", command=prt)
userMeno.add_command(label="نمایش کاربران  ", command=prt)

menobar.add_cascade(label="کابران", menu=userMeno)

SettingMnu = Menu(menobar, tearoff=0)
SettingMnu.add_command(label="شهریه", command=prt)
SettingMnu.add_command(label="بدهی", command=prt)
SettingMnu.add_separator()
SettingMnu.add_command(label="خروج", command=prt, foreground="red")

menobar.add_cascade(label="تنظیمات", menu=SettingMnu)

screen.config(menu=menobar)

Load()
screen.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from objRelashen import *

# lbl ha


screen = Tk()
screen.geometry("%dx%d+%d+%d" % (800, 400, 500, 400))
screen.title("پیام خوش آمد گویی")
screen.iconbitmap("img/icon.ico")


# def
def Register(User):
    if int(User["age"]) >= 18:

        col = "prs_name , prs_family , prs_age "
        val = " '" + User["Name"] + "','" + User["family"] + "','" + User["age"] + "'  "
        result = repository.Create("personel", col, val)
        if result == True:
            messagebox.showinfo("انجام شد", "خوش امدید ثبت نام شما انجام شد")
        else:
            messagebox.showerror("   خطا", "  انجام نشد")

        return result

    else:
        messagebox.showwarning("توجه", "هنوز بچه ای برا باشگاه رفتن")
        return False;


def OnCkickRegister():
    name = Name.get()
    family = Family.get()
    age = Age.get()
    us = {"Name": name, "family": family, "age": age}
    result = Register(us)
    if result == True:
        ListItem = [Name, Family, Age]
        insertData(ListItem)
        cleare(ListItem)
        txtName.focus_set()


def cleare(Listval):
    for item in Listval:
        item.set("")


def insertData(value):
    tbl.insert('', "end", text="1", value=[value[2].get(), value[1].get(), value[0].get()])


def GetSelction(e):
    btnDelet.place(x=410, y=160)


    selection_row = tbl.selection()
    print(selection_row)
    if selection_row != ():
        btnEdit.place(x=460, y=160)
    ListItem = [Name, Family, Age]
    cleare(ListItem)
    Name.set(tbl.item(selection_row)["values"][2])
    Family.set(tbl.item(selection_row)["values"][1])
    Age.set(tbl.item(selection_row)["values"][0])
    Id.set(tbl.item(selection_row)["values"][3])


def OnclickSearch():
    query = txtSearch.get()
    Search(query)


def Search(value):
    where = " prs_name Like '%" + value + "%' or prs_family Like '%" + value + "%' "
    result = repository.Search("personel", "*", where)
    CleanTable()


    for item in result:
        tbl.insert('', "end", value=[item[3], item[2], item[1], item[0]])


def Load():
    repository = Repository()
    result = repository.Read("personel", "*")
    CleanTable()


    for item in result:
        tbl.insert('', "end", value=[item[3], item[2], item[1], item[0]])


def CleanTable(self):
    for item in tbl.get_children():
        sel = (str(item),)
        tbl.delete(sel)


def OnclickDelet(self):
    result = messagebox.askquestion("هشدار", "آیا مطمعن هستید میخواهید این داده را حذف کنید")

    if result == "yes":
        Delate()


def Delate(self):
    repository = Repository()
    select_row = tbl.selection()

    if select_row != ():
        SelectItem = tbl.item(select_row)["values"]
        where = " prs_id='" + str(SelectItem[3]) + "' "
        result = repository.Delet("personel", where)
        if result:
            messagebox.showinfo("انجام شد ", "حذف اطلاعات با موفقیت انجام شد")
            Load()
    else:
        messagebox.showerror("خطا", "حذف انجام نشد")
    btnDelet.place_forget()


def OnclickEdit(self):
    repository = Repository()
    select_row = tbl.selection()
    SelectItem = tbl.item(select_row)["values"]

    where = " prs_id= '" + Id.get() + "' "
    col = "  prs_name='" + Name.get() + "',prs_family='" + Family.get() + "' , prs_age='" + Age.get() + "' "
    result = repository.Update("personel", col, where)
    if result:
        Load()
        btnEdit.place_forget()
        ListItem = [Name, Family, Age, Id]
        cleare(ListItem)


        messagebox.showinfo("انجام شد", "ویرایش انجام شد")
    else:
        messagebox.showerror("   خطا", "  انجام نشد")


def OnClickShowSearch():
    frmSearch.place(x=0, y=0)


def OnclickCloseSearch():
    frmSearch.place_forget()


def GetValue():
    counter = []
    for item in range(1, 130):
        counter.append(item)

    return counter


def prt(self):
    print("click shod")
    # end def


bgSearch = PhotoImage(file="img/backCard.png")
iconClose = PhotoImage(file="img/close.png")

lblName = Label(screen, text="نام").place(x=500, y=40)
lblFamily = Label(screen, text="نام خانوادکی").place(x=500, y=80)
lblage = Label(screen, text="سن").place(x=500, y=120)

# var ha

Name = StringVar()
Family = StringVar()
Age = StringVar()
Id = StringVar()

# input

txtName = Entry(screen, textvariable=Name, justify="right")
txtName.place(x=350, y=40)
txtFamily = Entry(screen, textvariable=Family, justify="right")
txtFamily.place(x=350, y=80)
txtId = Entry(screen, textvariable=Id, justify="right")
txtId.place_forget()

comobText = ttk.Combobox(screen, state="readonly", textvariable=Age, justify="right")
valuesCombo = GetValue()
comobText["value"] = valuesCombo
comobText.current(23)
comobText.place(x=350, y=120)

# frame

frmSearch = Frame(screen, width=300, height=400, background="black")
frmSearch.place(x=0, y=0)
frmSearch.place_forget()

# btns

btnRegester = Button(screen, text="ثبت نام", command=OnCkickRegister).place(x=350, y=160)
btnDelet = Button(screen, text="حذف", bg="red", fg="white", command=OnclickDelet)
btnDelet.place_forget()
btnEdit = Button(screen, text="ویرایش", bg="#00ff37", fg="#000000", command=OnclickEdit)
btnEdit.pack_forget()
btnSearchShow = Button(screen, text="نمایش جستجو", command=OnClickShowSearch).place(x=350, y=190)

cols = ("c1", "c2", "c3", "c4")
tbl = ttk.Treeview(screen, columns=cols, show="headings", height=50)

tbl.column("# 4", anchor=E, width=50)
tbl.heading("# 4", text="شماره سطر")

tbl.column("# 3", anchor=E, width=50)
tbl.heading("# 3", text="نام")

tbl.column("# 2", width=50)
tbl.heading("# 2", text="نام خانوادگی")

tbl.column("# 1", width=100)
tbl.heading("# 1", text="سن")
tbl.bind("<Button-1>", GetSelction)

tbl.place(x=300, y=220)
lblBg = Label(frmSearch, text="*", image=bgSearch).place(x=0, y=0)
lblsarch = Label(frmSearch, text="مقدار جستجو").place(x=140, y=10)
txtSearch = Entry(frmSearch)
txtSearch.place(x=10, y=10)
btnSearch = Button(frmSearch, text="جستجو کن", command=OnclickSearch).place(x=40, y=40)
btnClose = Button(frmSearch, text="*", command=OnclickCloseSearch, image=iconClose, bg="white").place(x=250,
                                                                                                      y=0)

menobar = Menu(screen)

userMeno = Menu(menobar, tearoff=0)

userMeno.add_command(label="افزودن کاربر", command=prt)
userMeno.add_command(label="نمایش کاربران  ", command=prt)

menobar.add_cascade(label="کابران", menu=userMeno)

SettingMnu = Menu(menobar, tearoff=0)
SettingMnu.add_command(label="شهریه", command=prt)
SettingMnu.add_command(label="بدهی", command=prt)
SettingMnu.add_separator()
SettingMnu.add_command(label="خروج", command=prt, foreground="red")

menobar.add_cascade(label="تنظیمات", menu=SettingMnu)

screen.config(menu=menobar)

Load()
screen.mainloop()
