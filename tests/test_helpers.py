import os

def load_test_file(filename):
    path = os.path.join(os.path.dirname(__file__), "test_data", filename)
    with open(path, "r") as f:
        return f.read()

def get_test_config(config_type):
    configs = {
        "terraform": "terraform.tf",
        "kubernetes": "k8s.yaml",
        "cloudformation": "cloudformation.json",
        "invalid": "invalid.txt"
    }
    return load_test_file(configs[config_type])