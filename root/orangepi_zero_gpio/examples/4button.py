#!/usr/bin/env python
import os
import sys
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

# >>> from pyA20.gpio import port
# >>> dir(port)
# ['PA0', 'PA1', 'PA10', 'PA11', 'PA12', 'PA13', 'PA14', 'PA15', 'PA16', 'PA18', 'PA19', 'PA2', 'PA3', 'PA6', 'PA7', 'PG6', 'PG7', 'POWER_LED', 'STATUS_LED', '__doc__', '__file__', '__name__', '__package__']
# >>> from pyA20.gpio import connector
# >>> dir(connector)
# ['LEDp1', 'LEDp2', '__doc__', '__file__', '__name__', '__package__', 'gpio1p10', 'gpio1p11', 'gpio1p12', 'gpio1p13', 'gpio1p15', 'gpio1p16', 'gpio1p18', 'gpio1p19', 'gpio1p21', 'gpio1p22', 'gpio1p23', 'gpio1p24', 'gpio1p26', 'gpio1p3', 'gpio1p5', 'gpio1p7', 'gpio1p8']

button1 = connector.gpio1p10
button2 = connector.gpio1p11
button3 = connector.gpio1p12
button4 = connector.gpio1p13
button5 = connector.gpio1p15
button6 = connector.gpio1p16
button7 = connector.gpio1p18
button8 = connector.gpio1p19
button9 = connector.gpio1p21
button10 = connector.gpio1p22
button11 = connector.gpio1p23
button12 = connector.gpio1p24
button13 = connector.gpio1p26
button14 = connector.gpio1p3
button15 = connector.gpio1p5
button16 = connector.gpio1p7
button17 = connector.gpio1p8

gpio.init()

'''Set directions'''
gpio.setcfg(button1, gpio.INPUT)
gpio.setcfg(button2, gpio.INPUT)
gpio.setcfg(button3, gpio.INPUT)
gpio.setcfg(button4, gpio.INPUT)
gpio.setcfg(button5, gpio.INPUT)
gpio.setcfg(button6, gpio.INPUT)
gpio.setcfg(button7, gpio.INPUT)
gpio.setcfg(button8, gpio.INPUT)
gpio.setcfg(button9, gpio.INPUT)
gpio.setcfg(button10, gpio.INPUT)
gpio.setcfg(button11, gpio.INPUT)
gpio.setcfg(button12, gpio.INPUT)
gpio.setcfg(button13, gpio.INPUT)
gpio.setcfg(button14, gpio.INPUT)
gpio.setcfg(button15, gpio.INPUT)
gpio.setcfg(button16, gpio.INPUT)
gpio.setcfg(button17, gpio.INPUT)


'''Enable pullup resistor'''
gpio.pullup(button1, gpio.PULLUP)
gpio.pullup(button2, gpio.PULLUP)
gpio.pullup(button3, gpio.PULLUP)
gpio.pullup(button4, gpio.PULLUP)
gpio.pullup(button5, gpio.PULLUP)
gpio.pullup(button6, gpio.PULLUP)
gpio.pullup(button7, gpio.PULLUP)
gpio.pullup(button8, gpio.PULLUP)
gpio.pullup(button9, gpio.PULLUP)
gpio.pullup(button10, gpio.PULLUP)
gpio.pullup(button11, gpio.PULLUP)
gpio.pullup(button12, gpio.PULLUP)
gpio.pullup(button13, gpio.PULLUP)
gpio.pullup(button14, gpio.PULLUP)
gpio.pullup(button15, gpio.PULLUP)
gpio.pullup(button16, gpio.PULLUP)
gpio.pullup(button17, gpio.PULLUP)

value_out = 1
try:
    print ('Press CTRL+C to exit')
    while True:
        '''Since we use pull-up the logic will be inverted'''
        state1 = gpio.input(button1)      # Read button state
        state2 = gpio.input(button2)
        state3 = gpio.input(button3)
        state4 = gpio.input(button4)
        state5 = gpio.input(button5)
        state6 = gpio.input(button6)
        state7 = gpio.input(button7)
        state8 = gpio.input(button8)
        state9 = gpio.input(button9)
        state10 = gpio.input(button10)
        state11 = gpio.input(button11)
        state12 = gpio.input(button12)
        state13 = gpio.input(button13)
        state14 = gpio.input(button14)
        state15 = gpio.input(button15)
        state16 = gpio.input(button16)
        state17 = gpio.input(button17)

        sleep(.2)
        if ( state1 == False ):
                os.system('echo 1')
        if ( state2 == False ):
                os.system('echo 2')
        if ( state3 == False ):
                os.system('echo 3')
        if ( state4 == False ):
                os.system('echo 4')
        if ( state5 == False ):
                os.system('echo 5')
        if ( state6 == False ):
                os.system('echo 6')
        if ( state7 == False ):
                os.system('echo 7')
        if ( state8 == False ):
                os.system('echo 8')
        if ( state9 == False ):
                os.system('echo 9')
        if ( state10 == False ):
                os.system('echo 10')
        if ( state11 == False ):
                os.system('echo 11')
        if ( state12 == False ):
                os.system('echo 12')
        if ( state13 == False ):
                os.system('echo 13')
        if ( state14 == False ):
                os.system('echo 14')
        if ( state15 == False ):
                os.system('echo 15')
        if ( state16 == False ):
                os.system('echo 16')
        if ( state17 == False ):
                os.system('echo 17')

except KeyboardInterrupt:
    print ('Goodbye.')


