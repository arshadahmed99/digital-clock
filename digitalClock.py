import tkinter as tk
from time import localtime, strftime
import math

# Main window
root = tk.Tk()
root.title("Digital + Analog Clock")
root.geometry("400x500")
root.resizable(False, False)

# Digital clock label
digital_label = tk.Label(root, font=('Arial', 40), background='black', foreground='cyan')
digital_label.pack(pady=20)

# Canvas for analog clock
canvas_size = 300
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg='white')
canvas.pack()

# Clock center
center_x = canvas_size // 2
center_y = canvas_size // 2
clock_radius = 140

# Draw clock circle
canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                   center_x + clock_radius, center_y + clock_radius)

# Function to update both clocks
def update_clock():
    # Digital
    current_time = strftime('%H:%M:%S %p')
    digital_label.config(text=current_time)

    # Analog
    t = localtime()
    hours = t.tm_hour % 12
    minutes = t.tm_min
    seconds = t.tm_sec

    # Clear previous hands
    canvas.delete("hands")

    # Hour hand
    hour_angle = math.radians((hours + minutes/60) * 30 - 90)
    hour_x = center_x + 60 * math.cos(hour_angle)
    hour_y = center_y + 60 * math.sin(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill='black', tags="hands")

    # Minute hand
    minute_angle = math.radians((minutes + seconds/60) * 6 - 90)
    minute_x = center_x + 90 * math.cos(minute_angle)
    minute_y = center_y + 90 * math.sin(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill='blue', tags="hands")

    # Second hand
    second_angle = math.radians(seconds * 6 - 90)
    second_x = center_x + 100 * math.cos(second_angle)
    second_y = center_y + 100 * math.sin(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill='red', tags="hands")

    # Update every 1 second
    root.after(1000, update_clock)

# Start the clock
update_clock()
root.mainloop()
