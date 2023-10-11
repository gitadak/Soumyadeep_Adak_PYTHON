def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

        if len(lines1) != len(lines2):
            return False

        for line1, line2 in zip(lines1, lines2):
            if line1 != line2:
                return False

        return True
    except FileNotFoundError:
        return False


file1_path = "file1.txt"
file2_path = "file2.txt"

result = compare_files(file1_path, file2_path)

if result:
    print("The files are identical.")
else:
    print("The files are different.")
