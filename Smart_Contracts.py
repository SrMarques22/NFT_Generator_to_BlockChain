# STEP 3

#Contrato Inteligente

'''
Se você quiser codificar junto, poderá encontrar o código de pré-requisito nas partes um e dois da série.
O que é um Contrato Inteligente?
Um contrato inteligente é um programa executado na blockchain Ethereum. Seu código e dados residem em um endereço específico na blockchain Ethereum.
Os NFTs são alimentados por contratos inteligentes que lidam com a transferibilidade e verificam a propriedade.
Você usará o padrão ERC-721 . Este é um padrão NFT que fornece funcionalidades para contratos inteligentes.
'''

#Configuração do ambiente "Alchemy"

'''
Crie uma conta na https://www.alchemy.com/ .
Alchemy é uma plataforma de desenvolvedor de blockchain focada em facilitar o desenvolvimento do Ethereum. 
Isso nos permite pular muito da programação técnica difícil do blockchain.
Após a criação da sua conta, clique em “Criar App” e preencha os seguintes parâmetros:

OBS, ao criar a conta no site a unica opção será ETHEREUM, basta seguir com essa e depois definir as opções abaixo para o APP dentro do site

Name: Name of your NFT project
Environment: Staging
Chain: Polygon
Network: Ropsten(gratis, mas esta inativada), ou Polygon (com taxas de gas, porem bem amis baixas que o ethereum), neste caso
aconselho colocar a Polygon, e depois, selecionar a categoria Polygon Mumbai que é um ambiente de teste, não esquecer de conectar
nessa rede no metamask para facilitar pode usar o link abaixo:
https://chainlist.org/ (obs: habilitar o botão TESTNETS no site)

adicionar matics fakes(criptomoedas fakes para testes de transações na blockchain):
https://faucet.polygon.technology/ - obs: não esquecer de selecionar a rede de teste mumbai criada acima antes de copiar o link da carteira



A fim de testes usar a Polygon Mumbai

Depois desses passos acima, verifica na sua carteira Metamask se está com o dinheiro FAKE

provavelmente que fique 02 ou 04 na frente do nome da moeda configurada no metamask

'''

#Criação do projeto

'''
Crie um diretório onde você salvará todos os seus arquivos de projeto.
Abra seu prompt de comando digitando “cmd” na pesquisa do Windows
Mude para o diretório onde você deseja criar sua pasta de projeto usando o comando “cd”.
Escreva na linha de comando:

cd C:\SEUDIRETÓRIO

Crie a pasta do projeto NFT e mude para esse diretório.
Escreva na linha de comando:


mkdir nft 
cd nft



Dentro da pasta do projeto, você inicializa o npm.
Se você não instalou o NPM: baixe o Node.js (https://nodejs.org/en/)

Escreva na linha de comando dentro da pasta do node que baixou:

npm init
Pressione enter e responda como eu fiz abaixo:

Na linha de comando:

Nome do pacote: (nft-creator)
2versão: (1.0.0)
3descrição: Meu primeiro NFT!
4ponto de entrada: (index.js)
5comando de teste:
repositório 6git:
7 palavras-chave:
8 autor:
9licença: (ISC)
10Para gravar em /Users/thesuperb1/Desktop/my-nft/package.json:
11
12{
13 "nome": "criador nft",
14 "versão": "1.0.0",
15 "descrição": "Meu primeiro NFT!",
16 "principal": "index.js",
17 "roteiros": {
18 "test": "echo \"Erro: nenhum teste especificado\" && exit 1"
19},
20 "autor": "",
21 "licença": "ISC"
22}

'''

