#!/bin/bash

anomaly=$1
iso_level=$2

int=1
while(( $int<=50 ))
do
    python3 mainDriver.py $anomaly $iso_level
    let "int++"
done