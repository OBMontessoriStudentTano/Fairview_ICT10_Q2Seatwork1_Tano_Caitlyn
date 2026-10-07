from pyscript import display, document

names = ["Caitlyn Tano", "Enzo Navarro", "Camille Dela Cruz", "Vincent Villanueva", "Scarlett Santos", "Theo Marasigan", "Valerie Bautista", "Damian Malabanan", "Vivienne Gatdula", "Isaiah Manansala", "Anna Dimaculangan"]

def enter(event):
    first_name = document.getElementById("text1").value.strip()
    last_name = document.getElementById("text2").value.strip()

    full_name = first_name + " " + last_name

    if full_name.lower() in [name.lower() for name in names]:
        document.getElementById("output").innerText = f"Congratulations {full_name}! You are now part of the CAC club"
    else:
        document.getElementById("output").innerText = f"Sorry {full_name}, your name is not on the list."