#Instalar capacete
'''
Capacete de segurança
O ambiente de desenvolvimento do Hardhat ajuda na criação de contratos inteligentes localmente antes de implantá-los na cadeia ativa. Para mais informações sobre o Hardhat, você pode visitar o site deles .

Execute na linha de comando:

npm install --save-dev hardhat
npx hardhat

O comando npx hardhat cria um projeto de hardhat.

Quando perguntado: “O que você quer fazer?”, responda “crie um hardhat.config.js vazio”

888    888                      888 888               888 888    888                      
888 888               888 888    888                      888 888               888 8888888888  8888b.  888d888 .
d88888 88888b.   8888b.  888888 888    888     "88b 888P"  d88" 888 888 "88b     "88b 888 888    888 .d888888 888    
888  888 888  888 .d888888 888 888    888 888  888 888    Y88b 888 888  888 888  888 Y88b. 888    888 "Y888888 888     
"Y88888 888  888 "Y888888  "Y888 
👷 Welcome to Hardhat v2.0.11 👷‍ 
? What do you want to do? … 
Create a sample project 
❯ Create an empty hardhat.config.js 
Quit

'''

#Organize o projeto

'''
Você cria duas pastas:

Contracts: Localização do seu código de contrato inteligente NFT
Scripts: Local para os scripts implantarem e interagirem com seus contratos inteligentes
Execute o seguinte na linha de comando (certifique-se de estar no diretório raiz NFT):

mkdir contracts
mkdir scripts

'''

#Escreva seu contrato inteligente

'''
Finalmente, a configuração está feita!
Vamos entrar na parte de codificação. Eu uso o VSCode como meu editor preferido.
Nesta parte, você escreverá contratos inteligentes no Solidity.
Solidity é uma linguagem de alto nível orientada a objetos especificamente para implementar contratos inteligentes.
Execute o seguinte na linha de comando:

npm install @openzeppelin/contracts

Isso instalará a openzeppelin biblioteca em nossa pasta. Você precisa dessas aulas mais tarde.
No seu editor (por exemplo, VScode):
Navegue até a contracts pasta e crie um novo arquivo MyNFT.sol
Copie o seguinte código no arquivo:

//Contract based on [https://docs.openzeppelin.com/contracts/3.x/erc721](https://docs.openzeppelin.com/contracts/3.x/erc721)
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract MyNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() public ERC721("MyNFT", "NFT") {}

    function mintNFT(address recipient, string memory tokenURI)
        public onlyOwner
        returns (uint256)
    {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}


Um homem sábio me disse uma vez que você não precisa reinventar a roda.
Portanto, no topo de nosso contrato inteligente, você está importando três classes de contrato inteligente OpenZeppelin .

@openzeppelin/contracts/token/ERC721/ERC721.sol


A declaração de importação acima contém a implementação do padrão ERC-721. Ao importar esta declaração, nosso contrato 
inteligente herda todos os métodos do padrão ERC-721. Mais informações aqui .

@openzeppelin/contracts/utils/Counters.sol


A declaração de importação acima é necessária, pois seu contrato inteligente precisa de um contador para acompanhar o 
número total de NFTs cunhadas e atribuir o ID exclusivo em nossa nova NFT.

@openzeppelin/contracts/access/Ownable.sol


Para permitir que apenas o proprietário do contrato inteligente crie NFTs, importamos o arquivo Ownable.sol. 
Isso é feito usando o controle de acesso . Se você quiser que alguém possa cunhar um NFT usando seu contrato inteligente, 
remova a palavra Ownablena linha 10 e onlyOwnerna linha 17.)

constructor() public ERC721 ("MyNFT" , "NFT)


Em nosso construtor ERC-721, você notará que passamos 2 strings NFTCreatore NFTC. A primeira variável é o nome do contrato 
inteligente e a segunda é seu símbolo. Sinta-se à vontade para alterar isso para qualquer que seja sua preferência!

mintNFT(endereço do destinatário, string de memória uri)

A função acima permite cunhar um NFT. Duas variáveis ​​são usadas como entrada:

address recipient: O endereço para onde o NFT deve ser enviado
string memory tokenURI: o URI (identificador uniforme de recursos) dos metadados NFT. Por favor, leia a parte 2 da série para criar os metadados.
'''

#Conecte Metamask, Alquimia e seu Projeto

