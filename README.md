<a className="gh-badge" href="https://datahub.io/core/airport-codes"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

## Description

Unicode character data from around the world. This dataset was sourced from the public domain resource at http://www.unicode.org/Public/UNIDATA/UnicodeData.txt, which aggregates information from various authoritative sources. The data is regularly updated to reflect the latest Unicode standards and character properties.

## Data

"data/unicode-characters.csv" contains the list of all Unicode characters, the attributes are identified in datapackage description.
Original source url is http://www.unicode.org/Public/UNIDATA/UnicodeData.txt  (stored in archive/source.csv)  

> Note: Currently the scripts is run automatically using Github Actions

## Preparation

You will need Python 3.6 or greater, to run the script

To update the data run the process script locally:
```bash
# To run locally you should do this
# Install using requirements
pip install -r scripts/requirements.txt
python3 scripts/process.py
```

## Automation

Montly updated 'Unicode Characters' datapackage could be found on the [datahub.io](http://datahub.io/):  
https://datahub.io/core/unicode-characters

## License

The source specifies that the data can be used as is without any warranty. Given size and factual nature of the data and its source from a US company would imagine this was public domain and as such have licensed the Data Package under the Public Domain Dedication and License (PDDL).
