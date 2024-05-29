from gpiozero import DigitalInputDevice, DigitalOutputDevice

# Define pins
#TODO: Define some kind of schema?
#TODO: Define correct pin numbers
#TODO: Allow some sort of configuration?
INPUT_PIN_RANGE = [i for i in range(1, 13)]
INPUT_PINS = [DigitalInputDevice(i) for i in INPUT_PIN_RANGE]

OUTPUT_PIN_RANGE = [i for i in range(14, 23)]
OUTPUT_PINS = [DigitalOutputDevice(i) for i in OUTPUT_PIN_RANGE]

class ByteReader:
    def __init__(self, input_pins = INPUT_PINS, output_pins = OUTPUT_PINS):
        self.input_pins = input_pins
        self.output_pins = output_pins

    def read_byte(self, address):
        for pin, bit in self.output_pins:
            up = (address >> bit) & 1
            if up:
                pin.on()
            else:
                pin.off()

        result = 0
        for pin, bit in self.input_pins:
            value = pin.is_active()
            result += value << bit
