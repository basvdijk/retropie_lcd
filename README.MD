
## Setup
Run `raspi-config` and enable i2c in advanced options

`$ sudo apt-get install python-smbus`

`$ sudo i2cdetect -y 0`
`$ sudo i2cdetect -y 1`

## External libs
i2c_lib and lcd_display.py are taken from the [raspi-gpio](https://github.com/paulbarber/raspi-gpio) package by Paul Barber

## Thanks
Thanks to Paul Barber for creating [raspi-gpio](https://github.com/paulbarber/raspi-gpio)