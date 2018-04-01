IC_PRODUCT_T825 = 1
TIC_PRODUCT_T834 = 2
TIC_PRODUCT_T500 = 3

#A setup packet bRequest value from USB 2.0 Table 9-4
USB_REQUEST_GET_DESCRIPTOR = 6

# A descriptor type from USB 2.0 Table 9-5
USB_DESCRIPTOR_TYPE_STRING = 3

# Generated by h2py e/tic_protocol.h with some spacing added manually
TIC_VENDOR_ID = 0x1FFB
TIC_PRODUCT_ID_T825 = 0x00B3
TIC_PRODUCT_ID_T834 = 0x00B5
TIC_PRODUCT_ID_T500 = 0x00BD

TIC_FIRMWARE_MODIFICATION_STRING_INDEX = 4

TIC_OPERATION_STATE_RESET = 0
TIC_OPERATION_STATE_DEENERGIZED = 2
TIC_OPERATION_STATE_SOFT_ERROR = 4
TIC_OPERATION_STATE_WAITING_FOR_ERR_LINE = 6
TIC_OPERATION_STATE_STARTING_UP = 8
TIC_OPERATION_STATE_NORMAL = 10

TIC_MISC_FLAGS1_ENERGIZED = 0
TIC_MISC_FLAGS1_POSITION_UNCERTAIN = 1

TIC_ERROR_INTENTIONALLY_DEENERGIZED = 0
TIC_ERROR_MOTOR_DRIVER_ERROR = 1
TIC_ERROR_LOW_VIN = 2
TIC_ERROR_KILL_SWITCH = 3
TIC_ERROR_REQUIRED_INPUT_INVALID = 4
TIC_ERROR_SERIAL_ERROR = 5
TIC_ERROR_COMMAND_TIMEOUT = 6
TIC_ERROR_SAFE_START_VIOLATION = 7
TIC_ERROR_ERR_LINE_HIGH = 8
TIC_ERROR_SERIAL_FRAMING = 16
TIC_ERROR_SERIAL_RX_OVERRUN = 17
TIC_ERROR_SERIAL_FORMAT = 18
TIC_ERROR_SERIAL_CRC = 19
TIC_ERROR_ENCODER_SKIP = 20

TIC_INPUT_STATE_NOT_READY = 0
TIC_INPUT_STATE_INVALID = 1
TIC_INPUT_STATE_HALT = 2
TIC_INPUT_STATE_POSITION = 3
TIC_INPUT_STATE_VELOCITY = 4

TIC_RESPONSE_DEENERGIZE = 0
TIC_RESPONSE_HALT_AND_HOLD = 1
TIC_RESPONSE_DECEL_TO_HOLD = 2
TIC_RESPONSE_GO_TO_POSITION = 3

TIC_PIN_NUM_SCL = 0
TIC_PIN_NUM_SDA = 1
TIC_PIN_NUM_TX = 2
TIC_PIN_NUM_RX = 3
TIC_PIN_NUM_RC = 4

TIC_PLANNING_MODE_OFF = 0
TIC_PLANNING_MODE_TARGET_POSITION = 1
TIC_PLANNING_MODE_TARGET_VELOCITY = 2

TIC_RESET_POWER_UP = 0
TIC_RESET_BROWNOUT = 1
TIC_RESET_RESET_LINE = 2
TIC_RESET_WATCHDOG = 4
TIC_RESET_SOFTWARE = 8
TIC_RESET_STACK_OVERFLOW = 16
TIC_RESET_STACK_UNDERFLOW = 32

TIC_PIN_STATE_HIGH_IMPEDANCE = 0
TIC_PIN_STATE_PULLED_UP = 1
TIC_PIN_STATE_OUTPUT_LOW = 2
TIC_PIN_STATE_OUTPUT_HIGH = 3

TIC_MIN_ALLOWED_BAUD_RATE = 200
TIC_MAX_ALLOWED_BAUD_RATE = 115385

