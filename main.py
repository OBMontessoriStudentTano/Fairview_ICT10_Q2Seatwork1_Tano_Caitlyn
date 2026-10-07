from pyscript import display, document

# List of names
names = ["Caitlyn Tano", "Enzo Navarro", "Camille Dela Cruz", "Vincent Villanueva", "Scarlett Santos", "Theo Marasigan", "Valerie Bautista", "Damian Malabanan", "Vivienne Gatdula", "Isaiah Manansala", "Anna Dimaculangan"]

# Function that checks if the entered name is on the list
def enter(event):

    # First and last names entered by user
    first_name = document.getElementById("text1").value.strip()
    last_name = document.getElementById("text2").value.strip()

    # Combine the first and last names
    full_name = first_name + " " + last_name

    # Checks if the name is on the list regardless of capitalization
    if full_name.lower() in [name.lower() for name in names]:
        
        # The message if the name is on the list
        document.getElementById("output").innerText = f"Congratulations {full_name}! You are now part of the Communication Arts club"
    else:

         # The message if the name not is on the list
        document.getElementById("output").innerText = f"Sorry {full_name}, your name is not on the list."