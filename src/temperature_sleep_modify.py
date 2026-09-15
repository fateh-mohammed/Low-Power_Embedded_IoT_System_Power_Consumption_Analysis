import machine # define pin. contains functions and classes that allow you to interact with the hardware components of the board, such as digital,analog pins, timers,internal sensors. It also provides functionality for low-power modes and interrupts.
import utime # measure time intervals and create time delays in your code. It includes functions like time.sleep() which allows you to pause the execution of your program for a specified number of seconds.

while True: # infinite loop. main loop. read inputs, perform calculations, and execute various tasks based on program logic.  interrupted by an external event: interrupt signal, or by a command to put the microcontroller into a low-power sleep mode.

    # machine.Pin() to initialize a digital pin and time.sleep() to pause the execution of your code for a specified duration.
    led=machine.Pin(6, machine.Pin.OUT)
    # Set up ADC to read the internal temperature sensor


    temp_sensor = machine.ADC(4)  # ADC channel 4 is the internal temperature sensor
    temp=temp_sensor.read_u16() #temp in 16bit
    led.value(1)
    sum=0
    
    
    ADC_voltage = temp * 3.3 / 65536 # 2^(16 bit) = 65536 integer number represents highest 3.3 volt integer  
    temp_celsius = 27-(ADC_voltage-0.706)/0.001721
    
    for i in range(8000):
        sum+=temp_celsius
        print("Temperature iteration:",i)
    
    # print("temp_sensor.read_u16(): {:.2f}".format(temp_sensor.read_u16()))
    print("Temperature: {:.2f}°C".format(sum)) #{:.2f}=3.14f,  {:d}=4d
    
    #sleep mode

    led.value(0)
    temp_sensor=None

    machine.deepsleep(3000)
    
    



