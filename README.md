The code and data for this paper ```Exploring Jiu-Jitsu Argumentation for Writing Peer Review Rebuttals```

# Dataset
The dataset is contained in the folder ```data``` (available in ). The code expects the data to be put in the data folder
----------------------------------------
The top level are the attitude roots:  
* Arg_other  
* Asp_clarity
* Asp_meaningful-comparison
* Asp_motivation-impact
* Asp_originality
* Asp_replicability
* Asp_substance

The attitude roots are categorized into the following folders:  
* actions (rebuttal actions such as rebuttal_answer, etc.)  
* rebuttal (the rebuttal sentences for the particular attitude theme)
* review (all the review sentences relevant to this attitude root)  

The top level also has the folder ```canonical_rebuttals_and_descs```. This contains the following files.  
* all_canonical_rebuttals_scores.tsv (contains all the canonical rebuttals with scores)  
* all_canonical_rebuttals.tsv (contains only the canonical rebuttals)
* all_cluster_descs.tsv (contains all the cluster descs)
* page_rank.py (contains the code used to run the page rank algorithm). 

# Codes
The codes used in this work are contained in the folder ```codes```.  Each of the tasks have seperate README files inside.
* end2end_review_to_canonical_rebuttal (code for the end to end canonical rebuttal generation task)
* rebuttal_identification (code for rebuttal identification task)
* rebuttal_scoring (code for the scoring task)
* review_to_desc (code for the review to description identification task)
