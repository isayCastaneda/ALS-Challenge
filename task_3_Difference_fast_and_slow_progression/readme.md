# To install exomizer run the follow command line 
 ```
sudo apt install default-jre -y
wget https://data.monarchinitiative.org/exomiser/latest/exomiser-cli-12.1.0-distribution.zip
unzip exomiser-cli-12.1.0-distribution.zip
cd exomiser-cli-12.1.0
mkdir data
cd data
wget https://data.monarchinitiative.org/exomiser/latest/2102_phenotype.zip
wget https://data.monarchinitiative.org/exomiser/latest/2102_hg38.zip 
unzip 2102_phenotype.zip
unzip 2102_hg38.zip
rm *zip
cd ..
nano application.properties  # change paths for directories and update data versions to 2102
nano analysis_als.yml   # create analysis
java -Xms2g -Xmx10g -jar exomiser-cli-12.1.0.jar --analysis analysis_als.yml  
```

- Follow the nexts steps to get VCF information 

  1. To get VCF information per user run process_vfc_data.py change the path information by the main vcf file
  2. Then run exomizer with run_exomizer.py, this dataset generet yml file per user please make sure that the path of main yml file is correct, also this file must be found in the exomizer folder.
  3. Run concat_data.py to cancatenate all data of exomizer result

- matched_ids.tsv is the bridge between originals ids and vcf ids

If you need help to run exomizer or change the path configuration please let me kwno to isay.castaneda@bowheadhealth.com
