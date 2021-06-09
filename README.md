# Title Matcher - CSE 272 Final Project

**A project by [Anthony Liu](mailto:hliu35@ucsc.edu) and [Alex Salman](mailto:aalsalma@ucsc.edu)**

The primary task of this program is to retrieve all the names of datasets in given documents

Last modified 06/08/2021

## Competition Descriptions
[Kaggle competition main page](https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data)

[Dataset download page](https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data/data)

[Program output guide and sample](https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data/overview/evaluation)


## Features as of 06/09/2021
1. Exact Match
2. spaCy NER
3. ~Fuzzy Match~ (disabled due to slow performance)
4. Custom Hyperparamters
5. Optional Training During Each Run

## Our Design Thoughts (Brainstorming Canvas)
[Link to Google Docs](https://docs.google.com/document/d/1zjpbcx4N6viEDxbHI9Jovx2x2zH4h5xOCiHbn1oLfGM/edit)


## Useful Shell Commands
Installing required packages
``` bash
pip3 install -r requirements.txt
```

Store train data at location:
``` bash
dataset/train/
```

Store test data at location:
``` bash
dataset/test/
```

Running the program: use `jpyter notebook` to run
``` 
main.ipynb
```


## FAQ

_Q: Why this is an IR project instead of an hodgepodge of algorithms?_

A: There are 4 components of an Information Retrieval system, "acquisition", "representation", "file organization", and "query". Although we are working primarily on string matching, this process is essential for the "query" component, where a query like "how many time XXX dataset was mentioned" is passed in. Therefore, we must devise a robust platform where documents are efficiently processed and stored, and where queries like this would receive accurate feedbacks.




