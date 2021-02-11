# By Kami Bigdely-Shamloo
# Consolidate duplicate conditional fragments
# This program changes car's gear according to the car speed. Then it 
# displays the updated gear on the car's front panel.

def change_gear(str_gear):
    print("Gear changed to", str_gear)

def display_gear(str_gear): 
    print("displayed gear:", str_gear)

def get_gear(speed):
    if 0 <= speed < 30:
        return '1'
    if 30 <= speed < 50:
        return '2'
    if 50 <= speed <= 90:
        return '3'
    if 90 <= speed:
        return '4'
    if speed <= 0:
        return 'R'

def process_speed(speed):
    gear = get_gear(speed)
    change_gear(gear)
    display_gear(gear)

if __name__ == "__main__":
    process_speed(40)
