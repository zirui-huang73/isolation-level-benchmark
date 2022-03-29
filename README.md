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
1. run setup script for db table set up
python3 setup.py
2. run a single test case: for example `./script.sh <anomaly> <isolation-level> <process-num>`, for example: `./script.sh LU S 10`
3. analyze statistics:
+ run `python3 statistics.py`

+ To run all test cases
1. `./run.sh <process-num>`, for example: `./run.sh 10`
2. analyze statistics:
+ run `python3 statistics.py`

