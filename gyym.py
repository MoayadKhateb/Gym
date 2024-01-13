from tkinter import *

details_trainers = []
details_phone_number = []
details_where_he_she_live = []
_subscriptions = []

class Gym:
    def _init_(self, trainers, where_he_she_live, subscriptions, schedule, phone_number, exercise_type, day_of_week, Complaint_Number="911"):
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


def printinfo():
    trainers = entry_trainers.get()
    where_he_she_live = entry_where_he_she_live.get()
    subscriptions = entry_subscriptions.get()
    schedule = entry_schedule.get()
    phone_number = int(entry_phone_number.get())


    app = Gym(trainers, where_he_she_live, subscriptions, schedule, phone_number, exercise_type, day_of_week)
    app.save_details()
    user_input = int(entry_user_input.get())
    for i in range(len(details_trainers)):
        if user_input == 1:
            label.config(text=f"details: {details_trainers[i]}, {details_phone_number[i]}, {details_where_he_she_live[i]}")
        elif user_input == 2:
            label.config(text=f"subscriptions: {_subscriptions}")
        elif user_input == 3:
            label.config(text=f"schedule: {_schedule}")
        elif user_input == 4:
            label.config(text=f"Complaint_Number: {911}")





def Gym_Schedule_window():
    Gym_Schedule_window = Toplevel(window)
    Gym_Schedule_window.geometry("500x500")
    Gym_Schedule_window.title("Gym Schedule")

    Gym_Schedule_label = Label(Gym_Schedule_window, text="Gym Schedule\nSunday : Push up\n Monday : Leg day\n Tuesday : Shoulders day\n Wednesday : Leg day\n Thursday : Piceps Day\n Friday and Saturday : Rest Days", font=("Helvetica", 16, "bold"))
    Gym_Schedule_label.pack()



    close_button = Button(Gym_Schedule_window, text="Close", command=Gym_Schedule_window.destroy)
    close_button.pack()


window = Tk()
window.geometry("500x500")
window.configure(bg="#000000")

frame = Frame(window, width=400, height=400, bg="#ffffff")
frame.propagate(False)
frame.pack(pady=80)

entry_trainers = Entry(frame, bg="#ffffff", font=10)
entry_trainers.pack(pady=10)
entry_trainers.insert(0, "Enter Name:")

entry_where_he_she_live = Entry(frame, bg="#ffffff", font=10)
entry_where_he_she_live.pack(pady=10)
entry_where_he_she_live.insert(0, "Where Live:")

entry_subscriptions = Entry(frame, bg="#ffffff", font=10)
entry_subscriptions.pack(pady=10)
entry_subscriptions.insert(0, "Subs (W or Y) :")

button_Gym_Schedule = Button(frame, text="Gym Schedule", command=Gym_Schedule_window)
button_Gym_Schedule.pack(pady=10)

entry_phone_number = Entry(frame, bg="#ffffff", font=10)
entry_phone_number.pack(pady=10)
entry_phone_number.insert(0, "Phone Number:")





button_press = Button(frame, text="Press", command=printinfo)
button_press.pack(pady=10)

label = Label(frame, text="")
label.pack()

window.mainloop()