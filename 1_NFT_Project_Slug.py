#Project from: https://betterprogramming.pub/create-your-own-nft-collection-with-python-82af40abf99f

#SUBSTITUIÇÕES:
'''
["Face"] --> Background
["Ears"] --> Slug
["Eyes"] --> Slime
["Hair"] --> Shell
["Mouth"] --> Iten
["Nose"] --> Hat
'''



from PIL import Image
from IPython.display import display
import random
import json
import os



# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

#Parte 1
'''A raridade é importante, pois cria escassez que, por sua vez, cria valor.
Você implementará raridade nas características atribuindo pesos aos diferentes tipos dentro de uma característica. 
O total dos pesos deve sempre somar 100.
Existem dois tipos de rostos (preto e branco). Você especifica para o programa que uma imagem tem 60% de chance de receber 
uma background branca e 40% de receber uma background preta.'''

#Background
background = ["Baby_Blue","Baby_Green","Blue","Cyan","Gray","Green","Orange","Pink","Purple","Red","Yellow"]
background_weights = [10,10,10,3,10,10,10,10,7,10,10]

#slug
slug = ["Baby_Green_Slug","Baby_Purple_Slug","Blue_Slug","Brown_Slug","Cyan_Slug","Gray_Slug","Green_Slug",
        "Marine_Blue_Slug","Orange_Slug","Pink_Slug","Purple_Slug","Red_Slug","Yellow_Slug"]
slug_weights = [7,10,7,10,7,7,8,7,7,7,7,7,9]

#slime
slime = ["Baby_Blue_Slime","Baby_Purple_Slime","Blue_Slime","Brown_Slime","Cyan_Slime","Gray_Slime","Green_Slime",
         "Lime_Slime","Marine_Blue_Slime","Orange_Slime","Pink_Slime","Purple_Slime","Red_Slime","Yellow_Slime"]
slime_weights = [7,8,7,7,7,7,7,8,7,7,7,7,7,7]

#shell
shell = ["Baby_Green_Shell","Baby_Purple_Shell","Black_Shell","Blue_Shell","Brown_Shell","Cyan_Shell","Green_Shell",
         "Marine_Blue_Shell","Orange_Shell","Pink_Shell","Purple_Shell","Red_Shell","Yellow_Shell"]
shell_weights = [7,8,7,9,7,7,7,8,7,10,7,8,8]

#itens
iten = ["Back_Slime","Bag","Battery","Board","Burguer","Candle","Chest","Controller","Diamond","Egg","Exhaust",
        "Mat","Ovni","Pokeball","Rocket","Sword","Toxic","Tree","Unicorn_Wings"]
iten_weights = [5,5,5,5,6,5,5,5,7,5,5,7,5,5,5,5,5,5,5]

#hat
hat = ["Bike_Helmet","Bishop","Cap","Dread_Style","Fisherman","Glasses","HeadPhones","Helmet","Hood",
       "Horns","Indigenous_Hat","Mask","Miner_Hat","Pink_Hair","Sheriff","Smooth_Hair","Top","Top_Hat","Unicorn_Horn","Winter_Cap"]
hat_weights = [5,5,5,5,5,5,5,5,5,5,5,1,6,6,5,5,5,6,5,6]

#Parte 2
r'''Dicionários são usados para redirecionar os nomes de características para seus nomes de arquivo. 
Você pode encontrar os nomes dos arquivos trait no seguinte local: …\subtrapunks-master\scripts\background_parts\ .
O nome do traço “Branco” é direcionado para background1 enquanto “Preto” é direcionado para background2.'''

#Classify traits

#Background
background_files = {
      "Baby_Blue": "Baby_Blue"
    ,"Baby_Green":"Baby_Green"
    ,"Blue":      "Blue"
    ,"Cyan":      "Cyan"
    ,"Gray":      "Gray"
    ,"Green":     "Green"
    ,"Orange":    "Orange"
    ,"Pink":      "Pink"
    ,"Purple":    "Purple"
    ,"Red":       "Red"
    ,"Yellow":    "Yellow"


}

