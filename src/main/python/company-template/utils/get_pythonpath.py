import os


def print_pythonpath():
    current_path = os.path.realpath(os.path.dirname(__file__))
    basepath = current_path.split("src")[0]
    all_paths = [
        "src/main/python/company-template",
        "src/main/python/company-template/pages",
        "src/main/python/company-template/tests",
        "src/main/python/company-template/utils",
    ]
    print("$PYTHONPATH:" + ":".join([basepath + i for i in all_paths]))


if __name__ == "__main__":
    print_pythonpath()
