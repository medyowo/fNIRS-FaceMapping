def use():
    print(f"{'=' * 50}\nLOADING DATABASE\n{'=' * 50}")
    data, labels = data_transform.pretreat_data()

    print(f"{'=' * 50}\nUSE GENERATED MODELS\n{'=' * 50}")


if __name__ == "__main__":
    use()