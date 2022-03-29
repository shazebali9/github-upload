"""
Created by Will and Shazeb
https://docs.google.com/document/d/1KrxEPAYheBIGF-mLeXfvrV44AxmIoe9lMnjiaZ9FYFY/edit?usp=sharing
"""
from tkinter import *
from tkinter import ttk

#creates lists to store user data
classes_count = 0
classes = []
entries = []
bgColor = "#0C2538"
txtColor = "#d1a553"
#creates window and settings for window
root=Tk()
root.title("NBPS GPA Calculator")
root.geometry("400x500")
root.configure(bg=bgColor)
#creates text widget
l1 = Label(root, text="This is a GPA calculator for North Broward Preperatory School.", bg = bgColor, fg=txtColor)
l1.grid()
l2 = Label(root, text="How many classes do you take?", bg = bgColor, fg=txtColor)
l2.grid(row = 1)

#Creates first entry box
estart = Entry(root, width = 10, highlightbackground=txtColor, bg=bgColor, fg=txtColor)
estart.grid(column = 0, row = 3)

btn1 = Button(root, text = "Enter", highlightbackground=bgColor, fg = 'white')
btn1.grid(column = 0, row = 2)

current_command = 0
#Gets how many classes you take
def input_counts():
    global classes_count
    try:
        classes_count = estart.get()
        estart.delete(0, "end")
        for i in range(int(classes_count)):
            data = "e" + str(i)
            entries.append(data)
            estart.destroy()
        return "w"
    
    except:
        return "l"

#Determines which classes count toward GPA calculation
def which_counts():
    for entry in entries:
        result = entry.get()
        if result == "y" or result == "yes" or result == "Y" or result == "Yes" or result == "YES":
            classes.append(["true"])
        else:
            classes.append(["false"])
            
    for entry in entries:
        entry.delete(0, "end")
        
    #print(classes)

#Appends data for class level    
def classes_level():
    #we repeat the same loop for a reason. Before any data is appended, all entrys need to be error checked. You don't want some classes having apended data before the loop breaks.
    for i in range(len(entries)):
        result = entries[i].get()
        if result != "cp" and result != "hon" and result != "ap" and result != "ib":
            return "l"
            break
    for i in range(len(entries)):
        result = entries[i].get()
        if result == "cp":
            classes[i].append("cp")
        if result == "hon":
            classes[i].append("hon")
        if result == "ib" or result == "ap":
            classes[i].append("accelerated")
    #print(classes)
    for i in range(len(entries)):
        entries[i].delete(0, "end")
    return "w"

#Appends data for grades
def input_grades():
    for i in range(len(entries)):
        try:
            test = float(entries[i].get())
        except:
            return "l"
            break
    for i in range(len(entries)):
        if classes[i][0]== "true":
            result = entries[i].get()
            classes[i].append(float(result))
        else:
            classes[i].append(0)
            
    #print(classes)
    for i in range(len(entries)):
        entries[i].delete(0, "end")
    return "w"
        
#Calculates weighted GPA for each class and appends the data
def calc_weighted(c):
    classes_count = c
    for i in range(int(classes_count)):
        grade = classes[i][2]
        #turns grade into gpa
        if grade >= 96.5:
            gpa = 4.33
        if grade >= 92.5 and grade <= 96.4:
            gpa = 4.00
        if grade >= 89.5 and grade <= 92.4:
            gpa = 3.67
        if grade >= 86.5 and grade <= 89.4:
            gpa = 3.33
        if grade >= 82.5 and grade <= 86.4:
            gpa = 3.00
        if grade >= 79.5 and grade <= 82.4:
            gpa = 2.67
        if grade >= 76.5 and grade <= 79.4:
            gpa = 2.33
        if grade >= 72.5 and grade <= 76.4:
            gpa = 2.00
        if grade >= 69.5 and grade <= 72.4:
            gpa = 1.67
        if grade >= 66.5 and grade <= 69.4:
            gpa = 1.33
        if grade >= 62.5 and grade <= 66.4:
            gpa = 1.00
        if grade >= 59.5 and grade <= 62.4:
            gpa = 0.67
        if grade < 59.5:
            gpa = 0.00
        #uses class level to weigh grades
        if classes[i][1] == "cp":
            gpa = gpa * 1.00
        if classes[i][1] == "hon":
            gpa = gpa * 1.15
        if classes[i][1] == "accelerated":
            gpa = gpa * 1.30
        #attaches gpa to classes list
        classes[i].append(gpa)

