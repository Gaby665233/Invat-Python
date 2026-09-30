- Product ID
- Product Title
- Merchant ID
- Category Label
- Product Code
- Number of Views
- Merchant Rating
- Listing Date

## Feature Engineering

Pe lângă titlul produsului au fost create următoarele caracteristici:

- lungimea titlului;
- numărul de cuvinte;
- numărul de cifre;
- numărul de caractere speciale;
- numărul de litere majuscule;
- lungimea celui mai lung cuvânt.

## Vectorizarea textului

Titlurile produselor sunt transformate în valori numerice folosind
TfidfVectorizer.

Sunt utilizate atât unigram-uri, cât și bigram-uri.

## Modele testate

Au fost comparate:

- Logistic Regression
- Linear SVC

Modelele sunt evaluate folosind:

- Accuracy
- Precision
- Recall
- F1-score
- Macro F1

Modelul final este ales pe baza scorului Macro F1.

## Structura proiectului

product-category-classifier/

- IMLP6_TASK_03-products.csv
- product_classification.ipynb
- train_model.py
- predict_category.py
- product_classifier.pkl
- requirements.txt
- README.md

## Instalare

Instalează bibliotecile necesare:

```bash
python -m pip install -r requirements.txt