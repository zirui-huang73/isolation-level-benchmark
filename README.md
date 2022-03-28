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
1. run setup script for db table set up
python3 setup.py

2. run tests
+ for a single test case: for example `./script.sh <anomaly> <isolation-level> <process-num>`, for example: `./script.sh LU S 10`
+ for all test cases: `./run.sh <process-num>`, for example: `./run.sh 10`

3. analyze statistics:
+ run `python3 statistics.py <sub dirname>`