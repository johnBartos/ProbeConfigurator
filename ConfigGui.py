from tkinter import *
import ConfigController
import tkinter.font
import tkinter.filedialog

root = Tk()

def make_gui(config_groups):
    group_font = tkinter.font.Font(root = root, weight= 'bold')
    i = 1
    for group in config_groups:
        Label(root, text=group.group_name, font=group_font).grid(row=i)
        for config in group.config_items:
            i += 1
            place_label_box(config, i)
            i += 1

def place_label_box(config, row):
    l = Label(root, text=config.name)
    l.grid(row=row)
    e = Entry(root)
    e.insert(END, config.value)
    e.grid(row=row, column=1)


path = tkinter.filedialog.askopenfilename(parent=root)

all_config_groups = ConfigController.get_all_configs(path)
make_gui(all_config_groups)
root.mainloop()
