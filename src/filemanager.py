class FileManager:
    def __init__(self, user_info_file):
        self.user_info_file = user_info_file

    def add_entry_to_file(self, entry):
        with open(self.user_info_file, 'a') as file:
            file.write(f'{entry}\n')

    def read_existing_entries(self):
        try:
            with open(self.user_info_file, 'r') as file:
                existing_entries = set(line.strip() for line in file)
            return existing_entries
        except FileNotFoundError:
            return set()

    def write_entries_to_file(self, entries):
        with open(self.user_info_file, 'w') as file:
            for entry in entries:
                file.write(f'{entry}\n')

    def clear_entries(self):
        with open(self.user_info_file, 'w'):
	        pass