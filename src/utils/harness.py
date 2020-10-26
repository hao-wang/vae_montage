import os

from utils import list_dir


class Harness:
    def __init__(self, seed_dir):
        self._seed_dir = seed_dir
        self._harness_dict = {}
        self.build_dict()

    def build_dict(self):
        js_list = list_dir(self._seed_dir)

        for js_path in js_list:
            with open(js_path, 'r') as f:
                js_name = os.path.basename(js_path)
                for line in f:
                    line = line.strip()
                    if not self.is_load(line):
                        continue

                    harness = self.get_harness(line)
                    if not harness.endswith('.js'):
                        continue

                    if js_name not in self._harness_dict:
                        self._harness_dict[js_name] = []
                    self._harness_dict[js_name] += [harness]

    def get_keys(self):
        return self._harness_dict.keys()

    def get_harness(self, line):
        if line.startswith('load("'):
            delimiter = '"'
        elif line.startswith('load(\''):
            delimiter = '\''
        return self.extract_path(line, delimiter)

    def get_list(self, seed_name):
        if seed_name in self._harness_dict:
            return self._harness_dict[seed_name]
        else:
            return []

    def extract_path(self, line, delimiter):
        line = line.split(delimiter)
        load_path = line[1]
        return os.path.basename(load_path)

    def is_load(self, line):
        return (line.startswith('load("') or
                line.startswith('load(\''))
