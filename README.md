# Exploring Jiu-Jitsu Argumentation for Writing Peer-Review Rebuttals 
This repo includes codes that we used for the experiments in our EMNLP 2023 paper (main):

```
Contact person: Sukannya Purkayastha

https://www.ukp.tu-darmstadt.de/

https://www.tu-darmstadt.de/

Don't hesitate to send us an e-mail or report an issue, if something is broken (and it shouldn't be) or if you have further questions.
```
> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication.

### Dataset
The dataset is contained in the folder ```data``` (available in ). The code expects the data to be put in the data folder

The top level are the attitude roots: 
``` 
├── Arg_other  
├── Asp_clarity
├── Asp_meaningful-comparison
├── Asp_motivation-impact
├── Asp_originality
├── Asp_replicability
├── Asp_substance
```

The attitude roots are categorized into the following folders: 
``` 
├── actions (rebuttal actions such as rebuttal_answer, etc.)  
├── rebuttal (the rebuttal sentences for the particular attitude theme)
├── review (all the review sentences relevant to this attitude root)  
```

The top level also has the folder ```canonical_rebuttals_and_descs```. This contains the following files.  
```python
├── all_canonical_rebuttals_scores.tsv (contains all the canonical rebuttals with scores)  
├── all_canonical_rebuttals.tsv (contains only the canonical rebuttals)
├── all_cluster_descs.tsv (contains all the cluster descs)
```

### Codes
The codes used in this work are contained in the folder ```codes```.  Each of the tasks has separate README files inside.
```
├── end2end_review_to_canonical_rebuttal (code for the end-to-end canonical rebuttal generation task)
├── rebuttal_identification (code for rebuttal identification task)
├── rebuttal_scoring (code for the scoring task)
├── review_to_desc (code for the review-to-description identification task)
```


### Citation
If you find this repository helpful, feel free to cite the following paper:

```
@misc{purkayastha2023exploring,
      title={Exploring Jiu-Jitsu Argumentation for Writing Peer Review Rebuttals}, 
      author={Sukannya Purkayastha and Anne Lauscher and Iryna Gurevych},
      year={2023},
      eprint={2311.03998},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
