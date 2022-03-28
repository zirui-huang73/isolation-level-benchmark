if [ $# != 3 ];then
	echo "Missing params. Usage: ./script anomaly iso_level process_num"
	echo "anomaly: LU NR PR RS WS"
	echo "iso_level: RC  RR  S"
	echo "process_num: number of processes to run concurrently"
	exit 1
fi

anomaly=$1
iso_level=$2
process_num=$3

for ((c = 0; c < $process_num; c++))
do
	exec python3 mainDriver.py $anomaly $iso_level &
done
	
