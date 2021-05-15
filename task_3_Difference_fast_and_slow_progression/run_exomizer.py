import yaml
import time
import concurrent.futures
from os import listdir
import subprocess
import yaml
import json

def execute_exomizer_parallel(vcf_user):
    print(vcf_user)
    vcf_path_file = "/home/ubuntu/jupyter_notebook/Volumes/jupyter/end-als/genomics-data/vcfUsers/" + vcf_user
    #take only patient id
    patient_id = vcf_user.split(".")[0]
    create_list_command = "mkdir /home/ubuntu/vcfResults/" + patient_id
    # creating folder to save vfc result
    subprocess.run(create_list_command, shell=True)
    # Read original yml template
    yaml_file = open("/home/ubuntu/analysis_als.yml")
    parsed_yml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
    # Change vcf input path
    parsed_yml_file ['analysis']['vcf'] = vcf_path_file
    # Chenge exomizer output path
    parsed_yml_file ['outputOptions']['outputPrefix'] = "/home/ubuntu/vcfResults/" + patient_id + "/"
    # Writing yml in user folder
    write_path = open("/home/ubuntu/vcfResults/" + patient_id +"/"+ patient_id + ".yml", "w")
    yaml.dump(parsed_yml_file, write_path)
     #run exomizer
    run_exomiser = "java -Xms2g -Xmx10g -jar /home/ubuntu/exomiser-cli-12.1.0/exomiser-cli-12.1.0.jar --analysis " + "/home/ubuntu/vcfResults/" + patient_id +"/"+ patient_id + ".yml"
    subprocess.run(run_exomiser, shell=True)

# Read all vcf per user 
vcf_list_paths = listdir("/home/ubuntu/jupyter_notebook/Volumes/jupyter/end-als/genomics-data/vcfUsers/")

# divide data in groups of 3 each core have 10gb of computer Ram 
start = time.perf_counter()
vcf_global_list = []
vcf_temporal_list = []
for i in range(len(vcf_list_paths)):
    vcf_temporal_list.append(vcf_list_paths[i])
    if ((i+1) % 3 == 0):
        vcf_global_list.append(vcf_temporal_list)
        vcf_temporal_list = []

for vcf in vcf_global_list:
    print(vcf)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(execute_exomizer_parallel, vcf)
        for result in results:
            print(result)

    finish = time.perf_counter()
    print("finished in {tiempo}".format(tiempo=round(finish-start, 2)))