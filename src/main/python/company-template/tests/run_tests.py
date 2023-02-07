import pytest
import datetime
import json
from utils.utilities import *

def run_tests():
    now = datetime.datetime.now()
    report_filename = f'report_{now.strftime("%Y-%m-%d_%H-%M-%S")}.html'

    user_data = read_config("test-data/user.yaml")
    config_data = read_config("config.yaml")
    config = {**user_data, **config_data}

    num_processes = config["num_processes"]
    conftest_dir = config["conftest_dir"]
    test_dir = config["test_dir"]

    args = [
        "-n " + num_processes,
        "--html=test-output/reports/" + report_filename,
        "--confcutdir={}".format(conftest_dir),
        "--json-arg={}".format(json.dumps(config)),
        test_dir
    ]
    pytest.main(args)

    

if __name__ == '__main__':
    run_tests()