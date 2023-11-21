import sys

def export_yaml(data, file_name):
    lines = data.splitlines()
    n = len(lines)


    try:
        # Export YAML Data to File
        with open(file_name, 'w') as f:
            for line in lines[1:n-1]:
                f.write(f"{line}\n")

    except Exception as error:
        print(f"\nError Encountered: \n \t {error} \n")
        print("Failed to Export YAML File. Exiting Program . . \n")
        sys.exit(1)

