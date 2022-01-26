from cargo import Cargo
from departamento import Departamento

class Empleado:
    secuencia_empleado_edd = 4
    empleados = [{"codigo":1,"nombre":"Andrés","cedula":"0912457896","cargo":1,"departamento":1,"sueldo":1512.64},
    {"codigo":2,"nombre":"Daniel","cedula":"0954518403","cargo":3,"departamento":2,"sueldo":1212.35},
    {"codigo":3,"nombre":"Juan","cedula":"0932459878","cargo":4,"departamento":3,"sueldo":1312.91},
    {"codigo":4,"nombre":"David","cedula":"0954569832","cargo":5,"departamento":4,"sueldo":1412.74},
    ]

    def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo):
        Empleado.secuencia_empleado_edd += 1
        self.codigo_empleado = Empleado.secuencia_empleado_edd
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = codCargo
        self.departamento = codDepartamento
        self.sueldo = sueldo

    def registro_empleados(self):
        return{"codigo":self.codigo_empleado,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}
