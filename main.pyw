
# * Project - GUI Password Generator
# * Date - 02-09-2022
# * Author - Rahul

from tkinter import *
import random
import datetime
import time

if __name__ == "__main__":
    # * Creating a GUI Window

    root = Tk()
    width = "800"
    height = "300"
    root.geometry(f"{width}x{height}")
    root.minsize(800, 300)
    root.maxsize(800, 300)
    root.title("Password Generator")
    root.wm_iconbitmap("icon.ico")

# * Writing Function to generate password


def genPass():
    try:
        date_time = datetime.datetime.now()
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOP"
        numbers = "1234567890"
        symbols = "!@#$%^&*{}[]?/<>,.;:"
        all = lowercase+uppercase+numbers+symbols
        passLength = length.get()
        if entry1.get() == '' and entry2.get() == '':  # * When site and length entry are empty
            password = "".join(random.sample(all, 16))
            passvalue.set(password)
            statusvar.set("Saving Password")
            sbar.update()
            time.sleep(1)
            statusvar.set("Password Saved in Saved Passwords/password.txt")
            with open("Saved Passwords/password.txt", 'r') as f:
                f.read()
            with open("Saved Passwords/password.txt", 'a') as f:
                f.writelines(
                    f"\nRandom Password Generated on on {date_time} is : {password}")
            f = open("Saved Passwords/password.txt", 'a')
            f.close()
        elif entry1.get() == '':  # * When site entry is empty
            password = "".join(random.sample(all, int(passLength)))
            passvalue.set(password)
            statusvar.set("Saving Password")
            sbar.update()
            time.sleep(1)
            statusvar.set("Password Saved in Saved Passwords/password.txt")
            with open("Saved Passwords/password.txt", 'r') as f:
                f.read()
            with open("Saved Passwords/password.txt", 'a') as f:
                f.writelines(
                    f"\nRandom Password Generated on on {date_time} is : {password}")
            f = open("Saved Passwords/password.txt", 'a')
            f.close()
        elif entry2.get() == '':  # * When length entry is empty
            password = "".join(random.sample(all, 16))
            passvalue.set(password)
            statusvar.set("Saving Password")
            sbar.update()
            time.sleep(1)
            statusvar.set("Password Saved in Saved Passwords/password.txt")
            with open("Saved Passwords/password.txt", 'r') as f:
                f.read()
            with open("Saved Passwords/password.txt", 'a') as f:
                f.writelines(
                    f"\nPassword generated for {site.get()} on {date_time} is : {password}")
            f = open("Saved Passwords/password.txt", 'a')
            f.close()
        else:  # * When both entries are given
            password = "".join(random.sample(all, int(passLength)))
            passvalue.set(password)
            statusvar.set("Saving Password")
            sbar.update()
            time.sleep(1)
            statusvar.set("Password Saved in Saved Passwords/password.txt")
            with open("Saved Passwords/password.txt", 'r') as f:
                f.read()
            with open("Saved Passwords/password.txt", 'a') as f:
                f.writelines(
                    f"\nPassword generated for {site.get()} on {date_time} is : {password}")
            f = open("Saved Passwords/password.txt", 'a')
            f.close()
    except Exception:
        pass

# * Function that copies the password for user


def copyText():
    if entry3.get() == '':
        copyBTN.config(text="COPY")
    else:
        entry3.event_generate(("<<SelectAll>>"))
        entry3.event_generate(("<<Copy>>"))
        copyBTN.config(text="COPIED!")
        copyBTN.update()
        time.sleep(2)
        copyBTN.config(text="COPY")


# * Heading Of the GUI
Label(text="Your PRIVACY is Priority for us",
      font="Lucida 16 bold", pady=12).pack()

# * Defining String Variables
site = StringVar()
length = StringVar()
passvalue = StringVar()

#! Created a frame
f0 = Frame(root)
Label(f0, text="Enter the name of the site for which you want to generate password",
      font="ariel 12", padx=23).pack(side=LEFT)
# * User can enter site name and entered data is stored in site variable
entry1 = Entry(f0, textvariable=site, width="34", font="caliber 16")
entry1.pack(side=LEFT)
f0.pack()

f0 = Frame(root, pady=12)
Label(f0, text="Enter the Length of password",
      font="ariel 12", padx=23).pack(side=LEFT)
# * User can enter length of password entered data is stored in length variable
entry2 = Entry(f0, textvariable=length, width="34", font="caliber 16")
entry2.pack(side=LEFT)
f0.pack()

f0 = Frame(root, pady=12)
#! Created Buttons
# * This button will generate passwords
Button(f0, padx=22, pady=12, bg="black", fg="white",
       text="Generate Password", font="Lucida 9 bold", command=genPass).pack(side=LEFT)
# * This button will exit the program
Button(f0, padx=22, pady=12, bg="black", fg="red",
       text="EXIT", font="Lucida 9 bold", command=exit).pack(side=LEFT, padx=12)
f0.pack()

f0 = Frame(root, pady=12)
Label(f0, text="Your Generated Password",
      font="ariel 12", padx=23).pack(side=LEFT)
# * Generated password will be shown in this entry
entry3 = Entry(f0, textvariable=passvalue, width="34",
               font="ariel 16 bold", fg="red")
entry3.pack(side=LEFT, padx=12)

# * This button will copy the generated password
copyBTN = Button(f0, padx=2, pady=2, bg="red", fg="black", text="COPY",
                 font="Lucida 9 bold", relief=SUNKEN, command=copyText)
copyBTN.pack(side=LEFT)
f0.pack()

statusvar = StringVar()
statusvar.set("Ready to use")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='w')
sbar.pack(side=BOTTOM, fill=X)

root.mainloop()
