from tkinter import *
window = Tk()
window.geometry("395x541")
window.resizable(0,0)
window.title(" Scientific Calculator")

def btn_click(item):
    global expression
    expression = expression+str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
expression = ""
input_text = StringVar()

input_frame = Frame(window, width = 312, height = 50, bd = 0,highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial',18,'bold'),
                   textvariable = input_text,width = 50, bg = "#eee",bd = 0, justify = LEFT)
input_field.pack(ipady = 10)#ipady is internal padding
btns_frame = Frame(window,width = 480,height = 272.5,bg = 'black')
btns_frame.pack()

#first row

sqroot = Button(btns_frame,text = "√",fg = "black",width = 10,height=3,bd = 0,
               bg = "#eee",cursor = "hand2",command = lambda:
               btn_click("√")).grid(row = 0, column = 0,padx = 1,pady = 1)
bracketO = Button(btns_frame,text = "(",fg = "black",width = 10,height=3,bd = 0,
               bg = "#eee",cursor = "hand2",command = lambda:
               btn_click("(")).grid(row = 0, column = 1,padx = 1,pady = 1)

bracketC = Button(btns_frame,text = ")",fg = "black",width = 10,height=3,bd = 0,
               bg = "#eee",cursor = "hand2",command = lambda:
               btn_click(")")).grid(row = 0, column = 2,padx = 1,pady = 1)
cbroot = Button(btns_frame,text = "∛",fg = "black",width = 10,height=3,bd = 0,
               bg = "#eee",cursor = "hand2",command = lambda:
               btn_click("∛")).grid(row = 0, column = 3,padx = 1,pady = 1)

clear = Button(btns_frame,text = "C",fg = "black",width = 10,height=3,bd = 0,
               bg = "#fff",cursor = "hand2",command = lambda:
               btn_clear()).grid(row = 0,column = 4, padx = 1, pady = 1)

#second row

e = Button(btns_frame,text = "e",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("e")).grid(row = 2, column = 0,padx = 1,pady = 1)
sinh =Button(btns_frame,text = "sinh",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("sinh")).grid(row = 2, column = 1,padx = 1,pady = 1)
cosh = Button(btns_frame,text = "cosh",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("cosh")).grid(row = 2, column = 2,padx = 1,pady = 1)
tanh = Button(btns_frame,text = "tanh",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("tanh")).grid(row = 2, column = 3,padx = 1,pady = 1)
exp = Button(btns_frame,text = "exp",fg = "black",width = 10,height=3,bd = 0,
               bg = "#eee",cursor = "hand2",command = lambda:
               btn_("exp")).grid(row = 2,column = 4, padx = 1, pady = 1)


#third row

pi = Button(btns_frame,text = "π",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("π")).grid(row = 3, column = 0,padx = 1,pady = 1)
sin= Button(btns_frame,text = "sin",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("sin")).grid(row = 3, column = 1,padx = 1,pady = 1)
cos = Button(btns_frame,text = "cos",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("cos")).grid(row = 3, column = 2,padx = 1,pady = 1)
tan = Button(btns_frame,text = "tan",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("tan")).grid(row = 3, column = 3,padx = 1,pady = 1)
divide = Button(btns_frame,text = "/",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("/")).grid(row = 3, column = 4,padx = 1,pady = 1)


#fourth row

x3 = Button(btns_frame,text = "x3",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("x3")).grid(row = 4, column = 0,padx = 1,pady = 1)
seven = Button(btns_frame,text = "7",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("7")).grid(row = 4, column = 1,padx = 1,pady = 1)
eight = Button(btns_frame,text = "8",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("8")).grid(row = 4, column = 2,padx = 1,pady = 1)
nine = Button(btns_frame,text = "9",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("9")).grid(row = 4, column = 3,padx = 1,pady = 1)
multiply = Button(btns_frame,text = "*",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("*")).grid(row = 4, column = 4,padx = 1,pady = 1)
#fifth row

