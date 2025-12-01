print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
class RomanToInteger:
    def __init__(self):
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    
    def convert(self, roman):
        total = 0
        prev_value = 0
        
        for char in reversed(roman):
            current_value = self.roman_map[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        
        return total

# Sử dụng
converter = RomanToInteger()
print(converter.convert("XIV"))  # 14
print(converter.convert("LVIII"))  # 58
