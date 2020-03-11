def mutate_string(string, position, character):
    str2=string[:position]+character+string[position+1:]
    return str2
