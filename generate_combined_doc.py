import os
import re

def main():
    files_to_combine = []

    # Get all information files
    for filename in os.listdir('.'):
        if filename.startswith('information') and filename.endswith('.txt'):
            files_to_combine.append(filename)

    # Sort files naturally
    def extract_number(filename):
        if filename == 'information.txt':
            return 0
        match = re.search(r'\((\d+)\)', filename)
        if match:
            return int(match.group(1))
        return 999

    files_to_combine.sort(key=extract_number)

    # Add Technical.txt at the end
    if os.path.exists('Technical.txt'):
        files_to_combine.append('Technical.txt')

    with open('DTECH_Ecosystem.txt', 'w') as outfile:
        outfile.write("# D-TECH ECOSYSTEM - MASTER DOCUMENT\n")
        outfile.write("=" * 80 + "\n\n")

        project_count = 1
        for filename in files_to_combine:
            try:
                with open(filename, 'r') as infile:
                    content = infile.read()

                    # Determine header
                    if filename == 'Technical.txt':
                        header = f"### {filename.upper()} ###\n"
                    else:
                        header = f"### PROJECT {project_count} ({filename}) ###\n"
                        project_count += 1

                    outfile.write(header)
                    outfile.write("-" * 80 + "\n\n")
                    outfile.write(content)
                    outfile.write("\n\n" + "=" * 80 + "\n\n")
            except Exception as e:
                print(f"Error reading {filename}: {e}")

if __name__ == '__main__':
    main()
