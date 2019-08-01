## About
* Converts `XML` to `TXT` for use in [this repository](https://github.com/skasewa/wronging)
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
### 1. Source and target
Download FCE Corpus and convert to source and target `.txt` files
```
python main_xml_to_txt.py --fce_xml_dir data/ --results_dir data/fce_txt/
```
  + `fce_xml_dir`: directory where the FCE `.xml` Corpus will be downloaded
  + `results_dir`: directory where the `.txt` data will be saved

### 2. Vocab
Run [skasewa's script](https://github.com/skasewa/wronging/blob/master/seq2seq/bin/tools/generate_vocab.py):
```
python generate_vocab.py --max_vocab_size 20000 --downcase True --infile data/fce_txt/test/source.txt --outfile data/fce_txt/test/vocab.txt
python generate_vocab.py --max_vocab_size 20000 --downcase True --infile data/fce_txt/train/source.txt --outfile data/fce_txt/train/vocab.txt
python generate_vocab.py --max_vocab_size 20000 --downcase True --infile data/fce_txt/dev/source.txt --outfile data/fce_txt/dev/vocab.txt
```
> Script has also been added to this repository for future use

> Number of words: 4,495 (test), 17,770 (train), 4,119 (dev)

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
