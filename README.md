# Greed_Planejador de Estudos

**Número da Lista**: 25<br>
**Conteúdo da Disciplina**: Greed

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0036435  |  Pedro Henrique Carvalho Campos |
| 20/0019520  |  Hian Praxedes de Souza Oliveira |

## Sobre 

Esse código é um exemplo de implementação do algoritmo Interval Scheduling para a criação de uma agenda ou planejador de estudos. 

Ao execultar ele o usuário deve escolher uma data e o horário de inico e término da atividade que deseja acrescentar. O usuário pode criar quantas tarefas quiser e após adicioná-las poderá criar a programação com todas as tarefas adicionadas por ele.

Para isso, o método gerar_programacao() é chamado quando o botão "Gerar Programação" é clicado, verificando se há pelo menos uma tarefa adicionada na lista tarefas. Caso contrário, exibe uma caixa de diálogo de erro.

Em seguida, as tarefas são ordenadas com base na data e no horário de término. Isso é feito usando o método sort() da lista tarefas e uma função lambda como chave de ordenação. A função lambda lambda x: (x[1], x[3]) extrai a data (índice 1) e a hora de término (índice 3) de cada elemento da lista, garantindo que as tarefas sejam ordenadas em ordem cronológica.

Após a ordenação, o método agendamento_intervalo() é chamado, passando a lista tarefas como argumento. Esse método implementa o algoritmo de Interval Scheduling.

### Vídeo de apresentação
[Apresentação](https://github.com/projeto-de-algoritmos/Greed_planejadorDeEstudos/blob/main/V%C3%ADdeo%20de%20apresenta%C3%A7%C3%A3o/V%C3%ADdeo%20de%20apresentacao.mp4)

## Screenshots

![image](https://github.com/projeto-de-algoritmos/Greed_planejadorDeEstudos/assets/70337717/8535c62b-4509-443a-a031-410f976cdd25) </br></br>
![image](https://github.com/projeto-de-algoritmos/Greed_planejadorDeEstudos/assets/70337717/3337a91e-67a2-4474-8f42-25de6bcc5917)</br></br>
![image](https://github.com/projeto-de-algoritmos/Greed_planejadorDeEstudos/assets/70337717/a62862f9-d1ad-4848-8814-fdcfcd72bcd0)</br></br>

## Instalação 
**Linguagem**: Python<br>

## Uso 
Abra o arquivo do código em um editor de código como o VSCode, o Sublime Text, o PyCharm ou qualquer outro de sua preferência.

Execute o código com o comando:

``` shell 
python3 planejadorDeEstudos.py
``` 

Aguarde até que a janela do programa esteja aberta e divirta-se.
