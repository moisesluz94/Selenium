O código foi criado para realizar teste de login em uma determinada página de logins de uma instituição de ensino. 
O resultado do teste, deveria ter integração com o monitoramento no Zabbix. Com isso, caso ocorresse alguma falha de login, seria gerado
um alerta no monitoramento. 

Programa Python está em uma estação Windows, e há uma ação no Zabbix que executa este programa. Este programa gera um log com a informações dos testes. 
Há outra ação no Zabbix, que executa um script (.bat), que realiza a leitura do log com o status e gera uma trigger monitoramento.
