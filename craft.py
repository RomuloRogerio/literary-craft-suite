import argparse
import sys
from pathlib import Path

# Lê os arquivos de regras do repositório
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
    
    return f"{agent_content}\n\n# REGRAS ANTI-IA MANDATÓRIAS:\n{anti_ai_rules}\n\n{syntax_rules}"

def run_claude(system_prompt: str, user_text: str):
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_text}]
    )
    return response.content[0].text

def run_openai(system_prompt: str, user_text: str):
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

def run_gemini(system_prompt: str, user_text: str):
    from google import genai
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=user_text,
        config={"system_instruction": system_prompt}
    )
    return response.text

def main():
    parser = argparse.ArgumentParser(description="Literary Craft Suite - CLI Multi-Modelo")
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
