from json import load


path:str = "models_dev/models.json"


# Get
def get_by_id(id:str) -> dict|None:
    with open(path,mode="r" ) as fp:
        _data = load(fp)
        result = _data.get(id)
        return result
    return None


# Get
def get_all_pedidos() -> dict:
    with open(path, mode="r") as fp:
        data = load(fp)
        return data
    
    
# Post
def create_pedido(**kwargs):
    last_key = max(get_all_pedidos().keys())

    
    
    
def last_id() -> int:
    last_key = max(get_all_pedidos().keys())
    return last_key 