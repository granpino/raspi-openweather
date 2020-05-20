#!/bin/bash
#
#create shortcut


# create shortcut on desktop
 
touch weather.desktop
cat <<EOF > weather.desktop

#!/usr/bin/bash

[Desktop Entry]
Name=Openweather
Type=Application
Exec=lxterminal -t "WEATHER" --working-directory=/home/pi/raspi-openweather/ -e ./weather.sh
Icon=/home/pi/raspi-openweather/logo.png
Comment=test
Terminal=true

EOF

sudo chmod 755 weather.desktop
sudo mv weather.desktop /home/pi/Desktop
