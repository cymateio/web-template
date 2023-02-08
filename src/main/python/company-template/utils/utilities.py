import yaml
import os
import sys
import json


# This is only used in Test Class + Run Test
def read_config(file_path):
    basepath = os.path.realpath(os.path.dirname(__file__))
    config_directory = basepath.split("src/")[0] + "config/"
    with open(config_directory + file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def get_user_data(config):
    return config["user"]


def get_base_url(config):
    return config["base_url"]


def get_num_processes(config):
    return config["num_processes"]
