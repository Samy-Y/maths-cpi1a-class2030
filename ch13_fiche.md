# Chapitre 13

*Résumé primitif.*

## Construction du corps de fractions

* Construction d'une classe d'équivalence de fractions à partir d'un anneau intègre $A$.
$$(N,D) \in A\times A\setminus\{0\}, (N,D) \sim (N',D') \iff N\cdot D' = N' \cdot D$$
* Définition du corps de fractions $\mathbb{K} = \{Cl(N,D) \mid N\in A, D\in A\setminus\{0\}\}$.
* Propriétés sur les égalités et les opérations dans le corps de fractions.
  * $\begin{cases} Cl(N,D) = Cl(N',D') \\ Cl(A,B) = Cl(A',B') \end{cases} \implies \begin{cases} Cl(NB + AD, BD) = Cl(N'B' + A'D', B'D') \\ Cl(AN,BD) = Cl(A'N', B'D') \end{cases}$
  * Opération additive $+$ : $Cl(N,D) + Cl(A,B) = Cl(NB + AD, BD)$
  * Opération multiplicative $\times$ : $Cl(N,D) \times Cl(A,B) = Cl(AN, BD)$
  * Muni de ces deux opérations, $\mathbb{K}$ est un corps commutatif.
* Injection canonique de $A$ dans $\mathbb{K}$ : $f : A \to \mathbb{K}, a \mapsto Cl(a,1) = \frac{a}{1}$.
  * $f$ est un morphisme d'anneaux injectifs.
  * On peut identifier $A$ à son image dans $\mathbb{K}$ notée $f(A)$, et ainsi considérer $A$ comme un sous-anneau de $\mathbb{K}$.
  * $\mathbb{K}$ est appelé le corps de fractions de $A$.
  * On peut bien le considérer comme une extension de $A$.
* $\mathbb{K}$ est le plus petit corps contenant $A$ : pour tout corps $L$ contenant $A$, il existe un morphisme d'anneaux injectif de $\mathbb{K}$ dans $L$ qui fixe les éléments de $A$.
* Si $A$ est un anneau de polynômes $\mathbb{K}[X]$, alors son corps de fractions est le corps des fractions rationnelles $\mathbb{K}(X)$.
$$\mathbb{K}(X) = \{Cl(P,Q) = \frac PQ \mid P\in \mathbb{K}[X], Q\in \mathbb{K}[X]\setminus\{0\}\}$$

## Corps des fractions rationnelles

### Degrés

* Degré d'une fraction rationnelle $F = \frac PQ$ : $\deg(F) = \deg(P) - \deg(Q)$.
* Propriétés sur les degrés :
  * $\deg(FG) = \deg(F) + \deg(G)$
  * $\deg(F + G) \leq \max(\deg(F), \deg(G))$
  * $\deg(F) = -\infty \iff F = 0$
  * $\deg(F) \in \Z\cup\{-\infty\}$
  * Si $F \in \mathbb{K}[X]^*$, alors $\deg(F) \in \N$.
    * La réciproque est fausse : $\deg(\frac{X^2}{X+1}) = 1$ mais $\frac{X^2}{X+1} \notin \mathbb{K}[X]$.

### Fraction dérivée

