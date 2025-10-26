
register = [
    {"id": "DR-TC166", "item": "first_name"},
    {"id": "DR-TC167", "item": "last_name"},
    {"id": "DR-TC168", "item": "date_of_birth"},
    {"id": "DR-TC169", "item": "sex"},
    {"id": "DR-TC170", "item": "country"},
    {"id": "DR-TC171", "item": "dni"},
    {"id": "DR-TC172", "item": "father_name"},
    {"id": "DR-TC173", "item": "mother_name"},
    {"id": "DR-TC174", "item": "ref_number_1"},
    {"id": "DR-TC175", "item": "fissure_type"},
]

valid_sex = [
    {"id": "DR-TC177", "item": "sex", "input":"masculino"},
    {"id": "DR-TC178", "item": "sex", "input":"femenino"},
]

valid_country = [
    {"id": "DR-TC179", "item": "country", "title": "Bolivia", "input" : "BO",},
    {"id": "DR-TC180", "item": "country", "title": "México", "input" : "MX",},
    {"id": "DR-TC181", "item": "country", "title": "Perú", "input" : "PE",},
    {"id": "DR-TC182", "item": "country", "title": "República Dominicana", "input" : "DO",},
]

valid_fissure_type = [
    {"id": "DR-TC183", "item": "fissure_type", "title": "Flap izquierdo", "input" : "Flap izq",},
    {"id": "DR-TC184", "item": "fissure_type", "title": "Flap Bilateral", "input" : "Flap Bilateral",},
    {"id": "DR-TC185", "item": "fissure_type", "title": "Flap derecho", "input" : "Flap der",},
]

special = [
    {"id": "DR-TC186", "item": "first_name", "input": "!!!!!!"},
    {"id": "DR-TC187", "item": "last_name", "input": "@@@@@@"},
    {"id": "DR-TC188", "item": "father_name", "input": "######"},
    {"id": "DR-TC189", "item": "mother_name", "input": "$$$$$$"},
    {"id": "DR-TC190", "item": "city", "input": "%"},
    {"id": "DR-TC191", "item": "province", "input": "^^^^^^^^"},
    {"id": "DR-TC192", "item": "address", "input": "&&&&&&&"},
]

input_invalid = [
    {"id": "DR-TC193", "item": "dni", "input": "&&&&@@@@@@"},
    {"id": "DR-TC194", "item": "ref_number_1", "input": "letras"},
    {"id": "DR-TC195", "item": "ref_number_2", "input": "letras"},
    {"id": "DR-TC199", "item": "sex", "input": "indefinido"},
    {"id": "DR-TC201", "item": "fissure_type", "input": "hueso"},
]

date_birth = [
    {"id": "DR-TC196", "title": "mm/dd/aaaa", "item": "date_of_birth", "input": "07/28/1999"},
    {"id": "DR-TC197", "title": "aaaa/dd/mm", "item": "date_of_birth", "input": "1997/15/12"},
]

country_invalid = [
    {"id": "DR-TC200", "item": "country", "title": "Estados Unidos", "input": "US"},
    {"id": "DR-TC223", "item": "country", "title": "Argentina", "input": "AR"},
    {"id": "DR-TC224", "item": "country", "title": "Brasil", "input": "BR"},
]

input_large = [
    {"id": "DR-TC203", "item": "first_name", "input": "AlejandroMaximilianoGonzalezFernandezSantosPerez"},
    {"id": "DR-TC204", "item": "last_name", "input": "RodriguezMartinezFernandezDelCampoGutierrezLopez"},
    {"id": "DR-TC205", "item": "father_name", "input": "LeonelMamaniMaximilianoGonzalezFernandezSantosPerezChoqueCasaMartinezFernandezDelCampoGutierrezLopez"},
    {"id": "DR-TC206", "item": "mother_name", "input": "ChoqueCasaMartinezFernandezDelCampoGutierrezLopezLeonelMamaniMaximilianoGonzalezFernandezSantosPerezChoque"},
    {"id": "DR-TC209", "item": "dni", "input": "12345678901654"},
    {"id": "DR-TC210", "item": "ref_number_1", "input": "32165459132189"},
    {"id": "DR-TC211", "item": "ref_number_2", "input": "89765432154852"},
    {"id": "DR-TC213", "item": "city", "input": "CochabambaMetropolitanaZonaCentroIndustrialSur"},
    {"id": "DR-TC214", "item": "province", "input": "ChapareTropicalRegionNorteExtensaMontañosaCasa"},
    {"id": "DR-TC215", "item": "address", "input": "Av.HeroesDelChacoNro4567ZonaCentralEdificioLibertadPiso8DepartamentoBReferenciaPlazaColonFrenteABancoUnion"},
]

input_large_special_pa = [
    {"id": "DR-TC207", "item": "sex", "input": "masculinofemeninootro"},
    {"id": "DR-TC208", "item": "country", "input": "paises bajos"},
    {"id": "DR-TC212", "item": "fissure_type", "input": "CaracteristicaExtendidaDePruebaParaVerificarExcesoDeLongitudPermitidaEnElCampoFeatureTypeDelProfesionalSistemaQA"},
]

duplicate = [
    {"id": "DR-TC217", "item": "dni", "input":"2349793"},
]

token = [
    {"id": "DR-TC218", "header":"header_login", "title":"sin autenticación", "message":"Not authenticated", "status":401},
    {"id": "DR-TC219", "header":"header_token_invalid", "title":"con token invalido", "message":"Invalid token", "status":401},
]

http_methods_invalid = [
    {"id": "DR-TC220", "item": "GET"},
    {"id": "DR-TC221", "item": "PUT"},
    {"id": "DR-TC222", "item": "DELETE"},
]



