# main.py
import time
import mapping
import navigation 
import math

# Global variables representing sensor data
R_ang = navigation.R_ang
L_ang = navigation.L_ang
acel = navigation.acel
direction = navigation.direction
x  = navigation.x
y = navigation.y


def main():
     
    try:
        map_instance = mapping.Map()
        #x, y= 1, 1  # Initial coordinates
        while True:
            x, y, direction = navigation.read_sensors(map_instance)  # Update global sensor values
            #print("x, y after reading sensors: ", x, ", ", y)
            x, y, direction = navigation.navigate(map_instance)  # Call navigation function
            print("x, y after navigation: ", x, ", ", y)
            time.sleep(1)  # Control loop frequency
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        # Clean up resources if needed
        pass

if __name__ == "__main__":
    main()