#Slug
slug_files = {
      "Baby_Green_Slug"           :"Baby_Green_Slug"
    ,"Baby_Purple_Slug"          :"Baby_Purple_Slug"
    ,"Blue_Slug"                 :"Blue_Slug"
    ,"Brown_Slug"                :"Brown_Slug"
    ,"Cyan_Slug"                 :"Cyan_Slug"
    ,"Gray_Slug"                 :"Gray_Slug"
    ,"Green_Slug"                :"Green_Slug"
    ,"Marine_Blue_Slug"          :"Marine_Blue_Slug"
    ,"Orange_Slug"               :"Orange_Slug"
    ,"Pink_Slug"                 :"Pink_Slug"
    ,"Purple_Slug"               :"Purple_Slug"
    ,"Red_Slug"                  :"Red_Slug"
    ,"Yellow_Slug"               :"Yellow_Slug"
}

#Slime
slime_files = {
     "Baby_Blue_Slime"          : "Baby_Blue_Slime"
    ,"Baby_Purple_Slime"        : "Baby_Purple_Slime"
    ,"Blue_Slime"               : "Blue_Slime"
    ,"Brown_Slime"              : "Brown_Slime"
    ,"Cyan_Slime"               : "Cyan_Slime"
    ,"Gray_Slime"               : "Gray_Slime"
    ,"Green_Slime"              : "Green_Slime"
    ,"Lime_Slime"               : "Lime_Slime"
    ,"Marine_Blue_Slime"        : "Marine_Blue_Slime"
    ,"Orange_Slime"             : "Orange_Slime"
    ,"Pink_Slime"               : "Pink_Slime"
    ,"Purple_Slime"             : "Purple_Slime"
    ,"Red_Slime"                : "Red_Slime"
    ,"Yellow_Slime"             : "Yellow_Slime"
}

#Shell
shell_files = {
     "Baby_Green_Shell"         : "Baby_Green_Shell"
    ,"Baby_Purple_Shell"        : "Baby_Purple_Shell"
    ,"Black_Shell"              : "Black_Shell"
    ,"Blue_Shell"               : "Blue_Shell"
    ,"Brown_Shell"              : "Brown_Shell"
    ,"Cyan_Shell"               : "Cyan_Shell"
    ,"Green_Shell"              : "Green_Shell"
    ,"Marine_Blue_Shell"        : "Marine_Blue_Shell"
    ,"Orange_Shell"             : "Orange_Shell"
    ,"Pink_Shell"               : "Pink_Shell"
    ,"Purple_Shell"             : "Purple_Shell"
    ,"Red_Shell"                : "Red_Shell"
    ,"Yellow_Shell"             : "Yellow_Shell"
}

#Item
iten_files = {
    "Back_Slime"               : "Back_Slime"
    ,"Bag"                      : "Bag"
    ,"Battery"                  : "Battery"
    ,"Board"                    : "Board"
    ,"Burguer"                  : "Burguer"
    ,"Candle"                   : "Candle"
    ,"Chest"                    : "Chest"
    ,"Controller"               : "Controller"
    ,"Diamond"                  : "Diamond"
    ,"Egg"                      : "Egg"
    ,"Exhaust"                  : "Exhaust"
    ,"Mat"                      : "Mat"
    ,"Ovni"                     : "Ovni"
    ,"Pokeball"                 : "Pokeball"
    ,"Rocket"                   : "Rocket"
    ,"Sword"                    : "Sword"
    ,"Toxic"                    : "Toxic"
    ,"Tree"                     : "Tree"
    ,"Unicorn_Wings"            : "Unicorn_Wings"
}

#Hat
hat_files = {
    "Bike_Helmet"              : "Bike_Helmet"
    ,"Bishop"                   : "Bishop"
    ,"Cap"                      : "Cap"
    ,"Dread_Style"              : "Dread_Style"
    ,"Fisherman"                : "Fisherman"
    ,"Glasses"                  : "Glasses"
    ,"HeadPhones"               : "HeadPhones"
    ,"Helmet"                   : "Helmet"
    ,"Hood"                     : "Hood"
    ,"Horns"                    : "Horns"
    ,"Indigenous_Hat"           : "Indigenous_Hat"
    ,"Mask"                     : "Mask"
    ,"Miner_Hat"                : "Miner_Hat"
    ,"Pink_Hair"                : "Pink_Hair"
    ,"Sheriff"                  : "Sheriff"
    ,"Smooth_Hair"              : "Smooth_Hair"
    ,"Top"                      : "Top"
    ,"Top_Hat"                  : "Top_Hat"
    ,"Unicorn_Horn"             : "Unicorn_Horn"
    ,"Winter_Cap"               : "Winter_Cap"
}

