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
        'uuid': "1a7c321e723211eb94390242ac130002", #Telemetry
        'characteristic': {
            "1a7c3796723211eb94390242ac130002": '98', #Batt %
            "1a7c38a4723211eb94390242ac130002": '7.2', #Batt V  
            "1a7c3976723211eb94390242ac130002": '2', #Internal State
            "1a7c3afc723211eb94390242ac130002": '123,456,789', #MU Euler
            "1a7c3bb0723211eb94390242ac130002": '12345,67890,67890,67890,67890', #Distance RAW
            "1a7c3c6e723211eb94390242ac130002": '12345,67890', #Encoder Tics
            "1a7c3f34723211eb94390242ac130002": '12345,67890', #Motor PWM
        }
    },
    {
        'uuid': "1a7c4006723211eb94390242ac130002", #Map
        'characteristic': {
            "1a7c40c4723211eb94390242ac130002": '123456789012345678901234567890', #Map
        }
    },
    {
        'uuid': "1a7c4a4c723211eb94390242ac130002", #Ctrl
        'characteristic': {
            "1a7c4b28723211eb94390242ac130002": '1,1,0', #Mode, r, fi
            "1a7c4bf0723211eb94390242ac130002": '7.2,', #RGB Led
            "1a7c4ff6723211eb94390242ac130002": '7.2,7.2,7.2', #PID
        }
    }
]