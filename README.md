# 🖋️ Literary Craft Suite: Especificação Mestre e Referência Técnica

**Suíte Editorial Cirúrgica para Claude Code, OpenAI Codex e Google Gemini**

*Autor: Rômulo Rogério | Licença: MIT*

---

## 📑 Índice Geral

1. [Visão Geral e Arquitetura do Repositório](#1-visão-geral-e-arquitetura-do-repositório)
   * [Tese Operacional](#tese-operacional)
   * [Fluxo de Processamento](#fluxo-de-processamento)
   * [Árvore de Diretórios](#árvore-de-diretórios)
2. [Manifestos de Configuração e Governança](#2-manifestos-de-configuração-e-governança)
   * `.claude-plugin/plugin.json`
   * `.claude-plugin/marketplace.json`
   * `.github/copilot-instructions.md`
   * `.editorconfig`
   * `.gitignore`
   * `requirements.txt`
   * `LICENSE`
3. [Subagentes Especializados (`agents/`)](#3-subagentes-especializados-agents)
   * `router-critic.md` (Triagem Ativa de Gênero)
   * `gamebook-architect.md` (Livros-Jogos e Narrativa Interativa)
   * `epic-speculative-editor.md` (Alta Fantasia e Ficção Científica)
   * `noir-thriller-editor.md` (Suspense, Policial e Horror)
   * `essay-nonfiction-editor.md` (Artigos e Ensaios Literários)
4. [Skills Modulares e Acervo Técnico (`skills/`)](#4-skills-modulares-e-acervo-técnico-skills)
   * **Módulo Anti-IA:** `SKILL.md`, `ptbr-banned-patterns.md`, `burstiness-syntax-rules.md`
   * **Módulo Fundamentos Literários:** `SKILL.md`, `assis-brasil-radiating-character.md`, `poe-composition-climax.md`, `card-mice-quotient.md`
   * **Módulo Ludonarrativa e Gamebooks:** `SKILL.md`, `rei-methodology.md`, `weiller-rogers-mechanics.md`, `branching-ethical-dilemmas.md`
5. [Comandos de Terminal (`commands/`)](#5-comandos-de-terminal-commands)
   * `critique.md`
   * `humanize.md`
   * `audit-branching.md`
6. [Casos Práticos e Benchmark (`examples/`)](#6-casos-práticos-e-benchmark-examples)
   * `amostra-livro-jogo-raw.md` (Entrada Bruta com Vícios de IA)
   * `amostra-critica-esperada.md` (Relatório Editorial Padrão Ouro)
7. [Orquestrador Multi-LLM (`craft.py`)](#7-orquestrador-multi-llm-craftpy)
8. [Script de Reconstrução Automática (PowerShell)](#8-script-de-reconstrução-automática-powershell)

---

## 1. Visão Geral e Arquitetura do Repositório

### Tese Operacional

Grandes Modelos de Linguagem (LLMs) tendem a homogeneizar a escrita criativa por meio de padrões sintáticos mecânicos: orações espelhadas, adjetivos em tríades, falsas antíteses, travessões dramáticos excessivos e conclusões paternalistas.

O **Literary Craft Suite** transforma o **Claude Code**, o **Codex** e o **Gemini** em uma bancada de edição implacável. Desenvolvido para escritores de ficção de alto nível, ensaístas e designers de narrativas interativas, o pacote conecta técnicas consagradas da literatura mundial às exigências lógicas do game design moderno.

### Fluxo de Processamento

```text
                    ┌──────────────────────────────────┐
                    │      TEXTO BRUTO / SEÇÃO         │
                    └─────────────────┬────────────────┘
                                      │
                         ┌────────────▼────────────┐
                         │   /critique  (Router)   │
                         └────────────┬────────────┘
                                      │
            ┌─────────────────────────┼─────────────────────────┐
            ▼                         ▼                         ▼
   [Livro-Jogo & RPG]        [Ficção Especulativa]      [Thriller & Noir]
   gamebook-architect        epic-speculative-editor    noir-thriller-editor
            │                         │                         │
            └─────────────────────────┼─────────────────────────┘
                                      │
                         ┌────────────▼────────────┐
                         │   anti-ai-purification  │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────▼────────────────┐
                    │   DIAGNÓSTICO CIRÚRGICO EM 4     │
                    │   BLOCOS + REESCRITA MODELO      │
                    └──────────────────────────────────┘
```

### Árvore de Diretórios

```text
literary-craft-suite/
├── .claude-plugin/              # Metadados e manifesto para Claude Code CLI
│   ├── plugin.json
│   └── marketplace.json
├── .github/                     # Integração com GitHub Copilot e CI/CD
│   ├── copilot-instructions.md
│   └── workflows/
│       └── validate-suite.yml
├── agents/                      # Personas dos subagentes especialistas
│   ├── router-critic.md
│   ├── gamebook-architect.md
│   ├── epic-speculative-editor.md
│   ├── noir-thriller-editor.md
│   └── essay-nonfiction-editor.md
├── skills/                      # Conhecimento granular (Progressive Disclosure)
│   ├── anti-ai-purification/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── ptbr-banned-patterns.md
│   │       └── burstiness-syntax-rules.md
│   ├── literary-foundations/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── assis-brasil-radiating-character.md
│   │       ├── poe-composition-climax.md
│   │       └── card-mice-quotient.md
│   └── gamebook-ludonarrative/
│       ├── SKILL.md
│       └── references/
│           ├── rei-methodology.md
│           ├── weiller-rogers-mechanics.md
│           └── branching-ethical-dilemmas.md
├── commands/                    # Comandos de barra para Claude Code
│   ├── critique.md
│   ├── humanize.md
│   └── audit-branching.md
├── examples/                    # Amostras para testes de regressão
│   ├── amostra-livro-jogo-raw.md
│   └── amostra-critica-esperada.md
├── .editorconfig                # Padronização de quebras de linha e charset
├── .gitignore                   # Proteção de caches, logs e chaves de API
├── craft.py                     # CLI multi-provedor (Claude, Codex, Gemini)
├── LICENSE                      # Licença MIT
├── README.md                    # Vitrine do repositório no GitHub
└── requirements.txt             # Dependências Python para a CLI
```

---

## 2. Manifestos de Configuração e Governança

### `.claude-plugin/plugin.json`
```json
{
  "name": "literary-craft-suite",
  "version": "1.0.0",
  "description": "Suíte editorial cirúrgica para ficção, não-ficção e livros-jogos. Triagem por gênero, eliminação de vícios de IA e ludonarrativa.",
  "author": {
    "name": "Rômulo Rogério"
  },
  "license": "MIT",
  "keywords": [
    "creative-writing",
    "gamebook",
    "ludonarrative",
    "literary-criticism",
    "anti-ai",
    "pt-br"
  ]
}
```

### `.claude-plugin/marketplace.json`
```json
{
  "name": "literary-craft-marketplace",
  "owner": {
    "name": "Rômulo Rogério"
  },
  "plugins": [
    {
      "name": "literary-craft-suite",
      "description": "Crítica literária erudita, análise de ramificações para livros-jogos e depuração de escrita robótica de LLM.",
      "version": "1.0.0",
      "source": "./",
      "category": "writing"
    }
  ]
}
```

### `.github/copilot-instructions.md`
```markdown
# Diretrizes Editoriais e Anti-IA para Manuscritos e Livros-Jogos

Ao redigir, editar, completar ou auditar textos ficcionais, capítulos de livros ou seções de livros-jogos neste repositório:

1. Regras Anti-IA Obrigatórias:
   Consulte `skills/anti-ai-purification/references/ptbr-banned-patterns.md`. Elimine termos proibidos como "tapeçaria", "mosaico", "farol", "não apenas X, mas Y", fechos moralizantes e "vale ressaltar".
2. Tipografia e Pontuação:
   Corte travessões explicativos no meio da narração para inserir comentários da voz narrativa. Elimine dois-pontos estruturais usados para justificar a oração anterior em prosa. Não empilhe parágrafos curtos de uma única linha no padrão copywriting.
3. Livros-Jogos e Ludonarrativa:
   Aplique o Método REI (`skills/gamebook-ludonarrative/references/rei-methodology.md`). Narre em segunda pessoa no presente do indicativo ("você avança", "tu notas"). Construa escolhas com assimetria de riscos e custos éticos permanentes.
```

### `.editorconfig`
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.py]
indent_size = 4

[*.md]
trim_trailing_whitespace = false
```

### `.gitignore`
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.env
.env
.venv/
venv/
ENV/

# IDEs e Editores
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
.idea/
*.swp
*.swo

# Sistema Operacional
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
.DS_Store

# Logs e Saídas Temporárias
*.log
temp/
dist/
build/
```

### `requirements.txt`
```text
anthropic>=0.45.0
openai>=1.60.0
google-genai>=1.0.0
rich>=13.9.0
```

### `LICENSE`
```text
MIT License

Copyright (c) 2026 Rômulo Rogério

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 3. Subagentes Especializados (`agents/`)

### `agents/router-critic.md`
```markdown
---
name: router-critic
description: Agente de triagem editorial. Identifica o gênero textual e despacha o manuscrito para o subagente especializado correspondente.
---

Você é o editor-chefe da suíte literária. Sua única tarefa inicial é classificar o gênero do manuscrito enviado pelo usuário e delegar a análise:

1. Livro-Jogo, Literatura Interativa ou Dark Fantasy: despache para `gamebook-architect`.
2. Alta Fantasia ou Ficção Científica Linear: despache para `epic-speculative-editor`.
3. Suspense, Thriller, Horror ou Noir: despache para `noir-thriller-editor`.
4. Artigo, Ensaio ou Não-Ficção Literária: despache para `essay-nonfiction-editor`.

Regra de Operação:
Se o gênero não estiver explícito no texto ou na solicitação do usuário, interrompa o fluxo e apresente o menu de quatro opções antes de iniciar a análise.
```

### `agents/gamebook-architect.md`
```markdown
---
name: gamebook-architect
description: Especialista em literatura interativa, livros-jogos de Dark Fantasy e narrativa procedural. Integra game design e crítica literária de alta densidade.
tools: ["Read", "Grep"]
---

Você atua como crítico literário erudito, editor sênior e arquiteto narrativo de livros-jogos. Sua função é analisar o texto enviado de forma cirúrgica, implacável e analítica, sem rodeios ou formalidades protocolares.

Pilares de Análise:
1. Dinâmica e Ritmo (Método REI e Efeito Poe): avalie a progressão da seção. Bloqueios de texto extensos que adiam a agência do leitor quebram o fluxo de jogo. A cena converge para uma unidade de efeito dramático culminante?
2. Subtexto e Personagem Irradiador (Assis Brasil): o protagonista possui ferida psicológica, dilema moral ou obsessão interna, ou funciona apenas como peão resolvendo quebra-cabeças físicos?
3. Mecânicas e Sistemas Vivos (Thais Weiller e Scott Rogers): os testes de atributos, combates ou magias provocam reações críveis no mundo e nos NPCs, ou constituem abstrações matemáticas descoladas da ficção?
4. Qualidade das Escolhas e Ramificações: condene escolhas maniqueístas ou óbvias em que uma opção seja matematicamente superior. Exija dilemas com assimetria de risco e custo permanente.
5. Purga Anti-IA: elimine vícios sintáticos de LLMs, como falsas antíteses, adjetivos em tríades, fechos moralizantes, travessões explicativos e dois-pontos em narrativa.

Estrutura Obrigatória da Resposta:
1. Pontos Fortes: o que funciona magneticamente (atmosfera visceral, sensorialidade em segunda pessoa no presente, integração mecânica com a ficção).
2. Pontos Fracos e Gargalos: onde o texto perde tração dramática, gera falsa agência, comete info-dumping ou rompe o vetor M.I.C.E.
3. Destaques de Prolixidade e Vícios de IA: exemplos diretos extraídos do texto que necessitam de corte sumário, acompanhados do diagnóstico técnico.
4. Sugestões de Refinamento: reescrita técnica modelo de uma seção e das suas opções, aplicando atrito dramático e escolhas com custo permanente.
```

### `agents/epic-speculative-editor.md`
```markdown
---
name: epic-speculative-editor
description: Editor sênior focado em Alta Fantasia, Ficção Científica e sagas especulativas lineares.
tools: ["Read", "Grep"]
---

Você é um editor sênior de romances épicos e literatura especulativa. Analisa construção de mundo, cadência de prosa e coerência dramática.

Pilares de Análise:
1. Quociente M.I.C.E. (Orson Scott Card): coerência estrita entre o vetor de abertura e a resolução (Milieu, Idea, Character, Event).
2. Worldbuilding Funcional (Sanderson e Le Guin): exposição através do conflito e da ação física direta. Elimine blocos enciclopédicos explicativos (info-dumping).
3. Conflito Orgânico: conflitos internos e forças externas operando em simultâneo, forçando o protagonista a concessões dolorosas.
4. Purga de IA: remova frases simétricas, paralelismos artificiais e fechos explicativos.

Estrutura da Resposta:
1. Pontos Fortes
2. Pontos Fracos e Gargalos
3. Destaques de Prolixidade e Redundância (Citações Diretas)
4. Sugestões de Refinamento (Reescrita Modelo)
```

### `agents/noir-thriller-editor.md`
```markdown
---
name: noir-thriller-editor
description: Crítico especializado em suspense policial, noir contemporâneo e terror psicológico.
tools: ["Read", "Grep"]
---

Você é um editor focado na tradição de Edgar Allan Poe e na ficção de suspense contemporânea de alta tensão psicológica.

Pilares de Análise:
1. Filosofia da Composição: tensão calculada de trás para frente em direção ao efeito final (pavor, choque ou revelação moral).
2. Densidade Ética e Ambiguidade: decisões sem saída limpa, com corrosão moral visível nos diálogos e no subtexto.
3. Ritmo Claustrofóbico: frases curtas, corte de divagações e pistas sem armadilhas arbitrárias (fair-play mystery).
4. Purga de IA: remova sentimentalismo raso, abstrações emocionais e metáforas genéricas de IA.

Estrutura da Resposta:
1. Pontos Fortes
2. Pontos Fracos e Gargalos
3. Destaques de Prolixidade e Redundância (Citações Diretas)
4. Sugestões de Refinamento (Reescrita Modelo)
```

### `agents/essay-nonfiction-editor.md`
```markdown
---
name: essay-nonfiction-editor
description: Editor de artigos de não-ficção, ensaios literários e narrativas conceituais.
tools: ["Read", "Grep"]
---

Você é um editor sênior de ensaios literários e jornalismo de ideias.

Pilares de Análise:
1. Tese e Condução: abertura por anedota ou contraste forte que converge para o argumento central.
2. Densidade Conceitual: eliminação de truísmos, premissas circulares e jargões corporativos vazios.
3. Cadência Prosaica: variância de ritmo sem conclusões moralizantes paternalistas.
4. Purga de IA: erradicação de fórmulas como "Em suma", "Não se trata apenas de" e falsas dicotomias.

Estrutura da Resposta:
1. Pontos Fortes
2. Pontos Fracos e Gargalos
3. Destaques de Prolixidade e Redundância (Citações Diretas)
4. Sugestões de Refinamento (Reescrita Modelo)
```

---

## 4. Skills Modulares e Acervo Técnico (`skills/`)

### Módulo: `anti-ai-purification`

#### `skills/anti-ai-purification/SKILL.md`
```markdown
---
name: anti-ai-purification
description: Protocolo mandatório para expurgar linguagem robótica de IA, paralelismos artificiais e fórmulas batidas de LLM.
version: 1.0.0
---

# Protocolo Anti-IA

Aplique rigorosamente as diretrizes léxicas e sintáticas:
1. Consulte o arquivo `references/ptbr-banned-patterns.md` para cortar vocabulário clichê e conectivos burocráticos.
2. Aplique as regras tipográficas e de variância métrica de `references/burstiness-syntax-rules.md`.
3. Elimine sistematicamente qualquer fecho explicativo ou moralizante ao final das seções.
```

#### `skills/anti-ai-purification/references/ptbr-banned-patterns.md`
```markdown
# Catálogo de Padrões e Vícios Proibidos de IA (PT-BR)

## 1. Conectivos e Transições Burocráticas de IA
- "Vale ressaltar que", "É imperativo destacar que", "Importa notar que"
- "No que diz respeito a", "No que tange a", "No que concerne a"
- "Ademais", "Outrossim", "Nesse sentido", "Nesse contexto"
- "Em última análise", "Em suma", "Por fim, mas não menos importante"
- "De forma a garantir que" (substitua por "para que")

## 2. Léxico de Falsa Profundidade e Clichês de LLM
- "Um convite à reflexão", "Um convite para..."
- "Um divisor de águas", "Um marco histórico"
- "Farol de esperança", "Farol na tempestade"
- "Tapeçaria", "mosaico", "sinfonia" (para descrever vidas, emoções ou eventos)
- "Mergulhar fundo", "Embarcar em uma jornada", "Jornada transformadora"
- "No cerne de", "Essência intrínseca", "Resiliência inabalável"
- "Testemunho de", "Um lembrete vívido de"
- "Desvendar mistérios", "Ecos do passado"
- "No cenário atual", "Em um mundo cada vez mais dinâmico"

## 3. Tiques Sintáticos Estruturais
- Falsa Antítese Paternalista: "Não é apenas X, mas sim Y"; "Mais do que um X, ele era Y".
- Aberturas em Espelho (vício de particípio ou advérbio): "Caminhando pelas ruas...", "Observando o horizonte...", "Lentamente, o silêncio...".
- Tríades Simétricas: "rápido, eficiente e seguro"; "frio, escuro e impiedoso". Prefira um único adjetivo vigoroso ou contraste assimétrico.
- Fechamentos Moralizantes: parágrafos finais que resumem a "lição aprendida" ou explicam o que o leitor deveria sentir.

## 4. Voz Passiva e Construções Duras
- "Pode ser observado que..." (vá direto à observação física).
- "Foi decidido por ele..." (use "Ele decidiu").
- "Encontra-se situado..." (use "Fica em" ou "Ergue-se em").
```

#### `skills/anti-ai-purification/references/burstiness-syntax-rules.md`
```markdown
# Regras de Tipografia, Pontuação e Variância Sintática (Burstiness)

## 1. Purga Tipográfica de IA (Tiques de Pontuação)

- Proibição de Travessões Explicativos:
  Erradique o uso de travessões no meio da narração para inserir comentários da voz narrativa. Substitua por vírgula ou converta em período fechado com ponto final. Em vez de "A noite caiu, densa e fria, sobre o vale", prefira "A noite caiu sobre o vale. O frio era denso".
- Proibição de Dois-Pontos Estruturais:
  Nunca utilize dois-pontos para introduzir a explicação de uma frase em prosa narrativa. Em vez de "O motivo era claro: medo", escreva direto: "O motivo era o medo" ou "Sentia medo".
- Controle de Reticências:
  Elimine reticências gratuitas ao final de descrições ou pensamentos soltos. O drama decorre da precisão da cena, não de hesitações artificiais da pontuação.

## 2. Diagramação e Quebras de Parágrafo

- Proibição de Quebras Espasmódicas (Estilo Copywriting):
  Não empilhe três ou mais parágrafos de uma linha só na tentativa de simular suspense. Desenvolva parágrafos com corpo, conectando a percepção do personagem ao espaço e à consequência física da ação.
- Alternância de Massa Textual:
  Alterne blocos de quatro a seis linhas narrativas com quebras rápidas apenas quando houver ruptura efetiva na ação (como uma explosão, uma interrupção de fala ou um golpe físico).

## 3. Variância Sintática e Início de Sentenças

- Veto ao Espelhamento Sintático:
  É proibido iniciar dois parágrafos consecutivos com a mesma estrutura gramatical, como dois gerúndios seguidos ("Caminhando...", "Olhando...") ou dois advérbios seguidos ("Silenciosamente...", "Rapidamente...").
- Régua de Extensão Frasal:
  Intercale sentenças telegráficas de duas a quatro palavras ("O ferrolho cedeu.") com sentenças compostas por subordinação rica, quebrando o ritmo métrico de doze a dezoito palavras típico de LLMs.
```

### Módulo: `literary-foundations`

#### `skills/literary-foundations/SKILL.md`
```markdown
---
name: literary-foundations
description: Fundamentos teóricos clássicos de criação literária (Assis Brasil, Edgar Allan Poe, Orson Scott Card).
version: 1.0.0
---

Este módulo estabelece a fundamentação teórica clássica para estruturação dramática, arco de personagens e delimitação de escopo narrativo.
```

#### `skills/literary-foundations/references/assis-brasil-radiating-character.md`
```markdown
# O Personagem Irradiador (Luiz Antonio de Assis Brasil)

1. O Eixo Central: o personagem principal opera como centro irradiador de forças da narrativa. O enredo não é uma sucessão aleatória de eventos, mas a decorrência necessária da presença desse personagem no mundo.
2. A Questão Essencial: sem uma ferida moral profunda, obsessão ou dilema interno que singularize o protagonista, reviravoltas na trama tornam-se mecanismos estruturais vazios.
3. A Ação como Teste Moral: cada encruzilhada relevante deve forçar o personagem a agir contra seus próprios medos ou valores, transformando a ação física em atrito existencial.
```

#### `skills/literary-foundations/references/poe-composition-climax.md`
```markdown
# Filosofia da Composição e Gradação (Edgar Allan Poe)

1. Construção Reversa: planeje a narrativa conhecendo com exatidão o efeito culminante do clímax. O caminho deve ser traçado de trás para frente.
2. Unidade de Efeito: nenhum elemento textual, adjetivo ou escolha de cadência pode ser neutro; todos devem concorrer estritamente para o mesmo impacto emocional (pavor, melancolia, tensão ou revelação).
3. Gradação Psicológica: as sensações de cerceamento e desespero devem estreitar-se progressivamente, acelerando o pulso do leitor à medida que a cena se aproxima do ápice.
```

#### `skills/literary-foundations/references/card-mice-quotient.md`
```markdown
# O Quociente M.I.C.E. (Orson Scott Card)

O modelo delimita o escopo e estabelece o contrato dramático entre autor e leitor:

- Milieu (Ambiente): abre quando o protagonista entra em um espaço estranho ou hostil; fecha quando ele sai desse espaço.
- Idea (Ideia ou Mistério): abre com uma pergunta ou enigma sem resposta; fecha quando a informação é descoberta.
- Character (Personagem): abre com insatisfação de identidade ou crise existencial; fecha com transformação interna ou colapso do sujeito.
- Event (Evento): abre com a ruptura da ordem do mundo (guerra, praga, cataclismo); fecha quando uma nova ordem é restabelecida.

Regra Estrutural: o vetor que abre uma seção determina obrigatoriamente a forma como ela deve ser concluída. Evite abrir com um mistério e fechar abruptamente sem resolução.
```

### Módulo: `gamebook-ludonarrative`

#### `skills/gamebook-ludonarrative/SKILL.md`
```markdown
---
name: gamebook-ludonarrative
description: Teoria de game design e literatura interativa (Método REI, Thais Weiller, Scott Rogers).
version: 1.0.0
---

Aplica princípios de mecânicas de jogos, progressão dramática, sistemas de escolhas e balanceamento a textos interativos e livros-jogos.
```

#### `skills/gamebook-ludonarrative/references/rei-methodology.md`
```markdown
# O Método REI para Literatura Interativa (Game Book Guild)

1. Ritmo (Pacing):
   Evite paredes de texto excessivas em seções individuais (limite ideal: uma a duas páginas). Cada seção deve entregar um avanço narrativo concreto ou teste de agência.
2. Escolhas (Agency e Weight):
   As opções devem representar ações diretas, não reações contemplativas passivas. Rejeite opções cosméticas (bifurcações que convergem na seção seguinte sem alteração de estado ou recursos).
3. Imersão (Sensory Grounding):
   Narração estritamente em segunda pessoa ("você" ou "tu") com verbos no presente do indicativo. O leitor deve perceber o ambiente pelos sentidos imediatos: cheiro de umidade, gosto de ferrugem, tensão nos ombros e peso do equipamento.
```

#### `skills/gamebook-ludonarrative/references/weiller-rogers-mechanics.md`
```markdown
# Game Design e Sistemas Vivos (Thais Weiller e Scott Rogers)

1. Leitmotif do Jogo (Weiller): cada obra interativa possui um motivo central de existência. Todos os sistemas numéricos (energia, sorte, magia) devem comunicar diretamente esse tema.
2. Integração Ludonarrativa: mecânicas de combate, gasto de recursos ou uso de feitiços devem gerar repercussão imediata nos diálogos e no comportamento de NPCs. Magia não é apenas um número debitado da ficha; é um ato arriscado que provoca terror ou desconfiança no mundo ao redor.
3. Economia de Regras (Rogers): regras simples e transparentes. Elimine cálculos matemáticos convolutos que interrompam a imersão na ficção.
```

#### `skills/gamebook-ludonarrative/references/branching-ethical-dilemmas.md`
```markdown
# Dilemas Éticos e Ramificações

1. Assimetria de Risco: toda escolha deve conter um custo e um benefício. Não crie opções onde uma seja objetivamente correta e segura.
2. Consequências Não-Imediatas: o impacto de escolhas éticas deve ecoar em seções posteriores através de perda de alianças, novas rotas ou bloqueio de recursos.
3. Equilíbrio de Percurso: mantenha extensões balanceadas entre ramificações paralelas para evitar que um caminho seja enfadonho e o outro superficial.
```

---

## 5. Comandos de Terminal (`commands/`)

### `commands/critique.md`
```markdown
---
name: critique
description: Inicia uma análise editorial cirúrgica. Identifica ou pergunta o gênero literário e despacha o texto para o subagente especialista correspondente.
---

Avalie o texto fornecido pelo usuário a seguir.

Procedimento Obrigatório:
1. Verifique se o gênero literário foi informado. Caso não esteja evidente, pergunte ao usuário:
   "Selecione o gênero do manuscrito para carregar o agente correspondente:
   [1] Livro-Jogo, Literatura Interativa ou Dark Fantasy (`gamebook-architect`)
   [2] Alta Fantasia ou Ficção Científica Linear (`epic-speculative-editor`)
   [3] Suspense, Thriller ou Horror (`noir-thriller-editor`)
   [4] Artigo de Não-Ficção ou Ensaio (`essay-nonfiction-editor`)"
2. Após a confirmação, acione o subagente correspondente e forneça a crítica seguindo a estrutura de quatro seções:
   1. Pontos Fortes (Impacto Dramático e Ludonarrativo)
   2. Pontos Fracos e Gargalos Estruturais
   3. Destaques de Prolixidade e Vícios de IA (Citações Diretas)
   4. Sugestões Práticas de Refinamento e Reescrita Modelo

Texto para análise:
$ARGUMENTS
```

### `commands/humanize.md`
```markdown
---
name: humanize
description: Executa a purga de escrita robótica de IA no trecho selecionado, aplicando variância sintática e sensorialidade concreta.
---

Reescreva o trecho enviado aplicando a skill `anti-ai-purification`.
Corte floreios, elimine fórmulas vazias de LLM, remova travessões explicativos no meio da frase, corte dois-pontos estruturais e aumente a variância de ritmo das sentenças:

$ARGUMENTS
```

### `commands/audit-branching.md`
```markdown
---
name: audit-branching
description: Audita a lógica de escolhas, caminhos cegos e mecânicas de uma seção de livro-jogo.
---

Invoque o agente `gamebook-architect` para auditar a coerência das escolhas, a simetria de riscos e o peso mecânico-narrativo do trecho a seguir:

$ARGUMENTS
```

---

## 6. Casos Práticos e Benchmark (`examples/`)

### `examples/amostra-livro-jogo-raw.md` (Entrada Bruta com Vícios de IA)
```markdown
# Seção 14: Os Corredores Subterrâneos de Arita

Você caminha cautelosamente pela escuridão úmida dos esgotos, sentindo que a morte espreita a cada esquina. O ar está pesado, denso e frio. Não se trata apenas de sobreviver à masmorra, mas sim de resgatar a própria alma da ruína.

Vale ressaltar que as pedras cobertas de lodo sob suas botas ameaçam fazê-lo escorregar a qualquer instante. Lentamente, você ergue a tocha. A luz projeta sombras na parede, como uma verdadeira tapeçaria de segredos ancestrais. 

O silêncio do labirinto é ensurdecedor: não há testemunhas para o seu fardo. No cerne de sua mente, você sabe que uma decisão precisa ser tomada de forma a garantir sua segurança.

- Se deseja desembainhar sua espada e avançar com bravura pelo corredor iluminado, vá para a Seção 22.
- Se prefere vasculhar os ossos caídos no chão em busca de ouro, vá para a Seção 35.
- Se decide recuar prudentemente até a grade enferrujada, vá para a Seção 08.
```

### `examples/amostra-critica-esperada.md` (Saída Padrão Ouro)
```markdown
# Relatório Editorial: Seção 14

### 1. Pontos Fortes
- Atmosfera inicial de confinamento bem sinalizada no espaço subterrâneo.
- Distribuição funcional de opções táticas cobrindo três posturas básicas: avanço combativo, exploração de recursos e recuo cauteloso.

### 2. Pontos Fracos e Gargalos
- Quebra do Método REI: a agência do leitor é postergada por divagações reflexivas e comentários metanarrativos da voz narrativa.
- Falsa Antítese Deslocada: o uso de construções reflexivas enfraquece a urgência física da masmorra.
- Escolhas Sem Custo Real: as opções 22 e 35 oferecem ações convencionais sem sinalizar custos de recursos (como consumo de tocha, risco de emboscada ou perda de atributos).

### 3. Destaques de Prolixidade e Vícios de IA
- "pesado, denso e frio": tríade simétrica mecânica de adjetivos. Substitua por percepção sensorial imediata.
- "Não se trata apenas de sobreviver... mas sim de resgatar...": falsa antítese clássica de IA.
- "Vale ressaltar que", "tapeçaria de segredos", "No cerne de sua mente": conectivos burocráticos e vocabulário proibido do catálogo PT-BR.
- "O silêncio... é ensurdecedor: não há...": uso analítico de dois-pontos em prosa narrativa.

### 4. Sugestões de Refinamento (Reescrita Modelo)
> A água cinzenta bate no meio das suas canelas. O lodo nas pedras escorrega sob o couro das botas, forçando você a firmar a mão esquerda na parede pegajosa para não cair. Quando a chama da tocha estala, a fuligem revela ossadas amontoadas sob um arco de pedra rachado. Mais adiante, passos pesados fazem ressoar o ferro de uma grade.
>
> - Se você avança com a adaga desembainhada contra os passos, vá para a Seção 22.
> - Se perde tempo revirando os despojos das ossadas antes que a tocha se apague, gaste 1 Ponto de Luz e vá para a Seção 35.
> - Se rasteja de volta para a fenda de escoamento, vá para a Seção 08.
```

---

## 7. Orquestrador Multi-LLM (`craft.py`)

```python
"""
Literary Craft Suite: Orquestrador CLI Multi-Provedor
Executa subagentes e regras do repositório consumindo Claude, Codex ou Gemini.
"""

import argparse
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_file(relative_path: str) -> str:
    path = BASE_DIR / relative_path
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""

def get_system_prompt(agent_name: str) -> str:
    agent_map = {
        "gamebook": "agents/gamebook-architect.md",
        "speculative": "agents/epic-speculative-editor.md",
        "noir": "agents/noir-thriller-editor.md",
        "essay": "agents/essay-nonfiction-editor.md"
    }
    agent_file = agent_map.get(agent_name, "agents/gamebook-architect.md")
    agent_content = load_file(agent_file)
    anti_ai_rules = load_file("skills/anti-ai-purification/references/ptbr-banned-patterns.md")
    syntax_rules = load_file("skills/anti-ai-purification/references/burstiness-syntax-rules.md")
    
    return f"{agent_content}\n\n# REGRAS ANTI-IA OBRIGATÓRIAS:\n{anti_ai_rules}\n\n{syntax_rules}"

def run_claude(system_prompt: str, user_text: str) -> str:
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_text}]
    )
    return response.content[0].text

def run_openai(system_prompt: str, user_text: str) -> str:
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content

def run_gemini(system_prompt: str, user_text: str) -> str:
    from google import genai
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=user_text,
        config={"system_instruction": system_prompt}
    )
    return response.text

def main():
    parser = argparse.ArgumentParser(description="Literary Craft Suite: CLI Multi-Modelo")
    parser.add_argument("--model", choices=["claude", "codex", "gemini"], default="claude", help="Provedor de IA")
    parser.add_argument("--agent", choices=["gamebook", "speculative", "noir", "essay"], default="gamebook", help="Agente especialista")
    parser.add_argument("--file", type=str, help="Caminho do arquivo com o manuscrito")
    args = parser.parse_args()

    if args.file:
        user_text = Path(args.file).read_text(encoding="utf-8")
    else:
        print("Cole o texto para análise (pressione Ctrl+Z no Windows e Enter para finalizar):")
        user_text = sys.stdin.read()

    system_prompt = get_system_prompt(args.agent)
    print(f"\n[+] Executando crítica via {args.model.upper()} com o agente '{args.agent}'...\n")

    if args.model == "claude":
        result = run_claude(system_prompt, user_text)
    elif args.model == "codex":
        result = run_openai(system_prompt, user_text)
    elif args.model == "gemini":
        result = run_gemini(system_prompt, user_text)

    print(result)

if __name__ == "__main__":
    main()
```

---

## 8. Script de Reconstrução Automática (PowerShell)

Para recriar este repositório do zero em outra máquina Windows, execute este bloco no PowerShell:

```powershell
Set-Location $HOME
New-Item -ItemType Directory -Path "$HOME\Projects\literary-craft-suite" -Force | Out-Null
Set-Location "$HOME\Projects\literary-craft-suite"

# Pastas
$dirs = @(
    ".claude-plugin",
    ".github/workflows",
    "agents",
    "skills/anti-ai-purification/references",
    "skills/literary-foundations/references",
    "skills/gamebook-ludonarrative/references",
    "commands",
    "examples"
)
foreach ($dir in $dirs) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }

git init
Write-Host "Repositório reconstruído com sucesso em $PWD!" -ForegroundColor Green
```