#Parte 3
'''
Cada imagem de avatar que você criar será uma combinação de seis fotos umas sobre as outras: rosto, nariz, boca, orelhas e olhos.
Portanto, você escreve um loop for que combina essas características em uma única imagem para um número total especificado de imagens.
Uma função cria um dicionário para cada imagem especificando quais características ela possui.
Essas características são fornecidas com base na função random.choices() .
Esta função percorre a lista de características de rosto (branco, preto) e retorna branco (60% de chance) ou preto (40% de chance).
'''

## Generate Traits

TOTAL_IMAGES = 1001  # Number of random unique images we want to generate

all_images = []


# A recursive function to generate unique image combinations
def create_new_image():
 new_image = {}  #

 # For each trait category, select a random trait based on the weightings
 new_image["background"] = random.choices(background, background_weights)[0]
 new_image["slug"] = random.choices(slug, slug_weights)[0]
 new_image["slime"] = random.choices(slime, slime_weights)[0]
 new_image["shell"] = random.choices(shell, shell_weights)[0]
 new_image["item"] = random.choices(iten, iten_weights)[0]
 new_image["hat"] = random.choices(hat, hat_weights)[0]

 if new_image in all_images:
  return create_new_image()
 else:
  return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
 new_trait_image = create_new_image()

 all_images.append(new_trait_image)

 #Parte 4
 '''
 É importante com projetos de avatar NFT que cada avatar seja único. Consequentemente, você precisará verificar se todas as imagens são exclusivas. 
 Uma função simples é escrita que faz um loop sobre todas as imagens e as armazena em uma lista e retorna as imagens duplicadas.
 Em seguida, você adiciona um identificador exclusivo a cada imagem.
'''


# Returns true if all images are unique
def all_images_unique(all_images):
 seen = list()
 return not any(i in seen or seen.append(i) for i in all_images)


print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
 item["tokenId"] = i
 i = i + 1

print(all_images)


#Parte 5
'''
Você atribuiu características com base nos pesos predefinidos e na função aleatória. Isso significa que é improvável que você tenha
exatamente 60 rostos brancos, mesmo que tenha definido o peso dos rostos brancos como 60. Para saber exatamente quanto cada traço ocorre, 
você deve saber quantos traços existem agora presentes em sua coleção de imagens.
Para fazer isso, você escreve o seguinte código:
Defina um dicionário para cada traço com suas respectivas classificações e inicie em 0
Faça um loop sobre suas imagens criadas e adicione-as ao seu respectivo dicionário de traços se você encontrar o traço.
'''

# Get Trait Counts

background_count = {}
for item in background:
 background_count[item] = 0

slug_count = {}
for item in slug:
 slug_count[item] = 0

slime_count = {}
for item in slime:
 slime_count[item] = 0

shell_count = {}
for item in shell:
 shell_count[item] = 0

iten_count = {}
for item in iten:
 iten_count[item] = 0

hat_count = {}
for item in hat:
 hat_count[item] = 0

for image in all_images:
 background_count[image["background"]] += 1
 slug_count[image["slug"]] += 1
 slime_count[image["slime"]] += 1
 shell_count[image["shell"]] += 1
 iten_count[image["item"]] += 1
 hat_count[image["hat"]] += 1

print(background_count)
print(slug_count)
print(slime_count)
print(shell_count)
print(iten_count)
print(hat_count)

#Parte 6
'''
Esta é a parte onde a mágica acontece: Criando a imagem!
Para cada imagem, o script executará o seguinte:
Abra o arquivo de características da imagem onde definimos os traços
Selecione a respectiva imagem de traço em seu diretório usando o pacote PIL .
Combine todas as características em uma imagem
Converta para RGB, este é o modelo de cores mais convencional
Salve no seu pc
'''
#### Generate Images

