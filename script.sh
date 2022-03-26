

if [ $# != 3 ];then
	echo "Missing params. Usage: ./script anomaly iso_level process_num"
	echo "anomaly: Lost-Update  Non-Repeatable-Read  Phantom-Read  Read-Skew  Write-Skew"
	echo "iso_level: RC  RR  S"
	echo "process_num: number of processes to run concurrently"
	exit 1
fi

anomaly=$1
iso_level=$2
process_num=$3

for ((c = 0; c < $process_num; c++))
do
	exec python mainDriver.py $anomaly $iso_level &
done
	
