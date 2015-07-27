import tkinter as tk
import ConfigController
import tkinter.font
import tkinter.filedialog
import Configs

root = tk.Tk()
root.wm_title("Marlin Probe Configurator")

def make_gui(config_groups):
    config_entries = []
    i = 1
    for group in config_groups:
        place_group_label(group.group_name, i)
        for config in group.config_items:
            i += 1
            config_entries.append(Configs.ConfigEntry(config.name, place_label_box(config, i)))
            i += 1
    place_save_button(i)
    return config_entries

def place_group_label(group_name, row):
    group_font = tkinter.font.Font(root = root, weight= 'bold')
    tk.Label(root, text=group_name, font=group_font).grid(row=row)

def place_label_box(config, row):
    l = tk.Label(root, text=config.name)
    l.grid(row=row, column = 0)
    e = tk.Entry(root)
    e.insert(tk.END, config.value)
    e.grid(row=row, column = 1)
    e.focus_set()
    return e

def place_save_button(row):
    button_font = tkinter.font.Font(root = root, weight= 'bold')
    tk.Button(root, text='Save', command = prompt_save_config, font=button_font).grid(row=row, column=0, columnspan=2, sticky=tk.W + tk.E + tk.N + tk.S, pady=(5, 0))

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
