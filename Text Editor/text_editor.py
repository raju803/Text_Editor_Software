from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font
class text_editor:
    current_open_file = "no_file"
    def open_file(self, event=""):
        #print("Openning File")
        open_return = filedialog.askopenfile(initialdir="/", title="select file to open", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if(open_return !=None):
            self.text_area.delete(1.0, END)
            for line in open_return:
                 self.text_area.insert(END,line)
            self.current_open_file =open_return.name
            open_return.close()

    def save_as_file(self, event=""):
        f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        text2save = self.text_area.get(1.0, END)
        self.current_open_file = f.name
        f.write(text2save)
        f.close()

    def save_file(self, event=""):
        if self.current_open_file =="no_file":
            self.save_as_file()
        else:
            f =open(self.current_open_file,"w+")
            f.write(self.text_area.get(1.0,END))
            f.close()

    def custom_quit(self):
        answer =messagebox.askokcancel("Are you Sure ?","Are you sure want to exit this page Your data will be lost and you will come on road")
        if(answer):
            print("Exit")
            quit()



    def res(self):
        print("Resize")
        root.geometry("500x500")



    def nor(self):
        print("Normal")
        root.geometry("")

    def new_file(self, event=""):
        self.text_area.delete(1.0,END)
        self.current_open_file =="no_file"

    def copy_text(self, event=""):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_text(self, event=""):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")

    def paste_text(self, event=""):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())
        
        
        
        

        
        
        


    def __init__(self,master):
        self.scroll=Scrollbar()
        self.scroll.pack(side=RIGHT, fill=Y)
        self.master=Font(family="Times New Roman", size=20, weight="bold", slant="italic")
        self.master = master  #5
        master.title("textpad") #1
        self.text_area =Text(self.master,undo=True,height=30,wrap=WORD,padx=10,pady=10, selectbackground="gray", yscrollcommand=self.scroll.set)  #2
        self.text_area.configure(font=master)
        
        self.text_area.pack(fill=BOTH,expand=1) #3
        self.scroll.config(command=self.text_area.yview)
        

        self.main_menu = Menu()  #4
        self.master.config(menu=self.main_menu)

        # creating file menu
        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New Page          Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="Open                  Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Save                   Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save as....", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Page Setup")
        self.file_menu.add_command(label="Print........         Ctrl+P")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit" , command=self.custom_quit)

        # Binding Working
        root.bind('<Control-n>',self.new_file)
        root.bind('<Control-o>',self.open_file)
        root.bind('<Control-s>',self.save_file)
        root.bind('<Control-Shift-s>',self.save_as_file)
        root.bind('<Control-p>')
        root.bind('<Control-c>')
        root.bind('<Control-x>')
        root.bind('<Control-v>')
        root.bind('<Control-z>')


         # creating Edit menu
        self.edit_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo          Ctrl+Z",command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut           Ctrl+X", command=self.cut_text)
        self.edit_menu.add_command(label="Copy          Ctrl+C", command=self.copy_text)
        self.edit_menu.add_command(label="Past          Ctrl+V", command=self.paste_text)
        self.edit_menu.add_command(label="Delete        Del")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Search with Bing      Ctrl+E ")
        self.edit_menu.add_command(label="Resize Window", command=self.res)
        self.edit_menu.add_command(label="NormalSize Window", command=self.nor)
        
        # creating Formate menu
        self.formate_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Formate", menu=self.formate_menu)
        self.formate_menu.add_command(label="Word Wrap")
        self.formate_menu.add_command(label="Font.......")

        # creating Code menu
        self.code_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Code", menu=self.code_menu)

        # creating Run menu
        self.run_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Run", menu=self.run_menu)
        

        # creating View menu
        self.view_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Zoom")
        self.view_menu.add_command(label="Status Bar")
        

        # creating Help menu
        self.help_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="View Help")
        self.help_menu.add_command(label="About Notepad")
        
        

        # Starus Bar 
        status = Label(root,text="Running.......\t\t\t Window(Ctrl)\t\t\t\t\t 100%", relief=SUNKEN, anchor=W, bd=1)
        status.pack(side=BOTTOM, fill=X)




root = Tk()
root.iconbitmap(r'C:\\Users\\user\\Downloads\\ico.ico')
te = text_editor(root)
#root.geometry("600x600")
root.mainloop()
