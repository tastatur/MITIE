#!/bin/bash

#PIG-Corpora ist für den SVM-Training einfach zu groß, um das Modell trainieren zu können, soll er gekürzt werden.

LINES=$(wc -l $1 | awk '{print $1}')

cd ~/masterarbeit-data/mitte/corpora/
SPLITSIZE=$((${LINES}/2))
split $1 -l $SPLITSIZE --additional-suffix=pig
cd -
