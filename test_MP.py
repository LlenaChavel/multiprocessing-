# /cygdrive/c/Users/Lena Sheveleva/OneDrive - Cardiff University/MPF_Facts_And_Fiction/python
#which python /usr/bin/python

import time
from multiprocessing import Pool
import defs

if __name__ == '__main__':

    # Define the dataset
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    # Output the dataset
    print ('Dataset: ' + str(dataset))

    # Run this with a pool of 5 agents having a chunksize of 3 until finished
    agents = 30
    chunksize = 3
    start_time = time.time()
    with Pool(processes=agents) as pool:
        result = pool.map(defs.square, dataset, chunksize)
    
    duration = time.time() - start_time
    # Output the result
    print ('Result:  ' + str(result)+ str(duration)+ 'seconds')