#!/bin/bash

python3.4 ./train.py -o $HOME/masterarbeit-data/mitte/training-out/pig-mt-model.dat -i $HOME/masterarbeit-data/mitte/corpora/pig -f $HOME/masterarbeit-data/mitte/features-output/total_word_feature_extractor.dat -t $1
