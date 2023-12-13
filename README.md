# Exploring Jiu-Jitsu Argumentation for Writing Peer-Review Rebuttals 🥋
This repo includes codes that we used for the experiments in our EMNLP 2023 paper (main Conference)

```
Contact person: Sukannya Purkayastha

https://www.ukp.tu-darmstadt.de/

https://www.tu-darmstadt.de/

Don't hesitate to send us an e-mail or report an issue, if something is broken (and it shouldn't be) or if you have further questions.
```
> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication.

### Installation ⚙️
The easiest way to run the code in this repo is to use Anaconda. If you haven't installed it, you can find the installation guidelines here: https://docs.anaconda.com/anaconda/install/

Start by creating a new conda envirionment:
```python
conda create --name jitsupeer python=3.8
```

And activate it:
```python
conda activate jitsupeer
```

Install requirements:
```python
pip install -r requirements.txt
```

### Dataset 💾
The dataset should be contained in the folder ```data``` . You need to download the data from https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/4000 and put it in the ```data``` folder.

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

### Codes 🧑‍💻
The codes used in this work are contained in the folder ```codes```.  Each of the tasks has separate README files inside.
```
├── end2end_review_to_canonical_rebuttal (canonical rebuttal generation task)
├── rebuttal_scoring (scoring task)
├── review_to_desc (review-to-description identification task)
```


### Citation
If you find this repository helpful, feel free to cite the following paper:

```
@inproceedings{purkayastha-etal-2023-exploring,
    title = "Exploring Jiu-Jitsu Argumentation for Writing Peer Review Rebuttals",
    author = "Purkayastha, Sukannya  and
      Lauscher, Anne  and
      Gurevych, Iryna",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.894",
    pages = "14479--14495",
    abstract = "In many domains of argumentation, people{'}s arguments are driven by so-called attitude roots, i.e., underlying beliefs and world views, and their corresponding attitude themes. Given the strength of these latent drivers of arguments, recent work in psychology suggests that instead of directly countering surface-level reasoning (e.g., falsifying the premises), one should follow an argumentation style inspired by the Jiu-Jitsu {``}soft{''} combat system: first, identify an arguer{'}s attitude roots and themes, and then choose a prototypical rebuttal that is aligned with those drivers instead of trying to invalidate those. In this work, we are the first to explore Jiu-Jitsu argumentation for peer reviews by proposing the novel task of attitude and theme-guided rebuttal generation. To this end, we enrich an existing dataset for discourse structure in peer reviews with attitude roots, attitude themes, and canonical rebuttals. To facilitate this process, we recast established annotation concepts from the domain of peer reviews (e.g., aspects a review sentence is relating to) and train domain-specific models. We then propose strong rebuttal generation strategies, which we benchmark on our novel dataset for the task of end-to-end attitude and theme-guided rebuttal generation and two subtasks.",
}
```
