# app/utils/abudevs_id.py
def generate_abudevs_id(first_name, student_id, serial):
    # e.g. #ABUDEVSJOCS0001
    prefix = "#ABUDEVS"
    name_part = first_name[:2].upper()
    id_part = student_id[3:5].upper()
    return f"{prefix}{name_part}{id_part}{serial:04}"
