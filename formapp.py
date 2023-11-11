from flask import Flask, render_template, request

app = Flask(__name__)
user_info_file = 'user_info.txt'

def add_entry_to_file(entry):
    with open(user_info_file, 'a') as file:
        file.write(f'{entry}\n')


def create_entry():
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']

    entry = f'{name},{age},{address}'
    return entry

def read_existing_entries():
    try:
        with open(user_info_file, 'r') as file:
            existing_entries = set(line.strip() for line in file)
        return existing_entries
    except FileNotFoundError:
        return set()

unique_entries = read_existing_entries()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/save', methods=['POST'])
def save():
    entry = create_entry()

    if entry in unique_entries:
        return 'Information already exists!'

    unique_entries.add(entry)
    add_entry_to_file(entry)

    return 'Information saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
