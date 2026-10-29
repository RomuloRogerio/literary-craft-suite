---
name: critique
description: Inicia uma análise editorial cirúrgica. Identifica ou pergunta o gênero literário e despacha o texto para o subagente especialista correspondente.
---

Avalie o texto fornecido pelo usuário a seguir.

### Procedimento Obrigatório:
1. Verifique se o gênero literário foi informado. Caso não esteja claro, pergunte ao usuário:
   *"Selecione o gênero do manuscrito para carregar o agente correspondente:*
   - **[1] Livro-Jogo / Literatura Interativa / Dark Fantasy** (`gamebook-architect`)
   - **[2] Alta Fantasia / Ficção Científica Linear** (`epic-speculative-editor`)
   - **[3] Suspense / Thriller / Horror** (`noir-thriller-editor`)
   - **[4] Artigo de Não-Ficção / Ensaio** (`essay-nonfiction-editor`)*"
2. Após a confirmação, acione o subagente correspondente e forneça a crítica seguindo rigorosamente a estrutura de 4 seções (Pontos Fortes, Pontos Fracos, Destaques de Prolixidade/IA, Sugestões de Refinamento).

Texto para análise:
$ARGUMENTS