x2 =  Button(btns_frame,text = "x2",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("x2")).grid(row = 5, column = 0,padx = 1,pady = 1)
fourth = Button(btns_frame,text = "4",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("4")).grid(row = 5, column = 1,padx = 1,pady = 1)
fifth = Button(btns_frame,text = "5",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("5")).grid(row = 5, column = 2,padx = 1,pady = 1)
sixth = Button(btns_frame, text = "6",fg = "black",width = 10,height=3,bd = 0,
               bg = "#fff",cursor = "hand2",command = lambda:
               btn_click("6")).grid(row = 5,column = 3, padx = 1, pady = 1)
minus = Button(btns_frame,text = "-",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("-")).grid(row = 5, column = 4,padx = 1,pady = 1)
#sixth row
log =  Button(btns_frame,text = "log",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("log")).grid(row = 6, column = 0,padx = 1,pady = 1)
one = Button(btns_frame,text = "1",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("1")).grid(row = 6, column = 1,padx = 1,pady = 1)
two = Button(btns_frame,text = "2",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("2")).grid(row = 6, column = 2,padx = 1,pady = 1)
three = Button(btns_frame, text = "3",fg = "black",width = 10,height=3,bd = 0,
               bg = "#fff",cursor = "hand2",command = lambda:
               btn_click("3")).grid(row = 6,column = 3, padx = 1, pady = 1)
plus = Button(btns_frame,text = "+",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("+")).grid(row = 6, column = 4,padx = 1,pady = 1)
#seventh row
ln =  Button(btns_frame,text = "ln",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("ln")).grid(row = 7, column = 0,padx = 1,pady = 1)
per = Button(btns_frame,text = "%",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("%")).grid(row = 7, column = 1,padx = 1,pady = 1)
zero = Button(btns_frame,text = "0",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#fff", cursor = "hand2", command = lambda:
              btn_click("0")).grid(row = 7, column = 2,padx = 1,pady = 1)
decimal = Button(btns_frame, text = ".",fg = "black",width = 10,height=3,bd = 0,
               bg = "#fff",cursor = "hand2",command = lambda:
               btn_click(".")).grid(row = 7,column = 3, padx = 1, pady = 1)
equal = Button(btns_frame,text = "=",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("=")).grid(row = 7, column = 4,padx = 1,pady = 1)
#eigth row
DEG =  Button(btns_frame,text = "DEG",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("DEG")).grid(row = 8, column = 0,padx = 1,pady = 1)
sininverse = Button(btns_frame,text = "sin-1",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("sin-1")).grid(row = 8, column = 1,padx = 1,pady = 1)
cosinverse = Button(btns_frame,text = "cos-1",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("cos-1")).grid(row = 8, column = 2,padx = 1,pady = 1)
taninverse = Button(btns_frame, text = "tan-1",fg = "black",width = 10,height=3,bd = 0,
               bg = "#eee",cursor = "hand2",command = lambda:
               btn_click("tan-1")).grid(row = 8,column = 3, padx = 1, pady = 1)
power = Button(btns_frame,text = "^",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("^")).grid(row = 8, column = 4,padx = 1,pady = 1)
#nine row
RAD =  Button(btns_frame,text = "RAD",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("RAD")).grid(row = 9, column = 0,padx = 1,pady = 1)
xinverse = Button(btns_frame,text = "x-1",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("x-1")).grid(row = 9, column = 1,padx = 1,pady = 1)
differentiate = Button(btns_frame,text = "f(x)",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("f(x)")).grid(row = 9, column = 2,padx = 1,pady = 1)
integrate = Button(btns_frame, text = " ∫ ",fg = "black",width = 10,height=3,bd = 0,
               bg = "#eee",cursor = "hand2",command = lambda:
               btn_click(" ∫ ")).grid(row = 9,column = 3, padx = 1, pady = 1)
denominator = Button(btns_frame,text = "1/x",fg = "black",width = 10,height = 3,bd = 0,
              bg = "#eee", cursor = "hand2", command = lambda:
              btn_click("1/x")).grid(row = 9, column = 4,padx = 1,pady = 1)





window.mainloop()
