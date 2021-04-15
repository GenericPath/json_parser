# Modified from
# https://github.com/cs230-stanford/cs230-code-examples/blob/master/tensorflow/vision/model/utils.py

import json, os, sys

class Params():
    """Class that loads hyperparameters from a json file.
    Example:
    ```
    params = Params(json_path)
    print(params.learning_rate)
    params.learning_rate = 0.5  # change the value of learning_rate in params
    ```
    """

    def __init__(self, json_path):
        self.update(json_path)

    def save(self, json_path):
        """Saves parameters to json file"""
        with open(json_path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    def update(self, json_path):
        """Loads parameters from json file"""
        if(os.path.exists(json_path)):
            with open(json_path) as f:
                params = json.load(f)
                self.__dict__.update(params)
        else:
            sys.exit("%s does not exist" % json_path)

    @property
    def dict(self):
        """Gives dict-like access to Params instance by `params.dict['learning_rate']`"""
        return self.__dict__