* Définition de la fraction dérivée : $F' = \frac{P'Q - PQ'}{Q^2}$.
* Propriétés sur la fraction dérivée :
  * $\deg(F') \leq \deg(F) - 1$.
    * *Exemple pertinent :* $F=\frac{X}{X+1}$, alors $\deg(F) = 0$ mais $\deg(F') = -2 \le \deg(F) - 1$.

## Zéros et pôles

* $\alpha$ est un zéro de $F$ de multiplicité $s$ lorsque $\alpha$ est une racine du numérateur de $F$ de multiplicité $s$.
* $\beta$ est un pôle de $F$ de multiplicité $t$ lorsque $\beta$ est une racine du dénominateur de $F$ de multiplicité $t$.
* **Important :** Les zéros et les pôles d'une fraction rationnelle sont définis seulement lorsque le numérateur et le dénominateur sont premiers entre eux, i.e. $F = \frac AB$ avec $A\wedge B = 1$.

## Forme irréductible

* Toute fraction rationnelle $F$ peut s'écrire de manière unique sous la forme irréductible $\frac AB$ avec $A\wedge B = 1$ et $B$ unitaire.

*Preuve :*

* Existence :
  * "Suppression" du coefficient dominant du dénominateur (ajout dans le numérateur, qui devient $P_{cfd}$) pour que le dénominateur soit unitaire.
  * Existence d'un PGCD $D$ de $P$ et $Q$ tel que $P_{cfd} = DA$ et $Q = DB$ avec $A\wedge B = 1$.
  * On réecrit donc $F$ sous la forme $\frac{P_{cfd}}{Q} = \frac{DA}{DB} = \frac AB$.

* Unicité :
  * Supposons que $F$ puisse s'écrire sous la forme $\frac AB$ et $\frac{A'}{B'}$ avec $A, B, A', B' \in \mathbb{K}[X]$, $A \wedge B = 1$, $A' \wedge B' = 1$, $B$ unitaire et $B'$ unitaire. Alors, on a :
    * $A'B = AB'$ (en utilisant l'égalité $\frac AB = \frac{A'}{B'}$).
    * Comme $B \mid A' B$, alors en utilisant le théorème de Gauss, on trouve que $B \mid B'$. De même, $B' \mid A B'$, donc $B' \mid B$ (sachant que $A$ et $B$ sont premiers entre eux).
    * Ainsi, $B$ et $B'$ sont deux polynômes associés et unitaires alors $B = B'$.
    * En remplaçant dans l'égalité, le résultat est démontré.

## Élément simple

* $F$ est un élément simple de $\mathbb{K}(X)$ soit lorsque...
  * $F = a\cdot X^k$ avec $a \in \mathbb{K}$ et $k \in \Z$. ($F$ est un monôme de degré $k$)
* ou bien...
  * $F = \frac{A}{P^n}$ avec :
    * $A \in \mathbb{K}[X]^*$,
    * $P \in \mathbb{K}[X]$ irréductible,
    * $n \in \N^*$,
    * $\deg(A) < \deg(P)$.

>[!NOTE] Élément simple nul ?
> J'en suis pas encore sûr. Je dois demander au prof.

## Partie entière et fractionnaire

* Il existe un unique couple $(E,G) \in \mathbb{K}[X] \times \mathbb{K}(X)$ tel que $F = E + G$ et $G$ est une fraction rationnelle strictement fractionnaire (i.e. $\deg(G) < 0$).
* $E$ est appelé la partie entière de $F$ tandis que $G$ est appelé la partie fractionnaire de $F$.
*Démonstration via division euclidienne.*

## Décomposition en éléments simples

### Décomposition en éléments simples de fractions rationnelles à dénominateur produit de facteurs premiers entre eux

$$F = \frac{A}{B_1 \cdots B_n}$$
avec :

* $A, B_1, \dots, B_n \in \mathbb{K}[X]$,
* $B_i$ et $B_j$ sont deux à deux premiers entre eux,
* $\deg(F) < 0$.

Il existe un unique $n$-uplet $(A_1, \dots, A_n) \in \mathbb{K}[X]^n$ tel que $F = \sum_{i=1}^n \frac{A_i}{B_i}$ et $\deg(A_i) < \deg(B_i)$ pour tout $i \in \{1, \dots, n\}$.

*Démonstration par récurrence sur $n$. Initialisation $n=2$ recommandée.*

### Décomposition en éléments simples d'une fraction rationnelle de la forme $\frac{A}{B^n}$

$$F = \frac{A}{B^n}$$
avec :

* $A, B \in \mathbb{K}[X]$,
* $n \in \N^*$,
* $\deg(F) < 0$.

Il existe un unique $n$-uplet $(A_1, \dots, A_n) \in \mathbb{K}[X]^n$ tel que :
$$F = \sum_{i=1}^n \frac{A_i}{B^i}$$
et $\deg(A_i) < \deg(B)$ pour tout $i \in \{1, \dots, n\}$.

*Démonstration par récurrence sur $n$. Hérédité démontrée via division euclidienne et utilisation de l'H.R.*

### Cas général (Théorème)

Soit $F = \frac AB \in \mathbb{K}(X)$,

avec :

* $A, B \in \mathbb{K}[X]$,
* $A \wedge B = 1$,
* $B$ unitaire.

On écrit $B$ sous la forme $B = \prod_{i=1}^r B_i^{\alpha_i}$ avec :

* $B_i$ et $B_j$ deux à deux distincts
* $B_i$ irréductible pour tout $i \in \{1, \dots, r\}$,
  * ce qui implique implicitement que les $B_i$ sont premiers entre eux,
* $\alpha_i \in \N^*$ pour tout $i \in \{1, \dots, r\}$.

Il existe d'uniques :

* $E \in \mathbb{K}[X]$,
* $A_{i,j} \in \mathbb{K}[X]$ pour tout $i \in \{1, \dots, r\}$ et tout $j \in \{1, \dots, \alpha_i\}$,

tels que :
$$F = E + \sum_{i=1}^r \sum_{j=1}^{\alpha_i} \frac{A_{i,j}}{B_i^j}$$
et $\deg(A_{i,j}) < \deg(B_i)$ pour tout $i \in \{1, \dots, r\}$ et tout $j \in \{1, \dots, \alpha_i\}$.

*Démonstration :*

1. Division euclidienne de $A$ par $B$ pour trouver un quotient $E$ et un reste $R$ tels que $A = EB + R$ avec $\deg(R) < \deg(B)$.
2. Utilisation de la première propriété pour trouver des éléments $A_{i,1}$ tels que $\frac RB = \sum_{i=1}^r \frac{A_{i,1}}{B_i^{\alpha_i}}$ avec $\deg(A_{i,1}) < \deg(B_i)$ pour tout $i \in \{1, \dots, r\}$, sachant que $B$ peut être décomposé en un produit $\prod_{i=1}^r B_i^{\alpha_i}$ avec $\deg(\frac{A_k}{B_k^{\alpha_k}}) < 0$ pour tout $k \in \{1, \dots, r\}$.
3. Utilisation de la seconde propriété pour trouver des éléments $A_{i,j}$ tels que $\frac{A_{i,1}}{B_i^{\alpha_i}} = \sum_{j=1}^{\alpha_i} \frac{A_{i,j}}{B_i^j}$ avec $\deg(A_{i,j}) < \deg(B_i)$ pour tout $j \in \{1, \dots, \alpha_i\}$ et tout $i \in \{1, \dots, r\}$.
4. En combinant toutes ces égalités, on trouve que $F = E + \sum_{i=1}^r \sum_{j=1}^{\alpha_i} \frac{A_{i,j}}{B_i^j}$ avec les conditions de degrés sur les $A_{i,j}$.

### Techniques de décomposition

#### Méthode par pôles simples

Soit $F = \frac AB \in \mathbb{K}(X)$ avec :

* $A \wedge B = 1$,
* $B = \prod_{i=1}^n (X - a_i)$
  * $a_i \in \mathbb{K}$ pour tout $i \in \{1, \dots, n\}$
  * les $a_i$ sont deux à deux distincts.

$F$ peut être décomposée de la manière suivante :

$$F = E + \sum_{i=1}^n \frac{\lambda_i}{X - a_i}$$
avec $E \in \mathbb{K}[X]$ et $\lambda_i \in \mathbb{K}$ pour tout $i \in \{1, \dots, n\}$.

* $\lambda_i = \frac{A(a_i)}{B'(a_i)}$ pour tout $i \in \{1, \dots, n\}$.

#### Méthode par pôles doubles

Soit $F = \frac AB \in \mathbb{K}(X)$ avec :

* $A \wedge B = 1$,
* $B = (X - a)^2 \cdot Q$ avec $Q(a) \neq 0$ et $a \in \mathbb{K}$.

$F$ peut être décomposée de la manière suivante :
$$F = E + \frac{\lambda_1}{X - a} + \frac{\lambda_2}{(X - a)^2} + \frac{A_1}{Q}$$

avec $\deg(A_1) < \deg(Q)$ et $\lambda_1, \lambda_2 \in \mathbb{K}$.

Et on a $\begin{cases} \lambda_2 = \frac{A(a)}{Q(a)} \\ \lambda_1 = (\frac{A}{Q})'(a) \end{cases}$.

#### Méthode par pôles multiples ($s \ge 3$)

Soit $F = \frac{P}{(X - a)^s \cdot Q}$ avec $Q(a) \neq 0$ et $a \in \mathbb{K}$, $s \ge 3$.

D'après la formule de Taylor, $P$ peut être décomposé de la manière suivante :
$$P = \sum_{k=0}^{n} P^{(k)}(a) \cdot \frac{(X - a)^k}{k!}$$

* Si $n < s$, alors $F$ peut être décomposée de la manière suivante :
$$F = \sum_{k=0}^{n} \frac{P^{(k)}(a)}{k!} \cdot \frac{1}{(X - a)^{s-k}}$$

* Si $n \ge s$, alors $F$ peut être décomposée de la manière suivante :
$$F = \sum_{k=0}^{s-1} \frac{P^{(k)}(a)}{k!} \cdot \frac{1}{(X - a)^{s-k}} + \underbrace{\sum_{k=s}^{n} \frac{P^{(k)}(a)}{k!} \cdot (X - a)^{k-s}}_{\text{partie entière}}$$