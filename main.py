from time import sleep
from CG_RadSens import *

radSens = CG_RadSens(RS_DEFAULT_I2C_ADDRESS)

def setup():
    print("Initializing RadSens...")
    radSens.init()

    while not radSens.init():
        print("Sensor wiring error!")
        sleep(1)

    sensor_chip_id = radSens.get_chip_id()
    print(f"Chip ID: 0x{sensor_chip_id:02X}")

    firmware_version = radSens.get_firmware_version()
    print(f"Firmware version: {firmware_version}")

    print("-------------------------------------")
    print("Set Sensitivity example:\n")

    sensitivity = radSens.get_sensitivity()
    print(f"\t getSensitivity(): {sensitivity}")
    print("\t setSensitivity(55)... ")

    radSens.set_sensitivity(55)
    sensitivity = radSens.get_sensitivity()
    print(f"\t getSensitivity(): {sensitivity}")
    print("\t setSensitivity(105)... ")

    radSens.set_sensitivity(105)
    print(f"\t getSensitivity(): {radSens.get_sensitivity()}")
    print("-------------------------------------")
    print("HV generator example:\n")

    hv_generator_state = radSens.get_hv_generator_state()
    print(f"\n\t HV generator state: {hv_generator_state}")
    print("\t setHVGeneratorState(false)... ")

    radSens.set_hv_generator_state(False)
    hv_generator_state = radSens.get_hv_generator_state()
    print(f"\t HV generator state: {hv_generator_state}")
    print("\t setHVGeneratorState(true)... ")

    radSens.set_hv_generator_state(True)
    hv_generator_state = radSens.get_hv_generator_state()
    print(f"\t HV generator state: {hv_generator_state}")
    print("-------------------------------------")
    print("LED indication control example:\n")

    led_state = radSens.get_led_state()
    print(f"\n\t LED indication state: {led_state}")
    print("\t turn off LED indication... ")

    radSens.set_led_state(False)
    led_state = radSens.get_led_state()
    print(f"\t LED indication state: {led_state}")
    print("\t turn on led indication... ")

    radSens.set_led_state(True)
    led_state = radSens.get_led_state()
    print(f"\t LED indication state: {led_state}")
    print("\n-------------------------------------")
    sleep(5)

def loop():
    print("Rad intensity dynamic: ", radSens.get_rad_intensy_dynamic())
    print("Rad intensity static: ", radSens.get_rad_intensy_static())
    print("Number of pulses: ", radSens.get_number_of_pulses())
    sleep(2)

if __name__ == "__main__":
    setup()
    while True:
        loop()