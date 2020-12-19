#!/usr/bin/env bash
set -e

declare -r DEST="/media/$USER/CIRCUITPY"
if [ ! -d "$DEST" ]; then
    echo "ERROR: No such directory: $DEST"
    exit 1
fi

# Install files

# TODO: Some smarter way than this
declare -r FILE_LIST="
code.py
secrets.py
fonts/Roboto/Roboto-Regular-8.bdf
lib/adafruit_adt7410.mpy
lib/adafruit_bus_device/
lib/adafruit_esp32spi/
lib/adafruit_io/
lib/adafruit_register/
lib/neopixel.mpy
"
echo "$FILE_LIST" | xargs -n 1 cp -vRut "$DEST/" --parents
