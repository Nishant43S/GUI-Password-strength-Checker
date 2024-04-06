from tkinter import *
import ttkbootstrap as ttkb
import tkinter.messagebox as tmsg
from ttkbootstrap.constants import *

if __name__=="__main__":          ##############  main app function
    def check_password_strength():
        password = Password_Entry.get()

        if password.strip() == "":
            tmsg.showwarning("Error...","Enter password")
        else:
                    # Criteria points
            points = {
                'length':5,           # Minimum length of 5 characters
                'uppercase': 2,        # Points for at least one uppercase letter
                'lowercase': 1,        # Points for at least one lowercase letter
                'special': 3,          # Points for at least one special character
                'number': 2            # Points for at least one digit
            }


            total_points = 0

            # Check each criterion and calculate points
            if len(password) >= points['length']:
                total_points += points['length']

            if any(char.isupper() for char in password):
                total_points += points['uppercase']

            if any(char.islower() for char in password):
                total_points += points['lowercase']

            if any(char.isdigit() for char in password):
                total_points += points['number']

            if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>/?'" for char in password):
                total_points += points['special']

            # Determine strength based on total points
            strength = ""
            if total_points >= 12:
                strength = "very strong"
            elif total_points >= 8:
                strength = "strong"
            elif total_points >= 6:
                strength = "good"
            else:
                strength = "weak"

            result = "Password is {}. Total points: {}".format(strength, total_points)
            print(result)

            if total_points >= 12:
                StrengthOutput.configure(foreground="#4bc87f")
            elif total_points >= 8:
                StrengthOutput.configure(foreground="#ffb03b")
            elif total_points >= 6:
                StrengthOutput.configure(foreground="#3fc5f0")
            else:
                StrengthOutput.configure(foreground="red")
            Strengthvar.set(strength)
            Pointvar.set(total_points)
            PassLength.set(len(password))



if __name__=="__main__":      ##############   window size
    def Setsize(Width,Height):
        root.geometry(f"{Width}x{Height}")
        root.minsize(width=Width,height=Height)
        root.maxsize(width=Width,height=Height)

root = ttkb.Window(themename="superhero")
AppTitle = ttkb.Label(                            ###  App heading
   master=root,text="password Strength Checker 🔑",
    font=("ds-digital",20),foreground="#f4991a"
)
AppTitle.pack(side=TOP,pady=9)

EntryFrame = ttkb.Frame(
    master=root,
    width=500,
    height=100
)
EntryFrame.pack(side=TOP,pady=15,padx=6)


Password_Entry = ttkb.Entry(         ########  input field
    master=EntryFrame,
    font=('ds-digital',13),
    bootstyle="success",width=26
)
Password_Entry.grid(row=0,column=0)

BtnStyle = ttkb.Style()
BtnStyle.configure("success.TButton",font=('ds-digital',13))

CheakBtn = ttkb.Button(              ########### button
    master=EntryFrame,text="Check",
    bootstyle="success",
    style="success.TButton",
    command=check_password_strength
)

OutputFrame = ttkb.Frame(   #######  output frame
    master=root,
    width=500,
    height=300
)
OutputFrame.pack(side=TOP,padx=23,pady=16,anchor=W)

######  variables

Strengthvar = StringVar()
Pointvar = StringVar()
PassLength = StringVar()

StrengthLabel = ttkb.Label(    ####  strength label
    master=OutputFrame,
    font=("ds-digital",19),
    text="Strength "
)
StrengthLabel.grid(row=0,column=0,sticky=W,padx=5)

StrengthOutput = ttkb.Label(
    master=OutputFrame,
    font=("ds-digital",19),
    textvariable=Strengthvar
)
StrengthOutput.grid(row=0,column=1)

PointsLabel = ttkb.Label(
    master=OutputFrame,
    font=("ds-digital",19),
    text="point "
)
PointsLabel.grid(row=1,column=0,sticky=W,padx=5)

PointsOutput = ttkb.Label(
    master=OutputFrame,
    font=("ds-digital",19),
    textvariable=Pointvar
)
PointsOutput.grid(row=1,column=1)

PasswordLengthLabel = ttkb.Label(
    master=OutputFrame,
    font=("ds-digital",19),
    text="Length "
)
PasswordLengthLabel.grid(row=2,column=0,sticky=W,padx=5)

PasswordLengthOutput = ttkb.Label(
    master=OutputFrame,
    font=("ds-digital",19),
    textvariable=PassLength
)
PasswordLengthOutput.grid(row=2,column=1)

CreaterNameLabel = ttkb.Label(
    master=root,
    text="Created by Nishant Maity",
    font=("ds-digital",9),
    bootstyle="warning"
)
CreaterNameLabel.pack(side=BOTTOM)


CheakBtn.grid(row=0,column=1)
root.title("Password Strength Checker")
Setsize(500,300)
root.mainloop()
