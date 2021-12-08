import os
from pathlib import Path
import json


CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "suffix.json")
PATH_FILE = os.path.join(CUR_DIR, "data", "path.json")

os.chmod(DATA_FILE, 0o0777)

DL_PATH = Path(os.path.join(Path.home() / "Downloads"))
DESKTOP = Path(os.path.join(Path.home() / "Desktop"))


class Data:

    def read_data(self) -> dict:
        """Read data from data/suffix.json"""
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)


    def _write_data(self, data):
        """Write data in Json file"""
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_suffix(self, suffix, directory) -> bool:
        """Write data in data/suffix.json"""
        suffixes_dict = Data().read_data()
        if not suffix in suffixes_dict:
            suffixes_dict[suffix] = directory
            Data()._write_data(suffixes_dict)
            return True
        return False

    def remove_data(self, suffix) -> bool:
        """Remove suffix from data file"""
        suffix_dict = Data().read_data()
        if suffix in suffix_dict:
            suffix_dict.pop(suffix)
            Data()._write_data(suffix_dict)
            return True
        return False


class PathToDir:

    def check_path(self, dir_path):
        return Path(dir_path)

    def write_path(self, dir_path):
        """Write path in json file"""
        if Path(dir_path).is_dir():
            with open(PATH_FILE, "w") as f:
                json.dump(dir_path, f)
                return True
        return False

    def read_path(self) -> str:
        """return path from Json file"""
        with open(PATH_FILE, "r", encoding='utf-8') as f:
            return json.load(f)






if __name__ == "__main__":
    d = PathToDir()
    #d.remove_data("tar.gz")
    # clean_folder(DL_PATH)
    # d.write_path("c://")
    # Data()._write_data(["2", "1"])


