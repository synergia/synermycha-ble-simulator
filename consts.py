BLUEZ_SERVICE_NAME = 'org.bluez'
LE_ADVERTISING_MANAGER_IFACE = 'org.bluez.LEAdvertisingManager1'
DBUS_OM_IFACE = 'org.freedesktop.DBus.ObjectManager'
DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'

LE_ADVERTISEMENT_IFACE = 'org.bluez.LEAdvertisement1'

GATT_MANAGER_IFACE = 'org.bluez.GattManager1'

GATT_SERVICE_IFACE = 'org.bluez.GattService1'
GATT_CHRC_IFACE =    'org.bluez.GattCharacteristic1'
GATT_DESC_IFACE =    'org.bluez.GattDescriptor1'

STANDARD_SUFFIX = "-0000-1000-8000-00805f9b34fb"

# DEVICE INFO SERVICE
UUID_SERVICE_DEVICE_INFO = '0000180a-0000-1000-8000-00805f9b34fb'
UUID_CHARACTERISTIC_MANUFACTURER_NAME = '00002a29-0000-1000-8000-00805f9b34fb'
UUID_CHARACTERISTIC_MODEL_NUMBER = '00002a24-0000-1000-8000-00805f9b34fb'
UUID_CHARACTERISTIC_SERIAL_NUMBER = '00002a25-0000-1000-8000-00805f9b34fb'
UUID_CHARACTERISTIC_FIRMWARE_REVISION = '00002a26-0000-1000-8000-00805f9b34fb'
UUID_CHARACTERISTIC_HARDWARE_REVISION = '00002a27-0000-1000-8000-00805f9b34fb'
UUID_CHARACTERISTIC_SOFTWARE_REVISION = '00002a28-0000-1000-8000-00805f9b34fb'

# BATTERY SERVICE
UUID_SERVICE_BATTERY = '0000180f-0000-1000-8000-00805f9b34fb'
UUID_CHARACTERISTIC_BATTERY_STATE = '00002a19-0000-1000-8000-00805f9b34fb'