TIC_DEFAULT_COMMAND_TIMEOUT = 1000
TIC_MAX_ALLOWED_COMMAND_TIMEOUT = 60000

TIC_MAX_ALLOWED_CURRENT = 3968
TIC_MAX_ALLOWED_CURRENT_T825 = 3968
TIC_MAX_ALLOWED_CURRENT_T834 = 3456
TIC_MAX_ALLOWED_CURRENT_T500 = 3093
TIC_MAX_ALLOWED_CURRENT_CODE_T500 = 32
TIC_CURRENT_LIMIT_UNITS_MA = 32

TIC_MIN_ALLOWED_ACCEL = 100
TIC_MAX_ALLOWED_ACCEL = 0x7FFFFFFF
TIC_MAX_ALLOWED_SPEED = 500000000

TIC_MAX_ALLOWED_ENCODER_PRESCALER = 0x7FFFFFFF
TIC_MAX_ALLOWED_ENCODER_POSTSCALER = 0x7FFFFFFF

TIC_SPEED_UNITS_PER_HZ = 10000
TIC_ACCEL_UNITS_PER_HZ2 = 100

TIC_CONTROL_MODE_SERIAL = 0
TIC_CONTROL_MODE_STEP_DIR = 1
TIC_CONTROL_MODE_RC_POSITION = 2
TIC_CONTROL_MODE_RC_SPEED = 3
TIC_CONTROL_MODE_ANALOG_POSITION = 4
TIC_CONTROL_MODE_ANALOG_SPEED = 5
TIC_CONTROL_MODE_ENCODER_POSITION = 6
TIC_CONTROL_MODE_ENCODER_SPEED = 7

TIC_SCALING_DEGREE_LINEAR = 0
TIC_SCALING_DEGREE_QUADRATIC = 1
TIC_SCALING_DEGREE_CUBIC = 2

TIC_STEP_MODE_FULL = 0
TIC_STEP_MODE_HALF = 1
TIC_STEP_MODE_MICROSTEP1 = 0
TIC_STEP_MODE_MICROSTEP2 = 1
TIC_STEP_MODE_MICROSTEP4 = 2
TIC_STEP_MODE_MICROSTEP8 = 3
TIC_STEP_MODE_MICROSTEP16 = 4
TIC_STEP_MODE_MICROSTEP32 = 5

TIC_DECAY_MODE_MIXED = 0
TIC_DECAY_MODE_SLOW = 1
TIC_DECAY_MODE_FAST = 2
TIC_DECAY_MODE_MODE3 = 3
TIC_DECAY_MODE_MODE4 = 4
TIC_DECAY_MODE_T825_MIXED = 0
TIC_DECAY_MODE_T825_SLOW = 1
TIC_DECAY_MODE_T825_FAST = 2
TIC_DECAY_MODE_T834_MIXED50 = 0
TIC_DECAY_MODE_T834_SLOW = 1
TIC_DECAY_MODE_T834_FAST = 2
TIC_DECAY_MODE_T834_MIXED25 = 3
TIC_DECAY_MODE_T834_MIXED75 = 4
TIC_DECAY_MODE_T500_AUTO = 0

TIC_PIN_PULLUP = 7
TIC_PIN_ANALOG = 6

TIC_PIN_FUNC_POSN = 0
TIC_PIN_FUNC_MASK = 0x0F
TIC_PIN_FUNC_DEFAULT = 0
TIC_PIN_FUNC_USER_IO = 1
TIC_PIN_FUNC_USER_INPUT = 2
TIC_PIN_FUNC_POT_POWER = 3
TIC_PIN_FUNC_SERIAL = 4
TIC_PIN_FUNC_RC = 5
TIC_PIN_FUNC_ENCODER = 6
TIC_PIN_FUNC_KILL_SWITCH = 7

