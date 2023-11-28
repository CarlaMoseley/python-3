from src.ValidationException import ValidationException
class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_file(file_name):
    with open(file_name, "r") as file1:
        line_number = 0
        while True:
            line = file1.readline()
            if not line:
              break
            line_number =+ 1
            parts = line.strip().split(',')
            if len(parts) !=2:
                raise ValidationException(f"Invalid format in line {line_number}: {line}")

                car, mileage_str = parts
def main():
    file_path = "C:/Users/f92slpy/techprojects\python-3/files\input.txt"
    try:

        validate_file(file_path)

    except ValidationException as ve:
        print(ve)

if __name__=='__main__':
    main()