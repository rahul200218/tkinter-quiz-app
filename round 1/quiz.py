import tkinter as tk
import random


global c
c=0

root = tk.Tk()
root.attributes('-fullscreen', True)


from tkinter import *
from PIL import Image, ImageTk



# open the image file and resize it to match the size of the root window
bg_image = Image.open("C:\\Users\\HP\\Downloads\\coding4.png").resize((root.winfo_screenwidth(), root.winfo_screenheight()))

# create a PhotoImage object from the resized image
bg_photo = ImageTk.PhotoImage(bg_image)

# set the image as the background of the root window
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


import keyboard
import sys


def on_key_press(event):
    global c
    print(event.name)
    if event.name == 'left windows' or event.name == 'right windows' or event.name=='esc':
        print("Windows key pressed! Terminating program.")
        c=1
        if c==1:
            root.destroy()
    elif event.name=='alt':
        c=1
        if c==1:
            root.destroy()

# Listen for key events in a separate thread
keyboard.on_press(on_key_press)




global points
points = 0

var1 = tk.StringVar(value=None)
var2 = tk.StringVar(value=None)
var3 = tk.StringVar(value=None)
var4 = tk.StringVar(value=None)
var5 = tk.StringVar(value=None)

var6 = tk.StringVar(value=None)
var7 = tk.StringVar(value=None)
var8 = tk.StringVar(value=None)
var9 = tk.StringVar(value=None)
var10 = tk.StringVar(value=None)

var11 = tk.StringVar(value=None)
var12 = tk.StringVar(value=None)
var13 = tk.StringVar(value=None)
var14 = tk.StringVar(value=None)
var15 = tk.StringVar(value=None)

var16 = tk.StringVar(value=None)
var17 = tk.StringVar(value=None)
var18 = tk.StringVar(value=None)
var19 = tk.StringVar(value=None)
var20 = tk.StringVar(value=None)

var21 = tk.StringVar(value=None)
var22 = tk.StringVar(value=None)
var23 = tk.StringVar(value=None)
var24 = tk.StringVar(value=None)
var25 = tk.StringVar(value=None)

var26 = tk.StringVar(value=None)
var27 = tk.StringVar(value=None)
var28 = tk.StringVar(value=None)
var29 = tk.StringVar(value=None)
var30 = tk.StringVar(value=None)



def welcome():
   


    def destroy_all_frames(root):
    # Get a list of all the child widgets of the root window
        children = root.winfo_children()

    # Recursively destroy each child widget that is a Frame
        for child in children:
            if isinstance(child, tk.Frame):
                child.destroy()
            else:
            # If the child widget is not a Frame, call this function recursively
                destroy_all_frames(child)

    destroy_all_frames(root)

    

    frame2 = tk.Frame(root,bg="black")
      
    frame2.pack()
    frame2.place(x=450,y=450)
    label11 = tk.Label(frame2, text="Hope you enjoyed the competition \U0001F607 \nYour team played well \U00002B50 \nthankyou \U00002764 \n Bye \U0001F44B",bg="black" ,font=("Arial", 19, "bold"),fg="white")
    label11.grid(row=0, column=0, padx=10, pady=10, sticky="W")


    

global frame1


def start():
    global b1
    b1.destroy()

    timer_label = tk.Label(root, text="3:00",  font=("Arial", 24), bd=2, relief="solid")
    timer_label.pack(side="right", anchor="n" , padx=200,pady=200)
    timer_label.place(x=1100,y=600)

    points_label=tk.Label(root)
    points_label.pack_forget()

    def countdown(minutes, seconds):
    # update the timer label
        global points
        global frame1
        global frame2
        global frame3
        timer_label.config(text=f"{minutes:02}:{seconds:02} \U0000231B")
    
        if minutes == 0 and seconds == 0:
        # stop the timer when it reaches 0
            
            points_label.config(text=f'{"your points is"}:{points} \U0001F600',bg="red",font=("Arial", 24), bd=2, relief="solid" ,fg="black")
            points_label.pack()
            welcome()
            return
        elif seconds == 0:
            import keyboard

            def disable_windows_key(e):
                if e.name == 'left windows' or e.name == 'right windows':
                    return False

            keyboard.on_press(disable_windows_key)

        # subtract one minute when seconds reach 0
            root.after(1000, countdown, minutes-1, 59)
        else:
        # subtract one second
            import keyboard

            def disable_windows_key(e):
                if e.name == 'left windows' or e.name == 'right windows':
                    return False

            keyboard.on_press(disable_windows_key)

            root.after(1000, countdown, minutes, seconds-1)

