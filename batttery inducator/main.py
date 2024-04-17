import tkinter as tk
import psutil


def check_battery():
    battery = psutil.sensors_battery()
    if battery is not None:
        if battery.power_plugged:
            print("Zaryadlovchi ulangan!")
        else:
            print("Zaryadlovchi ulanmagan!")
    root.after(
        2000, check_battery
    )  # Har 2 soniyada zaryadlovchini tekshirishni takrorlash


root = tk.Tk()
root.after(
    2000, check_battery
)  # Dasturni boshlaganda birinchi marta tekshirishni o'rnatish
root.mainloop()
