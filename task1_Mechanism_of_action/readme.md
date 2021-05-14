# Summary
Amyotrophic lateral sclerosis (ALS) is associated with progressive loss of motor neurons in the motor cortex and spinal cord. Several mechanisms of neuronal death have been proposed; however, it is generally accepted that ALS is the end result of a deleterious interplay between genetic and environmental factors. Therefore, this interplay has multiple pathways modulated by complex underlying genetic factors. With this project we aimed to identify mechanisms playing a role in the disease by studying gene expression data that result from the interaction of genetic and environmental factors. We had access to gene expression data from motor neurons that were derived from induced pluripotent stem cells generated from 137 ALS patients and 32 healthy controls. It is likely that the sample size of patients and/or controls limited our ability to find differences.
Next, we hypothesized that the differences in gene expression levels between subgroups of ALS patients could allow us to identify the pathway or mechanisms playing a role in the disease pathophysiology. To achieve this, we performed unsupervised hierarchical clustering to identify subgroups of patients with different gene expression profiles. We found two main clusters with multiple subdivisions, Cluster1 and Cluster2.

After comparing the gene expression levels from Cluster1 to Cluster2 including sex, race and 5 differentiation markers as covariates, we identified 11366(change the number of genes and upgrade path way) genes that were differentially expressed after correcting for multiple testing (FDR<0.05). We then performed an overrepresentation pathways at Reactome (https://reactome.org/PathwayBrowser/#TOOL=AT) to identify the mechanisms in which these genes were involved stratifying by down- and up-regulated genes. The down-regulated genes are overrepresented significantly in multiple pathways (FILE path ways path)

# Data analysis

In order to identify mechanisms that differ from ALS patients and healthy individuals we performed a differential expression analysis to identify genes whose expression was regulated differently. However, we did not identify significant differences. This analysis was underpower due to the limited sample size available in the study, however a larger sample size may lead to identification of relevant pathways. The analysis could also be affected by the heterogeneity present in the cohort, either by the batch effects or the different stages of cell development, although we corrected for it in our model.
As the aim of our analysis was to capture the mechanism related to the ALS pathophysiology, we explored the data and removed the technical artifacts when possible. It is known that transcriptomic data is prone to batch defects and that the iPScells could introduce too much variability as they are in diverse cell differentiation stages. Therefore, we made data exploration and normalization our priority.
We started working with the provided normalized DeSeq2 dataset. To assess the possible batch effects, we performed a Multidimensional scaling (MDS) analysis. We observed two main clusters with overlapping cases and controls suggesting a possible technical issue.

We then decided to look directly at the gene counts. To achieve this, we first extracted all the gene counts per patient from the different folders and created a matrix with gene counts. We excluded the control with ID CTRL-NEUEU392AE8 because this file containes 17 files into the folder.

We then performed the normalization on the raw count matrix in edgeR. For this we removed genes with low reads and then generated a new MDS; continuing to observe heterogeneity.

We included 5 out 6 markers as covariates, as Nestin had 38 missing values. We removed 10 cases and 2 controls for this analysis because they had missing values for the markers.


As quartile normalization, followed by log transformation of the data has been suggested as a good approach to remove batch effects, we implemented it using limma. When we included all the genes, we saw a homogeneous model, but after removing the low count genes, we observed heterogeneity. We decided to use this data for further analysis including the staining markers for cell differentiation as covariates as suggested in one of the Kaggle discussions. We included sex and race as covariates, as they also affect gene expression. We wanted to include age, as it affects the transcriptomic profile, but this was not possible due to missing values in the data set.

In the differential expression analysis comparing cases with controls, no representative gene was found filtering by an FDR <0.05, so it is necessary to repeat the experiment only filtering the cases.

To identify subgroups of patients with different transcriptomic profiles we decided to follow an unsupervised clustering approach. However, for this approach we needed to remove the heterogeneity in the data caused by the different differentiation stages of the iPS cells. We use the removeBatchEffect function in the limma package to correct for the staining markers. After generating an MDS plot, we did not observe any more heterogeneity in the data.

We did not use this correction for the differential expression analysis as this function is not intended to be used prior to linear modelling. Thus, for the differential expression analysis we continued using the markers as covariates, but the data was used to genered heirarchical clustering.

In the first level of the dendrogram, we observed two main clusters with multiple smaller clusters. After some trial and error with a different number of sub-clusters, we decided to focus on the two main groups. We extracted the individuals belonging to each cluster, Cluster1 has 78 individuals, while Cluster2 has 46. 

After running a linear model including the covariates, we found 11,362 genes that were differentially expressed after correcting for multiple testing (FDR<0.05).

In order to extract the biological meaning of the identified genes, we performed overrepresentation analysis in Reactome (https://reactome.org/PathwayBrowser/#TOOL=AT). As input we introduced separately the genes that were down and up regulated, and selected the option “Project to human” for the analysis. The output of the analysis including the overrepresented genes can be found in XXX and XXX files.
# Discussion
Our top priority was to identify the mechanism playing a role in the disease by comparing gene expression differences in ALS patients compared to controls. However, we did not observe any significant difference between ALS patients and controls after correcting for multiple testing. It is likely that this lack of differential gene expression was due to limitations in the sample size.
We identified two main subgroups or clusters of gene expression with several subdivisions.
Interestingly, genes involved in L13a-mediated translational silencing of Ceruloplasmin expression are regulated differently in Cluster1 compared to Cluster2, suggesting a higher expression of ceruloplasmin in Cluster one compared to cluster2. Ceruloplasmin is known to be altered in neurological diseases, as ceruloplasmin is related to iron/copper metabolism, it is linked to neurologic symptoms and signs.
Selenocysteine synthesis is another pathway relevant to ALS, as it has been shown that the cerebrospinal fluid of ALS patients contains elevated levels of selenium species. A recent study suggests that these elevated levels result from mutations causing ALS, as they only observed this in a patient with a mutation in TUBA4A (Mandrioli Et al. Neurodegener Dis 2017;17:171-180). A further study comparing the genetic mutation from patients in Cluster1 with Cluster2 could help us to assess if there is indeed a genetic component involved in this pathway.
Other pathways potentially related to ALS include Response of EIF2AK4 (GCN2) to amino acid deficiency showing different regulation in Cluster1 compared to Cluster 2 are response of EIF2AK4 (GCN2) to amino acid deficiency, eukaryotic translation elongation and endosomal/vacuolar pathway.
In conclusion, our results showed that ALS is being caused by multiple pathways. We observe 2 main subgroups in the gene expression data set. These results suggest that ALS results from multiple interactions of genes that alter multiple pathways that converge in the phenotype. Each of the clusters identified in this study can have different altered pathway subdivisions that may assist in designing new approaches to target drug development or in subtyping the disease.