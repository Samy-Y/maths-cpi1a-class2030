# Recueil spécial "Khôlle Spéciale"

## Chapitre XII — Polynômes

>[!INFO] Instructions
> Montrer que si $A$ est un anneau intègre, alors $A^\mathbb N$ est aussi un anneau intègre.

On procède par absurde en supposant qu'il existe $(a_n)_n,(b_n)_n \in A^\mathbb{N}$ tels que $(a_n)_n \times (b_n)_n = 0_{A^\mathbb{N}}$ avec $(a_n)_n \ne 0$ et $(b_n)_n \ne 0$
- On définit d'abord $i_0$ et $j_0$ les indices du premier terme non-nul des suites $(a_n)_n$ et $(b_n)_n$ respectivement.
$$\begin{cases} i_0 = \min(\{n \in \mathbb{N} ~\mid~ a_n \ne 0\}) \\ j_0 = \min(\{n \in \mathbb{N} ~\mid~ b_n \ne 0\})\end{cases}$$
- On peut donc tronquer les suites $(a_n)_n$ et $(b_n)_n$ de la manière suivante :
$$\begin{cases} \forall i < i_0, a_i = 0 \\ \forall j < j_0, b_j = 0\end{cases}$$
- Le produit $a_n \times b_n = c_n$ de Cauchy est défini pour tout $n \in \mathbb{N}$ comme suit :
$$\forall n \in \mathbb{N} : c_n = a_n \times b_n = \sum_{i+j=n} a_ib_j$$
- On fixe donc $n = i_0 + j_0$. La somme devient :
$$c_{i_0 + j_0} = \sum_{i+j=i_0+j_0} a_ib_j$$
	- Si $i < i_0$ alors $a_i = 0$ et le produit s'annule.
	- Si $i > i_0$ alors $j = j_0 + i_0 - i$ est forcément plus petit que $j_0$ et le produit s'annule.
	- Si $i=i_0$ on a $j = j_0$. Le produit est donc réduit à :
$$c_{i_0+j_0} = a_{i_0} b_{j_0} = 0$$
- D'après l'énoncé, $A$ est un anneau intègre, cela implique donc que $a_{i_0} = 0$ ou $b_{i_0} = 0$, ce qui contredit notre hypothèse de départ.
- On en déduit que $A^\mathbb{N}$ n'admet pas de diviseurs de 0. Un théorème en amont énonce déjà que $A^\mathbb{N}$ est un anneau de $A$, donc $A^\mathbb{N}$ est un anneau intègre.

---
>[!INFO] Instructions
> Montrer que les éléments inversibles de $\mathbb{K}[X]$ sont les polynômes de degré 0.
> $$P \in \mathbb{U}_{\mathbb{K}[X]} \iff \deg(P) = 0$$

On divise la démonstration dans le sens direct et indirect.
- Dans le sens direct $\implies$, dire que $P$ est inversible équivaut à dire que $\exists Q \in \mathbb{K}[X] , P\times Q = 1$
- Le degré de ce polynôme $P\times Q$ est $\deg(P\times Q) = \deg(P) + \deg(Q) = 0$.
- Comme $P$ et $Q$ sont non-nuls ($Q$ est non-nul, trivial), alors leurs degrés sont $\ge 0$. Dans ce cas, on déduit clairement que leurs degrés sont nuls. CQFD.
- Dans le sens indirect $\impliedby$, on part du fait que $P$ est un monôme d'un unique élément non-nul $a$ de $\mathbb K$.
- Comme cet élément $a$ est non-nul et que $\mathbb K$ est un corps, alors cet élément est inversible.
- En posant $Q = a^{-1}$, on a $P \times Q =1$. Donc $P$ est inversible dans $\mathbb K[X]$.

---
>[!INFO] Instructions 
> **Division Euclidienne :** Montrer que pour tout polynômes $A,B \in \mathbb K[X]$ avec $B \ne 0$, il existe un unique couple $(Q,R) \in \mathbb K[X]^2$ tels que $A = B\times Q + R$ et $\deg(R) < \deg(B)$.

- On procède par récurrence forte sur $n = \deg(A)$.
%% to continue %%
---
>[!INFO] Instructions
> **Formule de Taylor polynomiale :** Soit $P \in \mathbb{K}[X]$ tel que $\deg(P) = n$ et $a \in \mathbb{K}$. Montrer que :
> $$P = \sum_{k=0}^n \frac{P^{(k)}(a)}{k!}(X-a)^k$$

### Première approche (Cours)
On démontre le résultat par linéarité en évaluant l'effet de l'opérateur de dérivation sur les monômes de la base canonique $\{X^0, \dots, X^n\}$.
- **Étape 1 : Décomposition des monômes de la base**
    - On pose $Q_i = X^i$ pour tout $i \in [\![0,n]\!]$. Par translation, $Q_i = (X - a + a)^i$.
    - L'application directe de la formule du binôme de Newton donne :
    $$Q_i = \sum_{k=0}^i C_i^k a^{i-k}(X-a)^k$$
- **Étape 2 : Identification des coefficients par dérivation**
    - On calcule la dérivée $k$-ième du polynôme $Q_i$ puis on l'évalue au point $X = a$. Par annulation de tous les termes contenant le facteur $(a-a)$ sauf le terme constant résiduel obtenu pour le rang de dérivation $j=k$, on obtient :
    $$Q_i^{(k)}(a) = k! \cdot C_i^k a^{i-k} \implies C_i^k a^{i-k} = \frac{Q_i^{(k)}(a)}{k!}$$
    - On réinjecte la valeur de ce coefficient dans l'expression d'origine de $Q_i$ :
    $$Q_i = \sum_{k=0}^i \frac{Q_i^{(k)}(a)}{k!}(X-a)^k$$
- **Étape 3 : Combinaison linéaire globale et inversion de sommation**
    - On décompose le polynôme quelconque $P$ sur la base canonique : $P = \sum_{i=0}^n \lambda_i X^i = \sum_{i=0}^n \lambda_i Q_i$.
    - En substituant l'expression de $Q_i$ établie à l'étape précédente, il vient :
$$P = \sum_{i=0}^n \lambda_i \sum_{k=0}^i \frac{Q_i^{(k)}(a)}{k!}(X-a)^k$$
    - Le domaine d'indices est défini par la condition triangulaire $0 \le k \le i \le n$. En inversant l'ordre des symboles de sommation, l'expression devient :
$$P = \sum_{k=0}^n \frac{1}{k!} \left( \sum_{i=k}^n \lambda_i Q_i^{(k)}(a) \right) (X-a)^k$$
- **Étape 4 : Identification finale**
    - Par linéarité de l'opérateur de dérivation successive, le bloc sommatif interne correspond exactement à l'expression de la dérivée $k$-ième de $P$ évaluée au point $a$ :
