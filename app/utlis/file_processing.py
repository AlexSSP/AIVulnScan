import os
import hashlib
import yaml
import hcl2

def compute_file_hash(file_path: str) -> str:
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            sha256.update(block)
    return sha256.hexdigest()

def parse_config_file(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    with open(file_path, "r") as f:
        content = f.read()

    if ext == ".json":
        return json.loads(content)
    elif ext == ".yaml" or ext == ".yml":
        return yaml.safe_load(content)
    elif ext == ".tf":
        return hcl2.loads(content)
    else:
        raise ValueError(f"Unsupported file format: {ext}")