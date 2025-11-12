class ReverseWords:
    def reverse_string(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Sử dụng
reverser = ReverseWords()
input_str = 'hello .py'
output_str = reverser.reverse_string(input_str)
print(output_str)  # .py hello