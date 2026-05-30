import re
import os

# Liste des fichiers à traiter ordonnés selon la capture d'écran
FILES_TO_PROCESS = [
    "260109 CH10.tex",
    "260128 CH11.tex",
    "260206 CH12.tex",
    "260220 CH13.tex",
    "260304 CH14.tex",
    "260410 CH14-B.tex",
    "260422 CH14-C.tex"
]

OUTPUT_FILE = "extraits_theoremes_preuves.tex"

# Expression régulière non-gourmande pour capturer les blocs entiers
ENV_PATTERN = re.compile(r'\\begin\{(theorem|property|proof)\}.*?\\end\{\1\}', re.DOTALL)

LATEX_PREAMBLE = """\\documentclass[11pt,a4paper]{article}
\\usepackage{fontspec}
\\usepackage{amsmath,amssymb,amsthm}

\\newtheorem{theorem}{Théorème}[section]
\\newtheorem{property}{Propriété}[section]

\\title{Recueil des Théorèmes, Propriétés et Démonstrations}
\\date{\\today}

\\begin{document}
\\maketitle
"""

LATEX_POSTAMBLE = """
\\end{document}
"""

def extract_environments(file_path):
    if not os.path.exists(file_path):
        print(f"[Avertissement] Fichier introuvable : {file_path}")
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    extracted_blocks = []
    for match in ENV_PATTERN.finditer(content):
        extracted_blocks.append(match.group(0))
        
    return extracted_blocks

def main():
    combined_content = []
    
    for filename in FILES_TO_PROCESS:
        print(f"Analyse de {filename}...")
        blocks = extract_environments(filename)
        
        if blocks:
            section_title = filename.replace(".tex", "").replace("_", " ")
            combined_content.append(f"\\section*{{Extraits : {section_title}}}\n")
            combined_content.extend(blocks)
            combined_content.append("\n\\vspace{1em}\n")
            print(f"-> {len(blocks)} environnements extraits.")
            
    if not combined_content:
        print("[Erreur] Aucun environnement trouvé dans les fichiers spécifiés.")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(LATEX_PREAMBLE)
        f.write("\n\n".join(combined_content))
        f.write(LATEX_POSTAMBLE)
        
    print(f"\n[Succès] Fichier généré : {OUTPUT_FILE}")

if __name__ == "__main__":
    main()