# start the timer
    countdown(20, 0)


    global frame1
    frame1 = tk.Frame(root,bg="black")
    frame1.place(x=400,y=100)

    label1 = tk.Label(frame1, text=" 1) The keyword used to transfer control from a function back to the \ncalling function is?",bg="black" ,font=("Arial", 19, "bold"),fg="#00FF00")
    label1.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    

    rb1 = tk.Radiobutton(frame1, text="Switch", variable=var1, value="Switch",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
    rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    rb2 = tk.Radiobutton(frame1, text="Goto", variable=var1, value="Goto",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
    rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    rb3 = tk.Radiobutton(frame1, text="Return", variable=var1, value="Return",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
    rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    var1.set(None)  # Set the initial value of the StringVar to None

    submit_btn = tk.Button(frame1, text="Submit \U0001F44D", font=("Arial", 15),command=lambda: check_answer1(var1.get()),bg="#00ff00")
    submit_btn.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer1(answer):
        global points
        if answer == "Return":
            points = points + 10

        print("Your points is", points)
        
        frame1.destroy()

        global frame2
        frame2 = tk.Frame(root,bg="black")
      
        frame2.pack()
        frame2.place(x=400,y=100)

        label2 = tk.Label(frame2, text="2) Which operator is used to continue the definition of macro in the next line?",bg="black" ,font=("Arial", 19, "bold"),fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame2, text="#", variable=var2, value="#",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame2, text="/", variable=var2, value="/",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame2, text="# #", variable=var2, value="##",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var2.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame2, text="Submit \U0001F44D",font=("Arial", 15), command=lambda: check_answer2(var2.get()),bg="#00ff00")
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer2(answer):
        global points
        if answer == "/":
            points = points + 10
        print("Your points is", points)
        global frame2
        frame2.destroy()

        global frame3
        frame3 = tk.Frame(root,bg="black")
        frame3.pack()
        frame3.place(x=400,y=100)

        # label2 = tk.Label(frame3, text='"What will be the output of the program if value 25 given to scanf()?\n#include<stdio.h>\nint main()\n{\nint i;\nprintf("%d\n", scanf("%d", &i));return 0;}"',bg="black" ,font=("Arial", 19, "bold"),fg="white")
        # label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        text_widget = tk.Text(frame3,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=10)
        code = '''3) What is the output of the following code snippet?
                    int main() {
	                    int sum = 2 + 4 / 2 + 6 * 2;
	                    printf("%d", sum);
	                    return 0;
                    }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame3, text="12", variable=var3, value="12",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame3, text="2", variable=var3, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame3, text="16", variable=var3, value="16",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var3.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame3, text="Submit \U0001F44D", command=lambda: check_answer3(var3.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer3(answer):
        global points
        if answer == "16":
            points = points + 10
        print("Your points is", points)
        global frame3
        frame3.destroy()


        global frame4
        frame4 = tk.Frame(root,bg="black")
        frame4.pack()
        frame4.place(x=400,y=100)

        label2 = tk.Label(frame4, text="4) How are String represented in memory in C?",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame4, text="The object of some class", variable=var4, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame4, text="An array of characters", variable=var4, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame4, text="LinkedList of characters", variable=var4, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var4.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame4, text="Submit \U0001F44D", command=lambda: check_answer4(var4.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer4(answer):
        global points
        if answer == "2":
            points = points + 10
        print("Your points is", points)
        global frame4
        frame4.destroy()


        global frame5
        frame5 = tk.Frame(root,bg="black")
        frame5.pack()
        frame5.place(x=400,y=100)

        text_widget = tk.Text(frame5,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''5) What will be the output of the following code snippet?
                    #include <stdio.h>
                    void solve() {
                                int first = 10, second = 20;
                                int third = first + second;
                            {
                                int third = second - first;
                                printf("%d ", third);
                            }
                            printf("%d", third);
                    }
                    int main() {
	                solve();
	                return 0;
                    }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame5, text="10 20", variable=var5, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame5, text="10 30", variable=var5, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame5, text="20 10", variable=var5, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var5.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame5, text="Submit \U0001F44D", command=lambda: check_answer5(var5.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer5(answer):
        global points
        if answer == "2":
            points = points + 10
        print("Your points is", points)
        global frame5
        frame5.destroy()

        global frame6
        frame6 = tk.Frame(root,bg="black")
        frame6.pack()
        frame6.place(x=400,y=100)

        label2 = tk.Label(frame6, text="6) What does the following declaration indicate? int x: 8;",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame6, text="x ratio 8", variable=var6, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame6, text="x is equal to 8", variable=var6, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame6, text="x is an 8 bit integer", variable=var6, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var6.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame6, text="Submit \U0001F44D", command=lambda: check_answer6(var6.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer6(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame6
        frame6.destroy()

        global frame7
        frame7 = tk.Frame(root,bg="black")
        frame7.pack()
        frame7.place(x=400,y=100)

        label2 = tk.Label(frame7, text="7) What is the size of the int data type (in bytes) in C?",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame7, text="2", variable=var7, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame7, text="4", variable=var7, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame7, text="6", variable=var7, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var7.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame7, text="Submit \U0001F44D", command=lambda: check_answer7(var7.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer7(answer):
        global points
        if answer == "2":
            points = points + 10
        print("Your points is", points)
        global frame7
        frame7.destroy()

        global frame8
        frame8 = tk.Frame(root,bg="black")
        frame8.pack()
        frame8.place(x=400,y=100)

        text_widget = tk.Text(frame8,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''8) Find Output in follwing code:
                            void main ()
                            {
                                int x = 128;
                                printf ("%d", 1 + x++);
                            }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame8, text="128", variable=var8, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame8, text="129", variable=var8, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame8, text="130", variable=var8, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var8.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame8, text="Submit \U0001F44D", command=lambda: check_answer8(var8.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer8(answer):
        global points
        if answer == "2":
            points = points + 10
        print("Your points is", points)
        global frame8
        frame8.destroy()


        global frame9
        frame9 = tk.Frame(root,bg="black")
        frame9.pack()
        frame9.place(x=400,y=100)

        label2 = tk.Label(frame9, text="9) Which of the following is the exit controlled loop",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame9, text="while", variable=var9, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame9, text="for", variable=var9, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame9, text="do-while", variable=var9, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var9.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame9, text="Submit \U0001F44D", command=lambda: check_answer9(var9.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer9(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame9
        frame9.destroy()


        global frame10
        frame10 = tk.Frame(root,bg="black")
        frame10.pack()
        frame10.place(x=400,y=100)

        text_widget = tk.Text(frame10,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''10) Predict the output of the following code segment:
                // Add stdio.h header file in below code
                int main()
                {
                    unsigned int a = -1;
                    int b = ~0;
                    int result;
                    if (b == a)
                        printf(“equal”);
                    else
                        printf(“unequal”);
                    return 0;
                }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame10, text="error", variable=var10, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame10, text="unequal", variable=var10, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame10, text="equal", variable=var10, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var10.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame10, text="Submit \U0001F44D", command=lambda: check_answer10(var10.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer10(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame10
        frame10.destroy()

        global frame11
        frame11 = tk.Frame(root,bg="black")
        frame11.pack()
        frame11.place(x=400,y=100)

        label2 = tk.Label(frame11, text="11) Find out the correct order",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame11, text="char < int < double", variable=var11, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame11, text="int > char > float", variable=var11, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame11, text=" double > char > int", variable=var11, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var11.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame11, text="Submit \U0001F44D", command=lambda: check_answer11(var11.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer11(answer):
        global points
        if answer == "1":
            points = points + 10
        print("Your points is", points)
        global frame11
        frame11.destroy()


        global frame12
        frame12 = tk.Frame(root,bg="black")
        frame12.pack()
        frame12.place(x=400,y=100)

        label2 = tk.Label(frame12, text="12) No of keywords in C ",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame12, text="only 31", variable=var12, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame12, text="only 35", variable=var12, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame12, text="only 32", variable=var12, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var12.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame12, text="Submit \U0001F44D", command=lambda: check_answer12(var12.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer12(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame12
        frame12.destroy()


        global frame13
        frame13 = tk.Frame(root,bg="black")
        frame13.pack()
        frame13.place(x=400,y=100)

        text_widget = tk.Text(frame13,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''13) #include <stdio.h>
                  int main() {
                  int i = 1;
                  if (i++ && (i == 1)) {
                        printf("Yes");
                  }
                  else {
                        printf("No");
                    }
                  return 0;
                }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame13, text="yes", variable=var13, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame13, text="no", variable=var13, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame13, text="both", variable=var13, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var13.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame13, text="Submit \U0001F44D", command=lambda: check_answer13(var13.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer13(answer):
        global points
        if answer == "2":
            points = points + 10
        print("Your points is", points)
        global frame13
        frame13.destroy()

        global frame14
        frame14 = tk.Frame(root,bg="black")
        frame14.pack()
        frame14.place(x=400,y=100)

        text_widget = tk.Text(frame14,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''14) What will be the output of the following code snippet?
                    #include <stdio.h>
                    void solve() {
                        int ch = 2;
                        switch(ch) {
                            case 1: printf("1 ");
                            case 2: printf("2 ");
                            case 3: printf("3 ");
                            default: printf("None");
                        }
                    }
                    int main() {
                        solve();
                        return 0;
                    }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame14, text="2 3 None", variable=var14, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame14, text="1 2 3 None", variable=var14, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame14, text="2", variable=var14, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var14.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame14, text="Submit \U0001F44D", command=lambda: check_answer14(var14.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer14(answer):
        global points
        if answer == "1":
            points = points + 10
        print("Your points is", points)
        global frame14
        frame14.destroy()

        global frame15
        frame15 = tk.Frame(root,bg="black")
        frame15.pack()
        frame15.place(x=400,y=100)

        label2 = tk.Label(frame15, text="15) Array elements are always stored in _____ memory locations.",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame15, text="Random", variable=var15, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame15, text="Sequential", variable=var15, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame15, text="Sequential and Random", variable=var15, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var15.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame15, text="Submit \U0001F44D", command=lambda: check_answer15(var15.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer15(answer):
        global points
        if answer == "2":
            points = points + 10
        print("Your points is", points)
        global frame15
        frame15.destroy()

        global frame16
        frame16 = tk.Frame(root,bg="black")
        frame16.pack()
        frame16.place(x=400,y=100)

        text_widget = tk.Text(frame16,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''16) What will be the output of the following c program
                    #include <stdio.h>
                    int main() {
                        int x[5]={ 10, 20, 30};
                        printf("%d",x[3]);
                        return 0;
                    }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame16, text="30", variable=var16, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame16, text="none", variable=var16, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame16, text="0", variable=var16, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var16.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame16, text="Submit \U0001F44D", command=lambda: check_answer16(var16.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer16(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame16
        frame16.destroy()


        global frame17
        frame17 = tk.Frame(root,bg="black")
        frame17.pack()
        frame17.place(x=400,y=100)

        label2 = tk.Label(frame17, text="17) Suppose a C program has floating constant 1.414, what's the best way\n to convert this as "'float'" data type?",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame17, text="(float)1.414", variable=var17, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame17, text="1.414f or 1.414F", variable=var17, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame17, text="float(1.414)", variable=var17, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var17.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame17, text="Submit \U0001F44D", command=lambda: check_answer17(var17.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer17(answer):
        global points
        if answer == "2":
            points = points + 10
        print("Your points is", points)
        global frame17
        frame17.destroy()

        global frame18
        frame18 = tk.Frame(root,bg="black")
        frame18.pack()
        frame18.place(x=400,y=100)

        text_widget = tk.Text(frame18,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''18) Let x be an integer which can take a value of 0 or 1.
                  if (x == 0) {
                        x = 1;
                    }
                  else {
                        x = 0;
                    }
                is equivalent to which one of the following?'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame18, text="x=x+1", variable=var18, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame18, text="x=x", variable=var18, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame18, text="x=!x", variable=var18, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var18.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame18, text="Submit \U0001F44D", command=lambda: check_answer18(var18.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer18(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame18
        frame18.destroy()

        global frame19
        frame19 = tk.Frame(root,bg="black")
        frame19.pack()
        frame19.place(x=400,y=100)

        text_widget = tk.Text(frame19,bg="black" ,font=("Arial", 13, "bold"),fg="#00FF00",height=20)
        code = '''19) What will be the output of the following C code?
                  #include <stdio.h>
                  int main(){
                  int i, j;
                  for (i = 2; i < 10; i++) {
                        for (j = 2; j <= (i / j); j++)
                        if (!(i % j))
                            break;
                        if (j > (i / j))
                            printf("%d ", i);
                        }
                  return 0;
                  }'''
        text_widget.insert(tk.END, code)
        text_widget.grid(row=0,sticky="W")

        rb1 = tk.Radiobutton(frame19, text="3 5 7 9", variable=var19, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame19, text="2 3 4 5 6 7 8 9", variable=var19, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame19, text="2 3 5 7", variable=var19, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var19.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame19, text="Submit \U0001F44D", command=lambda: check_answer19(var19.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer19(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame19
        frame19.destroy()

        global frame20
        frame20 = tk.Frame(root,bg="black")
        frame20.pack()
        frame20.place(x=400,y=100)

        label2 = tk.Label(frame20, text="20) Who is the father of c ?",bg="black" ,font=("Arial", 19, "bold")
,fg="#00FF00")
        label2.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        rb1 = tk.Radiobutton(frame20, text="james gosling", variable=var20, value="1",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rb2 = tk.Radiobutton(frame20, text="rasmus lerdorf", variable=var20, value="2",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        rb3 = tk.Radiobutton(frame20, text="dennis ritchie", variable=var20, value="3",bg="black",fg="red",selectcolor="black",font=("Arial", 13, "bold"))
        rb3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        var20.set(None)  # Set the initial value of the StringVar to None

        submit_btn2 = tk.Button(frame20, text="Submit \U0001F44D", command=lambda: check_answer20(var20.get()),bg="#00ff00", font=("Arial", 15))
        submit_btn2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    def check_answer20(answer):
        global points
        if answer == "3":
            points = points + 10
        print("Your points is", points)
        global frame20
        frame20.destroy()



global b1
b1=tk.Button(root,text="Start",command=start, width=20,bg="#00ff00", fg="red",height=2, font=("Arial", 10,"bold"))
b1.pack(side=tk.BOTTOM, anchor=tk.S,pady=200)

from PIL import Image, ImageTk

img2 = Image.open("C:\\Users\\HP\\Pictures\\coding3.png")

# Resize the image
img2 = img2.resize((100, 100), Image.ANTIALIAS)

# Create a PhotoImage object from the resized image
photo_img2 = ImageTk.PhotoImage(img2)

# Create a label to display the image
image_label2 = tk.Label(root, image=photo_img2)

image_label2.pack()
image_label2.place(x=0,y=0)





root.mainloop()
