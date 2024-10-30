from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import backend
import subprocess


class main_window:
    def Deleteq(self):
        tablename = self.Quizing_Name.get()
        questionid = self.deletequestion_field.get()
        backend.Delete_question(questionid, tablename)
        
        self.CreateQuiz_Frame.destroy()
        self.CreateQuiz_Frame1.destroy()
        self.Create_Quiz_Set1()
    def Create_Quiz_Set1(self):
        self.Create_Quiz_Frame.destroy()
        self.CreateQuiz_Frame = Frame(self.Recent_Quiz, height=70, width=1000, bd=2, bg="lightblue")
        self.CreateQuiz_Frame.pack()

        self.Quizing_Name = Entry(self.CreateQuiz_Frame, font=("arial", 15), bg="lightblue")
        self.Quizing_Name.place(x=20, y=20)
        self.Quizing_Name.insert(0, self.id)
        self.deletequestion_field = Entry(self.CreateQuiz_Frame, font=("arial", 15), bg="white")
        self.deletequestion_field.place(y = 20, x = 250)
        self.deletequestion_field.insert(0, "Enter Question Id")
        self.cancel1 = Button(self.CreateQuiz_Frame, text="Cancel", width=6, font=("arial", 12), bg="red",
                              fg="white", command=self.Cancel_QuizFrame)
        self.cancel1.place(y=20, x=910)

        self.Refresh = Button(self.CreateQuiz_Frame, text="Delete", width=6, font=("arial", 12), bg="tomato", command=self.Deleteq)
        self.Refresh.place(y=20, x=820)
        self.Add_Quiz = Button(self.CreateQuiz_Frame, text="Add Quiz", width=10, font=("arial", 12), bg="green",
                               fg="white", command=self.Createquitions)
        self.Add_Quiz.place(y=20, x=710)

        self.CreateQuiz_Frame1 = Frame(self.Recent_Quiz, height=500, width=1000, bg="yellow")
        self.CreateQuiz_Frame1.pack(fill=BOTH)

        self.my_canvas = Canvas(self.CreateQuiz_Frame1, height=530)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = ttk.Scrollbar(self.CreateQuiz_Frame1, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>',
                            lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        self.s_frame = Frame(self.my_canvas)

        self.my_canvas.create_window((0, 0), window=self.s_frame, anchor=NW)

        datas = backend.GetQuistions(self.Quizing_Name.get())
        j = 1
        print(datas)
        for data in datas:
            f = Frame(self.s_frame, height=200, width=950, relief=GROOVE, bd=5)
            f.pack(pady=5)
            f.propagate(0)
            questionid = Label(f, text=f"{data[0]}")
            questionid.place(x = 800, y = 0)
            t = data[1].split(":")
            text = ""
            for i in t:
                text += i + " "
            l = Label(f, text=f"{j} . {text}", font=("arial", 15))
            l.place(x=5, y=0)
            op1 = Label(f, text=f"A). {data[2]}", font=("arial", 15))
            op1.place(x=50, y=60)
            op2 = Label(f, text=f"B). {data[3]}", font=("arial", 15))
            op2.place(x=250, y=60)
            op3 = Label(f, text=f"C). {data[4]}", font=("arial", 15))
            op3.place(x=450, y=60)
            op4 = Label(f, text=f"D). {data[5]}", font=("arial", 15))
            op4.place(x=650, y=60)
            answer = Label(f, text=f"Answer : {data[6]}", font=("arial", 15), fg="green")
            answer.place(x=50, y=100)
            j += 1
    def Create_Quiz_Set(self):
        self.id = self.Quiz_Set_Id.get()
        print(self.id)
        if self.id != "":
            datas = backend.SelectAll_Tables()
            d = []
            for data in datas:
                d.append(str(data[0]))
            print(d)
            if self.id in d:
                self.Create_Quiz_Set1()
            else:
                messagebox.showinfo("Warning", "Question is not exists. If you want to create click Create")


    def Addquition(self):
        quition = self.Type_Quitions_Entry.get()
        quition = quition.split(" ")
        quiz = ""
        for i in quition:
            quiz = quiz + i + ":"

        option1 = self.Options1.get()
        option2 = self.Options2.get()
        option3 = self.Options3.get()
        option4 = self.Options4.get()
        answer = self.Answer_Field.get()
        tablename = self.Quizing_Name.get()

        if quition != "" and option1 != "" and option2 != "" and option3 != "" and option4 != "" and answer != "":
            backend.InsertValue(quiz, option1, option2, option3, option4, answer, tablename)
            f = Frame(self.s_frame, height=200, width=950, relief=GROOVE, bd=5)
            f.pack(pady=5)
            f.propagate(0)
            datas = backend.GetQuistions(tablename)
            data = datas[0][0]
            texts = quiz.split(":")
            text = ""
            for t in texts:
                text += t + " "
            questionid = Label(f, text=f"{data}")
            questionid.place(x=800, y=0)
            l = Label(f, text=f"1 . {text}", font=("arial", 15))
            l.place(x=5, y=0)
            op1 = Label(f, text=f"A). {option1}", font=("arial", 15))
            op1.place(x=50, y=60)
            op2 = Label(f, text=f"B). {option2}", font=("arial", 15))
            op2.place(x=250, y=60)
            op3 = Label(f, text=f"C). {option3}", font=("arial", 15))
            op3.place(x=450, y=60)
            op4 = Label(f, text=f"D). {option4}", font=("arial", 15))
            op4.place(x=650, y=60)
            answer = Label(f, text=f"Answer : {answer}", font=("arial", 15), fg="green")
            answer.place(x=50, y=100)
            self.Adquestion_Destroy()
        else:
            messagebox.showwarning("Error", "Please enter all field.")
    def Createquitions(self):
        self.Add_quitions_frame = Frame(self.CreateQuiz_Frame, height=160, width=1000, relief=GROOVE, bd=2, bg="lightgreen")
        self.Add_quitions_frame.pack()
        self.Type_Quitions_Label = Label(self.Add_quitions_frame, text="Type Question :", font=("arial", 15), bg="lightgreen")
        self.Type_Quitions_Label.place(x = 10, y = 10)
        self.Type_Quitions_Entry = Entry(self.Add_quitions_frame, font=("arial", 15), width=70)
        self.Type_Quitions_Entry.place(x = 200, y = 10)
        self.Options_Label = Label(self.Add_quitions_frame, font=("arial", 15), text="Options :", bg="lightgreen")
        self.Options_Label.place(x = 10, y = 60)
        self.Options1 = Entry(self.Add_quitions_frame, font=("arial", 15), width=10)
        self.Options1.place(x = 200, y = 60)
        self.Options2 = Entry(self.Add_quitions_frame, font=("arial", 15), width=10)
        self.Options2.place(x=320, y=60)
        self.Options3 = Entry(self.Add_quitions_frame, font=("arial", 15), width=10)
        self.Options3.place(x=440, y=60)
        self.Options4 = Entry(self.Add_quitions_frame, font=("arial", 15), width=10)
        self.Options4.place(x=560, y=60)
        self.Answer_Label = Label(self.Add_quitions_frame, font=("arial", 15), text="Answer :", bg="lightgreen")
        self.Answer_Label.place(x = 10, y = 110)
        self.Answer_Field = Entry(self.Add_quitions_frame, font=("arial", 15))
        self.Answer_Field.place(x = 200, y = 110)

        self.Add_Quitionbtn = Button(self.Add_quitions_frame, text="Add Quiz", width=10, font=("arial", 12), bg="green", fg="white", command=self.Addquition)
        self.Add_Quitionbtn.place(x = 700, y = 110)
        self.Cancel_Quitionbtn = Button(self.Add_quitions_frame, text="Cancel", width=10, font=("arial", 12), bg="red",
                                     fg="white", command=self.Adquestion_Destroy)
        self.Cancel_Quitionbtn.place(x=850, y=110)

    def Adquestion_Destroy(self):
        self.Add_quitions_frame.destroy()
        self.CreateQuiz_Frame.configure(height=70)



    def Cancel_QuizFrame(self):
        self.CreateQuiz_Frame.destroy()
        self.CreateQuiz_Frame1.destroy()
        self.ReRecent_Quize()
        self.Create_Quizbtn = Button(self.Toolbar, text="Create Quiz", font=("airla", 15), command=self.Create_Quiz)
        self.Create_Quizbtn.place(x=850, y=13)
    def Cancel_QuizFrame1(self):
        self.Create_Quiz_Frame.destroy()
        self.ReRecent_Quize()
        self.Create_Quizbtn = Button(self.Toolbar, text="Create Quiz", font=("airla", 15), command=self.Create_Quiz)
        self.Create_Quizbtn.place(x=850, y=13)
    def Create_Quiz(self):
        self.Recent_Quiz1.destroy()
        self.Create_Quizbtn.destroy()
        self.Create_Quiz_Frame = Frame(self.Recent_Quiz, height=150, width=1000, relief=GROOVE, bd=2)
        self.Create_Quiz_Frame.pack()
        self.Quiz_Id = Label(self.Create_Quiz_Frame, text="Quiz Set Name: ", font=("arial", 15))
        self.Quiz_Id.place(x = 10, y = 10)
        self.Quiz_Set_Id = Entry(self.Create_Quiz_Frame, font=("arial", 15))
        self.Quiz_Set_Id.place(x = 160, y = 10)


        self.Create_Setbtn = Button(self.Create_Quiz_Frame, text="Create", font=("arial", 15), bg="green", fg="white", command=self.Create_Quiz_Set2)
        self.Create_Setbtn.place(x = 800, y = 100)
        self.Cancel_Setbtn = Button(self.Create_Quiz_Frame, text="Cancel", font=("arial", 15), bg="red", fg="white", command=self.Cancel_QuizFrame1)
        self.Cancel_Setbtn.place(x=900, y=100)

    def Create_Quiz_Set2(self):
        if self.Quiz_Set_Id.get() != "":
            backend.Create_Quiz_Set(self.Quiz_Set_Id.get())
            self.Create_Quiz_Set()
        else:
            messagebox.showwarning("Error", "Please enter Question name.")
    def DeleteQuistion(self):
        data = self.textentry.get()
        if data != "":
            backend.DeleteTable(data)
        else:
            messagebox.showwarning("Error", "Please enter question name")
    def ReRun(self):
        self.Result_Frame.destroy()
        self.CreateMain_Window()

    def Your_Result(self, result, text, q):
        self.Test_Frame.destroy()
        self.Result_Frame = Frame(self.window, height=400, width=800, bd=2, relief=GROOVE)
        self.Result_Frame.pack(pady=50)
        self.Result_Frame.propagate(0)
        self.test_name = Label(self.Result_Frame, text=text, font=("arial", 17))
        self.test_name.pack(pady=10)
        self.result_label = Label(self.Result_Frame, text=f"Your Result : {result}/{q}", font=("arial", 17))
        self.result_label.pack(pady=10)
        percentage = (result/q)*100
        self.percentage_label = Label(self.Result_Frame, text=f"Your Percentage : {percentage}", font=("arial", 17))
        self.percentage_label.pack(pady=10)
        if(percentage <= 59):
            self.percentage_label.configure(fg="red")
        else:
            self.percentage_label.configure(fg="green")
        self.Ok_Button = Button(self.Result_Frame, text="Exit",width=20, font=("arial", 15), command=self.ReRun)
        self.Ok_Button.pack(pady=10)

    def Test_Result(self):
        tablename1 = self.Testname.cget("text")
        tablename2 = tablename1.split(":")
        tablename3 = tablename2[1].split(" ")
        data = backend.GetQuistions(tablename3[1])
        self.Answer_Set = []
        self.Result = 0
        for i in range(1, len(data)+1):
            v = f"answer{i}"
            self.Answer_Set.append(vars(self)[v].get())

        for k in range(0, len(data)):
            print(self.Answer_Set[k],"==",data[k][6])
            if self.Answer_Set[k] == data[k][6]:
                self.Result += 1
            else:
                self.Result += 0
        self.Your_Result(self.Result, tablename1, len(data))
    def PlayQuition(self):
        d = self.textentry.get()
        if d != "":
            datas = backend.GetQuistions(d)
            self.Toolbar.destroy()
            self.Recent_Quiz.destroy()
            self.Test_Frame = Frame(self.window, bg="lightpink", height=700)
            self.Test_Frame.pack(fill=BOTH)
            self.min = 0
            self.sec = 0
            def runtime():
                self.time = f"{self.min}:{self.sec}"
                self.Testtime.configure(text = f"Time : {self.time}")
                if(self.sec==60):
                    self.min += 1
                    self.sec = 0
                else:
                    self.sec += 1

                self.Testtime.after(1000, runtime)
            self.Testtime = Label(self.Test_Frame, text="Time : ", font=("arial", 20), bg="lightpink")
            self.Testtime.pack()
            self.Testname = Label(self.Test_Frame, text=f"Test Name : {d}", font=("arial", 20), bg="lightpink")
            self.Testname.place(x = 20, y = 0)
            self.Test_Frame1 = Frame(self.Test_Frame, height=600)
            self.Test_Frame1.pack(fill=BOTH)
            self.Test_Canvas = Canvas(self.Test_Frame1, height=600, width=950, bg="white")
            self.Test_Canvas.pack(side=LEFT, expand=1, pady=20)

            self.my_scrollbar2 = ttk.Scrollbar(self.Test_Frame1, orient=VERTICAL, command=self.Test_Canvas.yview)
            self.my_scrollbar2.pack(side=RIGHT, fill=Y)

            self.Test_Canvas.configure(yscrollcommand=self.my_scrollbar2.set)
            self.Test_Canvas.bind('<Configure>',
                             lambda e: self.Test_Canvas.configure(scrollregion=self.Test_Canvas.bbox("all")))

            self.s_frame2 = Frame(self.Test_Canvas, bg="white")

            self.Test_Canvas.create_window((0, 0), window=self.s_frame2, anchor=NW)

            j = 1

            for data in datas:
                f = Frame(self.s_frame2, height=200, width=950, relief=GROOVE, bd=5)
                f.pack(pady=5)
                f.propagate(0)
                t = data[1].split(":")
                text = ""
                for i in t:
                    text += i + " "

                l = Label(f, text=f"{j} . {text}", font=("arial", 15))
                l.place(x=5, y=0)
                op1 = Label(f, text=f"A. {data[2]}", font=("arial", 15), height=1, width=10)
                op1.place(x=50, y=60)
                op2 = Label(f, text=f"B. {data[3]}", font=("arial", 15), height=1, width=10)
                op2.place(x=250, y=60)
                op3 = Label(f, text=f"C. {data[4]}", font=("arial", 15), height=1, width=10)
                op3.place(x=450, y=60)
                op4 = Label(f, text=f"D. {data[5]}", font=("arial", 15), height=1, width=10)
                op4.place(x=650, y=60)
                v = f"answer{j}"
                label = Label(f, text="Answer : ", font=("arial", 15))
                label.place(x = 50, y = 120)
                vars(self)[v] = Entry(f, font=("arial", 15))
                vars(self)[v].place(x = 150, y = 120)

                j += 1

            self.Submit_Test = Button(self.s_frame2, text="Submit",width=50, bg="lightgreen", font=("arial", 15), command= self.Test_Result)
            self.Submit_Test.pack(pady=30)


            runtime()
        else:
            messagebox.showwarning("Error", "Please enter Question name.")

    def EditQuition(self):
        string = self.textentry.get()
        if string != "":
            self.Create_Quizbtn.invoke()
            self.Quiz_Set_Id.insert(0,string)
            self.Create_Quiz_Set()
        else:
            messagebox.showwarning("Error", "Please enter Question name.")
    def ReRecent_Quize(self):
        self.Recent_Quiz1 = Frame(self.Recent_Quiz, height=630, width=1000, relief=GROOVE, bg="lightgreen")
        self.Recent_Quiz1.pack()
        self.Recent_Quiz1.propagate(0)
        self.my_canvas1 = Canvas(self.Recent_Quiz1, height=680, width=950, bg="white")
        self.my_canvas1.pack(side=LEFT, expand=1, pady=50)

        self.my_scrollbar1 = ttk.Scrollbar(self.Recent_Quiz1, orient=VERTICAL, command=self.my_canvas1.yview)
        self.my_scrollbar1.pack(side=RIGHT, fill=Y)

        self.my_canvas1.configure(yscrollcommand=self.my_scrollbar1.set)
        self.my_canvas1.bind('<Configure>',
                             lambda e: self.my_canvas1.configure(scrollregion=self.my_canvas1.bbox("all")))

        self.s_frame1 = Frame(self.my_canvas1, bg="white")

        self.my_canvas1.create_window((0, 0), window=self.s_frame1, anchor=NW)
        self.Recent_Quiz.pack_propagate(0)
        datas = backend.SelectAll_Tables()
        self.textentry = Entry(self.Recent_Quiz1, font=("arial", 15), width=50)
        self.textentry.place(x = 10, y = 10)
        self.playbtn = Button(self.Recent_Quiz1, text="Test", font=("arial", 11), width=10, bg="lightpink",command = self.PlayQuition)
        self.playbtn.place(x=650, y=10)
        self.editbtn = Button(self.Recent_Quiz1, text="Edit", font=("arial", 11), width=10, bg="lightblue", command= self.EditQuition)
        self.editbtn.place(x = 760, y = 10)
        self.deletebtn = Button(self.Recent_Quiz1, text="Delete", font=("arial", 11), width=10, bg="tomato",
                                command=self.DeleteQuistion)
        self.deletebtn.place(x=870, y=10)
        for data in datas:
            self.frame = Frame(self.s_frame1, height=50, width=950, bg="lightblue", relief=GROOVE, bd=2)
            self.frame.pack(pady=10)
            self.label = Label(self.frame, bg="lightblue",text=f"{data[0]}", font=("arial", 15))
            self.label.place(x=30, y=10)

    def open_puzzle(self):
        subprocess.Popen(['python', 'Puzzle.py'])
    
    def notes(self):
        subprocess.Popen(['python', 'notes.py'])	

    def __init__(self, window):

        self.window = window
        self.window.title("PuzzlED")
        self.CreateMain_Window()
        self.window.mainloop()

    def CreateMain_Window(self):
        self.Toolbar = Frame(self.window, height=70, width=1000, relief=GROOVE, bd=2, bg="lightgreen")
        self.Toolbar.pack()
        self.Title = Label(self.Toolbar, text="PuzzlED", font=("arial", 22), bg="lightgreen")
        self.Title.place(x=20, y=13)
        self.Create_Quizbtn = Button(self.Toolbar, text="Create Quiz", font=("airla", 15), command=self.Create_Quiz)
        self.Create_Quizbtn.place(x=850, y=13)
        self.puzzle_button = Button(self.Toolbar, text="Puzzle", font=("airla", 15), command=self.open_puzzle)
        self.puzzle_button.place(x=760, y=13)
        self.notes_button = Button(self.Toolbar, text="Notes", font=("airla", 15), command=self.notes)
        self.notes_button.place(x=670, y=13)
        self.Recent_Quiz = Frame(self.window, height=630, width=1000, relief=GROOVE, bd=2, bg="white")
        self.Recent_Quiz.pack()

        self.ReRecent_Quize()


window = Tk()
window.geometry("1000x700")
window.resizable(False, False)
main_window(window)
