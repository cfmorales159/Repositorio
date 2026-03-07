#!/bin/bash
echo "What do you want to check?"
read localhost

while true
do 
	if ping -q -c 2 -W 1 $localhost > /dev/null; then 
		echo "Hey, you're up!!"
		break
	else
		echo "$localhost is currently down."
	fi
	sleep 2 
done
