import os

def concatenate_files(directory, output_file, extensions=('.h', '.cpp', '.cs')):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extensions):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"// Start of {file_path}\n")
                        outfile.write(infile.read())
                        outfile.write(f"\n// End of {file_path}\n\n")

# Usage
directory_to_search = os.path.dirname(os.path.abspath(__file__))
output_file = 'concatenated_files.txt'
concatenate_files(directory_to_search, output_file)
