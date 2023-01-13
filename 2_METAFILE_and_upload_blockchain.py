# STEP 2

from PIL import Image
from IPython.display import display
import random
import json
import os

#SUBSTITUIÇÕES:
'''
["Face"] --> Background
["Ears"] --> Slug
["Eyes"] --> Slime
["Hair"] --> Shell
["Mouth"] --> Iten
["Nose"] --> Hat
'''


#O que são metadados NFT?

#fonte: https://betterprogramming.pub/generate-your-nft-metadata-11a878c082b9

'''
Os metadados NFT são o núcleo de um NFT. É um documento JSON que geralmente contém o seguinte:
.Nome do NFT
.Descrição do NFT
.Link para a imagem hospedada
.Características
.Etc…
Esses metadados NFT serão a entrada do seu contrato inteligente NFT que você implantará na rede Ethereum na terceira parte.
'''

#Carregue suas imagens NFT na nuvem
'''
O upload de imagens para o blockchain é muito caro, pois são grandes em tamanho.
A melhor prática é carregar apenas o link de sua imagem para o blockchain e armazenar sua imagem em um sistema de arquivos interplanetário 
(mais sobre isso posteriormente).
Pinata permite que você carregue imagens NFT gratuitamente usando IPFS (InterPlanetary File System). Este é um sistema distribuído de 
compartilhamento de arquivos.
Inscreva-se para uma conta gratuita e carregue sua pasta de imagens NFT para a nuvem pinata.
Chamei meu projeto de “NFT Creator”, mas sinta-se à vontade para escolher um nome diferente.

*OBS: Se o upload for bem-sucedido, você poderá ver os arquivos enviados no Blockchain (metodo de envio IPFS)

#Copiando a URL BASE

Clique no seu projeto e copie o link.
Este é o seu “URL BASE”, que você precisará mais tarde.
Exemplo: https://gateway.pinata.cloud/ipfs/Qmb86L8mUphwJGzLPwXNTRiK1S4scBdj9cc2Sev3s8uLiB
'''



# IMPORTANTE !!!
#OBS: O PARAMETRO ALL_IMAGE ABAIXO SERVER APENAS PARA NÃO DAR ERRO NO PROGRAMA, MAS NA HORA DE MONTAR O PROGRAMA UTILIZAR AS VARIAVEIS
# DO ARQUIVO "Exemplo_NFT_Generator.py".
all_images = []





#Gerar metadados NFT
'''
all-traits.json
Na primeira parte da série NFT Creator, você criou uma lista chamada “all_images” especificando as características de cada imagem.  
Simplesmente, despeje essa lista em um arquivo .json usando a função json.dump().
'''
#### Generate Metadata for all Traits
os.mkdir(f'./metadata')

METADATA_FILE_NAME = './metadata/all-traits.json';
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#[token_id].json
'''
Em seguida, você deseja criar um arquivo .json específico para cada imagem:

carregar no all_traits.json
Especifique suas imagens "URL BASE" que você copiou anteriormente no site Pinata. Certifique-se de adicionar um “/” adicional no final!
Especifique o nome do seu projeto
Faça um loop no dicionário all_traits .json usando o acessador de chaves e gere um arquivo .json individual para cada imagem NFT exclusiva.
Para esta imagem, você receberá, por exemplo, o seguinte arquivo .json:
'''
#### Generate Metadata for each Image

f = open('./metadata/all-traits.json',)
data = json.load(f)

# Changes this IMAGES_BASE_URL to yours
IMAGES_BASE_URL = "https://gateway.pinata.cloud/ipfs/Qmb86L8mUphwJGzLPwXNTRiK1S4scBdj9cc2Sev3s8uLiB/"
PROJECT_NAME = "NFT_CREATOR"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URL + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("background", i["background"]))
    token["attributes"].append(getAttribute("slug", i["slug"]))
    token["attributes"].append(getAttribute("slime", i["slime"]))
    token["attributes"].append(getAttribute("shell", i["shell"]))
    token["attributes"].append(getAttribute("iten", i["iten"]))
    token["attributes"].append(getAttribute("hat", i["hat"]))

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()

#Carregue os metadados para pinata
'''
Carregue seus metadados gerados para Pinata da mesma forma que para as imagens.

Logo você conseguirá visualizar seu metadata correspondente a imagem correta, confira uma para ver se correspondem as informações
'''

