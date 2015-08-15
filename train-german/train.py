#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import codecs
from ctypes import c_char_p

import sys
import os
import re

from mitie import *


def get_tokens_from_sentence(opennlp_sentence):
    tokens = []
    entites = []
    entity_label = ""
    entity_start = 0
    for token_or_markup in opennlp_sentence.split():
        if re.match("<START:[^>]+>", token_or_markup):
            entity_start = len(tokens)
            entity_label = re.sub("<START:([^>]+)>", r"\1", token_or_markup)
        elif re.match("<END>", token_or_markup):
            entity = {"range": range(entity_start, len(tokens)), "label": entity_label}
            entites.append(entity)
            entity_label = ""
            entity_start = 0
        else:
            tokens.append(token_or_markup)
    return tokens, entites


def load_opennlp_samples(corpora_file):
    corpora_data = codecs.open(corpora_file, encoding='utf-8')
    corpora_samples = []
    for sentence in corpora_data:
        tokens, entities = get_tokens_from_sentence(sentence)
        opennlp_sample = ner_training_instance(tokens)
        for entity in entities:
            opennlp_sample.add_entity(entity["range"], c_char_p(entity["label"].encode('utf-8')))
        corpora_samples.append(opennlp_sample)
    return corpora_samples


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-i', '--input')
    parser.add_argument('-f', '--features')
    args = parser.parse_args()

    output_model = args.output
    corpora = args.input
    features_file = args.features

    trainer = ner_trainer(c_char_p(features_file.encode('utf-8')))
    samples = load_opennlp_samples(corpora)
    for sample in samples:
        trainer.add(sample)
    trainer.num_threads = 4
    ner = trainer.train()
    ner.save_to_disk(c_char_p(output_model.encode('utf-8')))

    # Testing
    tok = ["Ross", "Perot", "wäre", "vielleicht", "ein", "prächtiger", "Diktator", "."]
    extracted = ner.extract_entities(tok)
    print("\nEntities found:", extracted)
    for e in extracted:
        range = e[0]
        tag = e[1]
        entity_text = " ".join(tok[i] for i in range)
        print("    " + tag + ": " + entity_text)
