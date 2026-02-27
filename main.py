#Created by Pr. Ismayil Aliyev

import tkinter                  #importing the tkinter library
from tkinter import ttk             #importing ttk module for special widgets (such as combobox)
from tkinter import messagebox          #


def data_entry():               #function for saving all user data
    terms_check_data = terms_check_var.get()            #getting user's Term checking result and saving it to terms_check_data variable
    if terms_check_data=="Accepted":                 #checking if user accepted the Terms or not, if yes printing all other variables
        #User data
        firstname_data = first_name_entry.get()             #getting user's first name and saving it to firstname_data variable
        lastname_data = last_name_entry.get()             #getting user's last name and saving it to lastname_data variable
        if firstname_data and lastname_data:
            title_data = user_title_combobox.get()             #getting user's title and saving it to title_data variable
            age_data = user_age_spinbox.get()               #getting user's age and saving it to age_data variable   
            server_data = user_server_combobox.get()               #getting user's server and saving it to server_data variable
            
            #Course data
            reg_status_data = reg_status_var.get()
            numcourses_data = numcourses_spinbox.get()                 #getting user's course numbers and saving it to numcourses_data variable
            numsemesters_data = numsemesters_spinbox.get()                  #getting user's semester numbers and saving it to numsemesters_data variable
            
            print("First name: ", firstname_data, "Last name: ", lastname_data, "Title: ", title_data)
            print("Age: ", age_data, "Server: ", server_data)
            print("Registration Status: ", reg_status_data, "Course numbers: ", numcourses_data, "Semester numbers: ", numsemesters_data)

            #Terms data
            print(f"Terms & Conditions: {terms_check_data}")
            print("--------------------------------------------------")

        else :
            tkinter.messagebox.showwarning(title="Name Error ~ Ismayil Groups", message="You must have a name for registering in Ismayil Groups MMC.")

    else :                                                      #if not printing the rules of Your Majesty Sir Ismayil
        tkinter.messagebox.showwarning(title="Terms Error ~ Ismayil Groups", message="You must accepts the Terms & Conditions of Ismayil Groups MMC.")


root_window = tkinter.Tk()        #creating the main window which will contain all other widgets
root_window.title("Ismayil's Data Entry Form")      #setting the title of root window

frame = tkinter.Frame(root_window)                   #creating frame box inside of main window
frame.pack()             #displays the frame to the main window

#Saving user information
user_info_frame = tkinter.LabelFrame(frame, text="User Information")          #creating another labeled frame inside of frame
user_info_frame.grid(row=0, column=0, padx=20, pady=10)           #displays user_info_frame in the frame + positioning the user info with padding in direction of x and y

first_name_label = tkinter.Label(user_info_frame, text="First Name")            # creating a label (display widget) for displaying the first name
first_name_label.grid(row=0, column=0)          #displays (placing the label in certain row, column) First name in the user_info_frame

last_name_label = tkinter.Label(user_info_frame, text="Last Name")          # creating a label (display widget) for displaying the last name
last_name_label.grid(row=0, column=1)           #displays (placing the label in certain row, column) Last name in the user_info_frame

first_name_entry = tkinter.Entry(user_info_frame)           #creating an entry (input widget) for the First name info
first_name_entry.grid(row=1, column = 0)            #placing the entry in certain row, column in the user_info_frame

last_name_entry = tkinter.Entry(user_info_frame)            #creating an entry (input widget) for the Last name info      
last_name_entry.grid(row=1, column=1)           #placing the entry in certain row, column in the user_info_frame

user_title_label = tkinter.Label(user_info_frame, text="Title")           #creating a label (display widget) for displaying the title
user_title_label.grid(row=0, column=2)            #displays (placing the label in certain row, column) title in the user_info_frame

user_title_combobox = ttk.Combobox(user_info_frame, value=["Mr.", "Ms.", "Dr.", "Pr."])            #creating a combobox (input widget for selection) for the Title info
user_title_combobox.grid(row=1, column=2)              #placing the combobox in certain row, column in the user_info_frame

