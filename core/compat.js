// Quill Chrome - lets the Thunderbird core (which calls `browser.*`) run on Chrome.
// Import this module first in every entry point.
if (typeof globalThis.browser === "undefined") globalThis.browser = chrome;
