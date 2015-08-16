#!/bin/bash

#PIG-Corpora ist für den SVM-Training einfach zu groß, um das Modell trainieren zu können, soll er gekürzt werden.

LINES=$(wc -l $1 | awk '{print $1}')

cd ~/masterarbeit-data/mitte/corpora/
EXTRACTLINES=$((${LINES}/3))
sort -S 1G -R $1 | head -n $EXTRACTLINES > pig-shrinked.train
cd -