TIC_CMD_SET_TARGET_POSITION = 0xE0
TIC_CMD_SET_TARGET_VELOCITY = 0xE3
TIC_CMD_HALT_AND_SET_POSITION = 0xEC
TIC_CMD_HALT_AND_HOLD = 0x89
TIC_CMD_RESET_COMMAND_TIMEOUT = 0x8C
TIC_CMD_DEENERGIZE = 0x86
TIC_CMD_ENERGIZE = 0x85
TIC_CMD_EXIT_SAFE_START = 0x83
TIC_CMD_ENTER_SAFE_START = 0x8F
TIC_CMD_RESET = 0xB0
TIC_CMD_CLEAR_DRIVER_ERROR = 0x8A
TIC_CMD_SET_MAX_SPEED = 0xE6
TIC_CMD_SET_STARTING_SPEED = 0xE5
TIC_CMD_SET_MAX_ACCEL = 0xEA
TIC_CMD_SET_MAX_DECEL = 0xE9
TIC_CMD_SET_STEP_MODE = 0x94
TIC_CMD_SET_CURRENT_LIMIT = 0x91
TIC_CMD_SET_DECAY_MODE = 0x92
TIC_CMD_GET_VARIABLE = 0xA1
TIC_CMD_GET_VARIABLE_AND_CLEAR_ERRORS_OCCURRED = 0xA2
TIC_CMD_GET_SETTING = 0xA8
TIC_CMD_SET_SETTING = 0x13
TIC_CMD_REINITIALIZE = 0x10
TIC_CMD_START_BOOTLOADER = 0xFF
TIC_CMD_GET_DEBUG_DATA = 0x20

# offsets/indexes
TIC_VAR_OPERATION_STATE = 0x00
TIC_VAR_MISC_FLAGS1 = 0x01
TIC_VAR_ERROR_STATUS = 0x02
TIC_VAR_ERRORS_OCCURRED = 0x04
TIC_VAR_PLANNING_MODE = 0x09
TIC_VAR_TARGET_POSITION = 0x0A
TIC_VAR_TARGET_VELOCITY = 0x0E
TIC_VAR_STARTING_SPEED = 0x12
TIC_VAR_MAX_SPEED = 0x16
TIC_VAR_MAX_DECEL = 0x1A
TIC_VAR_MAX_ACCEL = 0x1E
TIC_VAR_CURRENT_POSITION = 0x22
TIC_VAR_CURRENT_VELOCITY = 0x26
TIC_VAR_ACTING_TARGET_POSITION = 0x2A
TIC_VAR_TIME_SINCE_LAST_STEP = 0x2E
TIC_VAR_DEVICE_RESET = 0x32
TIC_VAR_VIN_VOLTAGE = 0x33
TIC_VAR_UP_TIME = 0x35
TIC_VAR_ENCODER_POSITION = 0x39
TIC_VAR_RC_PULSE_WIDTH = 0x3D
TIC_VAR_ANALOG_READING_SCL = 0x3F
TIC_VAR_ANALOG_READING_SDA = 0x41
TIC_VAR_ANALOG_READING_TX = 0x43
TIC_VAR_ANALOG_READING_RX = 0x45
TIC_VAR_DIGITAL_READINGS = 0x47
TIC_VAR_PIN_STATES = 0x48
TIC_VAR_STEP_MODE = 0x49
TIC_VAR_CURRENT_LIMIT = 0x4A
TIC_VAR_DECAY_MODE = 0x4B
TIC_VAR_INPUT_STATE = 0x4C
TIC_VAR_INPUT_AFTER_AVERAGING = 0x4D
TIC_VAR_INPUT_AFTER_HYSTERESIS = 0x4F
TIC_VAR_INPUT_AFTER_SCALING = 0x51

TIC_VARIABLES_SIZE = 0x55

