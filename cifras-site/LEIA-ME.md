# Site de cifras

## Como colocar no ar (uma vez só)
1. Crie um repositório **público** no GitHub (ex.: `cifras`).
2. Envie **todo o conteúdo desta pasta** (inclusive a pasta oculta `.github`) para o repositório.
3. Vá em **Settings → Pages**. Em *Source*, escolha **Deploy from a branch**, branch **main**, pasta **/ (root)** e salve.
4. Em **Settings → Actions → General → Workflow permissions**, marque **Read and write permissions** e salve.
5. Aguarde 1–2 minutos. O endereço será `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/`.

## Adicionar cifras
Coloque os PDFs na pasta `cifras/` e faça o upload. Em cerca de 30 segundos o GitHub atualiza
a lista sozinho (aba **Actions** mostra o andamento). Nada para editar.

## Tags — duas formas
**1. Por pastas (automático):** o nome da subpasta vira tag.
`cifras/Louvor/Grande é o Senhor.pdf` → tag **Louvor**. Pode usar mais de um nível de pastas.

**2. Pelo arquivo `tags.json`:** para qualquer PDF, em qualquer lugar:
```json
{
  "Grande é o Senhor.pdf": ["violão", "lenta"],
  "Outra Música.pdf": ["teclado"]
}
```
Use o nome exato do arquivo. Pode combinar as duas formas.

## No site
- **Pesquisa** por nome ou tag (ignora acentos e maiúsculas).
- **Tags**: clique em uma ou mais para filtrar.
- **Cifra aberta**: zoom A−/A+, modo escuro, rolagem automática com velocidade, anterior/próxima, baixar PDF.
