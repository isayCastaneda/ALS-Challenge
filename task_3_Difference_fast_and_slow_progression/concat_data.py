import subprocess
import numpy as np 
import time
import concurrent.futures
from os import listdir
import pandas as pd
# Get path where vcf per user are saved and get the id, put the id vcf user in csv file
vcf_paths = "/home/jupyter/end-als/genomics-data/vcfUsers/"
vcf_list_dir = listdir(vcf_paths) # list of vcf paths

for vcf_user in vcf_list_dir:
    # split vcf to get only the prefix (ind_001)
    output_file = vcf_user.split(".")[0]
    # paste complete vcf poath location 
    complete_vcf_path = vcf_paths + vcf_user
    # Get Id of vcf file by command line and convert in txt file
    batch_command = 'head -10000 {vcf} | grep "#CHROM" > {outputFileFormat}.txt'.format(vcf = complete_vcf_path, outputFileFormat=output_file) # Line -10000 show the firs columns of vcf table, show the user id 
    subprocess.run(batch_command, shell=True)
    # read txt file and change format to CSV file
    vcf_df = pd.read_csv(output_file + ".txt", sep='\t')
    # generate file wit id of patient
    vcf_df[output_file]=""
    vcf_df.to_csv(output_file +".csv")

# Getting csv from above code
path_csv_files = './csvFiles/'
list_csv = listdir(path_csv_files)
# creating dataframe to append results
csv_ids = pd.DataFrame(columns=['individual_id', 'cod_id'])

# create csv file with all ids
for csv in list_csv:
    if csv == '.ipynb_checkpoints':
        continue
    csv_names =  pd.read_csv('./csvFiles/'+ csv)
    csv_ids = csv_ids.append({'individual_id':csv_names.columns[11], 'cod_id': csv_names.columns[10]}, ignore_index=True)

# read CSV where Ids of  trasncript data are
matched_id = pd.read_csv('matched_ids.tsv', sep='\t')
    # merge id with the ids of abouve code
all_ids = csv_ids.merge(matched_id, how='left', left_on='cod_id', right_on='#VCF_ID').drop(['cod_id', 'SCORE'],axis=1)


all_vcf_file_result_path = '/home/jupyter/allVcfResults/'
all_vcf_file_result_list = listdir(all_vcf_file_result_path)

for id in all_vcf_file_result_list:
    rename_id = all_ids.loc[all_ids['individual_id'] == id, 'DATASET_ID'].reset_index(drop=True)[0]
    rename_batch_command = "mv "+ all_vcf_file_result_path + id + " " + rename_id
    subprocess.run(rename_batch_command, shell=True)

# Rename exomizer results
all_vcf_file_result_path = '/home/jupyter/allVcfExomizerResults/'
all_vcf_file_result_list = listdir(all_vcf_file_result_path)

for id in all_vcf_file_result_list:
    rename_id = all_ids.loc[all_ids['individual_id'] == id, 'DATASET_ID'].reset_index(drop=True)[0]
    #move data to actuall directory
    rename_batch_command = "mv "+ all_vcf_file_result_path + id + " " + rename_id
    subprocess.run(rename_batch_command, shell=True)

# concat exomizer result to get exomizer scores, this function generate dataset per column in "_AD.genes.tsv"
paths = 'results_vcf/' # results exomizer result path this files are renamed now
list_of_paths = listdir('results_vcf/')
global_information = []
# get columns of _AD.genes.tsv
columns = pd.read_csv('results_vcf/CASE-NEUAA599TMX/_AD.genes.tsv', sep="\t").columns[1:]
for column in columns:
    flag = True
    for case in list_of_paths:
        # concat _AD.genes.tsv
        complete_path = paths + case + '/' + '_AD.genes.tsv'
        temp_AD_df = pd.read_csv(complete_path, sep = '\t', usecols=['#GENE_SYMBOL', column]).rename(columns={column:case})
        
        if (flag):
            global_information = temp_AD_df
            flag = False
            continue
        #merge data per user by gene symbol
        global_information = global_information.merge(temp_AD_df, how='outer', on='#GENE_SYMBOL')
    global_information.to_csv(column + ".csv", index=False)
        
        