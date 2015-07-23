import Configurator
import Configs
probe_bed_lines = ["#define LEFT_PROBE_BED_POSITION", "#define RIGHT_PROBE_BED_POSITION", "#define BACK_PROBE_BED_POSITION", "#define FRONT_PROBE_BED_POSITION"]
probe_offset_lines = ["#define X_PROBE_OFFSET_FROM_EXTRUDER", "#define Y_PROBE_OFFSET_FROM_EXTRUDER", "#define Z_PROBE_OFFSET_FROM_EXTRUDER"]
probe_travel_lines = ["#define XY_TRAVEL_SPEED", "#define Z_RAISE_BEFORE_PROBING", "#define Z_RAISE_BETWEEN_PROBING"]
probe_servo_lines = ["#define NUM_SERVOS"]
probe_enable_lines = ["#define SERVO_ENDSTOPS", "#define SERVO_ENDSTOP_ANGLES"]

def get_user_input(full_config_set):
    new_configs = []
    for config in full_config_set:
        label = config.name + " (current: " + config.value + ") "
        new_val = input(label)
        new_configs.append(Configs.ConfigItem(config.name, new_val))
    return new_configs

def do_configuration():
    full_config_set = Configurator.find_config_lines(probe_bed_lines
                        + probe_offset_lines
                        + probe_travel_lines
                        + probe_servo_lines
                        + probe_enable_lines)
    new_configs = get_user_input(full_config_set)
    Configurator.write_new_config(new_configs)

def create_menu_options():
    menu = []
    menu.append(Configs.ConfigMenuItem("Bed Dimension", probe_bed_lines))
    menu.append(Configs.ConfigMenuItem("Probe Offsets", probe_offset_lines))
    menu.append(Configs.ConfigMenuItem("Probe Motion", probe_travel_lines))
    menu.append(Configs.ConfigMenuItem("Servo Properties", probe_servo_lines))
    return menu
