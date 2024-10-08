from json import load


path:str = "models_dev/models.json"


def get_by_id(id:str) -> dict|None:
    with open(path,mode="r" ) as fp:
        _data = load(fp)
        result = _data.get(id)
        return result
    return None


def load_model_dev() -> dict:
    with open(path, mode="r") as fp:
        data = load(fp)
        return data
    