'''
Você deseja criar um arquivo de ambiente onde possa armazenar com segurança sua chave de API Alchemy e sua chave privada Metamask.
Isso é necessário para poder interligar os dois com o seu projeto.

Instale o pacote dotenv no diretório do seu projeto. Este pacote permite carregar variáveis ​​ de ambiente do .envarquivo.
Execute os seguintes comandos na linha de comando:

npm install dotenv --save

Crie um arquivo .env chamado “.env” no diretório raiz e adicione o seguinte:

Chave privada de metamáscara (SITE COM PASSO A PASSO PARA EXPORTAR CHAVE NO METAMASK: https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key)
URL da API HTTP Alchemy (Assim que acessar o site com o app configurado, selecionar e clicar no botão view key)

Seu arquivo .env deve ficar assim:

ex:
API_URL = "https://eth-ropsten.alchemyapi.io/v2/your-api-key"
PRIVATE_KEY = "your-metamask-private-key"



Este é o exemplo da estrutura do seu projeto:

Exemplo da estrutura do seu projeto:
artifacts
cache
contracts
node_modules
scripts
.env
hardhat.config.js
package.json
package-lock.json

'''

#Instalar Ether.js

'''
Você aproveita a biblioteca Ether.js para implantação de contrato.
Escreva na linha de comando:

npm install --save-dev @nomiclabs/hardhat-ethers "ethers@^5.0.0"

'''

#Atualizar capacete
'''
Muitas dependências foram atualizadas, o que exige que nosso hardhat.config.js seja atualizado de acordo.

/**
* @type import('hardhat/config').HardhatUserConfig
*/
require('dotenv').config();
require("@nomiclabs/hardhat-ethers");
const { API_URL, PRIVATE_KEY } = process.env;
module.exports = {
   solidity: "0.8.1",
   defaultNetwork: "mumbai",
   networks: {
      hardhat: {},
      mumbai: { 
         url: API_URL,
         accounts: [`0x${PRIVATE_KEY}`]
      }
   },
}

'''

#Compilar nosso contrato
'''
Você compila o contrato chamando a tarefa “compile”.
Escreva na linha de comando:

npx hardhat compile

'''

#Escrever script de implantação
'''
Navegue até a pasta de scripts e crie um arquivo chamado “deploy.js.
Por favor, dê uma olhada aqui(https://hardhat.org/tutorial/testing-contracts#writing-tests) se você quiser mais detalhes sobre o que é feito exatamente.

async function main() {
  const MyNFT = await ethers.getContractFactory("MyNFT")

  // Start deployment, returning a promise that resolves to a contract object
  const myNFT = await MyNFT.deploy()
  console.log("Contract deployed to address:", myNFT.address)
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error)
    process.exit(1)
  })
  
Detalhamento dos conceitos mais importantes em deploy.js:

const MyNFT = await ethers.getContractFactory("MyNFT")

O ContractFactoryin ethers.jsé uma abstração usada para implantar novos contratos inteligentes, então MyNFTaqui está uma 
fábrica para instâncias do nosso contrato NFT. Ao usar o plug-in hardhat-ethers ContractFactorye Contractas instâncias são 
conectadas ao primeiro signatário por padrão.

const myNFT = await MyNFT.deploy()


Chamar deploy()a ContractFactoryiniciará a implantação e retornará a Promiseque resolve para um arquivo Contract. 
Este é o objeto que possui um método para cada uma de nossas funções de contrato inteligente.

'''

# Vamos implantar nosso contrato inteligente!
'''
Execute o seguinte na linha de comando (certifique-se de estar em seu diretório raiz):

npx hardhat run scripts/deploy.js --network ropsten



Você deve ver o seguinte resultado, mas com um endereço diferente:

Contract deployed to address: 0x81c587EB0fE773404c473DFQDCQ1327C470eED



Você pode ver seu contrato implantado usando o Ropsten etherscan (OU POLYGON MUMBI SCAN) .

A transação ficará mais ou menos assim:

No Fromcampo, você verá o endereço da sua conta MetaMask.

No Toendereço estará escrito “Criação de Contrato”.

Você pode clicar no “Txn Hash” para obter mais detalhes da transação



O contrato já está implantado.

No próximo artigo, você aprenderá como cunhar seus NFTs usando o contrato inteligente implantado.
'''