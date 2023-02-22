import pytest
import datetime
import json
import os
from utils.utilities import *


def run_tests():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    # report_filename = f"report_{current_time}.html"

    user_data = read_config("test-data/user.yaml")
    config_data = read_config("config.yaml")
    config = {**user_data, **config_data}

    num_processes = config["num_processes"]
    conftest_dir = config["conftest_dir"]
    test_dir = config["test_dir"]

    log_format = "{} - {} - {}".format("%(asctime)s", "%(levelname)s", "%(message)s")
    log_level = config["log-level"]
    log_cli = config["log-cli"]
    log_dir_path = create_log_dir(current_time)

    distmode = config["distmode"]

    args = [
        "--numprocesses=" + num_processes,
        "--dist={}".format(distmode),
        "-m smoke",
        f"--junitxml=test-output/results/result_{current_time}.xml",
        "-W ignore",
        "-o",
        f"log_cli={log_cli}",
        "-o",
        f"log_cli_format={log_format}",
        "-o",
        f"log_cli_level={log_level}",
        "-o",
        f"log_format={log_format}",
        "-o",
        f"log_level={log_level}",
        "-o",
        f"log_file_format={log_format}",
        "-o",
        f"log_file_level={log_level}",
        # "-o", "log_file=test-output/logs/" + log_filename,
        f"--html=test-output/reports/report_{current_time}.html",
        "--confcutdir={}".format(conftest_dir),
        "--log-dir={}".format(log_dir_path),
        "--json-arg={}".format(json.dumps(config)),
        test_dir,
    ]

    pytest.main(args)


def create_log_dir(datetime_format):
    dir_format = "LOG_" + datetime_format
    dir_path = "test-output/logs/" + dir_format
    os.makedirs(dir_path)
    return dir_path


if __name__ == "__main__":
    run_tests()
