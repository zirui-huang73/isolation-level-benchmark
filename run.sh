process_num=$1
iteration_num=$2
anomalies=("LU" "NR" "PR" "RS" "WS")
iso_levels=("RC" "RR" "S")
for anomaly in ${anomalies[*]}
do
    for iso_level in ${iso_levels[*]}
    do
        echo $anomaly, $iso_level, $process_num, $iteration_num
        exec ./script.sh $anomaly $iso_level $process_num $iteration_num &
    done
done