class StringProcessor:
    def __init__(self):
        self.input_string = ""
    
    def get_String(self):
        self.input_string = input("Nhập chuỗi: ")
    
    def print_String(self):
        print(self.input_string.upper())

# Sử dụng
processor = StringProcessor()
processor.get_String()
processor.print_String()