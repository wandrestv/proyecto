class Departamento:
    secuencia_departamento_edd = 5
    departamentos = [{"codigo":1,"departamento":"Gerencia"},
    {"codigo":2,"departamento":"Bodega"},
    {"codigo":3,"departamento":"Sistemas"},
    {"codigo":4,"departamento":"Ventas"},
    {"codigo":5,"departamento":"Control de Gestión"}
    ]
    def __init__(self,departamento_edd):
        Departamento.secuencia_departamento_edd += 1
        self.codigo_departamento_edd = Departamento.secuencia_departamento_edd
        self.departamento_edd = departamento_edd

    def registro_departamento_edd(self):
        return {"codigo":self.codigo_departamento_edd,"departamento":self.departamento_edd}