$$P^{(k)}(a) = \sum_{i=k}^n \lambda_i Q_i^{(k)}(a)$$
    - Par substitution de cette égalité dans la double somme, on valide la formule de Taylor :
$$P = \sum_{k=0}^n \frac{P^{(k)}(a)}{k!}(X-a)^k$$
### Deuxième approche (Bases)
L'approche repose sur l'unicité des coordonnées d'un vecteur dans une base de polynômes à degrés échelonnés.
- **Étape 1 : Justification de l'existence de la base**
    - La famille $\mathcal{B} = \left((X-a)^0, (X-a)^1, \dots, (X-a)^n\right)$ est composée de $n+1$ polynômes à degrés strictement échelonnés de $0$ à $n$.
    - Cette propriété de degré garantit que la famille est libre. Comme son cardinal ($n+1$) est égal à la dimension de l'espace vectoriel $\mathbb{K}_n[X]$, la famille $\mathcal{B}$ en constitue une base.
- **Étape 2 : Écriture de la décomposition**
    - Puisque $P \in \mathbb{K}_n[X]$, il s'exprime de manière unique comme combinaison linéaire des éléments de la base $\mathcal{B}$ :
$$P = \sum_{k=0}^n c_k (X-a)^k \quad \text{avec} \quad (c_0, \dots, c_n) \in \mathbb{K}^{n+1}$$
- **Étape 3 : Application de l'opérateur de dérivation linéaire**
    - On fixe un indice de dérivation $j \in [\![0, n]\!]$ et on applique la dérivation $j$-ième à l'égalité par linéarité.
    - Pour tout terme de la somme où $k < j$, la dérivation d'ordre supérieur au degré annule le terme.
    - Pour tout terme où $k \ge j$, la formule de dérivation successive d'une puissance donne :
$$P^{(j)} = \sum_{k=j}^n c_k \frac{k!}{(k-j)!}(X-a)^{k-j}$$
- **Étape 4 : Évaluation au point de translation ($X = a$)**
    - On évalue le polynôme dérivé en remplaçant la variable $X$ par le scalaire $a$.
    - Pour tout $k > j$, le facteur $(a-a)^{k-j}$ est nul, ce qui élimine la totalité des termes supérieurs de la sommation.
    - Pour le premier terme de la somme ($k = j$), l'expression se réduit à $c_j \frac{j!}{0!}(a-a)^0 = c_j \cdot j!$.
    - La somme s'effondre pour donner la relation directe :
$$P^{(j)}(a) = c_j \cdot j!$$
- **Étape 5 : Identification des coefficients**
    - Le factoriel $j!$ étant un scalaire inversible dans le corps $\mathbb{K}$, on isole le coefficient :
