from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Tip Calculator")
root.geometry("600x600+400+40")
root.configure(bg="#badbd0")
f = ("Times New Roman", 18, "bold")

def calculate_tip():
    bill = bill_entry.get()
    try:
        if bill == "":
            showerror("Issue", "Bill amount cannot be empty")
            bill_entry.delete(0, END)
            bill_entry.focus()
            return
        elif(bill.strip() == ""):
            showerror("Issue", "Bill amount cannot be spaces")
            bill_entry.delete(0, END)
            bill_entry.focus()
            return
        elif(bill.isalpha()):
            showerror("Issue", "Bill amount cannot be text")
            bill_entry.delete(0, END)
            bill_entry.focus()
            return
        elif float(bill)<0:
            showerror("Issue", "Bill amount cannot be negative")
            bill_entry.delete(0, END)
            bill_entry.focus()
            return
        else:
            pass
    except ValueError:
        showerror("Issue","Bill amount should not be special characters")
        bill_entry.delete(0, END)
        bill_entry.focus()
        return
    except Exception as e:
        showerror("Issue", str(e))
        bill_entry.delete(0, END)
        bill_entry.focus()
        return
    tip = tip_entry.get()
    try:
        if tip == "":
            showerror("Issue", "Tip Percentage cannot be empty")
            tip_entry.delete(0,END)
            tip_entry.focus()
            return
        elif (tip.strip()==""):
            showerror("Issue","Tip Percentage cannot be spaces")
            tip_entry.delete(0,END)
            tip_entry.focus()
            return
        elif(tip.isalpha()):
            showerror("Issue","Tip Percentage cannot be text")
            tip_entry.delete(0,END)
            tip_entry.focus()
            return
        elif float(tip)<0:
            showerror("Issue","Tip Percentage cannot be negative")
            tip_entry.delete(0,END)
            tip_entry.focus()
            return
        else:
            pass
    except ValueError:
        showerror("Issue","Tip Percentage cannot be special character")
        tip_entry.delete(0,END)
        tip_entry.focus()
        return
    except Exception as e:
        showerror("Issue",str(e))
        tip_entry.delete(0,END)
        tip_entry.focus()
        return
    people = people_entry.get()
    try:
        if people == "":
            showerror("Issue","Number of People cannot be empty")
            people_entry.delete(0,END)
            people_entry.focus()
            return
        elif (people.strip() == ""):
            showerror("Issue","Number of People cannot be spaces")
            people_entry.delete(0,END)
            people_entry.focus()
            return
        elif(people.isalpha()):
            showerror("Issue","Number of People cannot be text")
            people_entry.delete(0,END)
            people_entry.focus()
            return
        elif float(people)<0:
            showerror("Issue","Number of People cannot be negative")
            people_entry.delete(0,END)
            people_entry.focus()
            return
        else:
            pass
    except ValueError:
        showerror("Issue","Number of People cannot be special characters")
        people_entry.delete(0,END)
        people_entry.focus()
        return
    except Exception as e:
        showerror("Issue", str(e))
        people_entry.delete(0,END)
        people_entry.focus()
        return
    
    tip = (float(tip)/100)* float(bill)
    total_amount = float(tip) + float(bill)
    per_head = float(total_amount)/float(people)

    output = f" Total Tip: {round(tip,2)} \n Total Amount: {round(total_amount,2)}\n Total Per Person: {round(per_head,2)}"

    output_label = Label(text=output,font=f, anchor="e", justify=LEFT, bg="#badbd0")
    output_label.place(x=50, y=400)

def clear():
    bill_entry.delete(0,END)
    tip_entry.delete(0,END)
    people_entry.delete(0,END)
    bill_entry.focus()

label_msg = Label(root, text="Tip Calculator", font=f, bg='#badbd0')
label_msg.place(x=220, y=20)

bill_label = Label(root, text="Bill Amount:", font=f, bg='#badbd0')
bill_label.place(x=50, y=100)
bill_entry = Entry(root, font=f)
bill_entry.place(x=270, y=100)

tip_label = Label(root, text="Tip Percentage (%):", font=f, bg='#badbd0')
tip_label.place(x=50, y=150)
tip_entry = Entry(root, font=f)
tip_entry.place(x=270, y=150)

people_label = Label(root, text="Number of People:", font=f, bg='#badbd0' )
people_label.place(x=50, y=200)
people_entry = Entry(root, font=f)
people_entry.place(x=270, y=200)

calculate_button = Button(root, text="Calculate", font=f, command=calculate_tip)
calculate_button.place(x=250, y=280)

clear_button = Button(root, text="Clear", font=f, command=clear)
clear_button.place(x=270, y=340)

def on_closing():
    if askyesno("Exit", "Do You Want To Exit ?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()