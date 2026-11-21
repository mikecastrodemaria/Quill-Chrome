// Quill Chrome - service worker.
// Stateless on purpose: MV3 can stop it at any time, so requests for the
// side panel go through chrome.storage.session.

const MENUS = [
    { id: "quill-summarize", contexts: ["page"], title: "menuSummarize" },
    { id: "quill-explain", contexts: ["selection"], title: "menuExplain" },
    { id: "quill-translate", contexts: ["selection"], title: "menuTranslate" }
];

const setup = () => {
    chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch(console.error);
    chrome.contextMenus.removeAll(() => {
        for (const m of MENUS) {
            chrome.contextMenus.create({ id: m.id, contexts: m.contexts, title: chrome.i18n.getMessage(m.title) });
        }
    });
};

chrome.runtime.onInstalled.addListener(setup);
chrome.runtime.onStartup.addListener(setup);

chrome.contextMenus.onClicked.addListener((info, tab) => {
    // sidePanel.open() must run synchronously inside the user gesture.
    if (tab?.windowId !== undefined) {
        chrome.sidePanel.open({ windowId: tab.windowId }).catch(console.error);
    }
    chrome.storage.session.set({
        pendingRequest: {
            action: info.menuItemId.replace("quill-", ""),
            text: info.selectionText || "",
            tabId: tab?.id,
            ts: Date.now()
        }
    });
});
