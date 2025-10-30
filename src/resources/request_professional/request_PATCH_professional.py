
input_patch = [
    {"id": "DR-TC82", "item": "first_name"},
    {"id": "DR-TC83", "item": "last_name"},
    {"id": "DR-TC84", "item": "date_of_birth"},
    {"id": "DR-TC85", "item": "city"},
    {"id": "DR-TC86", "item": "province"},
    {"id": "DR-TC87", "item": "address"},
    {"id": "DR-TC88", "item": "dni"},
    {"id": "DR-TC89", "item": "personal_email"},
    {"id": "DR-TC90", "item": "phone"},
    {"id": "DR-TC91", "item": "profession"},
    {"id": "DR-TC92", "item": "specialty"},
]

input_sex_country = [
    {"id": "DR-TC94", "item": "sex", "title": "sex masculino", "input":"masculino"},
    {"id": "DR-TC95", "item": "sex", "title": "sex femenino", "input":"femenino"},
    {"id": "DR-TC96", "item": "country", "title": "country Bolivia", "input" : "BO",},
    {"id": "DR-TC97", "item": "country", "title": "country México", "input" : "MX",},
    {"id": "DR-TC98", "item": "country", "title": "country  Perú", "input" : "PE",},
    {"id": "DR-TC99", "item": "country", "title": "country República Dominicana", "input" : "DO",},
    {"id": "DR-TC100", "item": "country", "title": "country Estados Unidos", "input" : "US",},
    {"id": "DR-TC101", "item": "country", "title": "country Argentina", "input" : "AR",},
    {"id": "DR-TC102", "item": "country", "title": "country Brasil", "input" : "BR",},
]

input_patch_void = [
    {"id": "DR-TC103", "item": "first_name"},
    {"id": "DR-TC104", "item": "last_name"},
    {"id": "DR-TC105", "item": "date_of_birth"},
    {"id": "DR-TC106", "item": "sex"},
    {"id": "DR-TC107", "item": "country"},
    {"id": "DR-TC108", "item": "dni"},
    {"id": "DR-TC109", "item": "personal_email"},
    {"id": "DR-TC110", "item": "phone"},
    {"id": "DR-TC111", "item": "profession"},
    {"id": "DR-TC112", "item": "specialty"},
]

input_space = [
    {"id": "DR-TC114", "item": "first_name"},
    {"id": "DR-TC115", "item": "last_name"},
    {"id": "DR-TC116", "item": "dni"},
    {"id": "DR-TC117", "item": "phone"},
    {"id": "DR-TC118", "item": "profession"},
    {"id": "DR-TC119", "item": "specialty"},
]

input_space_special = [
    {"id": "DR-TC121", "item": "sex"},
    {"id": "DR-TC122", "item": "country"},
    {"id": "DR-TC123", "item": "personal_email"},
]

special = [
    {"id": "DR-TC124", "item": "first_name", "input": "!!!!!!"},
    {"id": "DR-TC125", "item": "last_name", "input": "@@@@@@"},
    {"id": "DR-TC153", "item": "profession", "input": "$$$$$$"},
    {"id": "DR-TC154", "item": "specialty", "input": "######"},
    {"id": "DR-TC155", "item": "city", "input": "*/**-"},
    {"id": "DR-TC156", "item": "province", "input": "^^^^^^^^"},
    {"id": "DR-TC157", "item": "address", "input": "&&&&&&&"},
]

date_birth = [
    {"id": "DR-TC126", "title": "mm/dd/aaaa", "item": "date_of_birth", "input": "05/30/1987"},
    {"id": "DR-TC152", "title": "aaaa/dd/mm", "item": "date_of_birth", "input": "2000/15/12"},
]

input_invalid = [
    {"id": "DR-TC128", "item": "sex", "input": "sin gener definido"},
    {"id": "DR-TC129", "item": "country", "input": "japon"},
    {"id": "DR-TC130", "item": "personal_email", "input": "esto no es un correo"},
    {"id": "DR-TC131", "item": "phone", "input": "letras"},
]

input_large = [
    {"id": "DR-TC133", "item": "first_name", "input": "FernandezSantosPerezAlejandroMaximilianoGonzalez"},
    {"id": "DR-TC134", "item": "last_name", "input": "CampoGutierrezLopezRodriguezMartinezFernandezDel"},
    {"id": "DR-TC137", "item": "city", "input": "SantaCruzRegionMetropolitanaZonaCentroIndustrialSur"},
    {"id": "DR-TC138", "item": "province", "input": "VillaTunariTropicalRegionNorteExtensaMontañosaCasa"},
    {"id": "DR-TC139", "item": "address", "input": "Av.BlancoGalindoKM41/2Nro4567ZonaCentralEdificioLibertadPiso8DepartamentoBReferenciaPlazaColonFrenteABancoUnion"},
    {"id": "DR-TC140", "item": "dni", "input": "90165412345678"},
    {"id": "DR-TC141", "item": "personal_email", "input": "pepito.grillo.excedidolongituddemaasdasgagsdasfeciendecaracteresparaelcampodeemailprofesional@ejemplopruebalarga.com"},
    {"id": "DR-TC142", "item": "phone", "input": "1230911789654"},
    {"id": "DR-TC143", "item": "profession", "input": "IngenieroDesarrolladorDeSoftwareEspecialistaEnArquitecturaDeSistemasDistribuidosEmpresarialesCloudAmzonico"},
    {"id": "DR-TC144", "item": "specialty", "input": "NeurocirujanoEspecialistaEnMicrocirugiaCerebralYColumnaVertebralAvanzadaConEntrenamientoInternacionalCertificado"},
]

input_large_special_pro = [
    {"id": "DR-TC135", "item": "sex", "input": "masculinofemeninootro"},
    {"id": "DR-TC136", "item": "country", "input": "chinatown"},
]

duplicate = [
    {"id": "DR-TC145", "item": "personal_email", "input":"profesional@project-x.com"},
    {"id": "DR-TC146", "item": "dni", "input":"70707070"},
    {"id": "DR-TC147", "item": "phone", "input":"70707070"},
]

token = [
    {"id": "DR-TC149", "header":"header_login", "title":"sin autenticación", "message":"Not authenticated", "status":401},
    {"id": "DR-TC150", "header":"header_token_invalid", "title":"con token invalido", "message":"Invalid token", "status":401},
    {"id": "DR-TC151", "header":"header_without_permits", "title":"con token sin permisos", "message":"Not enough permissions", "status":403},
]

id_not_exist = [
    {"input":1654555612, "title": "que no existente"},
]