user_age_label = tkinter.Label(user_info_frame, text="Age")            #creating a label (display widget) for displaying the age
user_age_label.grid(row=2, column=0)            #displays (placing the label in certain row, column) age in the user_info_frame

user_age_spinbox = tkinter.Spinbox(user_info_frame, from_=16, to=130)           #creating a spinbox (input widget for selection with arrows) for the Age info
user_age_spinbox.grid(row=3, column=0)             #placing the spinbox in certain row, column in the user_info_frame


user_server_label = tkinter.Label(user_info_frame, text="Server")           #creating a label (display widget) for displaying the server
user_server_label.grid(row=2, column=1)             #displays (placing the label in certain row, column) server in the user_info_frame

user_server_combobox = ttk.Combobox(user_info_frame, value=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])             #creating a combobox (input widget for selection) for the Server info
user_server_combobox.grid(row=3, column=1)              #placing the combobox in certain row, column in the user_info_frame

for widget in user_info_frame.winfo_children():            # looping through all widgets inside user_info_frame
    widget.grid_configure(padx=10, pady=5)             #adding padding to each widget using grid configuration

#Saving course information
courses_frame = tkinter.LabelFrame(frame, text="Course Registration")           #creating another labeled frame inside of frame
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)           #displays courses_frame in the frame + positioning the course info with padding in direction of x and y +  makes it stretch in all directions (north, east, west, south)

registration_label = tkinter.Label(courses_frame, text="Registration Status")               # creating a label (display widget) for displaying the registration status
registration_label.grid(row=0, column=0)               #displays (placing the label in certain row, column) the status in the courses_frame

reg_status_var = tkinter.StringVar()                #setting a variable for getting the output from registration checking
registration_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",                      #creating a checkbutton (input widget for checking) for the registration info
                                         variable=reg_status_var, onvalue="Registered", offvalue="Not registered")              #giving specific string values to onvalue and offvalue for output value (reg_status_var)      
registration_check.grid(row=1, column=0)            #placing the checkbutton in certain row, column in the courses_frame

numcourses_label = tkinter.Label(courses_frame, text="Completed Courses")           #creating a label (display widget) for displaying the completed cources
numcourses_label.grid(row=0, column=1)              #displays (placing the label in certain row, column) the completed cources in the courses_frame

numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")             #creating a spinbox (input widget for selection with arrows) for the Course number info
numcourses_spinbox.grid(row=1, column=1)               #placing the spinbox in certain row, column in the courses_frame

numsemesters_label = tkinter.Label(courses_frame, text="Semesters")             #creating a label (display widget) for displaying the semesters
numsemesters_label.grid(row=0, column=2)            #displays (placing the label in certain row, column) the semesters in the courses_frame

numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")           #creating a spinbox (input widget for selection with arrows) for the Semester number info
numsemesters_spinbox.grid(row=1, column=2)             #placing the spinbox in certain row, column in the courses_frame

for widget in courses_frame.winfo_children():           # looping through all widgets inside courses_frame
    widget.grid_configure(padx=10, pady=5)             #adding padding to each widget using grid configuration

#Accept Terms & Conditions
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")              #creating another labeled frame inside of frame
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)              #displays terms_frame in the frame + positioning the terms info with padding in direction of x and y +  makes it stretch in all directions (north, east, west, south)

terms_check_var = tkinter.StringVar(value="Not Accepted")               #setting a variable for getting the output from Terms checking
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions of the Ismayil Groups MMC",               #creating a checkbutton (input widget for checking) for the terms info
                                  variable=terms_check_var, onvalue="Accepted", offvalue="Not Accepted")            #giving specific string values to onvalue and offvalue for output value (terms_check_var)
terms_check.grid(row=0, column=0)               ##placing the checkbutton in certain row, column in the terms_frame

#Button Creation
enter_button = tkinter.Button(frame, text="Enter data", command=data_entry)             #creating button (another type of widget) inside of frame + accessing to the data_entry function with command
enter_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)            #displays enter_button in the frame + positioning the button info with padding in direction of x and y +  makes it stretch in all directions (north, east, west, south)


root_window.mainloop()              #continue running until closing the window

