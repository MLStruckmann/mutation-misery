import numpy as np
import datetime

def log_write(results):
    results = [np.append(x[0], x[1][:2]) for x in results]
    file_name= f'{datetime.datetime.now():%Y%m%d_%H%M%S}' + '.csv'
    np.savetxt('results/'+ file_name, results, delimiter=";", fmt='%s')

    
