import faker
import json
from random import randint


pedidos = {
    "1":{
        "name":"Mateus josé da silva",
        "date_entrada":"10-05-2021",
        "date_entrega":"12-05-2021",
        "valor":"160,00",
        "envio":"retirada",
    },
}
formas_envio = ("Correios-Sedex","Motoboy VIX","Retirada","Entrega Colatina")

fk = faker.Faker("pt-br")
data = []
temp = []

for n in range(10):
    name = fk.name()
    data_entrada = fk.date()
    date_entrega = fk.date()
    valor = round(float(randint(10,50) * (n +1 )),2)
    envio = formas_envio[randint(0,len(formas_envio)-1)]
    t = dict(name=name,data_entrada=data_entrada,date_entrega=date_entrega,value=valor,envio=envio)
    data.append(t.copy())
    t.clear()

k = range(len(data)-1)
d = dict(zip(k,data))
print(d)

with open("models_dev/models.json", "w+") as fp:
    json.dump(d,fp)