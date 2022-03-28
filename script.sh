
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

dateTime=$(date +'%Y-%m-%d-%H:%M:%S')

for ((c = 0; c < $process_num; c++))
do
  fileName="${dateTime}-$c"
	exec python3 mainDriver.py $anomaly $iso_level $fileName &
done
	
