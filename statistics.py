import os, json
import numpy as np

if __name__ == '__main__':
    dirPath = 'logs'
    latencies = []
    numProceeded = 0
    numSucceeded = 0
    numCorrect = 0

    for subDirPath in os.listdir('{0}'.format(dirPath)):
        for file in os.listdir('{0}/{1}'.format(dirPath, subDirPath)):
            with open('{0}/{1}/{2}'.format(dirPath, subDirPath, file)) as json_file:
                content = json.load(json_file)
                for key, value in content.items():
                    latencies.append(value['elapsed_time_second'])
                    numProceeded += 1
                    if value['succeed']:
                        numSucceeded += 1
                    if value['correct']:
                        numCorrect += 1

        perc_50th = np.median(np.array(latencies))
        perc_95th = np.percentile(np.array(latencies), 95)
        perc_99th = np.percentile(np.array(latencies), 99)
        average = np.average(np.array(latencies))

        print('--------------Statistics for {0}--------------'.format(subDirPath))
        print('Total number of transactions proceeded: {0}'.format(numProceeded))
        print('Total number of transactions succeeded: {0}'.format(numSucceeded))
        print('Total number of transactions correct: {0}'.format(numCorrect))
        print('Average latency: {:.3f} ms'.format(average * 1000))
        print('50 percentile latency: {:.3f} ms'.format(perc_50th * 1000))
        print('95 percentile latency: {:.3f} ms'.format(perc_95th * 1000))
        print('99 percentile latency: {:.3f} ms'.format(perc_99th * 1000))

        latencies.clear()
        numProceeded = 0
        numSucceeded = 0
        numCorrect = 0



