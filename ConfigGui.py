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
    e.focus_set()
    return e

def place_save_button(row):
    Button(root, text='Save', command = prompt_save_config).grid(row = row)

def prompt_save_config():
    new_file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".h")
    save_inputs(new_file_path)

def save_inputs(new_file_path):
    new_configs = []
    for i in inputs:
        new_val = i.config_entry.get()
        new_configs.append(Configs.ConfigItem(i.config_name, new_val))
    ConfigController.save_all_configs(config_path, new_file_path, new_configs)

config_path = tkinter.filedialog.askopenfilename(parent=root)
all_config_groups = ConfigController.get_all_configs(config_path)
inputs = make_gui(all_config_groups)
root.mainloop()
