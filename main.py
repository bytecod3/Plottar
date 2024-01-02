import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog as fd
import csv

# graphing imports
# import matplotlib as mpl
# mpl.rcParams['toolbar'] = 'None' # remove navbar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

# set default figure size to fit on window
plt.rcParams["figure.figsize"] = (10, 7)

frame_config = {
    "relief": GROOVE,

}

file_entry_config = {
    "width": 30,
    "relief": RAISED,
    "font": ('Verdana', 10)
}

# plot option buttons
plot_buttons = ["PLOT RAW", "PLOT FILTERED", "COMBINE", "CLR"]
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

    raw_data_file = fd.askopenfilename(
        title='Choose file',
        filetypes=file_types
    )

    # update GUI
    raw_file_entry.delete(0, END)
    raw_file_entry.insert(0, raw_data_file)

    # show file opening operations
    raw_file_open_status = Label(info_frame, text="[ ] Raw file loaded. Ready to plot...")
    raw_file_open_status.pack(anchor="w")


def open_filtered_file():
    """
    open filtered data file, csv
    :return:
    """
    file_types = (
        ('csv files', '*.csv'),
        ('text files', '*.txt')
    )

    raw_data_file = fd.askopenfilename(
        title='Choose file',
        filetypes=file_types
    )

    # update GUI
    filter_file_entry.delete(0, END)
    filter_file_entry.insert(0, raw_data_file)

    # show file opening operations
    filtered_file_open_status = Label(info_frame, text="[ ] Filtered file loaded. Ready to plot...")
    filtered_file_open_status.pack(anchor="w")


def show_message(title, message):
    """
    Show app messages
    :return:
    """
    showerror(title=title, message=message)


def plot_raw():
    """
    plot raw data
    :return:
    """
    draw_plot(filtered=False)


def plot_filtered_data():
    """
    plot filtered data
    :return:
    """
    draw_plot(filtered=True, combine=False)


def plot_raw_and_filtered():
    """
    combine raw data and filtered on the same plot
    :return:
    """
    draw_plot(filtered=False, combine=True)


