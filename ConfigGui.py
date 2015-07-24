from tkinter import *
import ConfigController
import tkinter.font
import tkinter.filedialog
import Configs

root = Tk()

def make_gui(config_groups):
    config_entries = []
    group_font = tkinter.font.Font(root = root, weight= 'bold')
    i = 1
    for group in config_groups:
        Label(root, text=group.group_name, font=group_font).grid(row=i)
        for config in group.config_items:
            i += 1
            config_entries.append(Configs.ConfigEntry(config.name, place_label_box(config, i)))
            i += 1
    place_save_button(i)
    return config_entries

def place_label_box(config, row):
    l = Label(root, text=config.name)
    l.grid(row=row)
    e = Entry(root)
    e.insert(END, config.value)
    e.grid(row=row, column=1)
    return e

def place_save_button(row):
    Button(root, text='Save', command = save_inputs).grid(row = row)

def save_inputs():
    new_configs = []
    for i in inputs:
        new_val = i.config_entry.get()
        new_configs.append(Configs.ConfigItem(i.config_name, new_val))
    ConfigController.save_all_configs(path, new_configs)

path = tkinter.filedialog.askopenfilename(parent=root)
all_config_groups = ConfigController.get_all_configs(path)
inputs = make_gui(all_config_groups)
root.mainloop()
