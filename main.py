import tkinter
from tkinter import *
from tkinter import filedialog as fd
import csv

frame_config = {
    "relief": GROOVE,

}

file_entry_config = {
    "width": 30,
    "relief": RAISED,
    "font": ('Verdana', 10)
}

# plot option buttons
plot_buttons = ["PLOT RAW", "PLOT FILTERED", "COMBINE"]
plot_btns_config = {
    "relief": RAISED,
    "font": ("Verdana", 10, "bold")
}


# file operations variables
# functions
def open_raw_file():
    """
    open raw data file, csv, split it plot
    :return:
    """

    file_types = (
        ('csv files', '*.csv'),
        ('text files', '*.txt')
    )

    data_file = fd.askopenfilename(
        title='Choose file',
        filetypes=file_types
    )

    with open(data_file, 'r') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            print(row)

    # update GUI
    raw_file_entry.insert(0, data_file)

    # show file opening operations
    raw_file_open_status = Label(info_frame, text="[ ] Raw file loaded. Ready to plot...")
    raw_file_open_status.pack(anchor="w")


"""
Initialize widgets for the app
"""

root = Tk()
root.geometry('1400x700')
root.title("Plottar")

# parent frame
root_frame = LabelFrame(root)
root_frame.pack(side="left", fill=Y, ipadx=10, ipady=20, pady=10)

graph_frame = LabelFrame(root, text="test")
graph_frame.pack(side="left", expand=True)

l = Label(graph_frame, text="Click")
l.pack(side="right")

# create file select frame
file_frame = LabelFrame(root_frame, text="Select files")
file_frame.pack(ipadx=10, side="top", pady=15)

raw_file_frame = Frame(file_frame)
raw_file_frame.pack(side="top")
raw_file_label = Label(raw_file_frame, text="Raw file")
raw_file_label.pack(side="left")
raw_file_entry = Entry(raw_file_frame, file_entry_config)
raw_file_entry.pack(side="left")
raw_file_select_btn = Button(raw_file_frame, text="...", command=open_raw_file)
raw_file_select_btn.pack(side="left")

filter_file_frame = Frame(file_frame)
filter_file_frame.pack(side="top")
filter_file_label = Label(filter_file_frame, text="Filter file")
filter_file_label.pack(side="left")
filter_file_entry = Entry(filter_file_frame, file_entry_config)
filter_file_entry.pack(side="left")
filter_file_select_btn = Button(filter_file_frame, text="...")
filter_file_select_btn.pack(side="left")

# create plotting buttons
plot_btn_frame = LabelFrame(root_frame, frame_config)
plot_btn_frame.pack(side="top", pady=15, padx=15, fill=X, ipady=5)

plot_raw_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[0])
plot_raw_btn.pack(side="left", expand=True)
plot_filtered_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[1])
plot_filtered_btn.pack(side="left", expand=True)
combine_plots_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[2])
combine_plots_btn.pack(side="left", expand=True)

# info frame
info_frame = LabelFrame(root_frame, frame_config, text="Info")
info_frame.pack(side="left", anchor="w", padx=15, pady=15, expand=True, fill=BOTH)

mainloop()
