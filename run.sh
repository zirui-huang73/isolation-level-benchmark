anomalies=("LU" "NR" "PR" "RS" "WS")
iso_levels=("RC" "RR" "S")

for i in $(seq 1 10)
do
  for anomaly in ${anomalies[*]}
    do
    for iso_level in ${iso_levels[*]}
    do
        python3 setup.py
        ./script.sh $anomaly $iso_level $i
    done
  done
done

