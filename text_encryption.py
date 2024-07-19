input_text: str = input()
assert input_text, "No text was provided!"

temp_symbol: str = ''
msg_len: int = len(input_text)
input_text = list(input_text)

for symbol in range(msg_len//2):
    temp_symbol = input_text[symbol]
    input_text[symbol] = input_text[msg_len - symbol - 1]
    input_text[msg_len - symbol - 1] = temp_symbol

print(''.join(x for x in input_text))