
input_patch = [
    {"id": "DR-TC235", "item": "first_name"},
    {"id": "DR-TC236", "item": "last_name"},
    {"id": "DR-TC237", "item": "father_name"},
    {"id": "DR-TC238", "item": "mother_name"},
    {"id": "DR-TC239", "item": "date_of_birth"},
    {"id": "DR-TC240", "item": "city"},
    {"id": "DR-TC241", "item": "province"},
    {"id": "DR-TC242", "item": "address"},
    {"id": "DR-TC243", "item": "dni"},
    {"id": "DR-TC244", "item": "ref_number_1"},
    {"id": "DR-TC245", "item": "ref_number_2"},
    {"id": "DR-TC246", "item": "fissure_type"},
]

input_sex_country_fissure_type = [
    {"id": "DR-TC248", "item": "sex", "title": "sex masculino", "input":"masculino"},
    {"id": "DR-TC249", "item": "sex", "title": "sex femenino", "input":"femenino"},
    {"id": "DR-TC250", "item": "country", "title": "country Bolivia", "input" : "BO",},
    {"id": "DR-TC251", "item": "country", "title": "country México", "input" : "MX",},
    {"id": "DR-TC252", "item": "country", "title": "country  Perú", "input" : "PE",},
    {"id": "DR-TC253", "item": "country", "title": "country República Dominicana", "input" : "DO",},
    {"id": "DR-TC254", "item": "fissure_type", "title": "fissure_type Flap izquierdo", "input" : "Flap izq",},
    {"id": "DR-TC255", "item": "fissure_type", "title": "fissure_type Flap Bilateral", "input" : "Flap Bilateral",},
    {"id": "DR-TC256", "item": "fissure_type", "title": "fissure_type Flap derecho", "input" : "Flap der",},
]

input_patch_void = [
    {"id": "DR-TC257", "item": "first_name"},
    {"id": "DR-TC258", "item": "last_name"},
    {"id": "DR-TC259", "item": "father_name"},
    {"id": "DR-TC260", "item": "mother_name"},
    {"id": "DR-TC261", "item": "date_of_birth"},
    {"id": "DR-TC262", "item": "sex"},
    {"id": "DR-TC263", "item": "country"},
    {"id": "DR-TC264", "item": "dni"},
    {"id": "DR-TC265", "item": "ref_number_1"},
    {"id": "DR-TC266", "item": "fissure_type"},
]

input_space = [
    {"id": "DR-TC268", "item": "first_name"},
    {"id": "DR-TC269", "item": "last_name"},
    {"id": "DR-TC270", "item": "father_name"},
    {"id": "DR-TC271", "item": "mother_name"},
    {"id": "DR-TC272", "item": "dni"},
    {"id": "DR-TC276", "item": "ref_number_1"},
]

input_space_special = [
    {"id": "DR-TC274", "item": "sex"},
    {"id": "DR-TC275", "item": "country"},
    {"id": "DR-TC277", "item": "fissure_type"},
]

special = [
    {"id": "DR-TC278", "item": "first_name", "input": "!!!!!!"},
    {"id": "DR-TC279", "item": "last_name", "input": "@@@@@@"},
    {"id": "DR-TC280", "item": "father_name", "input": "$$$$$$"},
    {"id": "DR-TC281", "item": "mother_name", "input": "######"},
    {"id": "DR-TC282", "item": "city", "input": "*/**-"},
    {"id": "DR-TC283", "item": "province", "input": "^^^^^^^^"},
    {"id": "DR-TC284", "item": "address", "input": "&&&&&&&"},
]

date_birth = [
    {"id": "DR-TC285", "title": "mm/dd/aaaa", "item": "date_of_birth", "input": "05/30/2000"},
    {"id": "DR-TC286", "title": "aaaa/dd/mm", "item": "date_of_birth", "input": "2010/15/12"},
]

input_invalid = [
    {"id": "DR-TC288", "item": "sex", "input": "sin gener definido"},
    {"id": "DR-TC289", "item": "country", "input": "BR"},
    {"id": "DR-TC290", "item": "fissure_type", "input": "brazo"},
    {"id": "DR-TC291", "item": "dni", "input": "letras"},
    {"id": "DR-TC292", "item": "ref_number_1", "input": "letras"},
    {"id": "DR-TC293", "item": "ref_number_2", "input": "letras"},
]

input_large = [
    {"id": "DR-TC295", "item": "first_name", "input": "FernandezSantosPerezAlejandroMaximilianoGonzalez"},
    {"id": "DR-TC296", "item": "last_name", "input": "CampoGutierrezLopezRodriguezMartinezFernandezDel"},
    {"id": "DR-TC297", "item": "father_name", "input": "LeonelMamaniMaximilianoGonzalezFernandezSantosPerezChoqueCasaMartinezFernandezDelCampoGutierrezLopez"},
    {"id": "DR-TC298", "item": "mother_name", "input": "ChoqueCasaMartinezFernandezDelCampoGutierrezLopezLeonelMamaniMaximilianoGonzalezFernandezSantosPerez"},
    {"id": "DR-TC301", "item": "dni", "input": "90165412345678"},
    {"id": "DR-TC302", "item": "ref_number_1", "input": "1230911789654"},
    {"id": "DR-TC303", "item": "ref_number_2", "input": "1230911789654"},
    {"id": "DR-TC305", "item": "city", "input": "SantaCruzRegionMetropolitanaZonaCentroIndustrialSur"},
    {"id": "DR-TC306", "item": "province", "input": "VillaTunariTropicalRegionNorteExtensaMontañosaCasa"},
    {"id": "DR-TC307", "item": "address", "input": "Av.BlancoGalindoKM41/2Nro4567ZonaCentralEdificioLibertadPiso8DepartamentoBReferenciaPlazaColonFrenteABancoUnion"},
]

input_large_special_pa = [
    {"id": "DR-TC299", "item": "sex", "input": "masculinofemeninootro"},
    {"id": "DR-TC300", "item": "country", "input": "chinatown"},
    {"id": "DR-TC304", "item": "fissure_type", "input": "CaracteristicaExtendidaDePruebaParaVerificarExcesoDeLongitudPermitidaEnElCampoFeatureTypeDelProfesionalSistemaQA"},
]

duplicate = [
    {"id": "DR-TC308", "item": "dni", "input":"2349793"},
]

id_not_exist = [
    {"input":1654555612, "title": "que no existente"},
]

id_invalid = [
    {"input":"purasletras", "item": "patient_id"},
]

token = [
    {"id": "DR-TC311", "header":"header_login", "title":"sin autenticación", "message":"Not authenticated", "status":401},
    {"id": "DR-TC312", "header":"header_token_invalid", "title":"con token invalido", "message":"Invalid token", "status":401},
]
