def tail(filename, numlines):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if numlines > len(lines):
                for line in lines:
                    print(line)
            else:
                for line in lines[-numlines:]:
                    print(line)

    except FileNotFoundError:
        print(f"file not found {filename}")            

tail("filename.txt", 3)