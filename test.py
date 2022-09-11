import tkinter
import tkinter as tk


class Aplikacja:
    user = True

    punktyGracz1 = 0
    punktyGracz2 = 0

    def __init__(self, okno):

        self.b1 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b1"),width=10, height=5)
        self.b1.grid(row=0,column=0)

        self.b2 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b2"), width=10, height=5)
        self.b2.grid(row=0, column=1)

        self.b3 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b3"), width=10, height=5)
        self.b3.grid(row=0, column=2)

        self.b4= tk.Button(okno, text="", command=lambda: self.zmien_tekst("b4"), width=10, height=5)
        self.b4.grid(row=1, column=0)

        self.b5 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b5"), width=10, height=5)
        self.b5.grid(row=1, column=1)

        self.b6 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b6"), width=10, height=5)
        self.b6.grid(row=1, column=2)

        self.b7 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b7"), width=10, height=5)
        self.b7.grid(row=2, column=0)

        self.b8 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b8"), width=10, height=5)
        self.b8.grid(row=2, column=1)

        self.b9 = tk.Button(okno, text="", command=lambda: self.zmien_tekst("b9"), width=10, height=5)
        self.b9.grid(row=2, column=2)

        self.b10 = tk.Button(okno, text="Restart", command=lambda: self.restart(), width=10, height=5)
        self.b10['bg'] = "yellow"
        self.b10.grid(row=2, column=4)

        self.b10 = tk.Button(okno, text="Wyczyść", command=lambda: self.wyczysc(), width=10, height=5)
        self.b10['bg'] = "blue"
        self.b10.grid(row=2, column=5)

        self.label1 = tkinter.Label(okno, text="Wygrywa:", font=10)
        self.label1.grid(row=3,column=0)

        self.label0 = tkinter.Label(okno, text="Gracz O: 0", font=10)
        self.label0.grid(row=4,column=0)

        self.label2 = tkinter.Label(okno, text="Gracz X: 0", font=10)
        self.label2.grid(row=5, column=0)

        self.label3 = tkinter.Label(okno, text="Tura dla: O",font=10)
        self.label3.grid(row=1, column=5)



    def wyczysc(self):
        self.reset()




    def restart(self):
        self.reset()
        Aplikacja.punktyGracz1 = 0
        Aplikacja.punktyGracz2 = 0

        self.label0.config(text=f"Gracz O: {Aplikacja.punktyGracz1}")
        self.label2.config(text=f"Gracz X: {Aplikacja.punktyGracz2}")

        self.label3.config(text=f"Tura dla: O")

    def reset(self):

        self.b1['text'] = ""
        self.b1['bg'] = "SystemButtonFace"
        self.b2['text'] = ""
        self.b2['bg'] = "SystemButtonFace"
        self.b3['text'] = ""
        self.b3['bg'] = "SystemButtonFace"
        self.b4['text'] = ""
        self.b4['bg'] = "SystemButtonFace"
        self.b5['text'] = ""
        self.b5['bg'] = "SystemButtonFace"
        self.b6['text'] = ""
        self.b6['bg'] = "SystemButtonFace"
        self.b7['text'] = ""
        self.b7['bg'] = "SystemButtonFace"
        self.b8['text'] = ""
        self.b8['bg'] = "SystemButtonFace"
        self.b9['text'] = ""
        self.b9['bg'] = "SystemButtonFace"


        if Aplikacja.user:
            self.label3.config(text=f"Tura dla: O")
        else:
            self.label3.config(text=f"Tura dla: X")





    def zmien_tekst(self,wybor):
        if wybor=="b1":
            if Aplikacja.user:
                self.b1['text'] = "O"
                self.b1['bg'] = "red"
                Aplikacja.user = False
            else:
                self.b1['text'] = "X"
                self.b1['bg'] = "green"
                Aplikacja.user = True

        elif wybor=="b2":
            if Aplikacja.user:
                self.b2['text'] = "O"
                self.b2['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b2['text'] = "X"
                self.b2['bg'] = "green"
                Aplikacja.user = True

        elif wybor=="b3":
            if Aplikacja.user:
                self.b3['text'] = "O"
                self.b3['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b3['text'] = "X"
                self.b3['bg'] = "green"
                Aplikacja.user = True


        elif wybor=="b4":
            if Aplikacja.user:
                self.b4['text'] = "O"
                self.b4['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b4['text'] = "X"
                self.b4['bg'] = "green"
                Aplikacja.user = True
        elif wybor=="b5":
            if Aplikacja.user:
                self.b5['text'] = "O"
                self.b5['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b5['text'] = "X"
                self.b5['bg'] = "green"
                Aplikacja.user = True

        elif wybor=="b6":
            if Aplikacja.user:
                self.b6['text'] = "O"
                self.b6['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b6['text'] = "X"
                self.b6['bg'] = "green"
                Aplikacja.user = True


        elif wybor=="b7":
            if Aplikacja.user:
                self.b7['text'] = "O"
                self.b7['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b7['text'] = "X"
                self.b7['bg'] = "green"
                Aplikacja.user = True


        elif wybor=="b8":
            if Aplikacja.user:
                self.b8['text'] = "O"
                self.b8['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b8['text'] = "X"
                self.b8['bg'] = "green"
                Aplikacja.user = True


        elif wybor=="b9":
            if Aplikacja.user:
                self.b9['text'] = "O"
                self.b9['bg'] = "red"
                Aplikacja.user=False
            else:
                self.b9['text'] = "X"
                self.b9['bg'] = "green"
                Aplikacja.user = True



        if(self.b1.cget('text') == "O" and self.b2.cget('text') == "O" and self.b3.cget('text')=="O"):

            Aplikacja.punktyGracz1+=1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b1.cget('text') == "X" and self.b2.cget('text') == "X" and self.b3.cget('text') == "X"):

            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()

        if(self.b4.cget('text') == "O" and self.b5.cget('text') == "O" and self.b6.cget('text')=="O"):
            Aplikacja.punktyGracz1+=1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b4.cget('text') == "X" and self.b5.cget('text') == "X" and self.b6.cget('text') == "X"):
            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()

        if(self.b7.cget('text') == "O" and self.b8.cget('text') == "O" and self.b9.cget('text')=="O"):
            Aplikacja.punktyGracz1+=1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b7.cget('text') == "X" and self.b8.cget('text') == "X" and self.b9.cget('text') == "X"):
            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()

        if(self.b1.cget('text') == "O" and self.b4.cget('text') == "O" and self.b7.cget('text')=="O"):
            Aplikacja.punktyGracz1+=1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b1.cget('text') == "X" and self.b4.cget('text') == "X" and self.b7.cget('text') == "X"):
            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()


        if(self.b2.cget('text') == "O" and self.b5.cget('text') == "O" and self.b8.cget('text')=="O"):
            Aplikacja.punktyGracz1+=1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b2.cget('text') == "X" and self.b5.cget('text') == "X" and self.b8.cget('text') == "X"):
            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()



        if(self.b3.cget('text') == "O" and self.b6.cget('text') == "O" and self.b9.cget('text')=="O"):
            Aplikacja.punktyGracz1+=1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b3.cget('text') == "X" and self.b6.cget('text') == "X" and self.b9.cget('text') == "X"):
            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()


        if(self.b1.cget('text') == "O" and self.b5.cget('text') == "O" and self.b9.cget('text')=="O"):
            Aplikacja.punktyGracz1+=1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b1.cget('text') == "X" and self.b5.cget('text') == "X" and self.b9.cget('text') == "X"):
            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()

        if (self.b3.cget('text') == "O" and self.b5.cget('text') == "O" and self.b7.cget('text') == "O"):
            Aplikacja.punktyGracz1 += 1
            self.label0.config(text=f"Gracz O:{Aplikacja.punktyGracz1}")
            self.reset()

        if (self.b3.cget('text') == "X" and self.b5.cget('text') == "X" and self.b7.cget('text') == "X"):
            Aplikacja.punktyGracz2 += 1
            self.label2.config(text=f"Gracz X:{Aplikacja.punktyGracz2}")
            self.reset()




okno = tk.Tk()
okno.title("Kółko i krzyżyk")
okno.geometry("576x400")
okno.resizable(False, False)
app = Aplikacja(okno)
okno.mainloop()