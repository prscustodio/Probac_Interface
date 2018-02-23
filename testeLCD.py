#Programa: Display LCD I2C com Raspberry Pi
#Autor: Arduino e Cia

import I2C_LCD_driver
import socket
import fcntl
import struct
import time

lcdi2c = I2C_LCD_driver.lcd()

#Exibe informacoes iniciais
lcdi2c.lcd_display_string("Arduino e Cia", 1,1)
lcdi2c.lcd_display_string("LCD I2C e RPi", 2,1)
time.sleep(4)

#Apaga o display
#lcdi2c.lcd_clear()