def draw_plot(filtered=False, combine=False):
    """
    draw a plot
    :param filtered:
    :param combine:
    :return:
    """

    # acceleration values
    x_acc = []
    y_acc = []
    z_acc = []

    # filtered acceleration values
    x_acc_filtered = []
    y_acc_filtered = []
    z_acc_filtered = []

    # plot raw data
    if filtered is False and combine is False:
        raw_data_file = raw_file_entry.get()

        if len(raw_data_file) == 0:
            show_message("Error", "Please select a file")

        # get the raw_data csv file and split into x,y,z
        with open(raw_data_file, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                # split into x, y, z lists
                x_acc.append(float(row[0]))
                y_acc.append(float(row[1]))
                z_acc.append(float(row[2]))

        # plot x, y, z
        fig, ax = plt.subplots()
        ax.grid()

        # plot the data
        ax.plot(x_acc, label="x_acceleration")
        ax.plot(y_acc, label="y_acceleration")
        ax.plot(z_acc, label="z_acceleration")

        # set legends
        ax.legend()

        # set axes title
        ax.set_title("Raw acceleration data")

        # set x and y labels
        ax.set_ylabel("Acceleration (m/s^2)")
        ax.set_xlabel("Time (s)")

        # create a tk drawing area
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        # toolbar = NavigationToolbar2Tk(canvas, root)
        # toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    # plot filtered data
    elif filtered is True and combine is False:
        # check if filtered data file is selected
        filtered_data_file = filter_file_entry.get()

        # error on empty select box
        if len(filtered_data_file) == 0:
            show_message("Error", "Please select a file")

        # open file
        with open(filtered_data_file, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                # split into x, y, z lists
                x_acc_filtered.append(float(row[0]))
                y_acc_filtered.append(float(row[1]))
                z_acc_filtered.append(float(row[2]))

        # plot x, y, z
        # create the plot canvas
        fig, ax = plt.subplots()
        ax.grid()

        # plot the data
        ax.plot(x_acc_filtered, label="filtered_x_acceleration")
        ax.plot(y_acc_filtered, label="filtered_y_acceleration")
        ax.plot(z_acc_filtered, label="filtered_z_acceleration")

        # set legends
        ax.legend()

        # set axes title
        ax.set_title("Filtered acceleration data")

        # set x and y labels
        ax.set_ylabel("Acceleration (m/s^2)")
        ax.set_xlabel("Time (s)")

        # create a tk drawing area
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        # toolbar = NavigationToolbar2Tk(canvas, root)
        # toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    # plot combined data
    elif filtered is False and combine is True:
        # delete the previous canvas

        filtered_data_file = filter_file_entry.get()
        raw_data_file = raw_file_entry.get()

        if len(filtered_data_file) == 0 or len(raw_data_file) == 0:
            show_message("Error", "Please select a file")

        # open raw data file
        with open(raw_data_file, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                # split into x, y, z lists
                x_acc.append(float(row[0]))
                y_acc.append(float(row[1]))
                z_acc.append(float(row[2]))

        # open filtered data file
        with open(filtered_data_file, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                # split into x, y, z lists
                x_acc_filtered.append(float(row[0]))
                y_acc_filtered.append(float(row[1]))
                z_acc_filtered.append(float(row[2]))

        # plot x, y, z
        fig, ax = plt.subplots()
        ax.grid()

        # plot the raw data
        ax.plot(x_acc, label="x_acceleration")
        ax.plot(y_acc, label="y_acceleration")
        ax.plot(z_acc, label="z_acceleration")

        # plot the filtered data
        ax.plot(x_acc_filtered, label="filtered_x_acceleration")
        ax.plot(y_acc_filtered, label="filtered_y_acceleration")
        ax.plot(z_acc_filtered, label="filtered_z_acceleration")

        # set legends
        ax.legend()

        # set axes title
        ax.set_title("Acceleration data")

        # set x and y labels
        ax.set_ylabel("Acceleration (m/s^2)")
        ax.set_xlabel("Time (s)")

        # create a tk drawing area
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        # toolbar = NavigationToolbar2Tk(canvas, root)
        # toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


def clear_plots():
    """
    clear the file entry boxes
    :return:
    """
    raw_file_entry.delete(0, END)
    filter_file_entry.delete(0, END)

    # delete the graph figure
    fig.clf()



"""
Initialize widgets for the app
"""

root = Tk()
root.geometry('1400x700')
root.title("Plottar")

# parent frame
root_frame = LabelFrame(root)
root_frame.pack(side="left", fill=Y, ipadx=10, ipady=20, pady=10)

graph_frame = LabelFrame(root)
graph_frame.pack(side="left", expand=True)

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
filter_file_select_btn = Button(filter_file_frame, text="...", command=open_filtered_file)
filter_file_select_btn.pack(side="left")

# create plotting buttons
plot_btn_frame = LabelFrame(root_frame, frame_config)
plot_btn_frame.pack(side="top", pady=15, padx=15, fill=X, ipady=5)

plot_raw_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[0], command=plot_raw)
plot_raw_btn.pack(side="left", expand=True)
plot_filtered_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[1], command=plot_filtered_data)
plot_filtered_btn.pack(side="left", expand=True)
combine_plots_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[2], command=plot_raw_and_filtered)
combine_plots_btn.pack(side="left", expand=True)
clear_plots_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[3], command=clear_plots)
clear_plots_btn.pack(side="left", expand=True)

# create a tk drawing area
# fig, ax = plt.subplots()
# plot dummy data
# ax.plot([1,2,3,4,1,2,3,8,1])

# pcanvas = FigureCanvasTkAgg(fig, master=graph_frame)
# pcanvas.draw()
# pcanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
# # toolbar = NavigationToolbar2Tk(canvas, root)
# # toolbar.update()
# pcanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

# info frame
info_frame = LabelFrame(root_frame, frame_config, text="Info")
info_frame.pack(side="left", anchor="w", padx=15, pady=15, expand=True, fill=BOTH)

mainloop()
