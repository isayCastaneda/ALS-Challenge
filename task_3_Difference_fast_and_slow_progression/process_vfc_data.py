import subprocess
import numpy as np 
import time
import concurrent.futures
from os import listdir
import pandas as pd

# create funcion that read vcf file and cut by user line, this function allow parallelize each command per thread
def execute_bash_parallel(user):
    # bash command to get vcf files per user
    bashCommand = "gunzip -c /home/jupyter/end-als/genomics-data/AnswerALS_subset_annovar.hg38_anno_and_geno.no_intergenic.vcf.gz | cut -f1-9,{line} > /home/jupyter/end-als/genomics-data/vcfUsers/ind_00{n_user}.vcf".format(line=9+user, n_user=user)
    print("numero de usuario processado {u}".format(u=user))
    #execut bash command
    subprocess.run(bashCommand, shell=True)
    return 'Finish user {u}'.format(u=user)

if  __name__ == "__main__":
    start = time.perf_counter() # initializing counter to know how long it takes to perform the task
    number_users_in_vfc = np.arange(1,31) # It is necessary to put the number of users that the threads can support and the memory will be
    # initialize multi thread prosses
    with concurrent.futures.ProcessPoolExecutor() as executor: 
        results = executor.map(execute_bash_parallel, number_users_in_vfc)
        for result in results:
            print(result)
    
    finish = time.perf_counter() # finish time counter
    
    print("finished in {tiempo} ...".format(tiempo = round(finish-start, 2)))

    