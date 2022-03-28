process_num=$1
anomalies=("LU" "NR" "PR" "RS" "WS")
iso_levels=("RC" "RR" "S")
for anomaly in ${anomalies[*]}
do
    for iso_level in ${iso_levels[*]}
    do
        ./script.sh $anomaly $iso_level $process_num
    done
done