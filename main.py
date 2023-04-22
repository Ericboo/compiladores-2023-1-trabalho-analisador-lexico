import re

def analizar(source_code):
    keyword = r"int|float|char|double|if|else|while|return|struct"
    identifier = r"[a-zA-Z_][a-zA-Z0-9_]*"
    int_const = r"\d+"
    float_const = r"\d+\.\d+"
    operator = r"[+\-*/=!<>]"
    delimitator = r"[(),;{}]"
    
    std_reco = "|".join([
        keyword, 
        float_const,
        int_const, 
        identifier,
        operator, 
        delimitator
    ])
    
    tokens = []
    for linha in source_code.split("\n"):
        for token in re.findall(std_reco, linha):
            if re.match(keyword, token):
                tokens.append(('KEYWORD', token))
            elif re.match(float_const, token):
                tokens.append(('CONST', token))
            elif re.match(int_const, token):
                tokens.append(('CONST', token))
            elif re.match(identifier, token):
                tokens.append(('ID', token))
            elif re.match(operator, token):
                tokens.append(('OP', token))
            elif re.match(delimitator, token):
                tokens.append(('DEL', token))
    
    return tokens

# Exemplo de código-fonte em C
source_code = open('teste1.c').read()

# Analisar o código-fonte e imprimir a lista de tokens com as descrições
tokens = analizar(source_code)
for token in tokens:
    print(token)
