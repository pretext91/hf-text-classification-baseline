from datasets import load_dataset


def load_text_classification_dataset(dataset_name: str):
    dataset = load_dataset(dataset_name)
    return dataset


if __name__ == "__main__":
    dataset = load_text_classification_dataset("fancyzhx/ag_news")
    print(dataset)
    print(dataset["train"][0])