# isolation-level-benchmark

## Preparation
before start to run, configure database.ini like this:
```
[postgresql]
user=postgres
password=123456
database=postgres
```

## Testing
+ To run a single test case(for example: lost update with repeatable read level)
1. run setup script for db table set up: `python3 setup.py`
2. run the script for a single test case: 
+ `./script.sh <anomaly> <isolation-level> <process-num>` 
+ for example: `./script.sh LU S 10` is running the `./script.sh` for lost update anomaly, serializable isolation level, and with 10 processes.
3. analyze statistics:
+ run `python3 statistics.py`
+ this command will analyze data in all sub directories in "./logs" and return a report

+ To run all test cases
1. run the script for all test cases
+ `./run.sh <process-num>`
+ for example: `./run.sh 10` will run all tests of all anomalies with all isolation levels sequentially by calling `./script.sh`
2. analyze statistics:
+ run `python3 statistics.py`
+ this command will analyze data in all sub directories in "./logs" and return a report

