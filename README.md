# README

## Introdução

Essa é uma aplicação web desenvolvida com Flask que gera texto com base em uma mensagem de entrada. A aplicação utiliza a API do Groq para gerar o texto.

## Como usar

Para usar a aplicação, você precisa fazer uma solicitação POST para o endpoint `/groq-generator`. O corpo da solicitação deve conter os seguintes campos:

- **username**: o nome de usuário para autenticação
- **password**: a senha para autenticação
- **message**: a mensagem que você deseja que o modelo de linguagem gerencie

### Exemplo de solicitação:

```json
{
    "username": "seu_usuario",
    "password": "sua_senha",
    "message": "Este é um exemplo de mensagem"
}