os.mkdir(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Python_Teste\/')

for item in all_images:
 im1 = Image.open(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Background\{background_files[item["background"]]}.png').convert('RGBA')
 im2 = Image.open(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Slug\{slug_files[item["slug"]]}.png').convert('RGBA')
 im3 = Image.open(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Slime\{slime_files[item["slime"]]}.png').convert('RGBA')
 im4 = Image.open(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Shell\{shell_files[item["shell"]]}.png').convert('RGBA')
 im5 = Image.open(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Itens\{iten_files[item["item"]]}.png').convert('RGBA')
 im6 = Image.open(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Hat\{hat_files[item["hat"]]}.png').convert('RGBA')

 # Create each composite
 com1 = Image.alpha_composite(im1, im2)
 com2 = Image.alpha_composite(com1, im3)
 com3 = Image.alpha_composite(com2, im4)
 com4 = Image.alpha_composite(com3, im5)
 com5 = Image.alpha_composite(com4, im6)

 # Convert to RGB
 rgb_im = com5.convert('RGB')
 file_name = str(item["tokenId"]) + ".png"
 rgb_im.save(r"C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Python_Teste\Slug_Island #" + file_name)

 from PIL import Image
 from IPython.display import display
 import random
 import json
 import os

 # SUBSTITUIÇÕES:
 '''
 ["Face"] --> Background
 ["Ears"] --> Slug
 ["Eyes"] --> Slime
 ["Hair"] --> Shell
 ["Mouth"] --> Iten
 ["Nose"] --> Hat
 '''

 # O que são metadados NFT?

 # fonte: https://betterprogramming.pub/generate-your-nft-metadata-11a878c082b9

 '''
 Os metadados NFT são o núcleo de um NFT. É um documento JSON que geralmente contém o seguinte:
 .Nome do NFT
 .Descrição do NFT
 .Link para a imagem hospedada
 .Características
 .Etc…
 Esses metadados NFT serão a entrada do seu contrato inteligente NFT que você implantará na rede Ethereum na terceira parte.
 '''

 # Carregue suas imagens NFT na nuvem
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
 https://gateway.pinata.cloud/ipfs/QmZPizWQp7yiJtM2wmxR16Z5Lbc6ETMeqGem8rNjJKfk8k
 '''

 # Gerar metadados NFT
 '''
 all-traits.json
 Na primeira parte da série NFT Creator, você criou uma lista chamada “all_images” especificando as características de cada imagem.  
 Simplesmente, despeje essa lista em um arquivo .json usando a função json.dump().
 '''
 #### Generate Metadata for all Traits
 try:
    os.mkdir(fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Python_Teste\Metafiles')
 except FileExistsError:
    pass


 METADATA_FILE_NAME = fr'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Python_Teste\Metafiles\all-traits.json';
 with open(METADATA_FILE_NAME, 'w') as outfile:
     json.dump(all_images, outfile, indent=4)

 # [token_id].json
 '''
 Em seguida, você deseja criar um arquivo .json específico para cada imagem:

 carregar no all_traits.json
 Especifique suas imagens "URL BASE" que você copiou anteriormente no site Pinata. Certifique-se de adicionar um “/” adicional no final!
 Especifique o nome do seu projeto
 Faça um loop no dicionário all_traits .json usando o acessador de chaves e gere um arquivo .json individual para cada imagem NFT exclusiva.
 Para esta imagem, você receberá, por exemplo, o seguinte arquivo .json:
 '''


 #OBS: Os diretórios abaixo devem ser diferentes do de cima

 #### Generate Metadata for each Image

 f = open(r'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Python_Teste\Metafiles\all-traits.json', )
 data = json.load(f)

 # Changes this IMAGES_BASE_URL to yours
 IMAGES_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmZPizWQp7yiJtM2wmxR16Z5Lbc6ETMeqGem8rNjJKfk8k"
 PROJECT_NAME = "Slug_Island"


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
     token["attributes"].append(getAttribute("item", i["item"]))
     token["attributes"].append(getAttribute("hat", i["hat"]))

     with open(r'C:\Users\bruno.marques\OneDrive - Linx SA\Documentos\pixelart\Slug_Island\Python_Teste\Metafiles' + str(token_id) + ".json", 'w') as outfile:
         json.dump(token, outfile, indent=4)
 f.close()

 # Carregue os metadados para pinata
 '''
 Carregue seus metadados gerados para Pinata da mesma forma que para as imagens.

 Logo você conseguirá visualizar seu metadata correspondente a imagem correta, confira uma para ver se correspondem as informações
 '''

print('Programa Finalizado, Pegue suas Lesmas')