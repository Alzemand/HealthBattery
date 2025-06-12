#!/bin/bash

cp healthBattery.py healthbattery
chmod +x healthbattery
if [ -d "/usr/local/bin" ]; then
    sudo cp healthbattery /usr/local/bin/healthbattery
else
    echo "Error: /usr/local/bin does not exist. Please check your system configuration."
    exit 1
fi
echo "healthbattery installed successfully. You can run it using the command 'healthbattery'."