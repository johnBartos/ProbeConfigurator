import Configurator
import Configs

probe_bed_lines = ["#define LEFT_PROBE_BED_POSITION", "#define RIGHT_PROBE_BED_POSITION", "#define BACK_PROBE_BED_POSITION", "#define FRONT_PROBE_BED_POSITION"]
probe_offset_lines = ["#define X_PROBE_OFFSET_FROM_EXTRUDER", "#define Y_PROBE_OFFSET_FROM_EXTRUDER", "#define Z_PROBE_OFFSET_FROM_EXTRUDER"]
probe_travel_lines = ["#define XY_TRAVEL_SPEED", "#define Z_RAISE_BEFORE_PROBING", "#define Z_RAISE_BETWEEN_PROBING"]
probe_servo_lines = ["#define NUM_SERVOS"]
probe_enable_lines = ["#define SERVO_ENDSTOPS", "#define SERVO_ENDSTOP_ANGLES"]

def get_all_configs(file):
    bed_configs = Configurator.find_config_lines(file, probe_bed_lines)
    offset_configs = Configurator.find_config_lines(file, probe_offset_lines)
    travel_configs = Configurator.find_config_lines(file, probe_travel_lines)
    servo_configs = Configurator.find_config_lines(file, probe_servo_lines)
    enable_lines = Configurator.find_config_lines(file, probe_enable_lines)

    menu = []
    menu.append(Configs.ConfigGroup("Bed Dimension", bed_configs))
    menu.append(Configs.ConfigGroup("Probe Offsets", offset_configs))
    menu.append(Configs.ConfigGroup("Probe Motion", travel_configs))
    menu.append(Configs.ConfigGroup("Servo Properties", servo_configs))
    menu.append(Configs.ConfigGroup("Enables", enable_lines))

    return menu

def save_all_configs(file, new_configs):
    Configurator.write_new_config(file, new_configs)
