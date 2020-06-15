import numpy
import datetime

def log_write(results):
    file_name= f'{datetime.datetime.now():%Y%m%d_%H%M%S}' + '.csv'
    numpy.savetxt('results/'+ file_name, results, delimiter=";", fmt='%s')

    
