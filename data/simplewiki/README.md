## Simplewiki dataset
This directory provides cleaned and labeled dataset from [simplewiki][].
[simplewiki]: https://simple.wikipedia.org/

* `simplewiki-20190820-pages-articles.json.7z` has the text and categories for each article.
* `simplewiki-20190824-categories.json.7z` has the categories and relations between them.

### Schema

Pages/Articles are formatted with one article per line. Each article has
following schema.
```json
{
  "id": "6",
  "url": "https://simple.wikipedia.org/wiki?curid=6",
  "title": "Art",
  "text": "Art description goes here",
  "categories": ["Non-verbal communication", "Basic English 850 words"]
}
```
Categories are formatted as a one category per line. Each category has following
schema.
```json
{
  "name": "Canadian food",
  "uri": "https://simple.wikipedia.org/wiki/Category:Canadian_food",
  "broader": ["Commons category link is on Wikidata", "Foods by nationality", "Canada"],
  "subcategories": 1, 
  "pages": 1,
  "narrower": ["Canadian food companies"]
}
```

### Source dumps

| Dataset type   | Source dump used | Latest dump link      |
|----------------|------------------|-----------------------|
| Pages/Articles | [20190820][]     | [Articles latest][]   |
| Categories     | [20190824][]     | [Categories latest][] |

[20190820]: https://dumps.wikimedia.org/simplewiki/20190820/simplewiki-20190820-pages-articles.xml.bz2
[20190824]: https://dumps.wikimedia.org/other/categoriesrdf/20190824/simplewiki-20190824-categories.ttl.gz

[Articles latest]: https://dumps.wikimedia.org/simplewiki/
[Categories latest]: https://dumps.wikimedia.org/other/categoriesrdf/latest

### Scripts
We have scripts available to clean the upstream sources.

1. Steps to extract and merge from upstream wikipedia dumps:
```bash
> bunzip2 simplewiki-20190820-pages-articles.xml.bz2
> # extract data to ./extract directory
> python WikiExtractor.py -o extract --json simplewiki-20190820-pages-articles.xml -q
> cat extract/**/wiki_* > dataset.json
```

2. Steps to extract and clean upstream categories data:
```bash
> gunzip simplewiki-20190824-categories.ttl.gz
> python WikiCategoryExtractor.py simplewiki-20190824-categories.ttl
# should output categories.json in current directory
```

See also https://codito.in/simple-wikipedia-dataset

**License**
> All text content is multi-licensed under the Creative Commons
> Attribution-ShareAlike 3.0 License (CC-BY-SA) and the GNU Free Documentation
> License (GFDL).

See https://en.wikipedia.org/wiki/Wikipedia:Database_download
