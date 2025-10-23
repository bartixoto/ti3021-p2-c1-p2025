from datetime import date 

class Persona:
    def __init__(self,
                 rut: str,
                 nombres: str,
                 apellidos: str,
                 fecha_nacimiento: date,
                 cod_area: int,
                 telefono: int
    ):
        self.rut: str =rut
        self.nombres: str = nombres
        self.apellidos: str = apellidos
        self.fecha_nacimento: date = fecha_nacimiento
        self.cod_area: int = cod_area
        self.telefono: int = telefono


personas: list[Persona] = []
        
