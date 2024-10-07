from json import load


path:str = "models_dev/models.json"


def get_by_id(id:str) -> dict|None:
    with open(path,mode="r" ) as fp:
        _data = load(fp)
        result = _data.get(id)
        return result
    return None




print(get_by_id("9"))