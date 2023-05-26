import pandas as pd
from tkinter import *
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# Select First File
def sfile1():
    root.filename = filedialog.askopenfilename(initialdir="/",title="Select a File", filetypes=(("CSV FILES","*.xlsx"),))
    f = str(root.filename)
    entry_variable1.set(f)
    entry.configure(state='disabled')


# Main Operation
def Calculation():
    filename = entry_variable1.get()
    # Read the Excel file into a DataFrame
    df = pd.read_excel(filename)

    # Calculate total Net Amount by Mode and round the values
    total_net_amount_by_mode = df.groupby('Mode')['NET AMOUNT'].sum().round(0).reset_index()
    df1 = pd.DataFrame(total_net_amount_by_mode)
    df1.to_excel("./Final.xlsx")

    


# window
root = ttk.Window()
root.title("Total Net Amount")
root.geometry("700x300")

# title
title_label = ttk.Label(master = root, text = "Calculate", font = "Calibri 24 bold")
title_label.pack(side = TOP, padx=10, pady=10)

# Second Frame
input_frame1 = ttk.Frame(master = root)
entry_variable1 = ttk.StringVar()
entry = ttk.Entry(input_frame1, textvariable = entry_variable1)
b1 = ttk.Button(input_frame1, text='Select File', bootstyle=PRIMARY, command = sfile1)
b1.pack(side=LEFT, padx=5, pady=5)
entry.pack(side = LEFT)
input_frame1.pack()


# Fourth Frame
Input_frame3 = ttk.Frame(master = root)
b3 = ttk.Button(Input_frame3, text='Submit', bootstyle=PRIMARY, command = Calculation)
b3.pack(side=LEFT, padx=5, pady=5)
# entry1.pack(side = LEFT)
Input_frame3.pack()


root.mainloop()
