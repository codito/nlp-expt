#!/usr/bin/env python

import json
import rdflib
import sys
import time

from itertools import chain
from rdflib.namespace import RDFS


def check_consistency(df, labels):
    # Set of all categories from our dataset
    categories = set(chain.from_iterable(df.categories.values))
    diffs = list(x for x in categories if x.lower() not in labels)
    print(diffs)


def convert_categories_to_json(g):
    start = time.time()
    mediawiki = rdflib.Namespace('https://www.mediawiki.org/ontology#')
    rel_incategory = mediawiki['isInCategory']
    rel_subcategories = mediawiki['subcategories']
    rel_pages = mediawiki['pages']

    data = {}
    labels_map = {}
    for c, n in g.subject_objects(predicate=RDFS.label):
        data[str(n)] = {'name': str(n), 'uri': str(c), 'broader': [],
                        'narrower': []}
        labels_map[str(c)] = str(n)

    for s, p, o in g:
        label = labels_map.get(str(s))
        object_label = labels_map.get(str(o))
        if not label or p == RDFS.label:
            continue

        if p == rel_subcategories:
            data[label]['subcategories'] = int(o)

        if p == rel_pages:
            data[label]['pages'] = int(o)

        if p == rel_incategory and object_label:
            data[label]['broader'].append(object_label)
            data[object_label]['narrower'].append(label)

    with open('categories.json', 'w', encoding='utf-8') as f:
        f.writelines([json.dumps(x) + '\n' for x in data.values()])
    print('Completed in {0:.2f}s'.format(time.time() - start))


def main(argv):
    # df = pd.read_json('dataset.json', orient='records', lines=True)
    g = rdflib.Graph()
    g.parse(source=argv[1], format='ttl')

    # Set of labels for all categories
    # labels = {l.value.lower() for l in g.objects(predicate=rdflib.RDFS.label)}
    # check_consistency(df, labels)
    convert_categories_to_json(g)


if __name__ == "__main__":
    main(sys.argv)
