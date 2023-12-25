import machine
import utime

segments = [14, 16, 13, 3, 5, 11, 15]
common_pins = [18, 19, 20, 21]

digit_segments = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
]

def display_digit(digit, common_pin):
    # Turn off all common pins
    for pin in common_pins:
        machine.Pin(pin).value(1)  # 1 for common anode

    # Turn on the selected common pin
    machine.Pin(common_pin).value(0)  # 0 for common anode

    # Display the segments for the digit
    for pin, state in zip(segments, digit_segments[digit]):
        machine.Pin(pin).value(state)
        
def count_up_to_9999():
    for i in range(10000):
        thousands = i // 1000
        hundreds = (i // 100) % 10
        tens = (i // 10) % 10
        units = i % 10

        display_digit(thousands, 21)
        utime.sleep(0.1)
        display_digit(hundreds, 20)
        utime.sleep(0.1)
        display_digit(tens, 19)
        utime.sleep(0.1)
        display_digit(units, 18)
        utime.sleep(0.1)

def count_down_from_9999():
    for i in range(9999, -1, -1):
        thousands = i // 1000
        hundreds = (i // 100) % 10
        tens = (i // 10) % 10
        units = i % 10

        display_digit(thousands, 18)
        utime.sleep(0.1)
        display_digit(hundreds, 19)
        utime.sleep(0.1)
        display_digit(tens, 20)
        utime.sleep(0.1)
        display_digit(units, 21)
        utime.sleep(0.1)

# Main loop
while(1):
    count_up_to_9999()
    count_down_from_9999()
