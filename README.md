# 4a-plataforma-v2
Teste de Estudo em Desenvolvimento Python
por fde-capu

---

### Ex 1. Contagem de aparições de vetor em uma matriz.

O arquivo `bitmap.json` deve conter a matriz de referência.

:: Use: 

- `python3 main.py [1, 2, 3]`
- `python3 main.py 1, 2, 3`
- `python3 main.py 1 2 3`
- `python3 main.py "[1, 2, 3]"`
- `python3 main.py "1, 2, 3"`
- `python3 main.py "1 2 3"`
- `make unit` para rodar testes.

	(Aspas duplas `""` e simples `''` são aceitas.)

### Ex 2. Programa do Ex. 1 transformado em API Restful.

:: Use:

- `setup.sh`: cria um container escutando a porta 5000.
- `test.sh`: faz algumas chamadas `curl` no modelo `curl -d "2 5 7" localhost:5000`. A string referência pode ter as mesmas variações que no Ex. 1.
- `login.sh`: efetual login root no container, via Docker.

### Ex 3. Faça algumas estatísticas de uma corrida de super-heróis.

:: Use:

- `run.sh`: exibe as respostas de cada problema proposto.
