
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