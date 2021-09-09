from Stack import Stack
st = Stack()
def decimal_to_binary(decimal):
    while decimal:
        decimal, mod = decimal // 2, decimal % 2
        st.push(mod)
    bin = ''
    while not st.is_empty():
        bin += str(st.pop())
    return bytes(bin, encoding='utf-8')

decimal_to_binary(47)