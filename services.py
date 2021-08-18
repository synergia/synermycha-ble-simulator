from consts import *

SERVICES = [
    {
        'uuid': UUID_SERVICE_DEVICE_INFO,
        'characteristic': {
            UUID_CHARACTERISTIC_MANUFACTURER_NAME: 'MKNMiR Synergia',
            UUID_CHARACTERISTIC_MODEL_NUMBER: 'fake',
            UUID_CHARACTERISTIC_FIRMWARE_REVISION: '9.9.9-dev',
            UUID_CHARACTERISTIC_SOFTWARE_REVISION: '8.8.8-dev',
            UUID_CHARACTERISTIC_HARDWARE_REVISION: 'rev3',
            UUID_CHARACTERISTIC_SERIAL_NUMBER: '1234567890',
        }
    },
    {
        'uuid': UUID_SERVICE_TELEMETRY, #Telemetry
        'characteristic': {
            UUID_CHARACTERISTIC_BATTERY_PERCENTAGE: '98', #Batt %
            UUID_CHARACTERISTIC_BATTERY_VOLTAGE: '7.2', #Batt V  
            UUID_CHARACTERISTIC_INTERNAL_STATE: '2', #Internal State
            UUID_CHARACTERISTIC_MU_EULER: '123,456,789', #MU Euler
            UUID_CHARACTERISTIC_DISTANCE_RAW: '12345,67890,67890,67890,67890', #Distance RAW
            UUID_CHARACTERISTIC_ENCODER_TICS: '12345,67890', #Encoder Tics
            UUID_CHARACTERISTIC_MOTOR_PWM: '12345,67890', #Motor PWM
        }
    },
    # {
    #     'uuid': UUID_SERVICE_MAP, #Map
    #     'characteristic': {
    #         UUID_CHARACTERISTIC_MAP: 'opopopop', #Map
    #     }
    # },
    # {
    #     'uuid': UUID_SERVICE_CONTROL, #Ctrl
    #     'characteristic': {
    #         UUID_CHARACTERISTIC_MODE: '1,1,0', #Mode, r, fi
    #         UUID_CHARACTERISTIC_LED_RGB: '7.2,', #RGB Led
    #         UUID_CHARACTERISTIC_PID: '7.2,7.2,7.2', #PID
    #     }
    # }
]