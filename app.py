import os

import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

if __name__ == '__main__':
    pytest.main(["scripts/"])
