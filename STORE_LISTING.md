# Store listing — Chrome Web Store

Texts and answers for submitting Quill-Chrome on the [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole). Firefox version: [Quill-Firefox/STORE_LISTING.md](https://github.com/mikecastrodemaria/Quill-Firefox/blob/main/STORE_LISTING.md).

## 0. Before the first submission

- Register a developer account (one-time US$5 fee) and verify the contact email.
- Build the zip (see README → *Package*). Each upload must have a higher `version` in `manifest.json`.
- ⚠️ Prepare the images listed in section 6 — the store icon, at least one screenshot and the small promo tile are **required**.

## 1. Store listing tab

**Name** — comes from the manifest (`_locales/*/messages.json` → `extensionName`).

**Summary** — comes from the manifest (`extensionDescription`, max 132 characters).

**Description**

```
Quill brings an AI assistant to Chrome's side panel, next to the page you are reading.

• Chat with your choice of provider: Anthropic (Claude), OpenAI, OVHcloud AI Endpoints (EU hosting, free anonymous tier) or Ollama (100% local).
• Turn on "Page" to ask questions about the current page: its title, URL and text are sent with your message.
• One-click actions: Summarize, Key points, Translate, Explain selection.
• Right-click menu: summarize the page, explain or translate the selected text.
• Bring your own API key. Requests go directly from your browser to the provider you chose: no Quill server, no tracking.

Also works in Edge, Brave, Opera and Vivaldi. Sister project of Quill for Thunderbird and Quill for Firefox.
```

| Field | Value |
|---|---|
| Category | **Productivity** (Tools) |
| Language | English (French is also provided via `_locales/fr`) |
| Homepage URL | `https://github.com/mikecastrodemaria/Quill-Chrome` |
| Support URL | `https://github.com/mikecastrodemaria/Quill-Chrome/issues` |

## 2. Privacy practices tab

**Single purpose**

```
Quill is an AI chat assistant in the side panel that can answer questions about the page the user is currently reading, using the AI provider the user configured.
```

**Permission justifications**

| Permission | Justification to paste |
|---|---|
| `sidePanel` | The whole user interface (chat) is displayed in Chrome's side panel. |
| `storage` | Stores the user's settings and API keys locally, and the current conversation for the browser session. |
| `tabs` | Shows the title, URL and favicon of the active tab in the panel and updates them when the user switches tabs. |
| `activeTab` | Reads the current page only after a user action (quick action button or context-menu entry). |
| `scripting` | Injects a text-extraction function into the active page when the user asks a question about it. |
| `contextMenus` | Adds "Quill: summarize this page" and "explain / translate the selection" to the right-click menu. |
| Host permissions (`api.anthropic.com`, `api.openai.com`, `*.ai.cloud.ovh.net`, `localhost`, `127.0.0.1`) | Sends the user's chat requests to the AI provider they chose (Anthropic, OpenAI, OVHcloud AI Endpoints) or to their local Ollama server. |
| Optional host permission `<all_urls>` | Requested only when the user first asks about a page, so the page text can be read; the user can refuse or revoke it at any time. |

**Remote code**

```
No, I am not using remote code.
```

(All JavaScript is in the package; the extension only exchanges JSON with the AI APIs.)

**Data usage** — check:

- ☑ **Authentication information** — the user's API keys, stored locally and sent only to the matching provider
- ☑ **Website content** — page text, sent to the chosen provider when the user turns on "Page" or runs an action
- ☑ **Web history** — the URL and title of the page in that same request

Leave everything else unchecked. Then certify the three statements:

- ☑ I do not sell or transfer user data to third parties, outside of the approved use cases
- ☑ I do not use or transfer user data for purposes that are unrelated to my item's single purpose
- ☑ I do not use or transfer user data to determine creditworthiness or for lending purposes

(Sending data to the AI provider the user selected is the extension's core function, which is an approved use.)

**Privacy policy URL**

```
https://github.com/mikecastrodemaria/Quill-Chrome/blob/main/PRIVACY.md
```

## 3. Distribution tab

| Field | Value |
|---|---|
| Payments | Free of charge |
| Visibility | **Public** (or **Unlisted** for a first test round: installable via link only) |
| Regions | All regions |

## 4. Test instructions (for the reviewer)

```
No account is needed. Open the extension options, enable "OVHcloud AI Endpoints" (works without an API key, anonymous rate-limited tier) and set it as the active provider. Click the Quill toolbar icon to open the side panel, open any article and click "Summarize".
```

## 5. Release notes

### 0.2.1

The Chrome Web Store has no release-notes field shown to users: paste these notes in the **Test instructions** box for the reviewer (with the review text below), and add the first line to the top of the description as a "What's new" line if you like.

```
Version 0.2.1 - Describe the images of a page

- New "Images" button: Quill sends the main images of the page (up to 4, small icons skipped) to your AI model and describes them, including any visible text such as chart titles and figures.
- Turn on "Page" first to send the page text with the images: the answer relates each image to the article and ends with an overview.
- New right-click entry on any picture: "Quill: describe this image".
- Thumbnails of the images appear in your message. Images are resized to 1024 px before sending and are never stored.
- Needs a model that reads images: Claude, gpt-4o, OVHcloud Mistral-Small-3.2 (free anonymous tier), or Ollama gemma / llava / qwen2.5vl. A clear message tells you when the selected model can't read images.
- Fix: a request retried after granting page access keeps its images.
```

**For the reviewer (Test instructions)**

```
Version 0.2.1 adds image description. No new permission: manifest.json only changes its version number. The new right-click entry uses the "image" context of the existing contextMenus permission.

To test without an account: enable "OVHcloud AI Endpoints" in the options (no API key needed, model Mistral-Small-3.2-24B-Instruct-2506 reads images) and make it the active provider. Open an article with pictures, then click "Images" in the side panel, or right click a picture and choose "Quill: describe this image".

Images are fetched from the page, resized to 1024 px JPEG in the side panel, sent only to the provider chosen by the user, and never written to storage.
```

### 0.1.1

```
First release: AI chat in the side panel with 4 providers, current-page context, quick actions and context menu.
```

## 6. Images

| Asset | Size | Required | Status |
|---|---|---|---|
| Store icon | 128×128 PNG (96×96 artwork + transparent padding) | yes | ✅ `store/store-icon-128.png` (redrawn by `store/draw_icon.py`) |
| Screenshots | 1280×800 or 640×400, 1 to 5 | at least 1 | ✅ `screenshots/1-summarize.png`, `2-explain-selection.png`, `3-options.png`, `4-images.png` (v0.2) (24-bit, no alpha) |
| Small promo tile | 440×280 | yes | ✅ `store/promo-tile-440x280.png` (`store/draw_tile.py`) |
| Marquee promo tile | 1400×560 | no | ✅ `store/marquee-1400x560.png` (`store/draw_marquee.py`) |

**Screenshot captions** — the Chrome Web Store has no caption field; upload in this order (or `4-images.png` first to highlight v0.2) and reuse the texts in the description if you like:

`screenshots/1-summarize.png`

```
Summarize the page you are reading in one click, right in Chrome's side panel.
```

`screenshots/2-explain-selection.png`

```
Select a passage and ask Quill to explain it in plain words, from the side panel or the right-click menu.
```

`screenshots/3-options.png`

```
Choose your AI provider: Claude, OpenAI, OVHcloud AI Endpoints (free anonymous tier) or Ollama running locally.
```

`screenshots/4-images.png`

```
New in 0.2: describe the images of a page. With "Page" on, Quill relates each picture to the article.
```

## 7. After submission

- Review usually takes from a few hours to a few days; the broad optional host permission and `scripting` can make it longer.
- Status and rejection reasons appear in the dashboard and by email.
- For an update: bump `version`, rebuild the zip, **Package → Upload new package**, then **Submit for review**.
