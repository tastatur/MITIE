#!/bin/bash

#PIG Korpus ist riesig, um SVM trainieren zu können, soll er gekürzt werden. :( Ansonsten brauchen wir schnell > 24 GB RAM, und das habe ich nicht

python3.4 ./train.py -o $HOME/masterarbeit-data/mitte/training-out/pig-mt-model.dat -i $HOME/masterarbeit-data/mitte/corpora/pig-shrinked.train -f $HOME/masterarbeit-data/mitte/features-output/total_word_feature_extractor.dat -t $1
