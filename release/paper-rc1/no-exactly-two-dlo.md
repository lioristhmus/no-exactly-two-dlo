<div id="sec:title"></div>

# No Set Carries Exactly Two Dense Linear Orders without Endpoints

*A Cut-Rotation Proof in a Weak Zermelo Theory without Choice or Replacement*

**Lior Isthmus**

<div id="sec:abstract"></div>

## Abstract

Let $Z_{\mathrm{sep}}$ consist of Extensionality, Pairing, Infinity, Union, Power Set, and the full Separation schema, and write $s(X)=n$ when $X$ carries exactly $n$ isomorphism types of dense linear orders without endpoints. No form of Choice, Replacement, or Foundation is assumed. We prove

$$
Z_{\mathrm{sep}}
\vdash
\neg\exists X\,(s(X)=2).
$$ {#eq:abstract-main}

Using countable-carrier uniqueness and the Dedekind-infinite four-type alternative from the exact-three companion, exact two forces $X$ to be neither at most countable nor Dedekind-infinite and every DLO on $X$ to be rigid. A type-count-free dyadic reflection argument eliminates the possibility that both types are self-dual, leaving one rigid non-self-dual dual pair $\{[L],[L^*]\}$.

For each $c\in L$, four one-point cut orders form an antipodal two-colored square. Vertical monochromaticity would self-dualize both rays and then the whole carrier; hence

$$
L\cong\operatorname{Rot}_c(L).
$$

Rigidity gives a unique isomorphism $\rho_c:L\to\operatorname{Rot}_c(L)$. Define $\delta(c)=\rho_c^{-1}(c)$. Its graph is obtained by Separation inside $X\times X$, without forming a Replacement-generated family $(\rho_c)_{c\in X}$. Opposite-ray exchange and hereditary Dedekind-finiteness force $\delta$ to be an injective strictly decreasing surjection. Thus $\delta$ is an order reversal of $L$, contradicting $L\not\cong L^*$.

Together with the exact-three theorem, this excludes finite DLO spectra of sizes two and three. Spectra of size at least four are not decided here.

**Keywords.** dense linear orders; axiom of choice; Dedekind-finite sets; cut rotation; categoricity; weak set theory.

**2020 Mathematics Subject Classification.** Primary 03E25; Secondary 03E30, 03C35, 03C64, 06A05.

\tableofcontents

<div id="sec:introduction"></div>

## 1. Introduction

A **dense linear order without endpoints**, abbreviated **DLO**, is a nonempty strict linear order $(X,<)$ which is dense and has neither a least nor a greatest point. Throughout this paper,

$$
X\text{ is at most countable}
\quad\Longleftrightarrow\quad
X\hookrightarrow\omega,
$$

and

$$
X\text{ is Dedekind-infinite}
\quad\Longleftrightarrow\quad
\omega\hookrightarrow X.
$$

Without Choice these conditions need not be complementary.

In the language $\{<\}$, the DLO axioms form the complete theory $\operatorname{Th}(\mathbb Q,<)$; see [Marker 2002](#ref:marker2002). Thus the finite spectra considered here are precisely the numbers of models of this theory, up to internal isomorphism, on one fixed underlying set. For background on cardinal comparison and Dedekind-finite sets without Choice, see [Jech 1973](#ref:jech1973) and [Howard–Rubin 1998](#ref:howardrubin1998).

The companion paper [Isthmus 2026a](#ref:isthmus2026a) proves in the same weak theory that no set carries exactly three DLO types, thereby answering Shelah's Question 7.11 negatively [Shelah 2009](#ref:shelah2009). Two global spectrum results are used directly below: at-most-countable DLO uniqueness and the four-type alternative on every Dedekind-infinite carrier. Several elementary order-theoretic and foundational lemmas are also reused, including rigidity facts, finite ranking, binary-word coding, finite block sums, and bounded recursion. [Appendix B](#app:dyadic-engine) of the present paper extracts and proves the type-count-free dyadic reflection engine needed for exact two, rather than appealing to an exact-three theorem with altered hypotheses. The cited Lean 4 development formalizes the exact-three theorem package [Isthmus 2026b](#ref:isthmus2026b); the exact-two engine and cut-rotation argument are not claimed to be part of that formalization.

Exact two has a different obstruction from exact three. On three types, reversal has a fixed point and therefore supplies a self-dual type. On two types, reversal may exchange the two types and have no fixed point. The main task is therefore to break one rigid non-self-dual dual pair without first assuming a self-dual representative.

The proof is organized around two statements.

<div id="thm:intro-reduction"></div>

**Theorem 1.1 (Exact-two structural reduction).**
If $s(X)=2$, then:

1. $X\nhookrightarrow\omega$;
2. $\omega\nhookrightarrow X$;
3. every DLO on $X$ is rigid;
4. reversal exchanges the two types;
5. no DLO on $X$ is self-dual;
6. after naming one representative $L$, the two types are

   $$
   \{[L],[L^*]\},
   \qquad
   L\not\cong L^*.
   $$

<div id="thm:intro-cut-reversal"></div>

**Theorem 1.2 (Cut-preimage reversal).**
Let $L=(X,<)$ satisfy the residual conditions of Theorem 1.1. If every one-point cut rotation $\operatorname{Rot}_c(L)$ is isomorphic to $L$, then the unique cut-rotation isomorphisms determine a decreasing bijection

$$
\delta:X\longrightarrow X.
$$

Consequently $L\cong L^*$.

The finite cut square proves the hypothesis of Theorem 1.2. The contradiction with Theorem 1.1 then excludes exact two.

The new mechanism is local. Exact-three exclusion uses a self-dual representative and a full dyadic reflection tree. Exact-two exclusion uses the tree only to eliminate the all-self-dual reversal pattern. Once the remaining dual pair is isolated, a four-corner cut square and the point-indexed preimage map $\delta$ close the proof.

The paper is a genuine companion rather than a duplicate. The foundational coding, countable benchmark theorem, and Lindenbaum theorem are imported from [Isthmus 2026a](#ref:isthmus2026a). The present paper proves the exact-two reduction, a parameterized type-count-free reflection-tree engine, the cut-square theorem, and the cut-preimage reversal.

<div id="sec:formal-setting"></div>

## 2. Formal setting and imported results

<div id="def:2-1-base-theory"></div>

**Definition 2.1 (The base theory).**
$Z_{\mathrm{sep}}$ consists of Extensionality, Pairing, Infinity, Union, Power Set, and the full Separation schema. No use is made of Choice, Countable Choice, Dependent Choice, Replacement, Collection, or Foundation.

All orders are subsets of $X\times X$, and all witnessing maps are internal sets. The construction of $\omega$, bounded unique recursion, finite functions, finite block sums, and the relevant arithmetic are available in this theory by [Isthmus 2026a, Appendices A–B](#ref:isthmus2026a).

<div id="def:2-2-spectrum"></div>

**Definition 2.2 (Finite spectrum formulas).**
For every standard finite $n\ge1$, let $\operatorname{Spec}_{\ge n}(X)$ assert that there are $n$ pairwise nonisomorphic DLO relations on $X$. Put

$$
\operatorname{Spec}_{=n}(X)
:=
\operatorname{Spec}_{\ge n}(X)
\wedge
\neg\operatorname{Spec}_{\ge n+1}(X).
$$ {#eq:finite-spectrum-formula}

The notation $s(X)\ge n$ abbreviates $\operatorname{Spec}_{\ge n}(X)$, and $s(X)=n$ abbreviates $\operatorname{Spec}_{=n}(X)$. No quotient set of isomorphism classes is formed.

If $s(X)=n$ and $R_0,\ldots,R_{n-1}$ are pairwise nonisomorphic DLOs on $X$, then every DLO on $X$ is isomorphic to exactly one $R_i$. Otherwise an additional type would witness $s(X)\ge n+1$.

<div id="def:2-3-order-notation"></div>

**Definition 2.3 (Order notation).**
For sets $A,B$, the notation $A\hookrightarrow B$ means that an injection from $A$ to $B$ exists, and $A\nhookrightarrow B$ means that no such injection exists. For $m\in\omega$, the notation $|A|\le m$ abbreviates the existence of an injection $A\to m$, and $|A|=m$ abbreviates the existence of a bijection $A\to m$.

For a linear order $L=(X,<)$:

- $L^*$ is the reverse order;
- $(-\infty,c)_L$ and $(c,\infty)_L$ are the strict rays at $c$;
- an **order reversal** of $L$ is an anti-isomorphism $L\to L$;
- $L$ is **self-dual** if $L\cong L^*$;
- $L$ is **rigid** if its increasing automorphism group is trivial.

Finite order sums are taken over disjoint blocks. Empty blocks are omitted, and every new adjacent boundary is checked against the finite block-sum DLO criterion of [Isthmus 2026a, Lemma 2.7](#ref:isthmus2026a).

<div id="thm:2-4-subcountable-uniqueness"></div>

**Theorem 2.4 (At-most-countable DLO uniqueness).**
If $X$ carries a DLO and $X\hookrightarrow\omega$, then

$$
s(X)=1.
$$ {#eq:subcountable-uniqueness}

*Proof.*
This is [Isthmus 2026a, Lemma 3.11](#ref:isthmus2026a). The proof first shows that an infinite subcountable set is bijective with $\omega$, then carries out a deterministic least-index back-and-forth construction inside a fixed power set. ∎

<div id="thm:2-5-dedekind-alternative"></div>

**Theorem 2.5 (Dedekind-infinite four-type alternative).**
If $X$ carries a DLO and $\omega\hookrightarrow X$, then

$$
X\hookrightarrow\omega
\quad\text{or}\quad
s(X)\ge4.
$$ {#eq:dedekind-alternative}

*Proof.*
This is [Isthmus 2026a, Theorem 3.12](#ref:isthmus2026a). A choice-free monotone-subsequence construction gives a countable benchmark whose DLO complement is either subcountable or supports four pairwise nonisomorphic same-carrier DLOs. ∎

<div id="lem:2-6-automorphism-orbit"></div>

**Lemma 2.6 (A nontrivial increasing automorphism gives a countable orbit).**
If a linear order on $X$ has a nonidentity increasing automorphism, then

$$
\omega\hookrightarrow X.
$$ {#eq:automorphism-orbit}

*Proof.*
This is [Isthmus 2026a, Lemma 6.1](#ref:isthmus2026a). Choose $x<g(x)$ after replacing $g$ by $g^{-1}$ if necessary, and recursively form the strictly increasing orbit $g^n(x)$. ∎

<div id="cor:2-7-common-host"></div>

**Corollary 2.7 (Common-host self-duality criterion).**
If one linear order contains initial segments isomorphic to both $A$ and $A^*$, or final segments isomorphic to both, then

$$
A\cong A^*.
$$ {#eq:common-host}

*Proof.*
This is [Isthmus 2026a, Corollary 4.3](#ref:isthmus2026a), obtained from Lindenbaum's initial/final-segment theorem; see also [Ervin 2017, §2.3](#ref:ervin2017). ∎

<div id="lem:2-8-rigidity-convex"></div>

**Lemma 2.8 (Rigidity and reversals on convex suborders).**
Let $L$ be rigid.

1. Every convex suborder of $L$ is rigid.
2. Every reversal of a rigid order is involutive.
3. A rigid self-dual order has a unique reversal.

*Proof.*
This is [Isthmus 2026a, Lemma 4.8](#ref:isthmus2026a). A convex-suborder automorphism extends by the identity, two reversals differ by an automorphism, and the square of a reversal is an automorphism. ∎

<div id="sec:structural-reduction"></div>

## 3. Exact-two structural reduction

Throughout this section assume

$$
s(X)=2,
$$

and fix pairwise nonisomorphic representatives

$$
L_0=(X,<_{0}),
\qquad
L_1=(X,<_{1}).
$$

<div id="lem:3-1-not-subcountable"></div>

**Lemma 3.1 (An exact-two carrier is not at most countable).**
One has

$$
X\nhookrightarrow\omega.
$$

*Proof.*
Otherwise Theorem 2.4 would give $s(X)=1$. ∎

<div id="lem:3-2-not-dedekind-infinite"></div>

**Lemma 3.2 (An exact-two carrier is not Dedekind-infinite).**
One has

$$
\omega\nhookrightarrow X.
$$

*Proof.*
If $\omega\hookrightarrow X$, Theorem 2.5 gives either $X\hookrightarrow\omega$ or $s(X)\ge4$. The first alternative contradicts Lemma 3.1. In the second, discarding one of four witnesses gives $s(X)\ge3$, contradicting $s(X)=2$. ∎

<div id="lem:3-3-rigidity"></div>

**Lemma 3.3 (Every exact-two DLO is rigid).**
Every DLO on $X$ has trivial increasing automorphism group.

*Proof.*
A nontrivial increasing automorphism would give $\omega\hookrightarrow X$ by Lemma 2.6, contradicting Lemma 3.2. ∎

<div id="lem:3-4-hereditary-dedekind"></div>

**Lemma 3.4 (Hereditary Dedekind-finiteness).**
Let $Y\subseteq X$. Every injective map

$$
j:Y\longrightarrow Y
$$

is surjective.

*Proof.*
Suppose $j$ were injective and not surjective. Choose

$$
y_0\in Y\setminus j[Y]
$$

and define

$$
y_{n+1}=j(y_n)
$$

by bounded unique recursion inside the fixed set $\omega\times Y$. If $n<m$ and $y_n=y_m$, injectivity cancels the first $n$ iterates and gives

$$
y_0=j^{m-n}(y_0)\in j[Y],
$$

contrary to the choice of $y_0$. Thus $n\mapsto y_n$ is an injection $\omega\hookrightarrow Y\hookrightarrow X$, contradicting Lemma 3.2. ∎

<div id="def:3-5-reversal-action"></div>

**Definition 3.5 (Reversal action on the two types).**
For each $i<2$, let $\sigma(i)<2$ be the unique index satisfying

$$
L_i^*\cong L_{\sigma(i)}.
$$

The graph of $\sigma$ is the Separation-defined subset

$$
\{(i,j)\in2\times2:L_i^*\cong L_j\};
$$

exactness makes this relation a function. Reversing twice gives

$$
\sigma^2=\operatorname{id}_{2}.
$$

Hence either $\sigma=\operatorname{id}_{2}$ or $\sigma=(01)$.

<div id="lem:3-6-all-selfdual-flank"></div>

**Lemma 3.6 (Symmetric flank localization when all global types are self-dual).**
Assume every DLO on $X$ is self-dual. Let $P$ be a DLO on $X$ with an involutive reversal $k$, and suppose

$$
P=A+M+k[A],
\qquad
k[M]=M,
$$ {#eq:all-selfdual-flank}

where $A$ and $k[A]$ are nonempty DLOs without endpoints. Then

$$
A\cong A^*.
$$

*Proof.*
On the same carrier define

$$
R=A+M+k[A]^*,
\qquad
S=A^*+M+k[A].
$$

The displayed decomposition of $P$ makes $M$ convex; if it has at least two points, it is therefore internally dense. After empty blocks are omitted, every reduced boundary is dense because the flank on the required side has no endpoint. Hence the finite block-sum criterion makes $R$ and $S$ DLOs.

The map $k$ reverses the block order. On the reversed right flank, for example,

$$
x<_{k[A]^*}y
\quad\Longleftrightarrow\quad
y<_{k[A]}x
\quad\Longleftrightarrow\quad
k(x)<_A k(y)
\quad\Longleftrightarrow\quad
k(y)<_{A^*}k(x).
$$

The other blocks and mixed comparisons are immediate from $k[M]=M$ and the fact that $k$ reverses $P$. Thus $k:R\to S$ is an anti-isomorphism, and

$$
R^*\cong S.
$$

Every DLO on $X$ is self-dual, hence

$$
R\cong R^*\cong S.
$$

Under an isomorphism $R\to S$, the image of the initial block $A$ is an initial segment of type $A$, while the literal first block of $S$ is an initial segment of type $A^*$. Corollary 2.7 gives $A\cong A^*$. ∎

<div id="prop:3-7-all-selfdual-dichotomy"></div>

**Proposition 3.7 (All-self-dual rigid carrier dichotomy).**
Assume every DLO on $X$ is self-dual and let $L$ be a rigid DLO on $X$. Then

$$
X\hookrightarrow\omega
\quad\text{or}\quad
\omega\hookrightarrow X.
$$

*Proof.*
Choose a reversal $h$ of $L$. By rigidity it is unique and involutive. [Lemma B.1](#lem:b-1-reflection-split) gives the convex decomposition

$$
X=H+F_h+h[H],
$$

where $H$ and $h[H]$ are nonempty DLOs without endpoints and $F_h$ is empty or a singleton. Lemma 3.6, applied with $A=H$ and $M=F_h$, gives

$$
H\cong H^*.
$$

The half $H$ is rigid because it is convex in the rigid order $L$. Thus the standing hypotheses of the type-count-free dyadic engine in [Appendix B](#app:dyadic-engine) are satisfied. [Corollary B.8](#cor:b-8-dyadic-dichotomy) yields

$$
X\hookrightarrow\omega
\quad\text{or}\quad
\omega\hookrightarrow X.
$$

∎

<div id="thm:3-8-residual-normal-form"></div>

**Theorem 3.8 (Exact-two residual normal form).**
If $s(X)=2$, then:

1. $X\nhookrightarrow\omega$;
2. $\omega\nhookrightarrow X$;
3. every DLO on $X$ is rigid;
4. reversal exchanges the two types;
5. no DLO on $X$ is self-dual;
6. after naming one representative $L$, the spectrum is

   $$
   \{[L],[L^*]\},
   \qquad
   L\not\cong L^*.
   $$ {#eq:exact-two-residual}

*Proof.*
The first three assertions are Lemmas 3.1–3.3. If $\sigma=\operatorname{id}_2$, then every DLO on $X$ is self-dual: if $U\cong L_i$, then

$$
U^*\cong L_i^*\cong L_i\cong U.
$$

Choosing either rigid representative and applying Proposition 3.7 gives $X\hookrightarrow\omega$ or $\omega\hookrightarrow X$, contradicting Lemmas 3.1 and 3.2. Hence $\sigma=(01)$. A self-dual DLO would represent a fixed point of $\sigma$, so none exists. The final description follows. ∎

<div id="sec:cut-square"></div>

## 4. The one-point cut square

Fix the representative

$$
L=(X,<)
$$

from Theorem 3.8.

<div id="def:4-1-cut-square"></div>

**Definition 4.1 (The antipodal cut square).**
For $c\in X$, put

$$
A_c:=(-\infty,c)_L,
\qquad
B_c:=(c,\infty)_L.
$$

Define four relations on the carrier $X$ by

$$
\mathcal C_{00}^c
=
A_c+\{c\}+B_c,
$$

$$
\mathcal C_{01}^c
=
A_c^*+\{c\}+B_c^*,
$$

$$
\mathcal C_{10}^c
=
B_c+\{c\}+A_c,
$$

and

$$
\mathcal C_{11}^c
=
B_c^*+\{c\}+A_c^*.
$$

We display the square as

$$
\begin{matrix}
\mathcal C_{00}^c & \mathcal C_{10}^c\\
\mathcal C_{01}^c & \mathcal C_{11}^c.
\end{matrix}
$$

Thus the vertical edges are $\mathcal C_{00}^c$--$\mathcal C_{01}^c$ and $\mathcal C_{10}^c$--$\mathcal C_{11}^c$, while the horizontal edges are $\mathcal C_{00}^c$--$\mathcal C_{10}^c$ and $\mathcal C_{01}^c$--$\mathcal C_{11}^c$.

The order $\mathcal C_{10}^c$ is the **cut rotation** of $L$ at $c$ and is denoted

$$
\operatorname{Rot}_c(L).
$$ {#eq:cut-rotation}

<div id="lem:4-2-cut-square-actual"></div>

**Lemma 4.2 (The cut square is actual and antipodal).**
For every $c\in X$, all four relations in Definition 4.1 are DLOs on $X$. Moreover,

$$
\mathcal C_{11}^c
=
(\mathcal C_{00}^c)^*,
\qquad
\mathcal C_{10}^c
=
(\mathcal C_{01}^c)^*.
$$ {#eq:cut-square-antipodal}

*Proof.*
Each strict ray of a DLO is a convex DLO without endpoints. Reversing a ray preserves this property. Inserting one singleton between two endpointless DLO blocks satisfies the finite block-sum criterion. Each displayed relation is defined by Separation on $X\times X$. Reversing the block lists gives the two identities. ∎

<div id="lem:4-3-antipodal-coloring"></div>

**Lemma 4.3 (Antipodal two-color square).**
Color the four vertices of a $2\times2$ square with two colors. If antipodal vertices have opposite colors, then either both vertical edges are monochromatic or both horizontal edges are monochromatic.

*Proof.*
Fix the color of the upper-left vertex. The lower-right vertex has the other color. The upper-right vertex has one of the two colors, and the lower-left vertex, being antipodal to it, has the other. The two possible choices give the two conclusions. ∎

<div id="lem:4-4-selfdual-amalgamation"></div>

**Lemma 4.4 (Two rigid self-dual DLOs and one point self-dualize their union).**
Let $A$ and $B$ be disjoint carriers of rigid self-dual DLOs, and let $c\notin A\cup B$. Then $A\sqcup\{c\}\sqcup B$ carries a self-dual DLO.

*Proof.*
Let $r_A$ and $r_B$ be the unique reversals. By rigidity they are involutions. [Lemma B.1](#lem:b-1-reflection-split) shows that the two reflection halves of each order are nonempty DLOs without endpoints and that each fixed-point set is empty or a singleton. Put

$$
A^-:=\{a:a<r_A(a)\},
\qquad
A^+:=\{a:r_A(a)<a\},
$$

$$
F_A:=\{a\in A:r_A(a)=a\},
$$

and define $B^-,B^+$ and $F_B$ analogously. The two halves in each pair are exchanged by the relevant reversal.

Put

$$
F:=F_A\sqcup F_B\sqcup\{c\}.
$$

Map a point of $F_A$ to $0$, the point $c$ to $1$, and a point of $F_B$ to $2$. Because the three pieces are disjoint and the two fixed-point sets are empty or singletons, this is an injection $F\to3$. Finite ranking [Isthmus 2026a, Lemma 2.8](#ref:isthmus2026a) therefore gives an enumeration

$$
F=\{z_0,\ldots,z_{t-1}\},
\qquad
1\le t\le3.
$$

Give the carrier one of the following block orders:

$$
A^-+B^-+\{z_0\}+B^++A^+
\qquad(t=1),
$$

$$
A^-+\{z_0\}+B^-+B^++\{z_1\}+A^+
\qquad(t=2),
$$

or

$$
A^-+\{z_0\}+B^-+\{z_1\}+B^++\{z_2\}+A^+
\qquad(t=3).
$$

Every displayed order is a DLO: it starts and ends with endpointless DLO blocks, and no two singleton blocks are adjacent. Define

$$
h
=
\bigl(r_A\restriction(A^-\cup A^+)\bigr)
\cup
\bigl(r_B\restriction(B^-\cup B^+)\bigr)
\cup
\{(z_i,z_{t-1-i}):i<t\}.
$$ {#eq:selfdual-amalgamation-map}

The three domains in this union are disjoint, so $h$ is a function. Each restricted reversal is involutive, and $i\mapsto t-1-i$ is an involution on $t$; hence

$$
h^2=\operatorname{id}_{A\sqcup\{c\}\sqcup B}.
$$

In particular, $h$ is bijective. It reverses the entire block list and every internal block order, so it is an order reversal of the constructed DLO. Hence that DLO is self-dual. ∎

<div id="thm:4-5-vertical-exclusion"></div>

**Theorem 4.5 (A vertical monochromatic cut edge is impossible).**
Under the residual normal form of Theorem 3.8, the two DLOs

$$
\mathcal C_{00}^c
\quad\text{and}\quad
\mathcal C_{01}^c
$$

are nonisomorphic for every $c\in X$.

*Proof.*
Suppose

$$
f:\mathcal C_{00}^c\longrightarrow\mathcal C_{01}^c
$$

were an isomorphism.

If $f(c)<_{\mathcal C_{01}^c}c$, then $f(c)\in A_c$ and

$$
f[A_c]
=
(-\infty,f(c))_{\mathcal C_{01}^c}
=
\{x\in A_c:f(c)<_Lx<c\}
\subsetneq
A_c.
$$

The inclusion is proper because $f(c)\in A_c$ but $f(c)\notin f[A_c]$. This is a set-theoretic statement; the target happens to carry the reversed order on that subset. Thus $f\upharpoonright A_c$ is an injective nonsurjective selfmap of $A_c$, contradicting Lemma 3.4.

If $c<_{\mathcal C_{01}^c}f(c)$, then $f(c)\in B_c$ and

$$
f[B_c]
=
(f(c),\infty)_{\mathcal C_{01}^c}
=
\{x\in B_c:c<x<_L f(c)\}
\subsetneq
B_c,
$$

where the inclusion is proper because $f(c)\in B_c\setminus f[B_c]$. This gives the same contradiction. Therefore

$$
f(c)=c.
$$

It follows that $f[A_c]=A_c$ and $f[B_c]=B_c$. Since the target order reverses the inherited order on each ray, the restrictions of $f$ are order reversals of the original DLOs on $A_c$ and $B_c$. These ray orders are rigid by Lemma 2.8 because they are convex in the rigid order $L$. Lemma 4.4 therefore constructs a self-dual DLO on $X$, contradicting Theorem 3.8. ∎

<div id="thm:4-6-cut-rotation-type"></div>

**Theorem 4.6 (Every cut rotation has the original type).**
For every $c\in X$,

$$
\operatorname{Rot}_c(L)
\cong
L.
$$ {#eq:all-cut-rotations}

The isomorphism is unique.

*Proof.*
Color each corner $\mathcal C_{ij}^c$ by the unique exact-two type it represents. By Theorem 3.8, reversal exchanges the two types. The antipodal identities in Lemma 4.2 therefore make antipodal corners opposite in color. Lemma 4.3 gives a monochromatic direction.

The vertical direction is impossible by Theorem 4.5. Hence both horizontal edges are monochromatic. In particular,

$$
\mathcal C_{00}^c
=
L
\cong
\mathcal C_{10}^c
=
\operatorname{Rot}_c(L).
$$

If $f,g:L\to\operatorname{Rot}_c(L)$ are two isomorphisms, then $g^{-1}\circ f$ is an increasing automorphism of the rigid order $L$. Thus $f=g$. ∎

<div id="sec:cut-preimage"></div>

## 5. The cut-preimage reversal

Throughout this section, let $L=(X,<)$ be a rigid DLO satisfying the following two hypotheses:

$$
(\mathrm{HDF})
\qquad
\forall Y\subseteq X\ \forall j:Y\to Y,
\bigl(j\text{ injective}\Longrightarrow j[Y]=Y\bigr),
$$ {#eq:hereditary-dedekind-finiteness}

and

$$
(\mathrm{Rot})
\qquad
\forall c\in X,
\operatorname{Rot}_c(L)\cong L.
$$ {#eq:rotation-hypothesis}

In the exact-two application, $(\mathrm{HDF})$ is Lemma 3.4 and $(\mathrm{Rot})$ is Theorem 4.6.

<div id="def:5-1-cut-preimage"></div>

**Definition 5.1 (The cut-preimage map).**
For a fixed $c\in X$, let

$$
\rho_c:
L
\longrightarrow
\operatorname{Rot}_c(L)
$$

be the unique isomorphism supplied by $(\mathrm{Rot})$ and rigidity. Define

$$
\delta(c):=\rho_c^{-1}(c).
$$ {#eq:cut-preimage}

The graph of $\delta$ is the Separation-defined subset of $X\times X$

$$
\left\{
\begin{aligned}
(c,d)\in X\times X:\;&
\exists r\in\mathcal P(X\times X)\ \text{such that}\\
&r\text{ is an order isomorphism }L\to\operatorname{Rot}_c(L),\\
&(d,c)\in r
\end{aligned}
\right\}.
$$ {#eq:cut-preimage-graph}

Rigidity gives uniqueness of $r$, and bijectivity of $r$ gives uniqueness of $d$. No set of all maps $\rho_c$ is formed.

<div id="lem:5-2-ray-exchange"></div>

**Lemma 5.2 (Cut rotations exchange opposite rays).**
Let $d=\delta(c)$. Then $\rho_c$ restricts to order isomorphisms

$$
(-\infty,d)_L
\cong
(c,\infty)_L
$$ {#eq:left-to-right-ray}

and

$$
(d,\infty)_L
\cong
(-\infty,c)_L.
$$ {#eq:right-to-left-ray}

*Proof.*
In the rotated order

$$
\operatorname{Rot}_c(L)
=
(c,\infty)_L+\{c\}+(-\infty,c)_L,
$$

the strict initial segment below $c$ is the original right ray and the strict final segment above $c$ is the original left ray. Since $\rho_c(d)=c$, an order isomorphism sends the two rays at $d$ to these two segments. ∎

<div id="lem:5-3-delta-injective"></div>

**Lemma 5.3 (The cut-preimage map is injective).**
The function $\delta:X\to X$ is injective.

*Proof.*
Suppose

$$
\delta(c)=\delta(e)=d
$$

with $c<e$. Put

$$
A:=(-\infty,d)_L,
\qquad
T_c:=(c,\infty)_L,
\qquad
T_e:=(e,\infty)_L.
$$

Lemma 5.2 gives isomorphisms

$$
\rho_c\upharpoonright A:A\to T_c,
\qquad
\rho_e\upharpoonright A:A\to T_e.
$$

Therefore

$$
T_c
\xrightarrow{\ (\rho_c\upharpoonright A)^{-1}\ }
A
\xrightarrow{\ \rho_e\upharpoonright A\ }
T_e
\hookrightarrow
T_c
$$

is an injective selfmap of $T_c$ with range exactly $T_e$. The inclusion is proper because

$$
e\in T_c\setminus T_e.
$$

This contradicts $(\mathrm{HDF})$. The case $e<c$ is symmetric. ∎

<div id="lem:5-4-delta-decreasing"></div>

**Lemma 5.4 (The cut-preimage map is strictly decreasing).**
If $c<e$, then

$$
\delta(e)<\delta(c).
$$ {#eq:delta-decreasing}

*Proof.*
Suppose instead that

$$
\delta(c)<\delta(e).
$$

Put

$$
I_c:=(-\infty,\delta(c))_L,
\qquad
I_e:=(-\infty,\delta(e))_L.
$$

Then

$$
I_c\subsetneq I_e,
$$

with

$$
\delta(c)\in I_e\setminus I_c.
$$

Meanwhile,

$$
(e,\infty)_L
\subsetneq
(c,\infty)_L.
$$

Using Lemma 5.2, form the composite

$$
I_e
\xrightarrow{\ \rho_e\ }
(e,\infty)_L
\hookrightarrow
(c,\infty)_L
\xrightarrow{\ \rho_c^{-1}\ }
I_c
\hookrightarrow
I_e.
$$ {#eq:proper-ray-selfmap}

This is an injective selfmap of $I_e$, and

$$
\operatorname{ran}(\Psi_{c,e})
=
\rho_c^{-1}[(e,\infty)_L]
\subseteq
I_c
\subsetneq
I_e,
$$ {#eq:proper-ray-selfmap-range}

where $\Psi_{c,e}$ denotes the displayed composite. Thus it is not surjective, contradicting $(\mathrm{HDF})$. Hence $\delta(c)\not<\delta(e)$. Lemma 5.3 excludes equality, so $\delta(e)<\delta(c)$. ∎

<div id="cor:5-5-delta-bijective"></div>

**Corollary 5.5 (The cut-preimage map is a decreasing bijection).**
The function $\delta:X\to X$ is bijective and strictly decreasing.

*Proof.*
It is injective by Lemma 5.3. Hypothesis $(\mathrm{HDF})$, applied to $Y=X$, makes every injective selfmap of $X$ surjective. Strict decrease is Lemma 5.4. ∎

<div id="thm:5-6-cut-rotation-selfduality"></div>

**Theorem 5.6 (Cut-rotation self-duality theorem).**
Let $L=(X,<)$ be a rigid DLO satisfying $(\mathrm{HDF})$ and $(\mathrm{Rot})$. Then

$$
L\cong L^*.
$$

*Proof.*
Rigidity makes every cut-rotation isomorphism unique, so Definition 5.1 gives the cut-preimage map. Lemmas 5.2–5.4 and Corollary 5.5 show that $\delta$ is a decreasing bijection of $X$. Hence, for all $x,y\in X$,

$$
x<_L y
\quad\Longleftrightarrow\quad
\delta(y)<_L\delta(x)
\quad\Longleftrightarrow\quad
\delta(x)<_{L^*}\delta(y).
$$ {#eq:delta-anti-isomorphism}

For the reverse implication in the first equivalence, suppose $\delta(y)<_L\delta(x)$. If $y<_Lx$, strict decrease gives $\delta(x)<_L\delta(y)$, while $x=y$ contradicts the assumed strict inequality. Trichotomy therefore gives $x<_Ly$. Hence $\delta$ is an order isomorphism from $L$ to $L^*$. ∎

<div id="sec:main-theorem"></div>

## 6. Exact-two exclusion

<div id="thm:6-1-main"></div>

**Theorem 6.1 (No exact-two DLO spectrum).**
$Z_{\mathrm{sep}}$ proves

$$
\neg\exists X\,(s(X)=2).
$$ {#eq:main-theorem}

*Proof.*
Assume $s(X)=2$. Theorem 3.8 gives a rigid representative $L$ satisfying

$$
L\not\cong L^*,
$$

Lemma 3.4 gives $(\mathrm{HDF})$, and Theorem 4.6 gives $(\mathrm{Rot})$. Theorem 5.6 therefore gives $L\cong L^*$, a contradiction. ∎

<div id="cor:6-2-two-three-gap"></div>

**Corollary 6.2 (No exact two or exact three).**
One has

$$
Z_{\mathrm{sep}}
\vdash
\neg\exists X\,
\bigl(
\operatorname{Spec}_{=2}(X)
\vee
\operatorname{Spec}_{=3}(X)
\bigr).
$$ {#eq:two-three-gap}

*Proof.*
The exact-two case is Theorem 6.1. The exact-three case is [Isthmus 2026a, Theorem 6.3](#ref:isthmus2026a). ∎

<div id="cor:6-3-zf"></div>

**Corollary 6.3 (ZF consequence).**
ZF proves that no set carries exactly two DLO isomorphism types.

*Proof.*
ZF contains every axiom of $Z_{\mathrm{sep}}$. ∎

<div id="sec:scope"></div>

## 7. Scope and further questions

For each standard finite $n\ge2$, let $(\mathrm{FS})_n$ denote the metatheoretic assertion

$$
Z_{\mathrm{sep}}
\vdash
\neg\exists X\,
\operatorname{Spec}_{=n}(X).
$$

The present paper and its exact-three companion prove $(\mathrm{FS})_2$ and $(\mathrm{FS})_3$. They do not prove $(\mathrm{FS})_n$ for $n\ge4$.

The exact-two mechanism is specific to a two-color antipodal square. Once reversal is known to exchange the two types, opposite cut-square corners have opposite colors, and one of the two edge directions is forced to be monochromatic. Vertical monochromaticity is incompatible with the absence of self-dual types, so every cut rotation has the original type. For larger spectra, a four-corner cut square need not force any same-type edge, and the argument stops before the cut-preimage map can be defined globally.

Theorem 5.6 is independent of finite spectrum language. It says that a rigid DLO on a hereditarily Dedekind-finite carrier cannot be isomorphic to all of its one-point cut rotations unless it is self-dual. This cut-rotation rigidity principle may be useful in other choiceless classification problems.

The present methods do not decide whether any standard finite spectrum of size at least four can occur, or which such spectra are consistent. The countable-benchmark theorem gives only the lower bound $s(X)\ge4$ on a non-subcountable Dedekind-infinite carrier; that bound does not exclude exact four or any larger finite value.

<div id="app:weak-audit"></div>

## Appendix A. Weak-theory audit of the new construction

<div id="prop:a-1-cut-relations"></div>

**Proposition A.1 (Uniform formation of the cut rotations).**
For each $c\in X$, the graph of $\operatorname{Rot}_c(L)$ is a set obtained by Separation on $X\times X$.

*Proof.*
For $x,y\in X$, the relation $x<_{\operatorname{Rot}_c(L)}y$ is the finite disjunction saying that either:

1. $c<x<y$ in $L$;
2. $c<x$ and $y=c$;
3. $c<x$ and $y<c$;
4. $x=c$ and $y<c$;
5. $x<y<c$ in $L$.

This formula defines the block order

$$
(c,\infty)_L+\{c\}+(-\infty,c)_L
$$

inside the fixed set $X\times X$. ∎

<div id="prop:a-2-cut-table"></div>

**Proposition A.2 (The finite type table requires no Choice).**
For a fixed $c$, assigning to each of the four cut-square relations its unique exact-two representative is a finite set construction in $Z_{\mathrm{sep}}$.

*Proof.*
The four relations form a set by Pairing and Union. For each relation, exactness gives a unique index in $2$. The graph of the assignment is the Separation subset of the finite product $4\times2$ satisfying the internal isomorphism predicate. No choice from an infinite family is involved. ∎

<div id="prop:a-3-delta-graph"></div>

**Proposition A.3 (The cut-preimage graph uses no Replacement).**
The graph in Equation [\eqref{eq:cut-preimage-graph}](#eq:cut-preimage-graph) is a set in $Z_{\mathrm{sep}}$.

*Proof.*
Every candidate is a pair in the fixed set $X\times X$, and every candidate isomorphism is an element of the fixed power set $\mathcal P(X\times X)$. The formula in Equation [\eqref{eq:cut-preimage-graph}](#eq:cut-preimage-graph) therefore defines the graph by Separation. Uniqueness turns it into a function. At no point is the range

$$
\{\rho_c:c\in X\}
$$

formed. ∎

<div id="prop:a-4-composites"></div>

**Proposition A.4 (The ray composites are internal maps).**
Every restriction, inverse, inclusion, and finite composite used in Lemmas 5.3 and 5.4 is an internal set.

*Proof.*
Restrictions and inclusions are Separation-defined subsets of $X\times X$. The inverse of a bijection is obtained by reversing ordered pairs. The graph of a composite of two maps is defined by an existential formula on the appropriate fixed Cartesian product. Only finitely many maps are composed in each argument, so Pairing, Union, products, and Separation suffice. ∎


<div id="app:dyadic-engine"></div>

## Appendix B. A type-count-free dyadic reflection engine

This appendix isolates the reflection-tree mechanism needed in Proposition 3.7. It is parameterized by self-duality inputs rather than by an exact finite spectrum. In addition to the standing infrastructure recorded in [§2](#sec:formal-setting), it uses Lemma 2.8 and Lemma 3.6. Its remaining imported inputs are elementary foundational lemmas from the exact-three companion: finite ranking, finite unions of subcountable sets, explicit binary-word coding, and internally finite block sums [Isthmus 2026a, Lemmas 2.8, 3.4(1), B.3, and Proposition B.5](#ref:isthmus2026a). No result whose statement assumes $s(X)=3$ is used below.

To keep word sets distinct from finite ordinals, write

$$
\operatorname{Bin}_{<\omega}
:=
2^{<\omega},
\qquad
\operatorname{Bin}_n
:=
\{s\in\operatorname{Bin}_{<\omega}:|s|=n\},
$$

$$
\operatorname{Bin}_{<n}
:=
\{s\in\operatorname{Bin}_{<\omega}:|s|<n\},
\qquad
\operatorname{Bin}_{\le n}
:=
\{s\in\operatorname{Bin}_{<\omega}:|s|\le n\},
$$

and let

$$
N_n:=2^n.
$$

Here the right-hand side is the finite ordinal obtained by exponentiation, so $N_n\in\omega$. We use the explicit bijections

$$
v_n:\operatorname{Bin}_n\longrightarrow N_n
$$

and

$$
c_n:\operatorname{Bin}_{<n}\longrightarrow N_n-1
$$

from [Isthmus 2026a, Lemma B.3](#ref:isthmus2026a).

<div id="lem:b-1-reflection-split"></div>

**Lemma B.1 (Geometry of one reflection split).**
Let $I$ be a nonempty rigid self-dual DLO and let $r$ be its unique reversal. Put

$$
I_0:=\{x\in I:x<r(x)\},
$$

$$
I_1:=\{x\in I:r(x)<x\},
$$

and

$$
F_r:=\{x\in I:r(x)=x\}.
$$

Then:

1. $r$ is involutive;
2. $F_r$ is empty or a singleton;
3. $I_0$ and $I_1$ are nonempty proper convex DLOs without endpoints;
4. $I=I_0\sqcup F_r\sqcup I_1$;
5. $r$ anti-isomorphically exchanges $I_0$ and $I_1$.

*Proof.*
Lemma 2.8 gives involutivity. An order reversal has at most one fixed point: if $x<y$ were both fixed, reversal would give $y=r(y)<r(x)=x$. The two strict-inequality sets are respectively initial and final, are convex, and are exchanged by $r$.

They are nonempty because $r$ cannot fix every point of a nontrivial strict order, by the same two-point argument. To show that $I_0$ has no greatest point, take $x\in I_0$ and choose

$$
x<z_1<z_2<r(x).
$$

At most one of $z_1,z_2$ is fixed by $r$, so choose a nonfixed $z$.

- If $z<r(z)$, then $z\in I_0$ and $x<z$.
- If $r(z)<z$, reversing $z<r(x)$ gives $x<r(z)$, and $r(z)\in I_0$.

The remaining endpoint statements are symmetric or follow from initiality and finality. Density is inherited from convexity, and trichotomy gives the displayed decomposition. ∎

<div id="lem:b-2-singleton-placement"></div>

**Lemma B.2 (Sharp singleton placement).**
Let $q\ge1$. Let $C_0,\ldots,C_{q-1}$ be nonempty DLO blocks without endpoints and let $z_0,\ldots,z_{t-1}$ be singleton blocks. If $t\le q$, the order

$$
z_0+C_0+z_1+C_1+\cdots+z_{t-1}+C_{t-1}
+C_t+\cdots+C_{q-1}
$$ {#eq:typefree-singleton-placement}

with the initial alternating part omitted when $t=0$ and the final tail omitted when $t=q$, has no greatest point and contains no adjacent singleton blocks.

If $t=q+1$, no ordering of the $q$ DLO blocks and the $t$ singleton blocks can simultaneously avoid adjacent singletons and avoid a singleton final block.

*Proof.*
The displayed arrangement proves the first assertion. For the second, $q$ nonsingleton blocks provide at most $q$ separators between singleton blocks. Accommodating $q+1$ singleton blocks without adjacency forces the alternating pattern to begin and end with a singleton. ∎

For the rest of the appendix, fix a rigid DLO $L=(X,<)$ with an involutive reversal $h$, and write

$$
X=H+F_h+h[H]
$$ {#eq:typefree-root-decomposition}

as in Lemma B.1. Assume that $H$ is self-dual and that every DLO on $X$ is self-dual.

<div id="lem:b-3-child-localization"></div>

**Lemma B.3 (All-self-dual finite localization).**
Let $n<\omega$. Suppose that:

1. $H$ is partitioned into cells $(I_s)_{s\in\operatorname{Bin}_n}$ and a center set $P_{<n}$;
2. every $I_s$ is a nonempty convex rigid self-dual DLO;
3. there is an injective tag map

   $$
   \tau_n:P_{<n}\longrightarrow\operatorname{Bin}_{<n}.
   $$

For each $s\in\operatorname{Bin}_n$, let $r_s$ be the unique reversal of $I_s$ and put

$$
F_s:=\{x\in I_s:r_s(x)=x\}.
$$

Split $I_s$ by $r_s$, and, when $F_s$ is nonempty, tag its unique point by $s\in\operatorname{Bin}_n$. Then every resulting level-$(n+1)$ child cell $D$ satisfies

$$
D\cong D^*.
$$ {#eq:typefree-child-selfdual}

*Proof.*
The child cells are indexed by $\operatorname{Bin}_{n+1}$. Old center tags lie in $\operatorname{Bin}_{<n}$ and new center tags lie in $\operatorname{Bin}_n$. Old centers lie outside every level-$n$ cell, while a new center lies inside its parent cell; new centers from distinct parents lie in disjoint cells. Hence the combined tag assignment is injective into $\operatorname{Bin}_{<n+1}$.

Let $d\in\operatorname{Bin}_{n+1}$ index the target cell $D$, put $a=v_{n+1}(d)$, and define

$$
\rho(s)
=
\begin{cases}
 v_{n+1}(s),&v_{n+1}(s)<a,\\
 v_{n+1}(s)-1,&a<v_{n+1}(s).
\end{cases}
$$

Then

$$
\rho:
\{s\in\operatorname{Bin}_{n+1}:s\ne d\}
\longrightarrow
q,
\qquad
q:=N_{n+1}-1,
$$ {#eq:typefree-remaining-cell-ranking}

is a bijection. Thus the other child cells have a canonical enumeration

$$
C_0,\ldots,C_{q-1}.
$$

Composing the center tags with $c_{n+1}:\operatorname{Bin}_{<n+1}\to q$ injects the total center set into $q$. Finite ranking [Isthmus 2026a, Lemma 2.8](#ref:isthmus2026a) therefore gives some $t\le q$ and an enumeration

$$
z_0,\ldots,z_{t-1}
$$

of all accumulated center points. Lemma B.2 gives a block order $W_D$ on $H\setminus D$ in which every center is followed by a DLO cell and the final block is a DLO:

$$
W_D
=
z_0+C_0+\cdots+z_{t-1}+C_{t-1}
+C_t+\cdots+C_{q-1}.
$$ {#eq:typefree-localized-complement}

Here the initial alternating part is omitted when $t=0$, and the final tail is omitted when $t=q$. As sets,

$$
H=D\sqcup W_D,
\qquad
X=D\sqcup W_D\sqcup F_h\sqcup h[W_D]\sqcup h[D].
$$ {#eq:typefree-localized-carrier-partition}

The combined tag graph is the union of the old tag map with the Separation-defined graph

$$
\{(x,s)\in H\times\operatorname{Bin}_n:x\in F_s\},
$$

and the enumeration $i\mapsto C_i$ is the Separation-defined subset of $q\times\mathcal P(H)$ determined by $\rho$. Here and below, $W_D$ denotes both the displayed ordered block sum and its carrier $H\setminus D$.

Let

$$
\mathfrak B_D\subseteq(q+t)\times\mathcal P(H)
$$

be the graph of the displayed block family, and let

$$
\mathfrak R_D\subseteq(q+t)\times\mathcal P(H\times H)
$$

be the graph assigning to each singleton block the empty relation and to each cell block $C_i$ its order inherited from $L$. Both graphs are formed by Separation from the two finite enumerations. Applying [Isthmus 2026a, Proposition B.5](#ref:isthmus2026a) to $(\mathfrak B_D,\mathfrak R_D)$ yields the graph of the internally finite block-sum order $W_D$.

Give $D$ and $h[D]$ their orders inherited from $L$. Give $h[W_D]$ the mirror order

$$
u<_{h[W_D]}v
\quad\Longleftrightarrow\quad
h(v)<_{W_D}h(u).
$$ {#eq:typefree-mirror-order}

Put

$$
M_D:=W_D+F_h+h[W_D]
$$

and

$$
L_D:=D+M_D+h[D].
$$ {#eq:typefree-localized-order}

After empty blocks are omitted, the following list covers every boundary.

| Boundary | Range | Reason for density |
| --- | --- | --- |
| $D\mid z_0$ | $t>0$ | $D$ has no greatest point |
| $D\mid C_0$ | $t=0$ | $D$ has no greatest point |
| $z_i\mid C_i$ | $0\le i<t$ | $C_i$ has no least point |
| $C_i\mid z_{i+1}$ | $0\le i<t-1$ | $C_i$ has no greatest point |
| $C_j\mid C_{j+1}$ | $0\le j<q-1$ if $t=0$; $t-1\le j<q-1$ if $0<t<q$; none if $t=q$ | $C_j$ has no greatest point |
| $W_D\mid F_h$ | $F_h\ne\varnothing$ | $W_D$ has no greatest point |
| $F_h\mid h[W_D]$ | $F_h\ne\varnothing$ | $h[W_D]$ has no least point |
| $W_D\mid h[W_D]$ | $F_h=\varnothing$ | $W_D$ has no greatest point and $h[W_D]$ has no least point |
| internal mirror boundaries | all corresponding indices | duals of the preceding internal cases |
| $h[W_D]\mid h[D]$ | always | $h[D]$ has no least point |

The first block $D$ has no least point and the last block $h[D]$ has no greatest point. Hence the finite block-sum criterion makes $L_D$ a DLO on the same carrier $X$.

The map $h$ reverses $L_D$, exchanges $D$ with $h[D]$, and satisfies

$$
h[M_D]=M_D.
$$

Every DLO on $X$ is self-dual, so Lemma 3.6 applies to

$$
L_D=D+M_D+h[D]
$$

and gives $D\cong D^*$. ∎

<div id="def:b-4-level-state"></div>

**Definition B.4 (Complete dyadic level states).**
Put

$$
U_H
:=
\operatorname{Bin}_{<\omega}
\times
\mathcal P(H)
\times
\mathcal P(H\times H)
\times
\mathcal P(H).
$$ {#eq:typefree-tree-record-space}

A record $(s,I,r,F)\in U_H$ consists of a node, a cell, a reversal graph, and its fixed-point set.

For $n<\omega$, a subset $\mathcal S\subseteq U_H$ is a **valid level-$n$ state** if:

1. for every $s\in\operatorname{Bin}_{\le n}$, exactly one record $(s,I_s,r_s,F_s)$ belongs to $\mathcal S$, and no record with longer node belongs to $\mathcal S$;
2. $I_\varnothing=H$;
3. $r_s$ is the unique reversal of $I_s$, and

   $$
   F_s=\{x\in I_s:r_s(x)=x\};
   $$

4. for $|s|<n$,

   $$
   I_{s0}=\{x\in I_s:x<r_s(x)\},
   $$

   $$
   I_{s1}=\{x\in I_s:r_s(x)<x\};
   $$

5. every $I_s$ is nonempty, convex in $L$, rigid, self-dual, and a DLO;
6. for every $k\le n$,

   $$
   H
   =
   \left(\bigsqcup_{|s|=k}I_s\right)
   \sqcup
   P_{<k},
   $$ {#eq:typefree-level-partition}

   where

   $$
   P_{<k}
   :=
   \{x\in H:\exists s\ (|s|<k\text{ and }x\in F_s)\},
   $$

   and there is an injection

   $$
   P_{<k}\longrightarrow N_k-1.
   $$

Write $\operatorname{Valid}_H(n,\mathcal S)$ for the conjunction of these clauses.

<div id="thm:b-5-tree-actualization"></div>

**Theorem B.5 (Type-count-free dyadic actualization).**
For every $n<\omega$, there is a unique valid level-$n$ state $\mathcal S_n$. The states are coherent under restriction, and the complete tree

$$
\mathcal T_H
:=
\left\{
 u\in U_H:
 \exists n\in\omega\,
 \exists\mathcal S\in\mathcal P(U_H)\,
 \bigl(
  \operatorname{Valid}_H(n,\mathcal S)
  \wedge
  u\in\mathcal S
 \bigr)
\right\}
$$ {#eq:typefree-complete-tree}

is a set in $Z_{\mathrm{sep}}$.

*Proof.*
For $n=0$, the standing hypotheses make $H$ rigid and self-dual. Its reversal and fixed-point set are unique, so $\mathcal S_0$ exists uniquely.

Assume $\mathcal S_n$ exists uniquely. Every old center has a unique node tag: a point in $F_s$ belongs to neither child of $s$ and hence to no descendant cell, while cells at incomparable nodes lie in disjoint branches. Since each $F_s$ is empty or a singleton, the map

$$
P_{<n}\longrightarrow\operatorname{Bin}_{<n},
\qquad
x\longmapsto\text{the unique }s\text{ with }x\in F_s,
$$ {#eq:typefree-old-center-tags}

is injective.

Lemma B.1 determines the two geometric children of every level-$n$ cell. Lemma B.3, applied with the preceding tag map, makes every child self-dual. Each child is convex in $L$ and therefore rigid by Lemma 2.8. Its reversal and fixed-point set are consequently unique.

For $u\in U_H$, let $\operatorname{Old}_{\mathcal S_n}(u)$ mean $u\in\mathcal S_n$. Let $\operatorname{New}_{\mathcal S_n}(u)$ mean that

$$
u=(s,I,r,F),
\qquad
s=t^\frown\varepsilon,
\qquad
|t|=n,
\qquad
\varepsilon\in2,
$$

there is a parent record $(t,I_t,r_t,F_t)\in\mathcal S_n$, and:

- if $\varepsilon=0$, then $I=\{x\in I_t:x<r_t(x)\}$;
- if $\varepsilon=1$, then $I=\{x\in I_t:r_t(x)<x\}$;
- $r$ is the unique reversal of $I$;
- $F=\{x\in I:r(x)=x\}$.

Put

$$
\mathcal S_{n+1}
=
\{u\in U_H:
\operatorname{Old}_{\mathcal S_n}(u)
\vee
\operatorname{New}_{\mathcal S_n}(u)\}.
$$ {#eq:typefree-successor-state}

This is a Separation-defined subset of the fixed set $U_H$.

Tag old centers by their old nodes and a possible new center of $I_s$ by $s\in\operatorname{Bin}_n$. This gives an injection

$$
P_{<n+1}\longrightarrow\operatorname{Bin}_{<n+1}\xrightarrow{\ c_{n+1}\ }N_{n+1}-1.
$$

Clauses 1--5 of Definition B.4 hold by construction. For $k\le n$, the partition and center bound are inherited from $\mathcal S_n$. For $k=n+1$, Lemma B.1 partitions every parent into its two children and possible fixed point, while the displayed tag injection gives the required bound. Hence clause 6 holds as well. The geometric children are uniquely determined, and rigidity makes their reversals and fixed-point sets unique, so $\mathcal S_{n+1}$ is the unique valid level-$(n+1)$ state.

If $m>n$, the restriction of any valid level-$m$ state to nodes of length at most $n$ is a valid level-$n$ state and hence equals $\mathcal S_n$. Thus the states are coherent. Finally, $\operatorname{Valid}_H(n,\mathcal S)$ is a formula on the fixed set $\omega\times\mathcal P(U_H)$, and the displayed definition of $\mathcal T_H$ is Separation on $U_H$; no Replacement-generated range is formed. ∎

<div id="lem:b-6-center-countability"></div>

**Lemma B.6 (The center set is at most countable).**
Define

$$
Z_H
:=
\{x\in H:\exists(s,I,r,F)\in\mathcal T_H\ (x\in F)\}.
$$ {#eq:typefree-center-set}

Then

$$
Z_H\hookrightarrow\operatorname{Bin}_{<\omega}\hookrightarrow\omega.
$$ {#eq:typefree-center-countable}

*Proof.*
Every center belongs to $F_s$ for a unique node $s$: centers are excluded from all descendant cells, and incomparable nodes lie in disjoint cells. Two centers with the same tag lie in the empty-or-singleton set $F_s$ and are equal. Thus $x\mapsto s$ is an injection obtained by Separation from $H\times\operatorname{Bin}_{<\omega}$. The explicit finite-word code of [Isthmus 2026a, Lemma B.3](#ref:isthmus2026a) gives $\operatorname{Bin}_{<\omega}\hookrightarrow\omega$. ∎

<div id="thm:b-7-off-center"></div>

**Theorem B.7 (An off-center point generates an injective sequence).**
Let $x\in H\setminus Z_H$. For every $n$, let $s_n$ be the unique word of length $n$ whose cell contains $x$, and put

$$
y_n:=r_{s_n}(x).
$$ {#eq:typefree-off-center-sequence}

Then $n\mapsto y_n$ is an injection $\omega\hookrightarrow X$.

*Proof.*
The level partition and $x\notin Z_H$ give the unique cell $I_{s_n}$. Since $x$ is not fixed by $r_{s_n}$, the points $x$ and $y_n$ lie in opposite children. The next chosen cell $I_{s_{n+1}}$ is the child containing $x$, so

$$
y_n\notin I_{s_{n+1}}.
$$

If $m>n$, then

$$
y_m\in I_{s_m}\subseteq I_{s_{n+1}},
$$

and hence $y_m\ne y_n$.

The graph is the Separation-defined subset of $\omega\times X$

$$
G_x
:=
\left\{
(n,y)\in\omega\times X:
\exists s,I,r,F\,
\left[
\begin{aligned}
 &(s,I,r,F)\in\mathcal T_H,\\
 &|s|=n,\ x\in I,\ (x,y)\in r
\end{aligned}
\right]
\right\}.
$$ {#eq:typefree-off-center-graph}

Coherence and record uniqueness make $G_x$ a function, and the preceding argument makes it injective. ∎

<div id="cor:b-8-dyadic-dichotomy"></div>

**Corollary B.8 (Type-count-free rigid carrier dichotomy).**
Under the standing hypotheses of this appendix,

$$
X\hookrightarrow\omega
\quad\text{or}\quad
\omega\hookrightarrow X.
$$ {#eq:typefree-rigid-dichotomy}

*Proof.*
If $H\hookrightarrow\omega$, then $h[H]\hookrightarrow\omega$ and $F_h$ is empty or a singleton. The finite-union coding of [Isthmus 2026a, Lemma 3.4(1)](#ref:isthmus2026a) gives

$$
X=H+F_h+h[H]\hookrightarrow\omega.
$$

If $H\nhookrightarrow\omega$, Lemma B.6 implies $H\ne Z_H$. Choose one point in $H\setminus Z_H$ and apply Theorem B.7. ∎

<div id="sec:ai-disclosure"></div>

## AI-use disclosure {.unnumbered .unlisted}

AI systems were used extensively in an iterative, human-directed workflow for exploratory proof development, counterexample search, drafting, and adversarial review. The author set the research objectives, decided which candidate arguments to retain or reject, reviewed and approved the final manuscript, and takes responsibility for all mathematical claims and any remaining errors. AI systems are tools, not authors.

<div id="sec:references"></div>

## References

<div id="ref:ervin2017"></div>

- **Ervin 2017.** Garrett Ervin. “Every Linear Order Isomorphic to Its Cube Is Isomorphic to Its Square.” *Advances in Mathematics* 313 (2017): 237–281. DOI: 10.1016/j.aim.2017.04.010.

<div id="ref:howardrubin1998"></div>

- **Howard–Rubin 1998.** Paul Howard and Jean E. Rubin. *Consequences of the Axiom of Choice*. Mathematical Surveys and Monographs 59. American Mathematical Society, 1998.

<div id="ref:isthmus2026a"></div>

- **Isthmus 2026a.** Lior Isthmus. “No Set Carries Exactly Three Dense Linear Orders without Endpoints: A Proof in a Weak Zermelo Theory without Choice or Replacement.” Preprint, version `paper-rc6`, 2026. DOI: [10.5281/zenodo.21735262](https://doi.org/10.5281/zenodo.21735262). [GitHub](https://github.com/lioristhmus/no-exactly-three-dlo).

<div id="ref:isthmus2026b"></div>

- **Isthmus 2026b.** Lior Isthmus. *No Set Carries Exactly Three Dense Linear Orders without Endpoints: Lean 4 Formalization*. Software release. [GitHub](https://github.com/lioristhmus/no-exactly-three-dlo-lean). DOI: [10.5281/zenodo.21729423](https://doi.org/10.5281/zenodo.21729423).

<div id="ref:jech1973"></div>

- **Jech 1973.** Thomas J. Jech. *The Axiom of Choice*. Studies in Logic and the Foundations of Mathematics 75. North-Holland, 1973.

<div id="ref:marker2002"></div>

- **Marker 2002.** David Marker. *Model Theory: An Introduction*. Graduate Texts in Mathematics 217. Springer, 2002.

<div id="ref:shelah2009"></div>

- **Shelah 2009.** Saharon Shelah. “Model Theory without Choice? Categoricity.” *The Journal of Symbolic Logic* 74, no. 2 (2009): 361–401. arXiv:math/0504196. DOI: 10.2178/jsl/1243948319.
