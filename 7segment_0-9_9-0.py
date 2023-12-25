# 7-segment display (5641AS) without library on Raspberry Pi Pico

import machine
import utime

# Define GPIO pins connected to 7-segment display (5641AS)
segments = [14, 16, 13, 3, 5, 11, 15]

# Define the segments needed for each digit (0-9)
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

# Initialize GPIO pins
for pin in segments:
    machine.Pin(pin, machine.Pin.OUT)

# Function to display a digit on the 7-segment display
def display_digit(digit):
    for pin, state in zip(segments, digit_segments[digit]):
        machine.Pin(pin).value(state)

# Main loop
while True:
    # Display digits 0-9 repeatedly
    for digit in range(10):
        display_digit(digit)
        utime.sleep(1)  # Display each digit for 1 second

