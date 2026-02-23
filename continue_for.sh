#!/bin/bash 
echo "Welcome to the house"
sleep 1
echo "Going Up! "
for x in {1..17};
do
	if [[ $x == 10 ]];then
		continue
	fi
	echo "Floor $x "
	sleep 1
done



