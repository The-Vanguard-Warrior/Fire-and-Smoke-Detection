import time
import serial

ser = serial.Serial('com4', 9600)

time.sleep(2)

def temp():
    """
    Get temperature from serial and print it.
    """
    ser.write('t'.encode())
    s = str(ser.readline())

    s = s[2:]

    s = s.split("\\", maxsplit=1)[0]
    print(s)

def humidity():
    """
    Get humidity from serial and print it.
    """
    ser.write('h'.encode())
    s = str(ser.readline())

    s = s[2:]

    s = s.split("\\", maxsplit=1)[0]
    print(s)
    

def main():
    """
    Main function to handle user input and call appropriate functions.
    """
    while True:
        user_input = input()
        if user_input == 't':
            temp()
        elif user_input == 'h':
            humidity()
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()