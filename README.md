## About
* Converts `XML` to `TXT`
* Extracts original and corrected essays from [FCE Corpus](https://www.ilexir.co.uk/datasets/index.html)

#### Contents
[FCE Corpus](#fce-corpus) • [Requirements](#requirements) • [How to Make](#how-to-make) • [Acknowledgement](#acknowledgement) 

## FCE Corpus
* Cambridge Learner Corpus (CLC)'s First Certificate in English (FCE)
* 1,238 exam scripts taken in 2000 and 2001: 1,061 (train), 80 (dev), 97 (test)
* Dataset for error detection

## Requirements
* Tested on MacOS Mojave (10.14), Python 3.7.1
* Minidom: XML parser for Python

## How to Make
Download FCE Corpus and convert to `.txt` files
```
python main_xml_to_txt.py
```

#### Configuration options

| **Argument**                      | **Type** | **Default**                       |
|-----------------------------------|----------|-----------------------------------|
| `fce_xml_dir`                     | string   | `"data/"`                         |
| `results_dir`                     | string   | `"data/fce_txt/"`          |
+ `fce_xml_dir` is the directory where the FCE Corpus will be downloaded
+ `results_dir` is the directory where the `TXT` data will be saved

## Acknowledgement
* Please star or fork if this code was useful for you.

* Disclaimer: This is not my dataset, but I found the need to convert it to a different format for my specific task and model, thus the creation of this repository. Please read the [Licence Agreement](https://www.ilexir.co.uk/datasets/index.html) and use the following citation if you use this dataset:  
```
@inproceedings{yannakoudakis2011new,
  title={A new dataset and method for automatically grading ESOL texts},
  author={Yannakoudakis, Helen and Briscoe, Ted and Medlock, Ben},
  booktitle={Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies-Volume 1},
  pages={180--189},
  year={2011},
  organization={Association for Computational Linguistics}
}
```
