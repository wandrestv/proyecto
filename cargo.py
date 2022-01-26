class Cargo:
    secuencia_cargo_edd = 12
    cargos = [{"codigo":1,"cargo":"Gerente general"},
    {"codigo":2,"cargo":"Asistente"},
    {"codigo":3,"cargo":"Gerente de Bodega"},
    {"codigo":4,"cargo":"Gerente de Sistemas"},
    {"codigo":5,"cargo":"Gerente Comercial"},
    {"codigo":6,"cargo":"Gerente de Calidad"},
    {"codigo":7,"cargo":"Gerente de Recursos Humanos"},
    {"codigo":8,"cargo":"Auxiliar de Bodega"},
    {"codigo":9,"cargo":"Atención al Cliente"},
    {"codigo":10,"cargo":"Equipo Técnico"},
    {"codigo":11,"cargo":"Vendedor"},
    {"codigo":12,"cargo":"Asistente de Recursos Humanos"},
    ]
    def __init__(self,cargo_edd):
        Cargo.secuencia_cargo_edd += 1
        self.codigo_cargo_edd = Cargo.secuencia_cargo_edd
        self.cargo_edd = cargo_edd

    def registro_cargo_edd(self):
        return {"codigo":self.codigo_cargo_edd,"cargo":self.cargo_edd}
