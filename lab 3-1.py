import machine
import utime

z=1
j=1
# Define GPIO pins connected to 7-segment display (5641AS)
segments = [14, 16, 13, 3, 5, 11, 15]

# Define common pins for a 4-digit display
common_pins = [18, 19, 20, 21]

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
def display_digit(digit, common_pin):
    # Turn off all common pins
    for pin in common_pins:
        machine.Pin(pin).value(1)  # 1 for common anode

    # Turn on the selected common pin
    machine.Pin(common_pin).value(0)  # 0 for common anode

    # Display the segments for the digit
    for pin, state in zip(segments, digit_segments[digit]):
        machine.Pin(pin).value(state)

def first_digit():
    for i in range(0,10,1):
        display_digit(i,18)
        utime.sleep(0.1)
    
for s in range(0,1,1):
    first_digit()
    
for a in range(0,99,1):
    for y in range(0,10,1):
        display_digit(z,19)
        utime.sleep(0.1)
        display_digit(y,18)
        utime.sleep(0.1)
        if(y == 9):
            z+=1

            
        
            

            
        
    
        
        
    


