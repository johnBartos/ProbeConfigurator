import Configurator
import Configs
import tempfile
import os

probe_bed_lines = ["#define LEFT_PROBE_BED_POSITION", "#define RIGHT_PROBE_BED_POSITION", "#define BACK_PROBE_BED_POSITION", "#define FRONT_PROBE_BED_POSITION"]
probe_offset_lines = ["#define X_PROBE_OFFSET_FROM_EXTRUDER", "#define Y_PROBE_OFFSET_FROM_EXTRUDER", "#define Z_PROBE_OFFSET_FROM_EXTRUDER"]
probe_travel_lines = ["#define XY_TRAVEL_SPEED", "#define Z_RAISE_BEFORE_PROBING", "#define Z_RAISE_BETWEEN_PROBING"]
probe_servo_lines = ["#define NUM_SERVOS", "#define SERVO_ENDSTOPS", "#define SERVO_ENDSTOP_ANGLES"]
probe_enable_lines = ["#define ENABLE_AUTO_BED_LEVELING"]

def get_all_configs(file_path):
    bed_configs = Configurator.find_config_lines(file_path, probe_bed_lines)
    offset_configs = Configurator.find_config_lines(file_path, probe_offset_lines)
    travel_configs = Configurator.find_config_lines(file_path, probe_travel_lines)
    servo_configs = Configurator.find_config_lines(file_path, probe_servo_lines)
    enable_lines = Configurator.find_config_lines(file_path, probe_enable_lines)

    menu = []
    menu.append(Configs.ConfigGroup("Bed Dimension", bed_configs))
    menu.append(Configs.ConfigGroup("Probe Offsets", offset_configs))
    menu.append(Configs.ConfigGroup("Probe Motion", travel_configs))
    menu.append(Configs.ConfigGroup("Servo Properties", servo_configs))
    menu.append(Configs.ConfigGroup("Enables", enable_lines))

    return menu

def save_all_configs(old_file_path, new_file_path, new_configs):
    if(len(old_file_path) == 0 or len(new_file_path) == 0):
        return False
    with (tempfile.NamedTemporaryFile(dir=os.path.dirname(old_file_path), delete=False)) as temp:
        Configurator.write_new_config(old_file_path, temp, new_configs)
    os.replace(temp.name, new_file_path)
    return True
