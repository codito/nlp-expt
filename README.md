A bunch of random experiments in NLP.

## Usage

```bash
# create a virtualenv, I usually install pandas etc. in system
> python -m venv .venv --system-site-packages
> source .venv/bin/activate

# in case you don't have base packages, install them in venv
> pip install sklearn pandas seaborn jupterlab

> pip install cython
> pip install -r requirements.txt

# create an ipython kernel to use the virtualenv
> ipython kernel install --user --name=nlp-expt
# modify the kernel.json file to include python executable from the venv

> jupyter lab
```

## Data

### Simplewiki

A cleaned and category labeled dataset of articles/pages in
<https://simple.wikipedia.org>.

See [data/simplewiki][simplewiki_data] and [README][simplewiki_readme].

[simplewiki_data]: https://github.com/codito/nlp-expt/blob/master/data/simplewiki/
[simplewiki_readme]: https://github.com/codito/nlp-expt/blob/master/data/simplewiki/README.md

## License
Datasets are licensed similar to the upstream licenses. Check individual
sections above.
