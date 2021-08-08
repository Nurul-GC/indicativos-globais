![indig-icon](img/favicons/favicon-192x192.png)

# indicativos-globais

Com exatamente 240 valores a **IndiG API** \
esta composta por apenas 2 endpoints, correspondentes ao:

- **retorno total dos valores** 
  - `indigc.herokuapp.com/indicativos/`
- e ao **retorno de um valor específicado pelo seu número ‘id’** 
  - `indigc.herokuapp.com/indicativos/[id]/`
  
## Formatos Validos

A IndiG aceita dois formatos padrao:

- JSON
  - **_Para retorno de um `JSON` o `URI` da _API_ deve estar acompanhado da consulta `?format=json`_ no final...**
- API Navegável
  - **Para ter acesso aos valores de forma navegavel, basta abrir o `URI` da _API_ num navegador, mas, sem o valor da consulta...**

## Endpoints

- Raiz API: 
  - <https://indigc.heroku.app/?format=json>
```json
{
  "indicativos": "https://indigc.herokuapp.com/indicativos/?format=json"
}
```

- Lista de Paizes e Indicativos: 
  - <https://indigc.heroku.app/indicativos/?format=json>
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

- Valor especifico: 
  - <https://indigc.herokuapp.com/indicativos/7/?format=json>
```json
{
  "id": 7,
  "pais": "(ANGOLA, 244)"
}
```

[**Clique, para uma ilustração...**](https://nurul-gc.github.io/indicativos-globais)

---

&copy; 2021 Nurul-GC
