
import os

BASE_PATH = "src/resources/images"

def get_file_profile():
    return {
        "photo": ("profile.png", open(os.path.join(BASE_PATH, "profile.png"), "rb"), "image/png")
    }

def get_file_patient():
    return {
        "photo": ("patient.png", open(os.path.join(BASE_PATH, "patient.png"), "rb"), "image/png")
    }

def get_file_txt():
    return {
        "photo": ("imagen.txt", open(os.path.join(BASE_PATH, "imagen.txt"), "rb"), "text/plain")
    }

def get_file_BIG():
    return {
        "photo": ("big.png", open(os.path.join(BASE_PATH, "big.png"), "rb"), "image/png")
    }

def get_file_edit():
    return {
        "photo": ("profile_edit.png", open(os.path.join(BASE_PATH, "profile_edit.png"), "rb"), "image/png")
    }

#photo
def get_file_patient_photo():
    return {
        "file": ("patient.png", open(os.path.join(BASE_PATH, "patient.png"), "rb"), "image/png")
    }

def get_file_txt_photo():
    return {
        "file": ("imagen.txt", open(os.path.join(BASE_PATH, "imagen.txt"), "rb"), "text/plain")
    }