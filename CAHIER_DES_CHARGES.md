# Quill pour Google Chrome — Cahier des charges

| | |
|---|---|
| **Projet** | Quill Chrome (portage navigateur de Quill pour Thunderbird) |
| **Version du document** | 1.0 — 21/11/2026 |
| **Version logicielle visée** | v0.1 (MVP) → v1.0 |
| **Éditeur** | Supersonique Studio SARL |
| **Licence** | GPL-3.0 (identique à Quill Thunderbird) |

---

## 1. Contexte et objectifs

Quill est aujourd'hui une extension Thunderbird qui apporte l'assistance IA (Claude, OpenAI, OVHcloud AI Endpoints, Ollama) dans la messagerie : résumé, traduction, correction, réponse, chat.

L'objectif est de proposer **la même brique IA dans Google Chrome**, sous forme de **panneau latéral droit** (API `chrome.sidePanel`), avec :

1. **Le chat Quill** accessible en permanence à côté de la page consultée.
2. **L'accès aux différents endpoints / fournisseurs** déjà supportés par Quill (mêmes clés, mêmes modèles, bascule rapide).
3. **La prise en compte de la page courante** (URL, titre, contenu, sélection) pour pouvoir « discuter avec la page » : la résumer, l'expliquer, la traduire, en extraire des informations.

### Objectifs mesurables

- Ouvrir le panneau et poser une question en **moins de 2 clics**.
- Résumer la page courante en **1 clic** (action rapide).
- Aucune donnée envoyée ailleurs qu'au fournisseur IA choisi par l'utilisateur (**zéro serveur Quill**).
- Fonctionner 100 % en local avec Ollama.

---

## 2. Périmètre

### Inclus

- Extension Chrome **Manifest V3** (compatible Chromium : Chrome, Edge, Brave, Opera, Vivaldi).
- Panneau latéral (side panel) : chat, contexte de page, actions rapides.
- Page d'options : configuration des fournisseurs, des modèles, des limites et de la langue.
- Menu contextuel (clic droit) sur la page et sur une sélection.
- Interface bilingue FR / EN (v0.1), puis les 8 langues de Quill Thunderbird.

### Exclu (hors périmètre)

- Compte utilisateur / synchronisation serveur Quill.
- Automatisation de la page (clics, remplissage de formulaires) — éventuellement étudié après la v1.0.
- Version Firefox (possible plus tard : Firefox supporte `sidebar_action`, le cœur sera partageable).

---

## 3. Utilisateurs et cas d'usage

| Profil | Cas d'usage |
|---|---|
| Professionnel | Résumer un article, un rapport, une page de documentation avant une réunion |
| Développeur | Expliquer un extrait de code ou une doc technique sélectionnée |
| Polyglotte | Traduire la page ou un passage dans sa langue |
| Utilisateur soucieux de confidentialité | Discuter avec la page via Ollama en local, ou OVHcloud (hébergement UE) |
| Rédacteur | Reformuler / corriger un texte sélectionné, puis le copier |

### Scénarios principaux

- **S1 — Chat libre** : clic sur l'icône Quill → le panneau s'ouvre → l'utilisateur discute avec le modèle actif.
- **S2 — Discuter avec la page** : le panneau affiche la page courante (titre + URL) ; l'interrupteur « Inclure la page » est actif ; l'utilisateur demande « Quels sont les chiffres clés ? » → la réponse s'appuie sur le contenu de la page.
- **S3 — Action rapide** : bouton « Résumer » → résumé structuré de la page.
- **S4 — Sélection** : l'utilisateur sélectionne un paragraphe, clic droit → « Quill : expliquer la sélection » → le panneau s'ouvre et répond.
- **S5 — Changement d'onglet** : le contexte affiché suit automatiquement l'onglet actif.
- **S6 — Changement de fournisseur** : sélecteur dans l'en-tête du panneau, sans passer par les options.

---

## 4. Exigences fonctionnelles

Priorités : **P0** = v0.1 (MVP), **P1** = v0.2–v0.5, **P2** = v1.0+.

### 4.1 Panneau latéral

| ID | Exigence | Prio |
|---|---|---|
| F-01 | Clic sur l'icône de l'extension = ouverture du panneau latéral droit | P0 |
| F-02 | Raccourci clavier d'ouverture (`Alt+Q` par défaut, modifiable dans `chrome://extensions/shortcuts`) | P0 |
| F-03 | En-tête : logo, sélecteur fournisseur/modèle actif, bouton « Nouvelle conversation », bouton « Options » | P0 |
| F-04 | Thème clair/sombre suivant le système | P0 |
| F-05 | Panneau utilisable dès 320 px de large | P0 |

