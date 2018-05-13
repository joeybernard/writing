#!/bin/bash
LIST="0 1 2 3 4 5 6 7 8 9"
for INPUT in $LIST
do
echo "l($INPUT)/l(10)" | bc -l >>output.lst
done
