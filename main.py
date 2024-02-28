import os
import csv
from time import sleep
from CG_RadSens import *

radSens = CG_RadSens(RS_DEFAULT_I2C_ADDRESS)

output_file = "output.txt"
csv_file = "data.csv"

def save_to_txt(data):
    with open(output_file, "a") as file:
        file.write(data + "\n")

def save_to_csv(data):
    with open(csv_file, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def setup():
    save_to_txt("Initializing RadSens...")
    radSens.init()

    while not radSens.init():
        save_to_txt("Sensor wiring error!")
        if not os.path.exists(csv_file):
            save_to_csv(["Error logs"])
        save_to_csv(["Sensor wiring error!"])

        loop()
        sleep(1)

    sensor_chip_id = radSens.get_chip_id()
    save_to_txt(f"Chip ID: 0x{sensor_chip_id:02X}")

    firmware_version = radSens.get_firmware_version()
    save_to_txt(f"Firmware version: {firmware_version}")

    save_to_csv(["Chip ID", "Firmware version"])
    save_to_csv([sensor_chip_id, firmware_version])

    save_to_txt("-------------------------------------")
    save_to_txt("Set Sensitivity example:\n")

    sensitivity = radSens.get_sensitivity()
    save_to_txt(f"\t getSensitivity(): {sensitivity}")

    save_to_csv(["Sensitivity"])
    save_to_csv([sensitivity])

    save_to_txt("\t setSensitivity(55)... ")
    radSens.set_sensitivity(55)
    sensitivity = radSens.get_sensitivity()
    save_to_txt(f"\t getSensitivity(): {sensitivity}")

    save_to_csv([sensitivity])

    save_to_txt("\t setSensitivity(105)... ")
    radSens.set_sensitivity(105)
    sensitivity = radSens.get_sensitivity()
    save_to_txt(f"\t getSensitivity(): {sensitivity}")

    save_to_csv([sensitivity])

    save_to_txt("-------------------------------------")
    save_to_txt("HV generator example:\n")

    hv_generator_state = radSens.get_hv_generator_state()
    save_to_txt(f"\n\t HV generator state: {hv_generator_state}")

    save_to_csv(["HV Generator State"])
    save_to_csv([hv_generator_state])

    save_to_txt("\t setHVGeneratorState(false)... ")
    radSens.set_hv_generator_state(False)
    hv_generator_state = radSens.get_hv_generator_state()
    save_to_txt(f"\t HV generator state: {hv_generator_state}")

    save_to_csv([hv_generator_state])

    save_to_txt("-------------------------------------")
    save_to_txt("LED indication control example:\n")

    led_state = radSens.get_led_state()
    save_to_txt(f"\n\t LED indication state: {led_state}")

    save_to_csv(["LED Indication State"])
    save_to_csv([led_state])

    save_to_txt("\t turn off LED indication... ")
    radSens.set_led_state(False)
    led_state = radSens.get_led_state()
    save_to_txt(f"\t LED indication state: {led_state}")

    save_to_csv([led_state])

    save_to_txt("\t turn on led indication... ")
    radSens.set_led_state(True)
    led_state = radSens.get_led_state()
    save_to_txt(f"\t LED indication state: {led_state}")

    save_to_csv([led_state])

    save_to_txt("\n-------------------------------------")
    sleep(5)

def loop():
    rad_intensity_dynamic = radSens.get_rad_intensy_dynamic()
    rad_intensity_static = radSens.get_rad_intensy_static()
    number_of_pulses = radSens.get_number_of_pulses()

    print("Rad intensity dynamic: ", rad_intensity_dynamic)
    print("Rad intensity static: ", rad_intensity_static)
    print("Number of pulses: ", number_of_pulses)

    save_to_txt("Rad intensity dynamic: " + str(rad_intensity_dynamic))
    save_to_txt("Rad intensity static: " + str(rad_intensity_static))
    save_to_txt("Number of pulses: " + str(number_of_pulses))

    save_to_csv([rad_intensity_dynamic, rad_intensity_static, number_of_pulses])

    sleep(2)

if __name__ == "__main__":
    setup()
    while True:
        loop()