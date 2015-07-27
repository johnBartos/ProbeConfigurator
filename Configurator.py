import Configs

def print_configs(config_set):
    for c in config_set:
        print(c.name + " " + c.value)

def find_config_lines(path, config_lines):
    config_set = []
    with open(path, 'rU') as file:
        for line in file:
            for config in config_lines:
                if(config in line):
                    pos = line.find(config) + len(config) + 1
                    val = line[pos:].strip()
                    config = Configs.ConfigItem(config, strip_comment(val))
                    config_set.append(config)
    return config_set

def write_new_config(old_file_path, new_file, config_set):
    with open(old_file_path, 'rU') as file:
        for line in file:
            did_write = 0
            for config in config_set:
                if(config.name in line):
                    line_to_write = (config.name + " " + config.value + "\n").encode('UTF-8')
                    new_file.write(line_to_write)
                    did_write = 1
                    break
            if (did_write != 1):
                new_file.write(line.encode('UTF-8'))
                did_write = 0

def strip_comment(line):
    comment_pos = line.find("//")
    if(comment_pos != -1):
        return line[:comment_pos].strip()
    return line
