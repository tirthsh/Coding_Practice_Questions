def string_compression(chars):
    i = 0
    index = 0

    while (i < len(chars)):
        j = i
        while (j < len(chars) and chars[i] == chars[j]):
            j+= 1
        
        chars[index + 1] = chars[i]

        if j - 1 > 1:
            count = str(j-i)
            for char in count:
                chars[index + 1] = char
        
        i = j
    
    return index
            

s = ["a", "a", "b", "b"]
print(string_compression(s))





