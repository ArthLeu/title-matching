# Title Matcher

**A project by Anthony Liu and Alex Salman**

Last modified 05/03/2021

## TODO:
1. Exact Match
2. spaCy NER
3. *Maybe* Fuzzy Match again? If it could be faster?
4. Hyperparameter Tunning
5. Training a best possible model.

## Brainstorming Canvas
[Link to Google Docs](https://docs.google.com/document/d/1zjpbcx4N6viEDxbHI9Jovx2x2zH4h5xOCiHbn1oLfGM/edit)


## Project Descriptions
[Kaggle competition main page](https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data)

[Dataset download page](https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data/data)

[Program output guide and sample](https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data/overview/evaluation)


## Useful Scripts
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

Running the program:
``` bash
python3 main.py
```

----
## FAQ

_Q: Why this is an IR project instead of an hodgepodge of algorithms?_

A: There are 4 components of an Information Retrieval system, "acquisition", "representation", "file organization", and "query". Although we are working primarily on string matching, this process is essential for the "query" component, where a query like "how many time XXX dataset was mentioned" is passed in. Therefore, we must devise a robust platform where documents are efficiently processed and stored, and where queries like this would receive accurate feedbacks.




