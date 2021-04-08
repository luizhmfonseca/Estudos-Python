# Style 0 - none 1 - Bold 4 - Underline 7 - negative (inversão de cores...letra - fundo...fundo - Letra)
# Text 30 - branco 31 - Vermelho 32 - verde 33 - amarelo 34 - azul 35 - magenta (Similar roxo) 36 - sian (similar turqueza) 37 - cinza
# Back 40 - branco 41 - Vermelho 42 - verde 43 - amarelo 44 - azul 45 - magenta (Similar roxo) 46 - sian (similar turqueza) 47 - cinza

# *Estrutura de controle *Estrutura de repetição
# Padrão ANSI - Escape Sequence

# \033 #Código para representar COR no Python (incluir cód Style, back e Text depois do colchete)

# \033[0;33;44m

# \33[0;30;41m #letra comum (style), fonte branca (text), background vermelho
# \33[4;33;44m #letra under (style), fonte amarela (text), background azul
# \33[1;35;43m #letra comum (style), fonte magenta (text), background amarelo
# \33[30;42m   #letra comum (style), fonte branca (text), background verde
# \33[m        #letra comum (style), fonte brana (text), background preto
# \33[7;30m    #letra comum (style), fonte preta (text), background branco