def calc_unweighted(c):
    classes_count = c
    for i in range(int(classes_count)):
        grade = classes[i][2]
        #turns grade into gpa
        if grade >= 96.5:
            gpa = 4.0
        if grade >= 92.5 and grade <= 96.4:
            gpa = 4.0
        if grade >= 89.5 and grade <= 92.4:
            gpa = 3.7
        if grade >= 86.5 and grade <= 89.4:
            gpa = 3.3
        if grade >= 82.5 and grade <= 86.4:
            gpa = 3.0
        if grade >= 79.5 and grade <= 82.4:
            gpa = 2.7
        if grade >= 76.5 and grade <= 79.4:
            gpa = 2.3
        if grade >= 72.5 and grade <= 76.4:
            gpa = 2.0
        if grade >= 69.5 and grade <= 72.4:
            gpa = 1.7
        if grade >= 66.5 and grade <= 69.4:
            gpa = 1.3
        if grade >= 62.5 and grade <= 66.4:
            gpa = 1.0
        if grade < 62.5:
            gpa = 0.00
        #attaches gpa to classes list
        classes[i].append(gpa)

#final gpa calculations. average of all gpas that count.
def w_gpa_calc(c):
    classes_count = int(c)
    true_classes = 0
    big_gpa = 0
    calc_gpa = 0
    for i in range(classes_count):
        if classes[i][0] == "true":
            true_classes = true_classes + 1
        big_gpa = big_gpa + classes[i][3]
    calc_gpa = big_gpa / true_classes
    calc_gpa = round(calc_gpa, 2)
    return calc_gpa

def un_gpa_calc(c):
    classes_count = int(c)
    true_classes = 0
    big_gpa = 0
    calc_gpa = 0
    for i in range(classes_count):
        if classes[i][0] == "true":
            true_classes = true_classes + 1
        big_gpa = big_gpa + classes[i][4]
    calc_gpa = big_gpa / true_classes
    calc_gpa = round(calc_gpa, 2)
    return calc_gpa

#Each time switchboard is run, the command it runs changes
def switchboard():
    global current_command
    if current_command == 0:
        valid = input_counts()
        if valid == "w":
            #creates the entry boxes
            for i in range(len(entries)):
                entries[i] = Entry(root, width = 10, highlightbackground=txtColor, bg=bgColor, fg=txtColor)
                entries[i].grid(column = 0, row = 3 + i)
            current_command = current_command + 1
            l2.configure(text = "Do each of these classes count toward GPA? (y/n)")
                
    elif current_command == 1:
        which_counts()
        current_command = current_command + 1
        l2.configure(text = "What level is each class? cp/hon/ap/ib")
    elif current_command == 2:
        valid = classes_level()
        if valid == "w":
            current_command = current_command + 1
            l2.configure(text = "What are your grades in each glass (numbers not letters) ?")
        else:
           for i in range(len(entries)):
                entries[i].delete(0, "end")
        
    elif current_command == 3:
        valid = input_grades()
        if valid == "w":
            current_command = current_command + 1
            for i in range(len(entries)):
                entries[i].destroy()
            calc_weighted(classes_count)
            calc_unweighted(classes_count)
            l1.configure(text="Your NBPS Weighted GPA:")
            l2print= w_gpa_calc(classes_count)
            l2.configure(text= l2print)
            l3 = Label(root, text = "Your Standard Unweighted GPA:", bg = bgColor, fg=txtColor)
            l4print = un_gpa_calc(classes_count)
            l4 = Label(root, text= l4print, bg = bgColor, fg=txtColor)
            l3.grid(row = 4)
            l4.grid(row = 5)
            btn1.destroy()
        else:
            for i in range(len(entries)):
                entries[i].delete(0, "end")

#Gives the button a purpose
btn1.configure(command = switchboard)
#Starts the window loop
root.mainloop()
