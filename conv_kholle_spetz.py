import re

def parse_markdown_to_latex(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Nettoyage des conflits de dollars pour les environnements autonomes (align*, equation*)
    content = re.sub(
        r'\$\$\s*(\\begin\{(align\*?|equation\*?)\}.*?\\end\{\2\})\s*\$\$', 
        r'\1', 
        content, 
        flags=re.DOTALL
    )
    
    # Conversion des $$ restants (incluant \begin{cases}) en display math LaTeX \[ \]
    content = re.sub(r'\$\$(.*?)\$\$', r'\\[ \1 \\]', content, flags=re.DOTALL)

    # Conversion du gras Markdown vers LaTeX
    content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', content)

    # Suppression des séparateurs Markdown (---)
    content = re.sub(r'^---\s*$', '', content, flags=re.MULTILINE)

    latex_doc = [
        r"\documentclass[12pt,a4paper]{article}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[french]{babel}",
        r"\usepackage{amsmath, amssymb, amsfonts}",
        r"\usepackage{geometry}",
        r"\usepackage{xcolor}",
        r"\usepackage{tcolorbox}",
        r"\geometry{margin=2.5cm}",
        r"\begin{document}",
        r"\tableofcontents",
        r"\newpage"
    ]

    # Séparation du document par chapitres
    chapitres = re.split(r'^##\s+(Chapitre.*)$', content, flags=re.MULTILINE)
    
    # Extraction du titre principal
    titre_match = re.search(r'^#\s+(.*)$', chapitres[0], flags=re.MULTILINE)
    if titre_match:
        latex_doc.insert(8, f"\\title{{{titre_match.group(1).strip()}}}")
        latex_doc.insert(9, r"\maketitle")

    for i in range(1, len(chapitres), 2):
        titre_chapitre = chapitres[i].strip()
        contenu_chapitre = chapitres[i+1]

        latex_doc.append(f"\\section{{{titre_chapitre}}}")

        # Séparation par blocs d'instructions
        blocs = re.split(r'^>\[!(?:INFO|NOTE)\]\s*Instructions\s*', contenu_chapitre, flags=re.MULTILINE)

        if blocs[0].strip():
            latex_doc.append(blocs[0].strip())

        for bloc in blocs[1:]:
            lignes = bloc.split('\n')
            instructions = []
            preuve = []
            dans_instruction = True

            for ligne in lignes:
                if dans_instruction:
                    if ligne.startswith('>'):
                        # Nettoyage des balises de citation Markdown
                        instructions.append(ligne.lstrip('> \t'))
                    elif ligne.strip() == '':
                        pass
                    else:
                        dans_instruction = False
                        preuve.append(ligne)
                else:
                    preuve.append(ligne)

            texte_instruction = '\n'.join(instructions).strip()
            texte_preuve = '\n'.join(preuve).strip()

            # Formatage LaTeX pour l'instruction
            latex_doc.append(r"\begin{tcolorbox}[colback=gray!5, colframe=black!75, title=Instruction, fonttitle=\bfseries]")
            latex_doc.append(texte_instruction)
            latex_doc.append(r"\end{tcolorbox}")
            latex_doc.append("")
            
            # Gestion rudimentaire des listes non ordonnées pour la section preuve
            texte_preuve = re.sub(r'(?m)^[-*]\s+(.*)$', r'\\item \1', texte_preuve)
            texte_preuve = re.sub(r'(?:\\item.*\n?)+', r'\\begin{itemize}\n\g<0>\\end{itemize}\n', texte_preuve)
            
            latex_doc.append(texte_preuve)
            latex_doc.append(r"\newpage")

    latex_doc.append(r"\end{document}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(latex_doc))

if __name__ == "__main__":
    parse_markdown_to_latex("kholle_speciale.md", "kholle_speciale.tex")