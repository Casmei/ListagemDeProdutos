### Listagem de Produtos
## Objetivo
Inicialmente o projeto foi desenvolvido como um objeto de estudo, visando a aprendizagem e o treinamento.
Seu propósito é inteiramente **educativo e expositivo**. Nesse projeto foi aplicado o conceito de Models e a integração dele com os Templates.
## Proposta
### - Primeira Página | Listagem de Produtos
Encontramos na primeira página uma lista simples, criada a partir de um laço ```for```, que aplicara um estilo especíico para cada objeto da classe Produtos. Contém em seu cabeçalho os atributos definidos no arquivo **models.py**
 
![image](https://user-images.githubusercontent.com/68354933/131719409-4fcaba7a-3850-401a-a46c-5fcbf835561c.png)

### - Segunda Página | Produto
Ao clicarmos no nome de qualquer um dos produtos, seremos redirecionados para a página **produto**, podendo assim visualizar informações mais detalhadas sobre o produto em expecífico, mas de início eu não acrescentei nada.

- É importante frizar que são inseridos em suas urls os ID's dos respectivos produtos.

![image](https://user-images.githubusercontent.com/68354933/131719719-9f31623b-7828-463d-9642-2110728577aa.png)

### - Painel Adiministrativo | DjangoAdmin
O Django utiliza uma ORM, que abstrai o trabalho de criar diretamente a estrutura no banco, iremos criar uma classe que representará a tabela.

![image](https://user-images.githubusercontent.com/68354933/131726897-d87bfe9d-c04f-4b50-9ede-d3c69ceea15d.png)
