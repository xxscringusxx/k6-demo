def add_entry_to_file(user_info_file, entry):
    with open(user_info_file, 'a') as file:
        file.write(f'{entry}\n')

def create_entry(request):
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']

    entry = f'{name},{age},{address}'
    return entry

def read_existing_entries(user_info_file):
    try:
        with open(user_info_file, 'r') as file:
            existing_entries = set(line.strip() for line in file)
        return existing_entries
    except FileNotFoundError:
        return set()