# indexes
TIC_SETTING_NOT_INITIALIZED = 0x00
TIC_SETTING_CONTROL_MODE = 0x01
TIC_SETTING_NEVER_SLEEP = 0x02
TIC_SETTING_DISABLE_SAFE_START = 0x03
TIC_SETTING_IGNORE_ERR_LINE_HIGH = 0x04
TIC_SETTING_SERIAL_BAUD_RATE_GENERATOR = 0x05
TIC_SETTING_SERIAL_DEVICE_NUMBER = 0x07
TIC_SETTING_AUTO_CLEAR_DRIVER_ERROR = 0x08
TIC_SETTING_COMMAND_TIMEOUT = 0x09
TIC_SETTING_SERIAL_CRC_ENABLED = 0x0B
TIC_SETTING_LOW_VIN_TIMEOUT = 0x0C
TIC_SETTING_LOW_VIN_SHUTOFF_VOLTAGE = 0x0E
TIC_SETTING_LOW_VIN_STARTUP_VOLTAGE = 0x10
TIC_SETTING_HIGH_VIN_SHUTOFF_VOLTAGE = 0x12
TIC_SETTING_VIN_CALIBRATION = 0x14
TIC_SETTING_RC_MAX_PULSE_PERIOD = 0x16
TIC_SETTING_RC_BAD_SIGNAL_TIMEOUT = 0x18
TIC_SETTING_RC_CONSECUTIVE_GOOD_PULSES = 0x1A
TIC_SETTING_INVERT_MOTOR_DIRECTION = 0x1B
TIC_SETTING_INPUT_ERROR_MIN = 0x1C
TIC_SETTING_INPUT_ERROR_MAX = 0x1E
TIC_SETTING_INPUT_SCALING_DEGREE = 0x20
TIC_SETTING_INPUT_INVERT = 0x21
TIC_SETTING_INPUT_MIN = 0x22
TIC_SETTING_INPUT_NEUTRAL_MIN = 0x24
TIC_SETTING_INPUT_NEUTRAL_MAX = 0x26
TIC_SETTING_INPUT_MAX = 0x28
TIC_SETTING_OUTPUT_MIN = 0x2A
TIC_SETTING_INPUT_AVERAGING_ENABLED = 0x2E
TIC_SETTING_INPUT_HYSTERESIS = 0x2F
TIC_SETTING_CURRENT_LIMIT_DURING_ERROR = 0x31
TIC_SETTING_OUTPUT_MAX = 0x32
TIC_SETTING_SWITCH_POLARITY_MAP = 0x36
TIC_SETTING_ENCODER_POSTSCALER = 0x37
TIC_SETTING_SCL_CONFIG = 0x3B
TIC_SETTING_SDA_CONFIG = 0x3C
TIC_SETTING_TX_CONFIG = 0x3D
TIC_SETTING_RX_CONFIG = 0x3E
TIC_SETTING_RC_CONFIG = 0x3F
TIC_SETTING_CURRENT_LIMIT = 0x40
TIC_SETTING_STEP_MODE = 0x41
TIC_SETTING_DECAY_MODE = 0x42
TIC_SETTING_STARTING_SPEED = 0x43
TIC_SETTING_MAX_SPEED = 0x47
TIC_SETTING_MAX_DECEL = 0x4B
TIC_SETTING_MAX_ACCEL = 0x4F
TIC_SETTING_SOFT_ERROR_RESPONSE = 0x53
TIC_SETTING_SOFT_ERROR_POSITION = 0x54
TIC_SETTING_ENCODER_PRESCALER = 0x58
TIC_SETTING_ENCODER_UNLIMITED = 0x5C
TIC_SETTING_KILL_SWITCH_MAP = 0x5D
TIC_SETTING_SERIAL_RESPONSE_DELAY = 0x5E
TIC_SETTINGS_SIZE = 0x5F

TIC_BAUD_RATE_GENERATOR_FACTOR = 12000000
TIC_MAX_USB_RESPONSE_SIZE = 128
TIC_INPUT_NULL = 0xFFFF
TIC_CONTROL_PIN_COUNT = 5