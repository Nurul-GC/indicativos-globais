![indig-icon](img/favicon-192x192.png)

# indicativos-globais

Com exatamente 240 valores a **IndiG API** \
esta composta por apenas 2 endpoints, correspondentes ao:

- **retorno total dos valores** 
  - (https://indigc.herokuapp.com/indicativos/) 
- e ao **retorno de um valor específicado pelo seu número ‘id’** 
  - (https://indigc.herokuapp.com/indicativos/<id>/)
  
## Formatos Validos

A IndiG aceita dois formatos padrao:

- JSON
  - **_Para retorno de um `JSON` o `URI` da _API_ deve estar acompanhado da consulta `?format=json`_ no final...**
- API Navegável
  - **Para ter acesso aos valores de forma navegavel, basta abrir o `URI` da _API_ num navegador, mas, sem o valor da consulta...**

## Endpoints

- Raiz API: 
  - <https://indigc.herokuapp.com/?format=json>
```json
{
  "indicativos": "https://indigc.herokuapp.com/indicativos/?format=json"
}
```
![api-root-demo](img/demos/apiroot.png)

- Lista de Paizes e Indicativos: 
  - <https://indigc.herokuapp.com/indicativos/?format=json>
```json
[
    {
        "id": 1,
        "pais": "(AFEGANISTÃO, 93)"
    },
    {
        "id": 2,
        "pais": "(ÁFRICA DO SUL, 27)"
    },
    {
        "id": 3,
        "pais": "(ALASKA, 1907)"
    }, 
  ...
]
```
![indicativos-list-demo](img/demos/indicativoslist.png)

- Valor especifico: 
  - <https://indigc.herokuapp.com/indicativos/7/?format=json>
```json
{
  "id": 7,
  "pais": "(ANGOLA, 244)"
}
```
![indicativo-especific-demo](img/demos/indicativoespecifico.png)

---

&copy; 2021 Nurul-GC
