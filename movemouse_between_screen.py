#!/bin/bash

eval $(xdotool getmouselocation --shell)

if [ $Y -gt 1080 ]
then
    theta=0
	xdotool mousemove 953 540
else
    theta=180
	xdotool mousemove 962 1485
fi

eval $(xdotool getmouselocation --shell)
xdotool windowfocus $WINDOW
