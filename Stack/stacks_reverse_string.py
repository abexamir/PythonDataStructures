import Stack
def reverse_string(word):
    st = Stack()
    for i in word:
        st.push(i)
    new_word = ""
    while not st.is_empty():
        new_word += st.pop()
    return new_word