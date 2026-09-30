import pandas as pd
import pickle

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODEL_FILE = (
    BASE_DIR / "product_classifier.pkl"
)


def create_features(data):

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


def prepare_product(title):

    product = pd.DataFrame(
        {
            "Product Title": [title]
        }
    )

    product = create_features(
        product
    )

    return product[
        [
            "Product Title",
            "title_length",
            "word_count",
            "digit_count",
            "special_char_count",
            "uppercase_count",
            "longest_word_length"
        ]
    ]


# Încărcăm modelul
with open(
    MODEL_FILE,
    "rb"
) as file:

    model = pickle.load(
        file
    )


print(
    "=================================="
)

print(
    " PRODUCT CATEGORY CLASSIFIER"
)

print(
    "=================================="
)

print(
    "Introdu titlul unui produs."
)

print(
    "Scrie 'exit' pentru a închide programul."
)


while True:

    title = input(
        "\nTitlul produsului: "
    )

    if title.lower().strip() == "exit":

        print(
            "Program închis."
        )

        break


    if title.strip() == "":

        print(
            "Introdu un titlu valid."
        )

        continue


    product = prepare_product(
        title
    )

    prediction = model.predict(
        product
    )[0]


    print(
        "Categoria prezisă:",
        prediction
    )