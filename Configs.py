class ConfigItem:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ConfigGroup:
    def __init__(self, group_name, config_items):
        self.group_name = group_name
        self.config_items = config_items
