# Summary
We hypothesized that the difference in ALS progression results from the interaction of multiple pathways and these interactions are captured in the gene expression profile of the individuals. By comparing gene expression in a patient population, we can identify subgroups of patients and it allows us to assess if they were progressing fast or slow according to their clinical data. To identify the mechanisms involved in disease progression, we performed a differential expression analysis followed by pathway overrepresentation analysis.

We had access to gene expression data from motor neurons that were derived from induced pluripotent stem cells generated from 134 ALS patients. To eliminate technical noise and capture only the biology in the data, we normalized it and corrected it for the differentiation stages of the iPScells. Next, we performed unsupervised hierarchical clustering and we identified two main gene expression clusters.

We performed different statistical tests to assess the clinical relevance of the clusters and found significant differences in the ALS functional rating scale (ALSFRS) progression slope and the marker SB100, which are associated with disease progression. We did not observe any significance difference in age of symptom onset, sex, race, Escorial criteria, anatomical site of onset, ALS functional rating scale (ALSFRS) at baseline or latest measurements, cognitive behavior screen (CBS) scores (at baseline, latest measurement or progression slope)or in the rest of cell differentiation markers. The limited data provided did not allow us to test more clinical or environmental parameters

After observing the correlation of the clusters with variables related to disease progression, we assessed the difference in gene expression between the clusters. We identified 11362 genes that were differentially expressed after correcting for multiple testing (FDR<0.05). We then performed an overrepresentation pathways analysis at Reactome to identify the mechanisms in which these genes were involved stratifying by down- and up-regulated genes. The down-regulated genes are overrepresented significantly in multiple pathways (FILE link to git hub ).

# Data analysis

We started the analysis by exploring the data and removing the technical artefacts when possible. It is known that transcriptomic data is prone to batch effects and the fact that the iPScells could be in different differentiation stages, made data exploration and normalization our priority.

We first explored the normalized Deseq2 dataset by removing possible batch effects with a Multidimensional scaling (MDS) analysis. We then decided to look directly at the gene counts. To achieve this, we first extracted all the gene counts per patient from the different folders and created a matrix with gene counts and eliminated the control group.

The next step was to perform the normalization on the raw count matrix in edgeR. For this we removed genes with low reads and then generated a new MDS, but we still saw the heterogeneity.

# Quantile normalization 

As quartile normalization, followed by log transformation of the data has been suggested as a good approach to remove batch effects, we implemented it using limma. When we included all the genes, we saw a homogeneous model, but after removing the low count genes, we also see heterogeneity. We decided to use this data for further analysis including the staining markers for cell differentiation as covariates as suggested in one of the Kaggle discussions. We also included sex and race as covariates, as they affect gene expression. We also wanted to include age, as it affects the transcriptomic profile, but this was not possible, as there were many missing values in the data set.

# Remove batch effects
To identify subgroups of patients with different transcriptomic profiles we decided to follow an unsupervised clustering approach. However, for this approach we needed to remove the heterogeneity in the data caused by the different differentiation stages of the iPScells. We use the removeBatchEffect function in the limma package to correct for the staining markers. We included 5 out 6 markers as covariates, as nestin had 38 missing values. After generating a MDS plot, we did not observe any more heterogeneity in the data.

We did not use this correction for the differential expression analysis as this function is not intended to be used prior to linear modelling. Thus, for the differential expression analysis we continued using the markers as covariates.

# Clustering ands statistical test 
We extracted the individuals belonging to each cluster, Cluster1 contains 78 individuals, while Cluster2 has 46. To characterize the clusters and assess their clinical relevance and see if the differences were associated with the prognosis of ALS, we performed statistical tests comparing both clusters.


# Discussion
We observed a significant difference in the ALSFRS progression slope between the identified gene expression clusters.

We did not find any differences in the ALSFRS value at baseline or latest time point. This lack of differences may be due to problems with clinical source documentation and patient followup data. Some individuals only have one clinic visit and the clinical values for the baseline observation and latest time point appear as the same in the data portal table. The number of clinic visits at which the latest point was collected is variable and it is ad hoc and retrospective, resulting in too much variability. Without having robust, complete clinical data from all patients and the information of how this data was calculated it is difficult to draw accurate conclusions, thus we suggest to develop a well designed clinical protocol for key reference centers and include this information in the future.
For all the differential expression analysis performed during this project we have corrected for the cell differentiation stages by including the staining markers as covariates.

There were significant differences in S100B, an astrocyte marker. High levels of extracellular S100B may induce autocrine astrocytic activation that turns astrocytes into a proinflammatory and neurodegenerative phenotype (Villarreal et al. J Neurochem. 2014 Oct;131(2):190-205.) It has also been suggested that S100B expression might be an early occurring event in the ALS (Serrano et al. Mediators Inflamm. 2017; 2017: 1626204), so it might also be playing a role in the progression of the disease. We observed a higher percentage of cells with SB100 staining in Cluster1, suggesting they have more neurodegeneration than Cluster2. Moreover, SB100 protein positively correlates with a worse prognosis of ALS. (Sussmuth et al. Neurology. 2010;74(12):982–987)
Interestingly, after the differential expression analysis, we found that L13a-mediated translational silencing of Ceruloplasmin expression is regulated differently in Cluster1 compared to Cluster2, suggesting a higher expression of ceruloplasmin in Cluster one compared to cluster2. Ceruloplasmin is known to be altered in neurological diseases, as ceruloplasmin is related to iron/copper metabolism, it is linked to neurologic symptoms and signs. This result supports the idea that Cluster1 has more neurodegeneration and disease progression.
Selenocysteine synthesis is another pathway relevant to ALS, as it has been shown that the cerebrospinal fluid of ALS patients contains elevated levels of selenium species. A recent study suggests that these elevated levels result from mutations causing ALS, as they only observed this in a patient with a mutation in TUBA4A (Mandrioli Et al. Neurodegener Dis 2017;17:171-180). A further study comparing the genetic mutation from patients in Cluster1 with Cluster2 could help us to assess if there is indeed a genetic component involved in this pathway.

Other pathways potentially related to ALS include Response of EIF2AK4 (GCN2) to amino acid deficiency showing different regulation in Cluster1 compared to Cluster 2 are response of EIF2AK4 (GCN2) to amino acid deficiency, eukaryotic translation elongation and endosomal/vacuolar pathway.

One of the major limitations of our study is the number of missing values in the clinical data. We correlated the clusters to the data available in the data portal metadata, but when we tried the same with the parameters from other tables, we had many missing values. We consider that a more complete dataset would allow us to better assess the clinical relevance of these clusters.

In conclusion, we identified two subgroups of ALS patients that have different transcriptomic profiles. Main difference between the groups seems to be the neurodegeneration levels, as most of the pathways identified are related to it. Additionally, we observed differences in parameters associated with disease progression as the ALSFRS progression slope and the percentage of cells stained with SB100 were correlated. The pathway analysis at Reactome identified the mechanisms in which these genes were involved stratifying by down- and up-regulated genes. The down-regulated genes are overrepresented significantly in multiple pathways (FILE). The gene expression results and the identification of Cluster1 and Cluster2 will allow the generation of hypotheses that will be tested in the current dataset.