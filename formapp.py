from flask import Flask, render_template, request
from src.entrymethods import create_entry
from src.filemanager import FileManager 
from flask import redirect


app = Flask(__name__)
user_info_file = 'user_info.txt'

@app.route('/confirmation')
def confirmation():
    return "Entry saved!"


@app.route('/') 
def form():
    return render_template('form.html')


file_manager = FileManager(user_info_file)

@app.route('/save', methods=['POST'])
def save():
    entry = create_entry(request)

    unique_entries = file_manager.read_existing_entries()

    if entry in unique_entries:
        return 'Information already exists!'

    file_manager.add_entry_to_file(entry)

    return 'Information saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