### 4.2 Chat

| ID | Exigence | Prio |
|---|---|---|
| F-10 | Saisie multi-ligne, `Entrée` envoie, `Maj+Entrée` = retour à la ligne | P0 |
| F-11 | Historique de la conversation envoyé au modèle (contexte multi-tours) | P0 |
| F-12 | Rendu Markdown sûr des réponses (titres, gras, italique, listes, code, liens) — aucun HTML brut injecté | P0 |
| F-13 | Bouton « Copier » sur chaque réponse | P0 |
| F-14 | Indicateur de chargement ; en cas d'erreur, message clair et texte de la question restitué | P0 |
| F-15 | Conversation conservée pendant la session du navigateur (fermer/rouvrir le panneau ne la perd pas) | P0 |
| F-16 | Bouton « Stop » pour annuler une génération en cours | P1 |
| F-17 | Réponses en streaming (affichage progressif) | P1 |
| F-18 | Bouton « Régénérer » sur la dernière réponse | P1 |
| F-19 | Historique des conversations (liste, reprise, suppression, export Markdown) | P2 |

### 4.3 Fournisseurs / endpoints

| ID | Exigence | Prio |
|---|---|---|
| F-20 | Fournisseurs : Anthropic (Claude), OpenAI, OVHcloud AI Endpoints, Ollama — même couche API que Quill Thunderbird | P0 |
| F-21 | Activation de plusieurs fournisseurs ; un fournisseur actif choisi dans le panneau | P0 |
| F-22 | Par fournisseur : clé API, URL (OVH/Ollama), modèle ; chargement de la liste live des modèles | P0 |
| F-23 | Bouton « Tester la connexion » | P0 |
| F-24 | Endpoint « OpenAI-compatible » générique (LM Studio, vLLM, Mistral, Groq, OpenRouter…) avec URL libre | P1 |
| F-25 | Prompt système personnalisable | P1 |
| F-26 | Import des réglages depuis Quill Thunderbird (fichier JSON export/import) | P2 |

### 4.4 Contexte de la page courante

| ID | Exigence | Prio |
|---|---|---|
| F-30 | Affichage de la page courante : favicon, titre, domaine/URL | P0 |
| F-31 | Interrupteur « Inclure la page » : joint au message le titre, l'URL et le texte de la page | P0 |
| F-32 | Extraction du texte principal (`<article>`, `<main>`, sinon `<body>`), nettoyé (scripts, styles, navigation retirés), tronqué à une limite configurable | P0 |
| F-33 | Prise en compte de la sélection courante si elle existe (prioritaire / en plus du texte) | P0 |
| F-34 | Mise à jour automatique au changement d'onglet ou de navigation | P0 |
| F-35 | Pages non lisibles (`chrome://`, Chrome Web Store, PDF natif) : message explicite, chat toujours disponible | P0 |
| F-36 | Autorisation d'accès aux pages demandée **à la demande** (permission optionnelle), pas à l'installation | P0 |
| F-37 | Le contenu de page n'est envoyé qu'une fois par changement de page (pas recopié à chaque message) | P0 |
| F-38 | Lecture de PDF ouverts dans Chrome et des transcriptions YouTube | P2 |
| F-39 | Extraction type « Readability » (meilleure détection du contenu principal) | P1 |
| F-40 | Capture d'écran de l'onglet envoyée aux modèles vision | P2 |
| F-41 | Interaction multi-onglets (« compare cet onglet et celui-ci ») | P2 |

### 4.5 Actions rapides

| ID | Exigence | Prio |
|---|---|---|
| F-50 | Boutons : Résumer la page, Points clés, Traduire, Expliquer la sélection | P0 |
| F-51 | Menu contextuel : « Quill : résumer cette page », « Quill : expliquer la sélection », « Quill : traduire la sélection » | P0 |
| F-52 | Actions personnalisées (nom + prompt), comme dans Quill Thunderbird | P1 |
| F-53 | Insérer la réponse dans le champ de saisie actif de la page | P2 |

### 4.6 Options

| ID | Exigence | Prio |
|---|---|---|
| F-60 | Page d'options : fournisseurs, langue, longueur max. des réponses, taille max. du contenu de page | P0 |
| F-61 | Langue de l'interface (FR/EN en v0.1 ; 8 langues ensuite) et langue de réponse par défaut | P0 / P1 |

