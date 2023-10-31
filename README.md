O programa apresenta um sistema simples de cadastro de candidatos para posterior consulta por parte de um recrutador. Para criação de interface gráfica foi-se usado a biblioteca Tkinter e para armazenamento de dados o banco de dados SQLite.

# index.py
Esté é o arquivo principal do sistema. Ele importa a biblioteca Tkinter, como mencionado acima, e as classes de outros arquivos (CandidatoApp e RecrutadorApp). É no index que se encontra a interface do usuário com uma janela contendo dois botões: um para candidatos e outro para recrutadores.

# candidato.py
Este arquivo refere-se a classe CandidatoApp, que representa a interface gráfica de cadastro de candidatos.
É nesta sessão que se é coletado dados do candidato que foram inseridos na interface gráfica, armazenando-os num banco de dados SQLite chamado "dados_devs.db". 

# recrutador.py
Este arquivo define a classe RecrutadorApp, que representa a interface gráfica para recrutadores visualizarem candidatos com base em um consulta de filtros específicos. Para realizar uma consulta mais refinada é necessário preencher pelo menos um dos campos, caso contrário, o programa retornará todos os candidados do banco em questão.

#Integrantes:
Gustavo Victor Teixeira de Sousa;
Matrícula: 202209303602

Luana Rafaela da Silva;
Matrícula: 202208885063

Marcelo Reggiani;
Matrícula: 202208923496
