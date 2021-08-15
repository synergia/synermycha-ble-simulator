"""Example of how to create a Peripheral device/GATT Server"""
# Standard modules
import logging
import random

# Bluezero modules
from bluezero import async_tools
from bluezero import adapter
from bluezero import peripheral
from bluezero import tools
from consts import *
from services import SERVICES

l = tools.create_module_logger(__name__)
l.setLevel(logging.DEBUG)

cb_list = list()

def read_value():
    """
    Example read callback. Value returned needs to a list of bytes/integers
    in little endian format.
    This one does a mock reading CPU temperature callback.
    Return list of integer values.
    Bluetooth expects the values to be in little endian format and the
    temperature characteristic to be an sint16 (signed & 2 octets) and that
    is what dictates the values to be used in the int.to_bytes method call.
    :return: list of uint8 values
    """
    cpu_value = random.randrange(3200, 5310, 10) / 100
    # return list(int(cpu_value * 100).to_bytes(2, byteorder='little', signed=True))
    return list("yolo".encode())


def update_value(characteristic):
    """
    Example of callback to send notifications
    :param characteristic:
    :return: boolean to indicate if timer should continue
    """
    # read/calculate new value.
    new_value = read_value()
    # Causes characteristic to be updated and send notification
    characteristic.set_value(new_value)
    # Return True to continue notifying. Return a False will stop notifications
    # Getting the value from the characteristic of if it is notifying
    return characteristic.is_notifying


def notify_callback(notifying, characteristic):
    """
    Noitificaton callback example. In this case used to start a timer event
    which calls the update callback ever 2 seconds
    :param notifying: boolean for start or stop of notifications
    :param characteristic: The python object for this characteristic
    """
    if notifying:
        async_tools.add_timer_seconds(2, update_value, characteristic)

def read_value_callback_builder(service, characteristic):
    l.debug("Read char value %s %s", characteristic, str(service['characteristic'][characteristic]))
    return service['characteristic'][characteristic].encode()

def main(adapter_address):

    # Create peripheral
    peri = peripheral.Peripheral(adapter_address,
                                        local_name='SynerMycha Fake',
                                        appearance=1344)

    for serv_index, service in enumerate(SERVICES):
        peri.add_service(srv_id=serv_index, uuid=service["uuid"], primary=True)
        l.debug("Adding service %s", service["uuid"])

        for char_index, characteristic in enumerate(service['characteristic']):
            l.debug("Adding char %s %s", characteristic, service['characteristic'][characteristic].encode())

            cb_list.append(lambda: read_value_callback_builder(service, characteristic))
            peri.add_characteristic(srv_id=serv_index,
                                    chr_id=char_index,
                                    uuid=characteristic,
                                    flags=['read', 'notify'],
                                    value=service['characteristic'][characteristic].encode(),
                                    read_callback=cb_list[char_index],
                                    write_callback=None,
                                    notifying=True,
                                    notify_callback=notify_callback)



    # Add descriptor
    # cpu_monitor.add_descriptor(srv_id=1, chr_id=1, dsc_id=1, uuid=CPU_FMT_DSCP,
    #                            value=[0x0E, 0xFE, 0x2F, 0x27, 0x01, 0x00,
    #                                   0x00],
    #                            flags=['read'])
    # Publish peripheral and start event loop
    peri.publish()


if __name__ == '__main__':
    # Get the default adapter address and pass it to main
    main(list(adapter.Adapter.available())[0].address)