---

## 5. Exigences non fonctionnelles

### 5.1 Sécurité et confidentialité

- **NF-01** Clés API stockées dans `chrome.storage.local` (jamais `sync`, jamais dans le code). Champ masqué dans l'interface.
- **NF-02** Aucune télémétrie, aucun serveur intermédiaire : les requêtes vont directement de l'extension au fournisseur.
- **NF-03** Le contenu de la page n'est lu **que** si l'utilisateur active « Inclure la page » ou lance une action ; un indicateur visible le signale.
- **NF-04** Principe du moindre privilège : `host_permissions` limitées aux API des fournisseurs ; l'accès aux sites est une **permission optionnelle** (`optional_host_permissions`) demandée à la première utilisation.
- **NF-05** Rendu des réponses : échappement HTML systématique avant mise en forme Markdown ; liens ouverts avec `rel="noopener noreferrer"` ; CSP MV3 par défaut (pas d'`eval`, pas de script distant).
- **NF-06** Le contenu de la page est traité comme **donnée** : il est encadré dans le prompt (`<page>…</page>`) et le prompt système indique au modèle de ne pas suivre d'instructions qui s'y trouveraient (atténuation de l'injection de prompt).
- **NF-07** Politique de confidentialité publiée (exigée par le Chrome Web Store).

### 5.2 Performance

- **NF-10** Ouverture du panneau < 300 ms.
- **NF-11** Extraction de page < 500 ms sur une page standard ; limite par défaut 20 000 caractères.
- **NF-12** Service worker sans état critique (MV3 peut l'arrêter à tout moment) : l'état vit dans `chrome.storage`.

### 5.3 Compatibilité

- **NF-20** Chrome ≥ 116 (API `sidePanel.open`), Edge et autres Chromium récents.
- **NF-21** Ollama : nécessite `OLLAMA_ORIGINS=chrome-extension://*` (documenté).

### 5.4 Accessibilité / ergonomie

- **NF-30** Navigation clavier complète, focus visible, libellés ARIA, contraste WCAG AA.

### 5.5 Maintenabilité

- **NF-40** Le **cœur** (`API.js`, `providers.js`) est le même que celui de Quill Thunderbird ; seule une petite couche d'adaptation (`browser` ↔ `chrome`) diffère. Objectif v0.3 : un dossier `core/` partagé et un script de build qui produit les deux paquets.
- **NF-41** JavaScript ES modules natifs, sans dépendance ni bundler en v0.1.

---

## 6. Architecture technique

```
Quill-Chrome/
├── manifest.json            MV3 : side_panel, options, commands, permissions
├── background.js            Service worker : comportement de l'icône, menus contextuels,
│                            ouverture du panneau, transmission des demandes au panneau
├── core/                    Cœur partagé avec Quill Thunderbird
│   ├── compat.js            Shim : expose `browser` sur `chrome`
│   ├── providers.js         Registre des fournisseurs + stockage de la config
│   ├── API.js               Appels Anthropic / OpenAI / OVHcloud / Ollama
│   ├── page.js              Lecture de l'onglet actif (scripting.executeScript)
│   ├── markdown.js          Rendu Markdown sûr
│   └── i18n.js              Chaînes FR / EN
├── sidepanel/               Interface du panneau latéral (chat + contexte)
├── options/                 Page de configuration
├── _locales/{en,fr}/        Nom / description de l'extension
└── images/                  Icônes
```

### Flux « discuter avec la page »

```
Utilisateur ──► Panneau (sidepanel.js)
                   │ 1. chrome.tabs.query(onglet actif)
                   │ 2. chrome.scripting.executeScript(extraction) ──► Page web
                   │ 3. Construit les messages :
                   │      system  = prompt Quill + règles de sécurité
                   │      user    = <page url titre>texte</page> + question
                   │ 4. fetchResponse(config active, messages) ──► API fournisseur
                   ◄─────────────────────────────────── réponse
                   │ 5. Rendu Markdown sûr + bouton Copier
```

### Flux « menu contextuel »

```
Clic droit ─► background.js : chrome.sidePanel.open(windowId)
                            + chrome.storage.session.set({ pendingRequest })
Panneau     ◄─ storage.onChanged / lecture au chargement ─► exécute l'action
```

### Permissions

| Permission | Raison |
|---|---|
| `sidePanel` | Afficher le panneau latéral |
| `storage` | Réglages et conversation |
| `tabs` | Lire titre / URL de l'onglet actif et suivre les changements |
| `activeTab` | Accès ponctuel à la page lors d'un clic (icône, menu contextuel) |
| `scripting` | Extraire le texte de la page |
| `contextMenus` | Entrées du clic droit |
| `host_permissions` (API) | `api.anthropic.com`, `api.openai.com`, `*.ai.cloud.ovh.net`, `localhost` |
| `optional_host_permissions` `<all_urls>` | Lecture des pages et URL Ollama/OVH personnalisées, demandée à la demande |

---

## 7. Interface (maquette fonctionnelle)

```
┌─────────────────────────────────────┐
│ ✒ Quill   [Claude · sonnet-5-5 ▾] ＋ ⚙│  en-tête
├─────────────────────────────────────┤
│ 🌐 Titre de la page                  │  carte contexte
│    exemple.com/article     [● Page] │  (interrupteur)
│ [Résumer] [Points clés] [Traduire]  │  actions rapides
│ [Expliquer la sélection]            │
├─────────────────────────────────────┤
│                    Quelle est la    │
│                    conclusion ?  ◄──┤ utilisateur
│ ┌─────────────────────────────┐     │
│ │ La conclusion de l'article… │ ⧉   │ assistant + copier
│ └─────────────────────────────┘     │
├─────────────────────────────────────┤
│ [Posez une question…        ] [➤]  │  saisie
└─────────────────────────────────────┘
```

---

## 8. Feuille de route

| Version | Contenu | Estimation |
|---|---|---|
| **v0.1 — MVP** | Panneau latéral, chat multi-tours, 4 fournisseurs, sélecteur de fournisseur, contexte de page (URL/titre/texte/sélection), 4 actions rapides, menu contextuel, options, FR/EN | livrée avec ce document |
| v0.2 | Streaming, bouton Stop, Régénérer, extraction type Readability | 1–2 semaines |
| v0.3 | Cœur partagé Thunderbird/Chrome + script de build, endpoint OpenAI-compatible générique, prompt système personnalisable | 1–2 semaines |
| v0.4 | Actions personnalisées, 8 langues, langue de réponse | 1 semaine |
| v0.5 | Historique des conversations, export Markdown | 1 semaine |
| v1.0 | Publication Chrome Web Store (fiche, captures, politique de confidentialité), tests e2e (Puppeteer) | 1–2 semaines |
| v1.x | PDF / YouTube, vision (capture d'onglet), multi-onglets, insertion dans la page, version Firefox | — |

---

## 9. Critères d'acceptation de la v0.1

1. L'extension se charge sans erreur via `chrome://extensions` → « Charger l'extension non empaquetée » → dossier racine du dépôt.
2. Le clic sur l'icône (ou `Alt+Q`) ouvre le panneau à droite.
3. Avec une clé Anthropic valide, une question reçoit une réponse ; une seconde question tient compte de la première.
4. Le fournisseur actif peut être changé depuis le panneau ; la réponse suivante utilise le nouveau fournisseur.
5. Sur un article web, « Résumer » produit un résumé du contenu de la page.
6. Changer d'onglet met à jour la carte contexte.
7. Sur `chrome://settings`, la carte indique que la page n'est pas lisible et le chat reste fonctionnel.
8. Clic droit sur une sélection → « Expliquer la sélection » ouvre le panneau et répond sur ce texte.
9. Une clé invalide affiche un message d'erreur compréhensible et la question est restituée dans le champ.
10. Aucun appel réseau autre que vers le fournisseur configuré (vérifiable dans l'onglet Réseau des DevTools du panneau).

---

## 10. Risques et points d'attention

| Risque | Mitigation |
|---|---|
| Injection de prompt via le contenu d'une page | Contenu encadré, règle explicite dans le prompt système, aucune action automatique sur la page |
| Pages très longues → coût / limite de contexte | Troncature configurable, contenu envoyé une seule fois par page |
| Revue Chrome Web Store (permissions larges) | `<all_urls>` en permission optionnelle uniquement, justification dans la fiche |
| CORS Ollama | Documenter `OLLAMA_ORIGINS=chrome-extension://*` |
| Arrêt du service worker MV3 | Aucun état en mémoire dans le worker ; tout passe par `chrome.storage` |
| Divergence du code avec Quill Thunderbird | Cœur partagé (v0.3) |
