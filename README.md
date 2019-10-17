[![DOI](https://zenodo.org/badge/199615833.svg)](https://zenodo.org/badge/latestdoi/199615833)

## About
* Converts `XML` to `TXT` for use in [this repository](https://github.com/skasewa/wronging)
* Extracts original and corrected essays from [FCE Corpus](https://www.ilexir.co.uk/datasets/index.html)

#### Contents
[Requirements](#requirements) • [FCE Corpus](#fce-corpus) • [How to Make](#how-to-make) • [How to Cite](#acknowledgement) 

## Requirements
* Tested on MacOS Mojave (10.14), Python 3.7.1
* Minidom: XML parser for Python

## FCE Corpus
* Cambridge Learner Corpus (CLC)'s First Certificate in English (FCE)
* 1,238 exam scripts taken in 2000 and 2001: 1,061 (train), 80 (dev), 97 (test)
* Dataset for error detection

## How to Make
### 1. Source and target
Download FCE Corpus and convert to source and target `.txt` files
```
python main_xml_to_txt.py --fce_xml_dir data/ --results_dir data/fce_txt/
```
  + `fce_xml_dir`: directory where the FCE `.xml` Corpus will be downloaded
  + `results_dir`: directory where the `.txt` data will be saved

### 2. Vocab
Run [script](https://github.com/google/seq2seq/blob/master/bin/tools/generate_vocab.py):
```
python generate_vocab.py --max_vocab_size 20000 --downcase True --infile data/fce_txt/test/source.txt --outfile data/fce_txt/test/vocab.txt
python generate_vocab.py --max_vocab_size 20000 --downcase True --infile data/fce_txt/train/source.txt --outfile data/fce_txt/train/vocab.txt
python generate_vocab.py --max_vocab_size 20000 --downcase True --infile data/fce_txt/dev/source.txt --outfile data/fce_txt/dev/vocab.txt
```
> Script has also been added to this repository for future use

> Number of words: 4,495 (test), 17,770 (train), 4,119 (dev)

## Acknowledgement
* Please star or fork if this code was useful for you. If you use it in a paper, please cite as:
  ```
  @misc{cunha_sergio2019fce_xml2txt,
      author       = {Gwenaelle Cunha Sergio},
      title        = {{gcunhase/FCECorpusXML: Converting FCE Corpus from XML to TXT format}},
      month        = oct,
      year         = 2019,
      doi          = {10.5281/zenodo.3496455},
      version      = {1.0.0},
      publisher    = {Zenodo},
      url          = {https://github.com/gcunhase/FCECorpusXML}
      }
  ```

* *Disclaimer*: This is not my dataset, but I found the need to convert it to a different format for use with [this model](https://github.com/skasewa/wronging), thus the creation of this repository.

  * Please read the [Licence Agreement](https://www.ilexir.co.uk/datasets/index.html) before use:
    ```
    The Dataset is released for non-commercial research and educational purposes under the following licence agreement:

        1. By downloading this dataset and licence, this licence agreement is entered into, effective this date, between you, the Licensee, and the University of Cambridge, the Licensor.
        2. Copyright of the entire licensed dataset is held by the Licensor. No ownership or interest in the dataset is transferred to the Licensee.
        3. The Licensor hereby grants the Licensee a non-exclusive non-transferable right to use the licensed dataset for non-commercial research and educational purposes.
        4. Non-commercial purposes exclude without limitation any use of the licensed dataset or information derived from the dataset for or as part of a product or service which is sold, offered for sale, licensed, leased or rented.
        5. The Licensee shall acknowledge use of the licensed dataset in all publications of research based on it, in whole or in part, through citation of the following publication: Yannakoudakis, Helen and Briscoe, Ted and Medlock, Ben, ‘A New Dataset and Method for Automatically Grading ESOL Texts’, Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies.
        6. The Licensee may publish excerpts of less than 100 words from the licensed dataset pursuant to clause 3.
        7. The Licensor grants the Licensee this right to use the licensed dataset ‘as is’. Licensor does not make, and expressly disclaims, any express or implied warranties, representations or endorsements of any kind whatsoever.
        8. This Agreement shall be governed by and construed in accordance with the laws of England and the English courts shall have exclusive jurisdiction.
    ``` 

  * Please refer to the following citation if you use the FCE Corpus:  
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
