
import argparse
import utils
from FCECorpusHandler import FCECorpusHandler


""" Module to parse XML in Python using minidom
"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extracts transcript and summary from AMI Corpus.')
    parser.add_argument('--fce_xml_dir', type=str, default=utils.project_dir_name() + '/data/',
                        help='FCE Corpus download directory')
    parser.add_argument('--results_dir', type=str,
                        default=utils.project_dir_name() + '/data/fce_txt/',
                        help='FCE Corpus txt format')
    args = parser.parse_args()

    fceCorpusHandler = FCECorpusHandler(args)

    fceCorpusHandler.get_train_dev_test_sets()

    fceCorpusHandler.xml_to_txt(data_type="train")
    fceCorpusHandler.xml_to_txt(data_type="dev")
    fceCorpusHandler.xml_to_txt(data_type="test")
