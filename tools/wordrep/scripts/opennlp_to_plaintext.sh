#!/bin/bash

#Konvertiere OpenNLP-Korpus in PlainText
cat $1 | perl -pe 's/<END>//gi; s/<START:[^>]+>//gi' > $2/$(basename ${1}).txt
