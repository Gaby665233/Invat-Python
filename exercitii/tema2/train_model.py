import pandas as pd
import pickle

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    f1_score
)


# Folderul în care se află scriptul
BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = (
    BASE_DIR / "IMLP6_TASK_03-products.csv"
)

MODEL_FILE = (
    BASE_DIR / "product_classifier.pkl"
)


def create_features(data):
    """
    Creează caracteristici suplimentare
    din titlul produsului.
    """

    data = data.copy()

    data["title_length"] = (
        data["Product Title"].str.len()
    )

    data["word_count"] = (
        data["Product Title"]
        .str.split()
        .str.len()
    )

    data["digit_count"] = (
        data["Product Title"]
        .apply(
            lambda x: sum(
                char.isdigit()
                for char in x
            )
        )
    )

    data["special_char_count"] = (
        data["Product Title"]
        .apply(
            lambda x: sum(
                not char.isalnum()
                and not char.isspace()
                for char in x
            )
        )
    )

    data["uppercase_count"] = (
        data["Product Title"]
        .apply(
            lambda x: sum(
                char.isupper()
                for char in x
            )
        )
    )

    data["longest_word_length"] = (
        data["Product Title"]
        .apply(
            lambda x: max(
                [
                    len(word)
                    for word in x.split()
                ],
                default=0
            )
        )
    )

    return data


print("Încărcăm datele...")

df = pd.read_csv(DATA_FILE)


# Curățarea datelor
df = df.dropna(
    subset=[
        "Product Title",
        "Category Label"
    ]
).copy()


df["Product Title"] = (
    df["Product Title"]
    .astype(str)
    .str.strip()
)


df["Category Label"] = (
    df["Category Label"]
    .astype(str)
    .str.strip()
)


df = df[
    df["Product Title"] != ""
].copy()


df = df.drop_duplicates().copy()


# Eliminăm categoriile cu mai puțin de 2 produse
category_counts = (
    df["Category Label"]
    .value_counts()
)

valid_categories = (
    category_counts[
        category_counts >= 2
    ].index
)

df = df[
    df["Category Label"]
    .isin(valid_categories)
].copy()


# Feature engineering
df = create_features(df)


numeric_features = [
    "title_length",
    "word_count",
    "digit_count",
    "special_char_count",
    "uppercase_count",
    "longest_word_length"
]


feature_columns = [
    "Product Title"
] + numeric_features


X = df[feature_columns]

y = df["Category Label"]


# Împărțirea datelor
X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )
)


# Preprocesarea
preprocessor = ColumnTransformer(
    transformers=[
        (
            "text",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),
                min_df=2,
                max_features=30000
            ),
            "Product Title"
        ),
        (
            "numeric",
            StandardScaler(
                with_mean=False
            ),
            numeric_features
        )
    ]
)


models = {
    "Logistic Regression":
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        ),

    "Linear SVC":
        LinearSVC(
            class_weight="balanced"
        )
}


best_model = None
best_model_name = None
best_score = -1


for model_name, model in models.items():

    print("\nAntrenăm:", model_name)

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                model
            )
        ]
    )

    pipeline.fit(
        X_train,
        y_train
    )

    predictions = pipeline.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    macro_f1 = f1_score(
        y_test,
        predictions,
        average="macro",
        zero_division=0
    )

    print(
        f"Accuracy: {accuracy:.4f}"
    )

    print(
        f"Macro F1: {macro_f1:.4f}"
    )

    if macro_f1 > best_score:

        best_score = macro_f1

        best_model = pipeline

        best_model_name = model_name


print(
    "\nCel mai bun model:",
    best_model_name
)

print(
    "Macro F1:",
    round(best_score, 4)
)


# Salvăm modelul
with open(
    MODEL_FILE,
    "wb"
) as file:

    pickle.dump(
        best_model,
        file
    )


print(
    "\nModel salvat în:",
    MODEL_FILE
)