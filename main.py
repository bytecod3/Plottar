import tkinter
from tkinter import *

frame_config = {
    "relief": GROOVE,

}

file_entry_config = {
    "width": 30,
    "relief": RAISED,
    "font": ('Arial', 13)
}

# plot option buttons
plot_buttons = ["PLOT RAW", "PLOT FILTERED", "COMBINE"]
plot_btns_config = {
    "relief": RAISED,
    "font": ("Arial", 10, "bold")
}

def init_widgets():
    '''
    Initialize widgets for the app
    '''

    # parent frame
    root_frame = LabelFrame(root, background="red")
    root_frame.pack(side="left", fill=Y, ipadx=10, ipady=20, pady=10)

    graph_frame = LabelFrame(root, text="test", background="blue")
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
    raw_file_select_btn = Button(raw_file_frame, text="...")
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
    plot_btn_frame.pack(side="top", pady=15, padx=15, fill=X)

    plot_raw_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[0])
    plot_raw_btn.pack(side="left", expand=True)
    plot_filtered_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[1])
    plot_filtered_btn.pack(side="left", expand=True)
    combine_plots_btn = Button(plot_btn_frame, plot_btns_config, text=plot_buttons[2])
    combine_plots_btn.pack(side="left", expand=True)

    # info frame
    info_frame = LabelFrame(root_frame, frame_config, text="Info")
    info_frame.pack(side="top", anchor="w", padx=15, pady=15, expand=True, fill=BOTH)

    info_frame_entry = Label(info_frame, font=("Verdana", 10), text="Raw file opening failed")
    info_frame_entry.pack(side="left") # TODO: make this dynamic


root = Tk()
root.geometry('1400x700')
root.title("Plottar")

# create widgets
init_widgets()

mainloop()
