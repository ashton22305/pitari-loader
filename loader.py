from gpiozero import DigitalInputDevice, DigitalOutputDevice

BIT_COUNT = 12

# Define pins
#TODO: Define some kind of schema?
#TODO: Define correct pin numbers
#TODO: Allow some sort of configuration?
INPUT_PINS = [
    DigitalInputDevice(0),
    DigitalInputDevice(1),
    DigitalInputDevice(2),
    DigitalInputDevice(3),
    DigitalInputDevice(4),
    DigitalInputDevice(5),
    DigitalInputDevice(6),
    DigitalInputDevice(7),
    DigitalInputDevice(8),
    DigitalInputDevice(9),
    DigitalInputDevice(10),
    DigitalInputDevice(11),
    DigitalInputDevice(12)
]

OUTPUT_PINS = [
    DigitalOutputDevice(13),
    DigitalOutputDevice(14),
    DigitalOutputDevice(15),
    DigitalOutputDevice(16),
    DigitalOutputDevice(17),
    DigitalOutputDevice(18),
    DigitalOutputDevice(19),
    DigitalOutputDevice(20)
]

class ByteReader:
    def __init__(self, input_pins = INPUT_PINS, output_pins = OUTPUT_PINS):
        self.input_pins = input_pins
        self.output_pins = output_pins

    def read_byte(address):
        for i in range(BIT_COUNT):
            self.input_pin