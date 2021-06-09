def get_files(directory):
    res = []
    for elem in os.listdir(directory):
        p = os.path.join(directory, elem)
        if os.path.isdir(elem): res.extend(get_files(p))
        else: res.append(p)
    return res