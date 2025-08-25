import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Function to update time
def time():
    current_time = strftime('%H:%M:%S %p')  # Format: HH:MM:SS AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # Update every 1 second

# Create a label for the clock
label = tk.Label(root, font=('Arial', 50), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()

# Run the Tkinter event loop
root.mainloop()
