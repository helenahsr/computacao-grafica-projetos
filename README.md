# Projetos Computação Gráfica
Repositório para todos os scripts feitos para a matéria de Computação Gráfica

## Requisitos:
- Python 3.12.6 ou superior

## Como utilizar:

### 1. Clonar o repositório:


**No terminal, execute:**
```
git clone https://github.com/helenahsr/computacao-grafica-projetos.git
```

**Entre na pasta clonada:**
```
cd computacao-grafica-projetos
```

### 2. Configure o ambiente:

**No terminal, execute:**
```
python -m venv .venv
```

**Ative o ambiente executando:**
- VSCode:
```
.venv\Scripts\activate
```

- PowerShell:
```
.venv\Scripts\activate.ps1
```

- CMD:
```
.venv\Scripts\activate.bat
```
_Ao ativar, no início da linha de comando aparecerá `(.venv) PS`._

**Teste o funcionamento do ambiente com:**
```
pip list
```
A saída esperada é uma lista de dependências instaladas, mas caso ainda não tenha nenhuma, apenas `pip [num-versão]` vai aparecer.

### 3. Instale as dependências de `requirements.txt`;
```
pip install -r requirements.txt
```

Caso não funcione:
```
pip install PyOpenGL PyOpenGL_accelerate glfw numpy
```

### 4. Rodar os scripts:

**Acesse um dos projetos com (exemplo):**
```
cd Projeto1
```

**Rode o projeto com:**
```
python main.py
```