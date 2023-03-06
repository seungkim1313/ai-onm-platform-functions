def count_labels(label_list):
    counter = {}
    if not isinstance(label_list, list):
        raise TypeError("input must be a list")
    for label in label_list:
        if isinstance(label, list):
            sub_counter = count_labels(label)
            for key, val in sub_counter.items():
                if key in counter:
                    counter[key] += val
                else:
                    counter[key] = val
        else:
            if label in counter:
                counter[label] += 1
            else:
                counter[label] = 1
    return counter


if __name__ == "__main__":
    label_list = []
    print(count_labels(label_list))