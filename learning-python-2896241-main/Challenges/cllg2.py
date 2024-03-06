import os
from os import path

#versao1 pessoal

#def countfiles_bytes():
#    c=0
#    cd=os.getcwd()
#    for x,y,z0 in os.walk(cd):
#        for z in z0:
#            nam, ext = os.path.splitext(z)
#            if ext == 'txt':
#                w = os.path.join(cd,z)
#                info = os.stat(w)
#                c+=info.st_size
#    return c
#versao1 pessoal

#versao2 pessoal
def countfiles_bytes():
    c=0
    deps_dir="learning-python-2896241-main/Challenges/test_dir"
    cd=os.path.join(os.getcwd(),deps_dir)
    print(cd)
    for _,_,zou in os.walk(cd):
        for z in zou:
            nam, ext = os.path.splitext(z)
            if ext == ".txt":
                #print("Hi")
                w = os.path.join(cd,z)
                info = os.stat(w)
                c+=info.st_size
    return c
#versao2 pessoal

#versao3 pessoal
#def file_info():
#    c=0
#    deps_dir="deps"
#    cd=os.path.join(deps_dir)
#    for _,_,z0 in os.walk(cd):
#        for z in z0:
#            nam, ext = os.path.splitext(z)
#            if ext == '.txt':
#                w=os.path.join(cd,z)
#                info=os.stat(w)
#                c+=info.st_size
#    return c
#versao3 pessoal

#versao1 do chat gpt
#import os

#def count_files_bytes():
#    c = 0
#    cd = os.getcwd()
#    for _, _, arquivos in os.walk(cd):
#        for arquivo in arquivos:
#            nome, extensao = os.path.splitext(arquivo)
#            if extensao == '.txt':
#                caminho_arquivo = os.path.join(cd, arquivo)
#                info_arquivo = os.stat(caminho_arquivo)
#                c += info_arquivo.st_size
#    return c
#versao1 do chat gpt

#versao2 do chat gpt
#import os

#def count_files_bytes():
#    cd = os.getcwd()
    # Utilizando uma compreensão de lista para obter todos os arquivos .txt
#    arquivos_txt = [os.path.join(diretorio_atual, arquivo) 
#                    for diretorio_atual, _, arquivos in os.walk(cd)
#                    for arquivo in arquivos 
#                    if arquivo.endswith('.txt')]
    
    # Utilizando a função sum() para somar os tamanhos dos arquivos
#    total_bytes = sum(os.stat(arquivo).st_size for arquivo in arquivos_txt)
    
#    return total_bytes
#versao2 do chat gpt

def main():
    print(countfiles_bytes())

if __name__ == "__main__":
    main()