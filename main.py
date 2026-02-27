#Created by Pr. Ismayil Aliyev

import tkinter                  #importing the tkinter library
from tkinter import ttk             #importing ttk module for special widgets (such as combobox)


root_window = tkinter.Tk()        #creating the main window which will contain all other widgets
root_window.title("Ismayil's Data Entry Form")      #setting the title of root window

frame = tkinter.Frame(root_window)                   #creating frame box inside of main window
frame.pack()             #displays the frame to the main window

#Saving user information
user_info_frame = tkinter.LabelFrame(frame, text="User Information")          #creating another labeled frame inside of frame
user_info_frame.grid(row=0, column=0, padx=20, pady=20)           #displays user_info_frame in the frame + positioning the user info with padding in direction of x and y

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
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)           #displays courses_frame in the frame + positioning the course info with padding in direction of x and y +  makes it stretch in all directions (north, east, west, south)

registration_label = tkinter.Label(courses_frame, text="Registration Status")               # creating a label (display widget) for displaying the registration status
registration_label.grid(row=0, column=0)               #displays (placing the label in certain row, column) the status in the courses_frame

registration_check = tkinter.Checkbutton(courses_frame, text="Currently Registered")            #creating a checkbutton (input widget for checking) for the registration info
registration_check.grid(row=1, column=0)            #placing the checkbutton in certain row, column in the courses_frame

numcourses_label = tkinter.Label(courses_frame, text="Completed Courses")           #creating a label (display widget) for displaying the completed cources
numcourses_label.grid(row=0, column=1)              #displays (placing the label in certain row, column) the completed cources in the courses_frame

numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")             #creating a spinbox (input widget for selection with arrows) for the Course number info
numcourses_spinbox.grid(row=1, column=1)               #placing the spinbox in certain row, column in the courses_frame

numsemesters_label = tkinter.Label(courses_frame, text="Semesters")             #creating a label (display widget) for displaying the semesters
numsemesters_label.grid(row=0, column=2)            #displays (placing the label in certain row, column) the semesters in the courses_frame

numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")           #creating a spinbox (input widget for selection with arrows) for the Semester number info
numsemesters_spinbox.grid(row=1, column=2)             #placing the spinbox in certain row, column in the courses_frame

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

root_window.mainloop()              #continue running until closing the window

