
if [ $# != 3 ];then
	echo "Missing params. Usage: ./script anomaly iso_level process_num"
	echo "anomaly: LU  PR  NR  RS  WS"
	echo "iso_level: RC  RR  S"
	echo "process_num: number of processes to run concurrently"
	exit 1
fi

anomaly=$1
iso_level=$2
process_num=$3

dateTime=$(date +'%Y%m%d%H%M%S')
fileName="${anomaly}-${iso_level}-${process_num}-${dateTime}"
>&2 echo "\n------start running cases for ${fileName}------\n"

for ((c = 0; c < $process_num; c++))
do
	python3 mainDriver.py $anomaly $iso_level $fileName $c &
	pids[${c}]=$!
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done

>&2 echo "\n------finish running cases for ${fileName}, all subprocess end------\n"
