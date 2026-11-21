# ✒️ Quill pour Chrome — v0.1

Le chat Quill dans le **panneau latéral droit** de Chrome (et des navigateurs Chromium : Edge, Brave, Opera, Vivaldi), avec les mêmes fournisseurs que Quill Thunderbird et la possibilité de **discuter avec la page courante**.

Cahier des charges complet : [CAHIER_DES_CHARGES.md](CAHIER_DES_CHARGES.md).

## Fonctions de la v0.1

- Panneau latéral ouvert par l'icône Quill ou `Alt+Q`
- Chat multi-tours, rendu Markdown, bouton Copier, conversation conservée pendant la session
- Fournisseurs : **Anthropic (Claude)**, **OpenAI**, **OVHcloud AI Endpoints**, **Ollama** (local), avec bascule dans l'en-tête du panneau
- Carte « page courante » (favicon, titre, URL) qui suit l'onglet actif
- Interrupteur **Page** : joint le titre, l'URL et le texte de la page à votre message (une seule fois par page)
- Actions rapides : Résumer, Points clés, Traduire, Expliquer la sélection
- Clic droit : « Quill : résumer cette page », « expliquer / traduire la sélection »
- Page d'options : clés, URL, modèles (liste live), test de connexion, langue FR/EN, limites

## Installation (mode développeur)

1. Ouvrir `chrome://extensions`
2. Activer le **Mode développeur** (en haut à droite)
3. **Charger l'extension non empaquetée** → sélectionner le dossier racine de ce dépôt (celui qui contient `manifest.json`)
4. Épingler l'icône Quill, ouvrir les **Options** et saisir au moins une clé API

### Ollama

Ollama refuse par défaut les requêtes venant d'une extension. Avant de le lancer :

```powershell
$env:OLLAMA_ORIGINS = "chrome-extension://*"; ollama serve
```

## Accès aux pages

La lecture d'une page n'a lieu que lorsque vous activez **Page** ou lancez une action. Au premier usage, Chrome peut demander l'autorisation de lire les sites : elle est optionnelle et révocable dans `chrome://extensions`. Les pages internes (`chrome://…`) et le Chrome Web Store ne sont jamais lisibles.

Les données ne transitent que entre votre navigateur et le fournisseur choisi : pas de serveur Quill, pas de télémétrie.

## Structure

```
Quill-Chrome/
├── manifest.json        Manifest V3
├── background.js        Service worker : icône → panneau, menus contextuels
├── core/
│   ├── API.js           ⇐ copie de plugin/html/API.js de Quill
│   ├── providers.js     ⇐ copie de plugin/html/providers.js de Quill
│   ├── compat.js        expose `browser` sur `chrome` pour le cœur partagé
│   ├── page.js          lecture de l'onglet actif
│   ├── markdown.js      rendu Markdown sûr
│   └── i18n.js          chaînes FR / EN
├── sidepanel/           panneau latéral
├── options/             page d'options
└── _locales/            nom et description de l'extension
```

`core/API.js` et `core/providers.js` sont **identiques** à ceux de [Quill pour Thunderbird](https://github.com/mikecastrodemaria/Quill) : toute correction de la couche fournisseurs doit être reportée dans les deux (la v0.3 prévoit un dossier partagé et un script de build).

## Empaqueter

```powershell
Compress-Archive -Path manifest.json,background.js,styles.css,core,sidepanel,options,images,_locales -DestinationPath quill-chrome-0.1.0.zip -Force
```
