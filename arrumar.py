from pathlib import Path

# 1. Cria as pastas necessárias
Path(".github/assets").mkdir(parents=True, exist_ok=True)
Path(".github/ISSUE_TEMPLATE").mkdir(parents=True, exist_ok=True)

# 2. Cria o banner visual SVG
svg_text = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="100%" height="auto">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#31104b" />
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#a855f7" />
      <stop offset="50%" stop-color="#ec4899" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
  </defs>
  <rect width="1200" height="340" rx="16" fill="url(#bg)" />
  <text x="600" y="115" font-family="sans-serif" font-size="20" font-weight="700" letter-spacing="4" fill="#a855f7" text-anchor="middle">SUÍTE EDITORIAL MULTI-MODELO</text>
  <text x="600" y="185" font-family="sans-serif" font-size="52" font-weight="900" letter-spacing="-1" fill="#ffffff" text-anchor="middle">LITERARY CRAFT SUITE</text>
  <rect x="520" y="210" width="160" height="4" rx="2" fill="url(#accent)" />
  <text x="600" y="255" font-family="sans-serif" font-size="18" fill="#cbd5e1" text-anchor="middle">Crítica Literária Erudita • Ludonarrativa de Livros-Jogos • Purga Cirúrgica Anti-IA</text>
  <text x="600" y="285" font-family="monospace" font-size="13" font-weight="600" fill="#94a3b8" text-anchor="middle">CLAUDE CODE • OPENAI CODEX • GOOGLE GEMINI</text>
</svg>"""

Path(".github/assets/hero-banner.svg").write_text(svg_text, encoding="utf-8")

# 3. Atualiza o README principal com o banner e a estrutura visual
readme_text = """<div align="center">

<img src=".github/assets/hero-banner.svg" alt="Literary Craft Suite Banner" width="100%">

<p align="center">
  <b>🇧🇷 Português</b> •
  <a href="README_EN.md">🇺🇸 English Version</a>
</p>

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin%20Ready-6B46C1?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai)
[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-Ready-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Supported-8E75C2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Visão Geral

Modelos de Linguagem (LLMs) tendem a homogeneizar a escrita criativa por meio de padrões sintáticos mecânicos: orações espelhadas, adjetivos em tríades simétricas, falsas antíteses, travessões explicativos dramáticos e conclusões paternalistas vazias.

O **Literary Craft Suite** transforma o **Claude Code**, o **Codex** e o **Gemini** em uma bancada de edição analítica e cirúrgica. Desenvolvido para escritores de alta ficção, ensaístas e designers de livros-jogos, o pacote conecta princípios clássicos da dramaturgia e narrativa procedural à lógica formal do game design.

---

## ⚡ Instalação e Uso

No Claude Code:
```bash
/plugin marketplace add RomuloRogerio/literary-craft-suite