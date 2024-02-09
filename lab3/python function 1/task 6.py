def reverse_sentence(sentence):
    words = sentence.split()  
    reversed_sentence = " ".join(reversed(words)) 
    return reversed_sentence

example = input()
result = reverse_sentence(example)
print(result)

