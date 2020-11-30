# 4a-plataforma-v2
Teste de Estudo em Desenvolvimento Python
por fde-capu

---

O arquivo `bitmap.json` deve conter a matriz de referência.

### Ex 1. Contagem de aparições de vetor em uma matriz (definida pelo arquivo).

Use: 

- `python3 bmp_matrix.py [1, 2, 3]`
- `python3 bmp_matrix.py 1, 2, 3`
- `python3 bmp_matrix.py 1 2 3`
- `python3 bmp_matrix.py "[1, 2, 3]"`
- `python3 bmp_matrix.py "1, 2, 3"`
- `python3 bmp_matrix.py "1 2 3"`

	(double `""` and single `''` quotes accepted).


### Ex 2. Programa do Ex. 1 transformado em API Restful.

Use:

- `build.sh`: cria um container escutando a porta 5000.
- `test.sh`: faz algumas chamadas `curl` no modelo `curl -d "2 5 7" localhost:5000`. A string referência pode ter as mesmas variações que no Ex. 1.
