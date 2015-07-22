class ProbeBedConfig:
    def __init__(self, left, right, back, front):
        self.left = left #double
        self.right = right #double
        self.back = back #double
        self.front = front #double

class ProbeOffsetConfig:
    def __init__(self, x, y, z):
        self.x = x #double
        self.y = y #double
        self.z = z #double

class ProbeTravelConfig:
    def __init__(self, xy_speed, z_raise_before, z_raise_between):
        self.xy_speed = xy_speed #double
        self.z_raise_before = z_raise_before #double
        self.z_raise_between = z_raise_between #double

class ProbeServoConfig:
    def __init__(self, extend_angle, retract_angle):
        self.extend_angle = extend_angle #double
        self.retract_angle = retract_angle #double

class ProbeEnables:
    def __init__(self, min_endstops, auto_bed, servo_endstops, servo_angles):
        self.min_endstops = min_endstops #bool
        self.auto_bed = auto_bed #bool
        self.servo_endstops = servo_endstops #bool
        self.servo_angles = servo_angles #bool

class ProbeConfigs:
    def __init__(self, probe_bed, probe_offset, probe_travel, probe_servo, probe_enables):
        self.probe_bed = probe_bed
        self.probe_offset = probe_offset
        self.probe_travel = probe_travel
        self.probe_servo = probe_servo
        self.probe_enables = probe_enables

class ConfigItem:
    def __init__(self, name, value):
        self.name =name
        self.value = value
