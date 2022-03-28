import os, json
import sys

import numpy as np


if __name__ == '__main__':
    dirPath = 'logs'
    subDirPath = sys.argv[1]

    latencies = []
    numProceeded = 0
    numSucceeded = 0

    for file in os.listdir('{0}/{1}'.format(dirPath, subDirPath)):
        with open('{0}/{1}/{2}'.format(dirPath, subDirPath, file)) as json_file:
            content = json.load(json_file)
            for key, value in content.items():
                latencies.append(value['elapsed_time_second'])
                numProceeded += 1
                if value['return_status']:
                    numSucceeded += 1


    perc_50th = np.median(np.array(latencies))
    perc_95th = np.percentile(np.array(latencies), 95)
    perc_99th = np.percentile(np.array(latencies), 99)
    average = np.average(np.array(latencies))

    print('--------------Statistics--------------')
    print('Total number of transactions proceeded: {0}'.format(numProceeded))
    print('Total number of transactions succeeded: {0}'.format(numSucceeded))
    print('Average latency: {0} seconds'.format(average))
    print('50 percentile latency: {0} seconds'.format(perc_50th))
    print('95 percentile latency: {0} seconds'.format(perc_95th))
    print('99 percentile latency: {0} seconds'.format(perc_99th))



