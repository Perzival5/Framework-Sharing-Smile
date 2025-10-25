
register = [
    {"id": "DR-TC15", "item": "first_name"},
    {"id": "DR-TC16", "item": "last_name"},
    {"id": "DR-TC17", "item": "date_of_birth"},
    {"id": "DR-TC18", "item": "sex"},
    {"id": "DR-TC19", "item": "country"},
    {"id": "DR-TC20", "item": "dni"},
    {"id": "DR-TC21", "item": "personal_email"},
    {"id": "DR-TC22", "item": "phone"},
    {"id": "DR-TC23", "item": "profession"},
    {"id": "DR-TC24", "item": "specialty"},
]

special = [
    {"id": "DR-TC26", "item": "first_name", "input": "!!!!!!"},
    {"id": "DR-TC27", "item": "last_name", "input": "@@@@@@"},
    {"id": "DR-TC56", "item": "date_of_birth", "input": "######"},
    {"id": "DR-TC57", "item": "sex", "input": "$$$$$$"},
    {"id": "DR-TC58", "item": "country", "input": "%"},
    {"id": "DR-TC59", "item": "dni", "input": "^^^^^^^^"},
    {"id": "DR-TC60", "item": "personal_email", "input": "&&&&&&&"},
]

date_birth = [
    {"id": "DR-TC28", "title": "mm/dd/aaaa", "item": "date_of_birth", "input": "07/28/1999"},
    {"id": "DR-TC29", "title": "aaaa/dd/mm", "item": "date_of_birth", "input": "1997/15/12"},
]

input_invalid = [
    {"id": "DR-TC31", "item": "sex", "input": "sin genero"},
    {"id": "DR-TC32", "item": "country", "input": "japon"},
    {"id": "DR-TC33", "item": "personal_email", "input": "esto no es un correo"},
    {"id": "DR-TC34", "item": "phone", "input": "letras"},
]

input_large = [
    {"id": "DR-TC36", "item": "first_name", "input": "AlejandroMaximilianoGonzalezFernandezSantosPerez"},
    {"id": "DR-TC37", "item": "last_name", "input": "RodriguezMartinezFernandezDelCampoGutierrezLopez"},
    {"id": "DR-TC40", "item": "city", "input": "CochabambaMetropolitanaZonaCentroIndustrialSur"},
    {"id": "DR-TC41", "item": "province", "input": "ChapareTropicalRegionNorteExtensaMontañosaCasa"},
    {"id": "DR-TC42", "item": "address", "input": "Av.HeroesDelChacoNro4567ZonaCentralEdificioLibertadPiso8DepartamentoBReferenciaPlazaColonFrenteABancoUnion"},
    {"id": "DR-TC43", "item": "dni", "input": "12345678901654"},
    {"id": "DR-TC44", "item": "personal_email", "input": "juan.perez.excedidolongituddemaasdasgagsdasfeciendecaracteresparaelcampodeemailprofesional@ejemplopruebalarga.com"},
    {"id": "DR-TC45", "item": "phone", "input": "7896541230911"},
    {"id": "DR-TC46", "item": "profession", "input": "IngenieroDesarrolladorDeSoftwareEspecialistaEnArquitecturaDeSistemasDistribuidosEmpresarialesCloudAmzonico"},
    {"id": "DR-TC47", "item": "specialty", "input": "NeurocirujanoEspecialistaEnMicrocirugiaCerebralYColumnaVertebralAvanzadaConEntrenamientoInternacionalCertificado"},
]

input_large_special_pro = [
    {"id": "DR-TC38", "item": "sex", "input": "masculinofemeninootro"},
    {"id": "DR-TC39", "item": "country", "input": "china"},
]

token = [
    {"id": "DR-TC49", "header":"header_login", "title":"sin autenticación", "message":"Not authenticated", "status":401},
    {"id": "DR-TC61", "header":"header_token_invalid", "title":"con token invalido", "message":"Invalid token", "status":401},
    {"id": "DR-TC62", "header":"header_without_permits", "title":"con token sin permisos", "message":"Not enough permissions", "status":403},
]

http_methods_invalid = [
    {"id": "DR-TC50", "item": "GET"},
    {"id": "DR-TC51", "item": "PUT"},
    {"id": "DR-TC52", "item": "DELETE"},
]

duplicate = [
    {"id": "DR-TC53", "item": "personal_email", "input":"profesional@project-x.com"},
    {"id": "DR-TC54", "item": "dni", "input":"70707070"},
    {"id": "DR-TC55", "item": "phone", "input":"70707070"},
]

valid_sex = [
    {"id": "DR-TC63", "item": "sex", "input":"masculino"},
    {"id": "DR-TC64", "item": "sex", "input":"femenino"},
]

valid_country = [
    {"id": "DR-TC65", "item": "country", "title": "Bolivia", "input" : "BO",},
    {"id": "DR-TC66", "item": "country", "title": "México", "input" : "MX",},
    {"id": "DR-TC67", "item": "country", "title": "Perú", "input" : "PE",},
    {"id": "DR-TC68", "item": "country", "title": "República Dominicana", "input" : "DO",},
    {"id": "DR-TC69", "item": "country", "title": "Estados Unidos", "input" : "US",},
    {"id": "DR-TC70", "item": "country", "title": "Argentina", "input" : "AR",},
    {"id": "DR-TC71", "item": "country", "title": "Brasil", "input" : "BR",},
]