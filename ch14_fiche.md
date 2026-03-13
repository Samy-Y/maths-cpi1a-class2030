# Fiche CH14
*Résumé approximatif.*

## Espace vectoriel

### Définition initiale

$(E,+,\cdot)$ est un $\mathbb{K}$-espace vectoriel (ev) si :
1. $(E,+)$ est un groupe abélien,
2. La loi externe $\cdot : \mathbb{K} \times E \to E$ vérifie les propriétés suivantes :
   1. $\forall x \in E, 1_\mathbb{K} \cdot x = x$,
   2. $\forall \alpha, \beta \in \mathbb{K}, \forall x \in E, (\alpha + \beta) \cdot x = \alpha \cdot x + \beta \cdot x$,
   3. $\forall \alpha, \beta \in \mathbb{K}, \forall x \in E, (\alpha\beta) \cdot x = \alpha \cdot (\beta \cdot x)$.
   4. $\forall \alpha \in \mathbb{K}, \forall x, y \in E, \alpha \cdot (x + y) = \alpha \cdot x + \alpha \cdot y$.

* Les éléments de $E$ sont appelés des vecteurs.
* Les éléments de $\mathbb{K}$ sont appelés des scalaires.

### Exemples initiaux

* Si $\mathbb{K}$ est un corps, alors $\mathbb{K}^n$ est un $\mathbb{K}$-ev pour tout $n \in \mathbb{N}^*$.
* Si $E$ est un corps et $\mathbb{K}$ est un sous-corps *commutatif* de $E$, alors $E$ est un $\mathbb{K}$-ev.
  * Par exemple, $\mathbb{C}$ est un $\mathbb{R}$-ev.
* Si $\mathbb{K}$ est un corps commutatif et $D$ un ensemble *non-vide*, alors $(\mathbb{K}^D,+,\cdot)$ est un $\mathbb{K}$-ev.

## Sous-espace vectoriel

Un sous-espace vectoriel (sous-ev) de $E$ est une partie $F$ de $E$ qui est elle-même un $\mathbb{K}$-ev pour les lois induites par celles de $E$.

## Caractérisation d'un sous-espace vectoriel

Il existe trois équivalences pour une partie $F$ de $E$, avec $E$ un $\mathbb{K}$-ev :

$$\begin{align*}
F \text{ est un sous-ev de } E &\iff \begin{cases}F \neq \emptyset\\\forall \lambda,\gamma \in \mathbb{K}, \forall x,y \in F, \lambda x + \gamma y \in F\end{cases}\\
&\iff \begin{cases}0_E  \in F \\ \forall \lambda \in \mathbb{K}, \forall x,y \in F, \lambda x + y \in F\end{cases} ~\text{(important)}\\
\end{align*}$$

## Famille libre, génératrice et base

## Sous-espace vectoriel engendré par une partie

## Espace vectoriel de dimension finie
