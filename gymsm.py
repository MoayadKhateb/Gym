from tkinter import *

details_trainers = []
details_phone_number = []
details_where_he_she_live = []
_subscriptions = []
_schedule = []
_Complaint_Number = []
class Gym:
    def __init__(self, trainers, where_he_she_live, subscriptions, schedule, phone_number, Complaint_Number="911"):
        self.trainers = trainers
        self.phone_number = phone_number
        self.where_he_she_live = where_he_she_live
        self.subscriptions = subscriptions
        self.schedule = schedule
        self.Complaint_Number = Complaint_Number

    def save_details(self):
        details_trainers.append(self.trainers)
        details_phone_number.append(self.phone_number)
        details_where_he_she_live.append(self.where_he_she_live)
        _subscriptions.append(self.subscriptions)
        _schedule.append(self.schedule)
        _Complaint_Number.append(self.Complaint_Number)

def printinfo():
    trainers = entry_trainers.get()
    where_he_she_live = entry_where_he_she_live.get()
    subscriptions = entry_subscriptions.get()
    phone_number = int(entry_phone_number.get())

def Gym_Schedule_window():
    gym_schedule_window = Toplevel(window)
    gym_schedule_window.geometry("500x500")
    gym_schedule_window.title("Gym Schedule")

    gym_schedule_label = Label(gym_schedule_window, text="Gym Schedule\nSunday : Push up\n Monday : Leg day\n Tuesday : Shoulders day\n Wednesday : Leg day\n Thursday : Piceps Day\n Friday and Saturday : Rest Days", font=("Helvetica", 16, "bold"))
    gym_schedule_label.pack()

    close_button = Button(gym_schedule_window, text="Close", command=gym_schedule_window.destroy)
    close_button.pack()

def Complaint_Number_window():
    complaint_number_window = Toplevel(window)
    complaint_number_window.geometry("500x500")
    complaint_number_window.title("ComplaintNumber")

    complaint_number_label = Label(complaint_number_window, text="Complaint Number : 911", font=("Helvetica", 16, "bold"))
    complaint_number_label.pack()

    close_button = Button(complaint_number_window, text="Close", command=complaint_number_window.destroy)
    close_button.pack()

window = Tk()
window.geometry("500x500")
window.configure(bg="#000000")

frame = Frame(window, width=400, height=400, bg="#ffffff")
frame.propagate(False)
frame.pack(pady=80)

entry_trainers = Entry(frame, bg="#ffffff", font=10)
entry_trainers.pack(pady=15)
entry_trainers.insert(0, "Enter Name:")

entry_where_he_she_live = Entry(frame, bg="#ffffff", font=10)
entry_where_he_she_live.pack(pady=10)
entry_where_he_she_live.insert(0, "Where Live:")

entry_subscriptions = Entry(frame, bg="#ffffff", font=10)
entry_subscriptions.pack(pady=10)
entry_subscriptions.insert(0, "Subs (W or Y) :")

button_Gym_Schedule = Button(frame, text="Gym Schedule", command=Gym_Schedule_window)
button_Gym_Schedule.pack(pady=10)

button_Complaint_Number = Button(frame, text="Complaint Number", command=Complaint_Number_window)
button_Complaint_Number.pack(pady=10)

entry_phone_number = Entry(frame, bg="#ffffff", font=10)
entry_phone_number.pack(pady=10)
entry_phone_number.insert(0, "Phone Number:")

button_press = Button(frame, text="Press", command=printinfo)
button_press.pack(pady=10)

label = Label(frame, text="")
label.pack()

window.mainloop()