$$c_j = \frac{P^{(j)}(a)}{j!}$$
    - La substitution de cette valeur unique de $c_j$ dans l'expression de l'étape 2 (en basculant l'indice muet sur $k$) achève la démonstration.
---
>[!INFO] Instructions 
> Montrer que $\mathbb K[X]$ est un anneau principal.

> **Note :** On rappelle que tous les idéaux d'un anneau principal sont principaux.

**Considérons un idéal $I$ arbitraire de $\mathbb K[X]$.**
- **Si $I$ est réduit à 0, donc $I = \{0\}$, alors $I$ est engendré par $0$.**
$$I = 0 \cdot \mathbb K[X]$$
- **Si $I$ n'est pas réduit à $0$**, alors il existe un polynôme non-nul $P \in I$ de degré minimal $d$. Traduisons cela plus effectivement.
	- Posons l'ensemble ordonné des degrés des polynômes de $I$, noté $E$ :
$$E = \{\deg(P) \text{ tel que } P \in I\setminus\{0\}\}$$
	- $E$ est bel et bien non vide, parce que $I$ n'est pas réduit à 0.
	- $E \subset N$, donc $E$ admet un minimum $d$.
	- On peut donc dire que :
$$\exists P_0 \in I\setminus\{0\}, \deg(P_0) = d$$
- **Nous allons montrer que $I = P_0 \cdot \mathbb{K}[X] = \langle P_0 \rangle$.**
	- D'après la définition même d'un idéal, on sait que :
$$P_0\cdot \mathbb K[X] \subset I$$
	- Il suffit donc de montrer que $I \subset P_0 \cdot \mathbb K [X]$.
	- Pour cela, on considère un polynôme arbitraire $B \in I$.
	- On effectue la D.E. de ce polynôme par $P_0$. On trouve que :
$$\exists ! (Q,R) \in \mathbb K[X]^2, B = P_0 \times Q + R \quad \text{avec} \quad \deg(R) < \deg(P_0) = d$$
	- En réarrangeant les termes, on trouve que $R = B - P_0 \times Q$, et d'après la définition d'un idéal, cela veut dire que $R \in I$.
		- Si $R \ne 0$, alors son degré serait non-nul est inférieur à celui de $P_0$, or le degré de $P_0$ est défini comme étant le degré minimal de l'idéal $I$. C'est absurde.
		- L'unique possibilité est restante est $R = 0$. Par conséquent, $B = P_0\times Q$
	- On en déduit que tout élément arbitraire $B$ de $I$ appartient à $P_0 \cdot \mathbb K[X]$.
	- D'où $I \subset P_0 \cdot \mathbb K[X]$.
	- Par double-inclusion, $I = \langle P_0 \rangle$.
On en déduit que, dans tous les cas, $I$ est principal.
> [!INFO] Instructions
> 
> **Caractérisation des racines multiples par les dérivées :** Soit $P \in \mathbb{K}[X]$, $\alpha \in \mathbb{K}$ et $s \in \mathbb{N}^*$. Montrer que $\alpha$ est une racine de multiplicité $s$ de $P$ si et seulement si :
> 
> $$\forall k \in [\![0, s-1]\!], P^{(k)}(\alpha) = 0 \quad \text{et} \quad P^{(s)}(\alpha) \neq 0$$

La démonstration s'appuie sur la structure d'unicité de la division euclidienne révélée par la formule de Taylor en $\alpha$.
- **Étape 1 : Isolement du reste et du quotient par Taylor**
    - On écrit le développement de Taylor de $P$ au point $\alpha$ en scindant la sommation au rang $s$ :
$$P = \sum_{k=0}^n \frac{P^{(k)}(\alpha)}{k!}(X-\alpha)^k = (X-\alpha)^s \cdot \sum_{k=s}^n \frac{P^{(k)}(\alpha)}{k!}(X-\alpha)^{k-s} + \sum_{k=0}^{s-1} \frac{P^{(k)}(\alpha)}{k!}(X-\alpha)^k$$
    - Par propriété du degré, le second bloc de droite possède un degré strictement inférieur à $s$. Par unicité de la division euclidienne de $P$ par $(X-\alpha)^s$, on identifie directement le quotient $Q$ et le reste $R$ :
$$Q = \sum_{k=s}^n \frac{P^{(k)}(\alpha)}{k!}(X-\alpha)^{k-s} \quad \text{et} \quad R = \sum_{k=0}^{s-1} \frac{P^{(k)}(\alpha)}{k!}(X-\alpha)^k$$
- **Étape 2 : Traduction de la divisibilité d'ordre $s$**
    - Par définition de la multiplicité, $\alpha$ est racine d'ordre au moins $s$ si et seulement si $(X-\alpha)^s \mid P$, ce qui équivaut à l'annulation du reste $R$.
    - La famille de polynômes $\left((X-\alpha)^k\right)_{0 \le k \le s-1}$ étant libre (degrés échelonnés), le polynôme $R$ est nul si et seulement si tous ses coefficients sont nuls :
$$R = 0 \iff \forall k \in [\![0, s-1]\!], P^{(k)}(\alpha) = 0$$
- **Étape 3 : Verrouillage de la multiplicité exacte par la non-divisibilité**
    - Sous la condition $R=0$, on a $P = (X-\alpha)^s Q$. Pour que la multiplicité soit exactement égale à $s$, il faut et il suffit que $(X-\alpha) \nmid Q$, c'est-à-dire que $\alpha$ ne soit pas racine de $Q$ ($Q(\alpha) \neq 0$).
    - On évalue le polynôme quotient $Q$ en remplaçant $X$ par $\alpha$. Tous les termes s'annulent par la présence du facteur $(\alpha-\alpha)$ à l'exception du premier terme constant correspondant à l'indice $k=s$ :
$$Q(\alpha) = \frac{P^{(s)}(\alpha)}{s!}$$
    - Le factoriel étant non nul, l'indivisibilité se traduit par : $Q(\alpha) \neq 0 \iff P^{(s)}(\alpha) \neq 0$.
- **Étape 4 : Conclusion**
    - La conjonction logique de la nullité du reste (Étape 2) et de la non-nullité de l'évaluation du quotient (Étape 3) valide la double implication.
---
>[!INFO] Instructions
> **Conjugaison des racines multiples dans $\mathbb{R}[X]$ :** Soit $p \in \mathbb{R}[X]$, $z \in \mathbb{C}$ et $s \in \mathbb{N}^*$. Montrer que si $z$ est une racine de multiplicité $s$ de $p$, alors son conjugué $\bar{z}$ est aussi racine de $p$ avec la même multiplicité $s$.

La démonstration exploite la caractérisation de la multiplicité par les polynômes dérivés successifs combinée à la stabilité de $\mathbb{R}[X]$ par la conjugaison complexe.
- **Étape 1 : Lemme de conjugaison des polynômes réels**
    - Soit un polynôme $p = \sum_{m=0}^n a_m X^m \in \mathbb{R}[X]$. Par définition, tous ses coefficients sont réels : $\forall m \in [\![0, n]\!], a_m \in \mathbb{R} \implies \bar{a}_m = a_m$.
    - L'évaluation en tout complexe $z$ vérifie :
$$\overline{p(z)} = \overline{\sum_{m=0}^n a_m z^m} = \sum_{m=0}^n \bar{a}_m \bar{z}^m = \sum_{m=0}^n a_m \bar{z}^m = p(\bar{z})$$
    - Puisque la dérivation successive d'un polynôme à coefficients réels préserve la nature de ses coefficients, cette relation s'étend trivialement à toutes les dérivées de $p$ :
$$\forall k \in \mathbb{N}, \quad p^{(k)}(\bar{z}) = \overline{p^{(k)}(z)}$$
- **Étape 2 : Traduction par la caractérisation de Taylor**
    - Dire que $z$ est une racine de multiplicité $s$ de $p$ équivaut à la double condition sur ses dérivées :
$$\forall k \in [\![0, s-1]\!], \quad p^{(k)}(z) = 0 \quad \text{et} \quad p^{(s)}(z) \neq 0$$
- **Étape 3 : Passage au conjugué et identification**
    - On applique l'opérateur de conjugaison aux relations de l'étape précédente :
        - Pour la condition d'annulation ($k < s$) : $p^{(k)}(z) = 0 \implies \overline{p^{(k)}(z)} = \overline{0} \implies p^{(k)}(\bar{z}) = 0$.
        - Pour la condition d'arrêt ($k = s$) : $p^{(s)}(z) \neq 0 \implies \overline{p^{(s)}(z)} \neq 0 \implies p^{(s)}(\bar{z}) \neq 0$.
- **Étape 4 : Conclusion**
    - Le complexe $\bar{z}$ valide de manière exacte le critère d'ordre et la condition d'arrêt de la caractérisation par les dérivées successives. Sa multiplicité est donc rigoureusement égale à $s$.
---
>[!INFO] Instructions
> **Caractérisation des polynômes irréductibles de $\mathbb{R}[X]$ :** Montrer que les uniques polynômes irréductibles de $\mathbb{R}[X]$ sont les polynômes de degré 1 et les polynômes de degré 2 n'admettant aucune racine réelle ($\Delta < 0$).

La démonstration se segmente par une disjonction des cas selon le degré du polynôme $P \in \mathbb{R}[X]$.
- **Cas 1 : $\deg(P) = 1$**
    - Par définition, un polynôme de degré 1 ne peut pas se factoriser en produit de deux polynômes de degrés strictement inférieurs (les seuls diviseurs possibles sont de degré 0, donc les constantes inversibles). 
    - Tout polynôme de degré 1 est donc structurellement irréductibles dans $\mathbb{R}[X]$.
- **Cas 2 : $\deg(P) = 2$**
    - **Si $\Delta \ge 0$ :** $P$ admet au moins une racine réelle $\alpha$. D'après le théorème d'annulation, $(X-\alpha) \mid P$. On peut donc écrire $P = (X-\alpha)Q$ avec $\deg(Q)=1$. Les deux facteurs étant non constants, $P$ est réductible.
    - **Si $\Delta < 0$ :** Supposons par l'absurde que $P$ soit réductible. Il se factorise alors nécessairement sous la forme $P = P_1 P_2$ avec $\deg(P_1)=\deg(P_2)=1$. Or, tout polynôme de degré 1 dans $\mathbb{R}[X]$ admet une racine réelle. Cela impliquerait que $P$ possède une racine réelle, ce qui contredit l'hypothèse $\Delta < 0$. $P$ est donc irréductible.
- **Cas 3 : $\deg(P) \ge 3$ (Montrons qu'ils sont tous réductibles)**
    - **Sous-cas A (Si $P$ admet une racine réelle $\alpha$) :** On factorise immédiatement par son monôme minimal : $P = (X-\alpha)Q$ avec $\deg(Q) \ge 2$. Aucun des facteurs n'est une constante, donc $P$ est réductible.
    - **Sous-cas B (Si $P$ n'admet aucune racine réelle) :** - On plonge le polynôme dans le corps des complexes : $P \in \mathbb{R}[X] \subset \mathbb{C}[X]$. D'après le théorème fondamental de l'algèbre (d'Alembert-Gauss), $P$ admet au moins une racine complexe $z \in \mathbb{C} \setminus \mathbb{R}$.
        - D'après la propriété de conjugaison des racines, son conjugué $\bar{z}$ est également racine de $P$ avec la même multiplicité. Comme $z \notin \mathbb{R}$, on a $z \neq \bar{z}$.
        - Les deux racines étant distinctes, les monômes associés sont premiers entre eux dans $\mathbb{C}[X]$. Le produit des facteurs divise donc $P$ :
        $$(X-z)(X-\bar{z}) \mid P$$
        - On développe ce produit de facteurs conjugués : $(X-z)(X-\bar{z}) = X^2 - 2\text{Re}(z)X + |z|^2$. 
        - Ce polynôme est de degré 2 et possède des coefficients strictement réels. On a donc trouvé un facteur réel propre de degré 2 qui divise $P$ (car $\deg(P) \ge 3$). Par conséquent, $P$ est réductible.
- **Conclusion :** Les seuls blocs irréductibles sont bien les degrés 1 et les degrés 2 sans racine réelle.
## Chapitre XIV-A — Espaces vectoriels

> [!INFO] Instructions
> 
> **Théorème d'extension d'une famille libre :** Soit $(e_1, \dots, e_{n+1})$ une famille d'éléments de $E$. Montrer que :
> 
> $(e_1, \dots, e_{n+1})$ est libre $\iff$ $(e_1, \dots, e_n)$ est libre et $e_{n+1} \notin \text{Vect}(e_1, \dots, e_n)$

La démonstration repose sur l'équivalence entre la dépendance linéaire et la capacité d'un vecteur à s'exprimer comme combinaison linéaire des autres.
- **Sens direct ($\implies$) :**
    - Par propriété de structure, toute sous-famille d'une famille libre est libre, ce qui valide directement la liberté de $(e_1, \dots, e_n)$.
    - Supposons par l'absurde que $e_{n+1} \in \text{Vect}(e_1, \dots, e_n)$. Il existe alors des scalaires $(\lambda_1, \dots, \lambda_n) \in \mathbb{K}^n$ tels que $e_{n+1} = \sum_{k=1}^n \lambda_k e_k$.
    - Par transposition, on construit la relation : $\sum_{k=1}^n \lambda_k e_k - 1_{\mathbb{K}} \cdot e_{n+1} = 0$. Le coefficient de $e_{n+1}$ étant non nul ($-1 \neq 0$), la famille globale est liée, ce qui contredit l'hypothèse.
- **Sens indirect ($\impliedby$) :**
    - Soit la combinaison linéaire nulle globale : $\sum_{k=1}^{n+1} \lambda_k e_k = 0$.
    - Supposons par l'absurde que $\lambda_{n+1} \neq 0$. Le scalaire étant inversible dans le corps $\mathbb{K}$, on isole le vecteur terminal :
$$e_{n+1} = \sum_{k=1}^n \left(-\lambda_{n+1}^{-1} \lambda_k\right) e_k \implies e_{n+1} \in \text{Vect}(e_1, \dots, e_n)$$
    - Cette inclusion contredit directement l'hypothèse de séparation. On a donc nécessairement $\lambda_{n+1} = 0$.
    - L'égalité initiale s'effondre et se réduit à la somme partielle $\sum_{k=1}^n \lambda_k e_k = 0$.
    - L'hypothèse de liberté de la sous-famille $(e_1, \dots, e_n)$ impose immédiatement l'annulation de tous les coefficients restants : $\forall k \in [\![1, n]\!], \lambda_k = 0$.
    - L'intégralité des coefficients étant nuls, la famille globale est libre.

---
>[!INFO] Instructions
> **Liberté des familles échelonnées :** Soit $(e_1, \dots, e_n)$ une famille libre de $E$. Montrer que toute famille $(v_1, \dots, v_p)$ échelonnée par rapport à $(e_k)$ est libre.

Pour assainir les notations, on structure explicitement la décomposition de chaque vecteur sur la base de référence via l'application strictement croissante de saut d'indice $\varphi : [\![1, p]\!] \to [\![1, n]\!]$ :
$$\forall i \in [\![1, p]\!], \quad v_i = \alpha_i e_{\varphi(i)} + \sum_{j=\varphi(i)+1}^n \beta_{i,j} e_j \quad \text{avec} \quad \alpha_i \neq 0$$
- **Étape 1 : Hypothèse d'absurde et isolation du premier terme**
    - Supposons la famille $(v_1, \dots, v_p)$ liée. Il existe une combinaison linéaire nulle à coefficients non tous nuls : $\sum_{i=1}^p \lambda_i v_i = 0_E$.
    - On introduit l'indice critique $i_0$, représentant le **premier coefficient non nul** de la combinaison :
$$i_0 = \min(\{i \in [\![1, p]\!] ~\mid~ \lambda_i \neq 0\}) \implies \forall i < i_0, \lambda_i = 0$$
    - La sommation s'ampute de ses premiers termes nuls et s'isole sur son pivot :
$$\lambda_{i_0} v_{i_0} + \sum_{i=i_0+1}^p \lambda_i v_i = 0_E$$
- **Étape 2 : Organisation structurelle des indices par blocs**
    - On substitue les vecteurs par leur décomposition en mettant en évidence le comportement de l'indice de tête $\varphi(i_0)$ :
        - **Le vecteur pivot :** $\lambda_{i_0} v_{i_0} = \lambda_{i_0} \alpha_{i_0} e_{\varphi(i_0)} + \lambda_{i_0} \sum_{j=\varphi(i_0)+1}^n \beta_{i_0,j} e_j$
        - **Le bloc des vecteurs suivants ($i > i_0$) :** Par stricte croissance de $\varphi$, on a $\forall i > i_0, \varphi(i) \ge \varphi(i_0)+1$. Tous les vecteurs suivants se situent donc exclusivement dans le sous-espace engendré par les éléments lointains de la base :
$$\sum_{i=i_0+1}^p \lambda_i v_i \in \text{Vect}\left(e_{\varphi(i_0)+1}, \dots, e_n\right)$$
- **Étape 3 : Projection sur le vecteur de tête $e_{\varphi(i_0)}$**
    - En regroupant les termes de la combinaison globale sur la base libre $(e_k)$, le vecteur de tête $e_{\varphi(i_0)}$ n'apparaît **que** dans le développement du terme pivot $v_{i_0}$. L'équation globale se réécrit sous la forme condensée :
$$\left(\lambda_{i_0} \alpha_{i_0}\right) e_{\varphi(i_0)} + \sum_{k=\varphi(i_0)+1}^n \Gamma_k e_k = 0_E$$
    - La famille $(e_1, \dots, e_n)$ étant libre, tous les coefficients de cette combinaison linéaire sont obligatoirement nuls. On extrait l'équation sur le terme de tête :
$$\lambda_{i_0} \alpha_{i_0} = 0$$
- **Étape 4 : Contradiction et conclusion**
    - Par intégrité du corps $\mathbb{K}$, $\lambda_{i_0} \alpha_{i_0} = 0 \implies \lambda_{i_0} = 0$ ou $\alpha_{i_0} = 0$.
    - Or, $\alpha_{i_0} \neq 0$ par définition d'une famille échelonnée (coefficient dominant non nul), et $\lambda_{i_0} \neq 0$ par définition du minimum de l'Étape 1.
    - Cette contradiction réfute l'hypothèse de dépendance linéaire. La famille est libre.

---
>[!INFO] Instructions
> Dans un $\mathbb K$-espace vectoriel $E$, où $(e_1,\dots,e_n)$ en sont des éléments, montrer que :
> Si $v_1,\dots,v_{n+1} \in \mathrm{Vect}(e_1,\dots,e_n)$ alors $(v_1,\dots,v_{n+1})$ est liée.

La démonstration se fait par récurrence sur $n \in \mathbb{N}^*$.
- **Initialisation :** Le cas $n=1$ est trivial (deux vecteurs colinéaires à un même vecteur de base forment une famille liée).
- **Hérédité :** On suppose la propriété vraie pour $n-1$ et on montre qu'elle est vraie pour $n$.
    - Tout vecteur $v_j$ pour $j \in [\![1, n+1]\!]$ se décompose sur la base : $v_j = \sum_{i=1}^n \lambda_{i,j}e_i$.
    - Si tous les scalaires de la dernière ligne coordonnées ($\lambda_{n,k}$) sont nuls, alors $\forall j, v_j \in \mathrm{Vect}(e_1,\dots,e_{n-1})$. D'après l'hypothèse de récurrence ($n+1$ vecteurs dans un espace engendré par $n-1$ éléments), la famille est liée.
    - Sinon, il existe au moins un scalaire $\lambda_{n,j_0} \neq 0$. Par symétrie des rôles, on réordonne les indices pour fixer $j_0 = n+1$, impliquant $\lambda_{n,n+1} \neq 0$.
- **Élimination du pivot de base $e_n$ :**
    - On isole le dernier vecteur de base $e_n$ à l'aide de la dernière coordonnée non nulle du vecteur $v_{n+1}$ :
    $$e_n = \lambda_{n,n+1}^{-1} \left( v_{n+1} - \sum_{i=1}^{n-1} \lambda_{i,n+1} e_i \right)$$
- **Changement de variable (Famille réduite $(w_j)$) :**
    - On substitue $e_n$ dans l'expression de tous les autres vecteurs $v_j$ pour $j \in [\![1, n]\!]$ :
    $$v_j = \sum_{i=1}^{n-1} \lambda_{i,j} e_i + \lambda_{n,j} \lambda_{n,n+1}^{-1} \left( v_{n+1} - \sum_{i=1}^{n-1} \lambda_{i,n+1} e_i \right)$$
    - On regroupe les termes pour éliminer la dépendance en $e_n$ en définissant la variable combinatoire $w_j$ :
    $$w_j = v_j - \lambda_{n,j} \lambda_{n,n+1}^{-1} v_{n+1} = \sum_{i=1}^{n-1} \left( \lambda_{i,j} - \lambda_{n,j}\lambda_{n,n+1}^{-1}\lambda_{i,n+1} \right) e_i$$
    - Par structure, les $n$ vecteurs de la famille $(w_1, \dots, w_n)$ appartiennent tous à l'espace restreint $\mathrm{Vect}(e_1, \dots, e_{n-1})$.
- **Application de l'hypothèse de récurrence forte :**
    - La famille $(w_1, \dots, w_n)$ compte $n$ éléments au sein d'un espace engendré par $n-1$ vecteurs. Par hypothèse de récurrence, elle est liée.
    - Il existe donc un système de scalaires $(\alpha_1, \dots, \alpha_n) \neq (0, \dots, 0)$ tel que :
    $$\sum_{j=1}^n \alpha_j w_j = 0_E$$
- **Reconstruction de la liaison globale :**
    - On développe la somme en réinjectant la définition de $w_j$ :
    $$\sum_{j=1}^n \alpha_j \left( v_j - \lambda_{n,j} \lambda_{n,n+1}^{-1} v_{n+1} \right) = 0_E \iff \sum_{j=1}^n \alpha_j v_j + \underbrace{\left( - \sum_{j=1}^n \alpha_j \lambda_{n,j} \lambda_{n,n+1}^{-1} \right)}_{= \alpha_{n+1}} v_{n+1} = 0_E$$
    - On obtient une combinaison linéaire nulle sur la famille d'origine : $\sum_{j=1}^{n+1} \alpha_j v_j = 0_E$.
    - La sous-famille de coefficients $(\alpha_1, \dots, \alpha_n)$ étant non triviale, le vecteur global $(\alpha_1, \dots, \alpha_{n+1})$ est obligatoirement non nul.
- **Conclusion :** La famille complète $(v_1, \dots, v_{n+1})$ est liée, validant l'hérédité.
---
>[!INFO] Instructions
> **Théorème de la base incomplète (extraction d'une base) :** Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie et $G = \{g_1, \dots, g_m\}$ une famille génératrice de $E$. Si $L_0$ est une famille libre telle que $L_0 \subset G$, montrer qu'il existe une base $B$ de $E$ telle que $L_0 \subset B \subset G$.

L'idée fondamentale est d'extraire une famille libre de cardinal maximal coincée entre $L_0$ et $G$, puis de montrer par l'absurde qu'elle est nécessairement génératrice.
- **Étape 1 : Construction du candidat maximal par le bon ordre de $\mathbb{N}$**
    - On introduit l'ensemble $I$ des cardinaux des familles libres intermédiaires :
$$I = \{\text{card}(L) \text{ tel que } L \text{ est libre et } L_0 \subset L \subset G\}$$
    - $I$ est non vide car $\text{card}(L_0) \in I$.
    - $I$ est majoré par $m = \text{card}(G)$ car aucune sous-famille libre de $G$ ne peut dépasser son cardinal.
    - $I$ étant une partie de $\mathbb{N}$ non vide et majorée, elle admet un maximum, noté $n = \max(I)$. 
    - Par définition, il existe donc une famille libre $B$ telle que $L_0 \subset B \subset G$ avec $\text{card}(B) = n$.
- **Étape 2 : Démonstration du caractère générateur (Raisonnement par l'absurde)**
    - Pour montrer que $B$ est une base, il reste à prouver que $\text{Vect}(B) = E$. Comme $E = \text{Vect}(G)$, il suffit de montrer que $G \subset \text{Vect}(B)$.
    - Supposons par l'absurde qu'il existe un vecteur du générateur externe : $\exists k \in [\![1, m]\!]$ tel que $g_k \notin \text{Vect}(B)$.
    - D'après le théorème d'extension d'une famille libre, l'adjonction de ce vecteur préserve la liberté : la famille $B' = B \cup \{g_k\}$ est libre.
    - De plus, par construction, on conserve l'encadrement structurel : $L_0 \subset B \subset B' \subset G$.
    - On calcule le cardinal de cette nouvelle famille :
$$\text{card}(B') = \text{card}(B) + 1 = n + 1$$
    - Remplissant toutes les conditions, on en déduit que $(n+1) \in I$.
- **Étape 3 : Contradiction et conclusion**
    - L'affirmation $(n+1) \in I$ contredit directement la définition de $n$ comme étant le maximum absolu de l'ensemble $I$ ($n + 1 > n$).
    - L'hypothèse de départ est donc fausse : $G \subset \text{Vect}(B) \implies \text{Vect}(B) = \text{Vect}(G) = E$.
    - La famille $B$ est libre par construction et génératrice par effondrement de l'absurde ; c'est donc une base de $E$.
---
>[!INFO] Instructions
> **Théorème de la base incomplète/extraite :** Dans un $\mathbb K$-espace vectoriel $E$ de dimension finie, montrer que :
> - Si $L$ est une famille libre de $E$, alors on peut la compléter en une base de $E$.
> $$\exists B \text{ base de } E \text{ telle que } L \subset B$$
> - Si $G$ est une famille génératrice de $E$, alors on peut en extraire une base de $E$.
> $$\exists B \text{ base de } E \text{ telle que } B \subset G$$

Pour démontrer ce théorème, il est nécessaire de connaître ces deux propriétés :
- Pour toute famille libre $L_0$ inclue dans une famille génératrice $G$ ($L_0 \subset G$) :
$$\exists B \text{ base de } E \text{ telle que } L_0 \subset B \subset G$$
- Pour toute famille libre $L_0$ et toute famille génératrice $G$ :
$$\exists B \text{ base de } E \text{ telle que } L_0 \subset B \subset (L_0 \cup G)$$
La déduction en est triviale.

---
>[!INFO] Instructions
> Dans un $\mathbb K$-espace vectoriel $E$ où $F_1,\dots,F_n$ en sont des sev., montrer que :
> $$\sum_{k=1}^n F_k \text{ est une somme directe } \iff \exists ! (x_1,\dots,x_n) \in \prod_{k=1}^n F_k \text{ tel que } x = \sum_{k=1}^n x_k$$

> **Note :** La définition d'une somme direct de $F_k$ énonce que :
>$$\forall (x_1,\dots,x_n) \in \prod_{k=1}^n F_k, \quad \sum_{k=1}^n x_k = 0_E \implies x_k = 0_E, \forall k \in \dots$$

La démonstration est décomposée selon le sens direct/indirect.
- Dans le sens direct $\implies$, on pose $y_k$ vérifiant les mêmes propriétés et en réutilise la définition pour montrer que $x_k - y_k = 0_E$.
- Dans le sens indirect $\impliedby$, on pose juste $x = 0_E = \sum_{k=1}^n x_k$. Comme $0_E = 0_E + \dots + 0_E$, et qu'on sait (par hypothèse) qu'il admet une écriture unique, alors $x_k = 0_E$ pour tout $k$ compris entre 1 et $n$. On a donc vérifié la définition, et $\sum_{k=1}^n F_k$ est donc bel et bien une somme directe.
---
> [!INFO] Instructions
> 
> Soit $H$ un sev propre de $E$. Montrer que :
> $$H \text{ est un hyperplan de } E \iff \forall b \in E \setminus H, \ E = H \oplus \mathbb{K} \cdot b$$

- **Sens indirect ($\impliedby$) :** - Trivial par définition : un hyperplan est un sous-espace qui admet au moins une droite vectorielle comme supplémentaire. La condition étant vraie pour tout $b \notin H$, l'existence est largement vérifiée.
- **Sens direct ($\implies$) :**
    - **Substitution du vecteur de base :**
        - Puisque $H$ est un hyperplan, il existe un vecteur $a \notin H$ tel que $E = H \oplus \mathbb{K} \cdot a$.
        - Soit $b \in E \setminus H$. On décompose $b$ sur cette somme directe : $b = h_1 + \lambda_1 a$ (avec $h_1 \in H$).
        - Comme $b \notin H$, on a nécessairement $\lambda_1 \neq 0$, ce qui permet d'isoler le pivot original : $a = \lambda_1^{-1}(b - h_1)$.
    - **Génération de l'espace ($E = H + \mathbb{K} \cdot b$) :**
        - Tout vecteur $x \in E$ se décompose sous la forme $x = h_2 + \lambda_2 a$. En injectant l'expression de $a$, on obtient :
$$x = h_2 + \lambda_2 \lambda_1^{-1}(b - h_1) = \underbrace{(h_2 - \lambda_2 \lambda_1^{-1} h_1)}_{\in H} + \underbrace{(\lambda_2 \lambda_1^{-1})}_{\in \mathbb{K}} b$$
    - **Tranchage de l'intersection ($H \cap \mathbb{K} \cdot b = \{0_E\}$) :**
        - Soit $x \in H \cap \mathbb{K} \cdot b$. Il existe $\lambda \in \mathbb{K}$ tel que $x = \lambda b \in H$.   
        - Comme $b \notin H$ par hypothèse géométrique, la seule possibilité pour que le produit scalaire appartienne à $H$ est que $\lambda = 0$, d'où $x = 0_E$.

---
## Chapitre XIV-B — Applications linéaires
%% lemme des noyaux %%
%% multiplicité d'une valeur propre %%
## Chapitre XIV-C et XIV-D — Matrices et Déterminants

>[!NOTE] Instructions
>Montrer que $\forall A_1, A_2 \in \mathcal M_n(\mathbb K)$
>$$A_1 \sim A_2 \iff \exists f \in \mathcal L(E), \exists B_1,B_2 \text{ bases de } E, A_2 = [f]_{B_2} \text{ et } A_1 = [f]_{B_1}$$

On décompose la démonstration selon le sens direct/indirect.
**Démonstration dans le sens indirect $\impliedby$ :**
- Soit $f \in \mathcal L(E)$ et $B_1,B_2$ deux bases de $E$ telles que $A_2 = [f]_{B_2}$ et $A_1 = [f]_{B_1}$.
- On utilise les matrices de passage pour trouver que $[f]_{B_1} = P_{B_1}^{B_2} \times [f]_{B_2} \times P_{B_2}^{B_1}$.
- Donc $A_1 = P_{B_1}^{B_2} \times A_2 \times P_{B_2}^{B_1}$.
* Comme $P_{B_1}^{B_2} = (P_{B_2}^{B_1})^{-1}$, on trouve que $A_1 = P_{B_1}^{B_2} \times A_2 \times (P_{B_1}^{B_2})^{-1}$.
* Donc $A_1 \sim A_2$.
**Démonstration dans le sens direct $\implies$ :**
- Soit $P \in \mathrm{GL}_n(\mathbb{K})$ telle que $A_1 = P A_2 P^{-1}$.
- On sait qu'il existe un endomorphisme associé canoniquement à chacune des deux matrices $A_1$ et $A_2$.
- On pose arbitrairement $f \in \mathcal L(\mathbb{K}^n)$ tel que $[f]_{B_C^{(n)}} = A_1$.
- On va maintenant chercher une deuxième base $B$ de $\mathbb{K}^n$ telle que $[f]_B = A_2$.
- Soit $B$ la base formée par les colonnes de $P^{-1}$.
- Alors $P^{-1} = P_{B_C^{(n)}}^B$.
- D'où $A_2 = P^{-1} A_1 P = P_{B_C^{(n)}}^B \times A_1 \times P_{B}^{B_C^{(n)}}$.
- Donc $A_2 = P_{B_C^{(n)}}^B \times [f]_{B_C^{(n)}} \times P_{B}^{B_C^{(n)}}$.
- Donc $A_2 = [f]_B$. CQFD.

---
>[!INFO] Instructions
> Soit $f \in \mathcal{L}(E,F)$ avec $\dim(E)=p$, $\dim(F)=n$ et $\text{rg}(f)=r \neq 0$. Montrer qu'il existe une base $B$ de $E$ et une base $C$ de $F$ telles que :
> $$\text{Mat}(f,B,C) = \begin{pmatrix} I_r & 0_{r, \ p-r} \\ 0_{n-r, \ r} & 0_{n-r, \ p-r} \end{pmatrix}_{(n,p)}$$

- **Étape 1 : Alignement de la source $E$ sur le noyau $\text{Ker}(f)$**
    - D'après le théorème du rang, $\dim(\text{Ker}(f)) = p - r$. On extrait une base du noyau : $(e_{r+1}, \dots, e_p)$.
    - Par le théorème de la base incomplète, on complète cette famille libre en une base globale $B$ de $E$ :
    $$B = (\underbrace{e_1, \dots, e_r}_{\text{hors de } \text{Ker}(f)}, \ \underbrace{e_{r+1}, \dots, e_p}_{\in \text{Ker}(f)})$$
- **Étape 2 : Alignement du but $F$ sur l'image $\text{Im}(f)$**
    - Par linéarité, l'image est générée par les images de la base $B$. Les éléments du noyau s'annulant ($f(e_{r+1}) = \dots = f(e_p) = 0_F$), le système générateur se réduit aux premiers termes :
$$\text{Im}(f) = \text{Vect}\left(f(e_1), \dots, f(e_r)\right)$$
    - Cette famille génératrice compte $r$ vecteurs et $\dim(\text{Im}(f)) = r$ par hypothèse. C'est donc une base de $\text{Im}(f)$, donc elle est libre dans $F$.
    - Par le théorème de la base incomplète, on la complète en une base globale $C$ de $F$ : 
$$C = (\underbrace{f(e_1), \dots, f(e_r)}_{\text{base de } \text{Im}(f)}, \ \underbrace{\varepsilon_{r+1}, \dots, \varepsilon_n}_{\text{complément dans } F})$$
- **Étape 3 : Cartographie matricielle (Évaluation des blocs)**
    - On calcule les coordonnées des images $f(e_j)$ exprimées dans la base $C$ pour remplir les colonnes de la matrice :
        - **Bloc Gauche ($j \in [\!|1, r|\!]$) :** Chaque $f(e_j)$ est par construction le $j$-ième vecteur de la base $C$. Ses coordonnées forment la matrice identité $I_r$ complétée par des zéros en dessous.
        - **Bloc Droit ($j \in [\!|r+1, p|\!]$) :** Chaque $e_j$ appartenant au noyau, $f(e_j) = 0_F$. Ses coordonnées génèrent des colonnes entièrement nulles.
- **Visualisation mnémonique de la structure :**
$$\begin{array}{cc} & \begin{array}{ccc|ccc} \color{cyan}e_1 & \color{cyan}\cdots & \color{cyan}e_r & \color{orange}e_{r+1} & \color{orange}\cdots & \color{orange}e_p \end{array} \\ \begin{array}{c} \color{cyan}f(e_1) \\ \vdots \\ \color{cyan}f(e_r) \\ \hline \varepsilon_{r+1} \\ \vdots \\ \varepsilon_n \end{array} & \left( \begin{array}{ccc|ccc} 1 & & 0 & 0 & \cdots & 0 \\ & \ddots & & \vdots & & \vdots \\ 0 & & 1 & 0 & \cdots & 0 \\ \hline 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & & \vdots & \vdots & & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \end{array} \right) \end{array}$$

---
>[!NOTE] Instructions
> Montrer que :
> $$\forall A \in \mathcal M_n(\mathbb K), A \times \,^t\mathrm{Com}(A) = \,^t\mathrm{Com}(A) \times A = \det(A) \cdot I_n$$

Soit $A = (a_{i,j})_{1 \le i,j \le n} \in \mathcal{M}_n(\mathbb{K})$. Notons $B = \,^t\mathrm{Com}(A)$. Par définition de la transposition et des cofacteurs, le coefficient général de $B$ est donné par :
$$\forall i,k \in [\![1,n]\!], \quad b_{i,k} = A_{k,i}$$
Considérons le produit matriciel $D = B \times A = \,^t\mathrm{Com}(A) \times A$. Par définition du produit de deux matrices, le coefficient général $d_{i,j}$ de $D$ situé à la ligne $i$ et à la colonne $j$ s'écrit :
$$\forall i,j \in [\![1,n]\!], \quad d_{i,j} = \sum_{k=1}^n b_{i,k} a_{k,j} = \sum_{k=1}^n a_{k,j} A_{k,i}$$
Pour évaluer cette somme, nous devons distinguer deux cas selon la position du coefficient dans la matrice produit :
- **Cas 1 : Sur la diagonale principale ($i = j$)**
	- En injectant $j = i$ dans la relation, la somme devient :
$$d_{i,i} = \sum_{k=1}^n a_{k,i} A_{k,i}$$
	- On reconnaît immédiatement la formule du développement du déterminant de la matrice $A$ suivant sa $i$-ième colonne. On a donc :
$$\forall i \in [\![1,n]\!], \quad d_{i,i} = \det(A)$$
- **Cas 2 : Hors de la diagonale principale ($i \neq j$)**
	- Si $i \neq j$, la somme $\sum_{k=1}^n a_{k,j} A_{k,i}$ correspond au développement de Laplace suivant sa $i$-ième colonne d'une matrice fictive, notée $A^{(i \leftarrow j)}$, obtenue en remplaçant la $i$-ième colonne de $A$ par sa $j$-ième colonne.
$$A^{(i \leftarrow j)} = \begin{pmatrix} c_1 & \dots & \underbrace{c_j}_{\text{position } i} & \dots & \underbrace{c_j}_{\text{position } j} & \dots & c_n \end{pmatrix}$$
	- Cette matrice présente deux colonnes rigoureusement identiques (aux positions $i$ et $j$). Le déterminant étant une forme alternée, on a $\det(A^{(i \leftarrow j)}) = 0_\mathbb{K}$. Par conséquent :
$$\forall i \neq j, \quad d_{i,j} = 0_\mathbb{K}$$
	- En regroupant ces deux cas à l'aide du symbole de Kronecker $\delta_{i,j}$, on a $d_{i,j} = \det(A) \cdot \delta_{i,j}$. La matrice produit $D$ est donc une matrice diagonale dont tous les termes valent $\det(A)$ :

$$\,^t\mathrm{Com}(A) \times A = \begin{pmatrix} \det(A) & 0 & \dots & 0 \\ 0 & \det(A) & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \det(A) \end{pmatrix} = \det(A) \cdot I_n$$
**Démonstration de la commutativité :**
Pour établir que $A \times \,^t\mathrm{Com}(A) = \det(A) \cdot I_n$, on applique la relation fondamentale que l'on vient de prouver à la matrice transposée $\,^tA$ :
$$\,^t\mathrm{Com}(\,^tA) \times \,^tA = \det(\,^tA) \cdot I_n$$
En utilisant le lemme de structure de la comatrice démontre précédemment, on sait que $\mathrm{Com}(\,^tA) = \,^t\mathrm{Com}(A)$. En prenant la transposée de chaque membre, on a :
$$\,^t\mathrm{Com}(\,^tA) = \,^t(\,^t\mathrm{Com}(A)) = \mathrm{Com}(A)$$
De plus, le déterminant est invariant par transposition ($\det(\,^tA) = \det(A)$). L'égalité se simplifie en :
$$\mathrm{Com}(A) \times \,^tA = \det(A) \cdot I_n$$
En appliquant l'opérateur de transposition $\,^t(\cdot)$ de chaque côté de cette égalité matricielle, et en utilisant la propriété d'inversion de l'ordre du produit $(\,^t(M \times N) = \,^tN \times \,^tM)$, on obtient :
$$\,^t(\mathrm{Com}(A) \times \,^tA) = \,^t(\det(A) \cdot I_n) \implies \bigl(\,^t(\,^tA)\bigr) \times \,^t\mathrm{Com}(A) = \det(A) \cdot \,^tI_n$$
Comme $\,^t(\,^tA) = A$ et $\,^tI_n = I_n$, on valide de manière définitive la seconde identité :
$$A \times \,^t\mathrm{Com}(A) = \det(A) \cdot I_n$$
%% Si u est un projecteur de E, alors tr(u) = rg(u) (sa trace est égale à son rang) %%

---
>[!NOTE] Instructions
>Montrer que
>$$\varepsilon : \begin{matrix} (S_n,\circ) \to (\{-1, 1\},\times) \\ \sigma \mapsto \varepsilon(\sigma) \end{matrix}$$
> est un morphisme de groupes.

Il a été déjà démontré en amont que $\varepsilon$ est bien définie (carré de la définition).
Pour montrer que $\varepsilon$ est un morphisme de groupes, il suffit de montrer que pour toutes permutations $\sigma_1$ et $\sigma_2$ de $S_n$, on a :
$$\varepsilon(\sigma_1 \circ \sigma_2) = \varepsilon(\sigma_1) \cdot \varepsilon(\sigma_2)$$
On sait que $\varepsilon(\sigma) \in \{-1, 1\}$ pour toute permutation $\sigma$ de $S_n$. Donc $\varepsilon$ est une application de $S_n$ dans $\{-1, 1\}$.
Soient $\sigma_1$ et $\sigma_2$ deux permutations de $S_n$. Calculons $\varepsilon(\sigma_1 \circ \sigma_2)$ :

$$\begin{align*}

	\varepsilon(\sigma_1 \circ \sigma_2) &= \prod_{1 \le i < j \le n} \frac{(\sigma_1 \circ \sigma_2)(j) - (\sigma_1 \circ \sigma_2)(i)}{j - i} \\

	&= \prod_{1 \le i < j \le n} \frac{\sigma_1(\sigma_2(j)) - \sigma_1(\sigma_2(i))}{j - i}

\end{align*}$$
On peut réécrire le produit ci-dessus en regroupant les termes de la manière suivante :
$$\varepsilon(\sigma_1 \circ \sigma_2) = \prod_{1 \le i < j \le n} \frac{\sigma_1(\sigma_2(j)) - \sigma_1(\sigma_2(i))}{\sigma_2(j) - \sigma_2(i)} \cdot \frac{\sigma_2(j) - \sigma_2(i)}{j - i}$$
Comme $\sigma_1$ est une permutation, elle est bijective, donc on peut effectuer un changement de variable (muette) dans le premier produit. En posant $k = \sigma_2(i)$ et $l = \sigma_2(j)$, on obtient :
$$\varepsilon(\sigma_1 \circ \sigma_2) = \prod_{1 \le k \ne l \le n} \frac{\sigma_1(l) - \sigma_1(k)}{l - k} \cdot \prod_{1 \le i < j \le n} \frac{\sigma_2(j) - \sigma_2(i)}{j - i}$$
On reconnaît dans le premier produit la signature de $\sigma_1$ et dans le second produit la signature de $\sigma_2$ (sachant qu'elles sont toutes deux bijectives) :
$$\varepsilon(\sigma_1 \circ \sigma_2) = \varepsilon(\sigma_1) \cdot \varepsilon(\sigma_2)$$
Ainsi, $\varepsilon$ est un morphisme de groupes de $(S_n, \circ)$ dans $(\{-1, 1\}, \times)$.