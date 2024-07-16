// ==UserScript==
// @name         Keep Like Session Active
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Keeps the specified like session active on a webpage
// @author       You
// @match        https://example.com/*   // Replace with the URL of the webpage where you want to keep the session active
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Replace '#likeButton' with the actual selector for your like button
    let likeButton = document.querySelector('#likeButton');

    if (likeButton) {
        // Click the like button periodically to keep the session active
        setInterval(function() {
            likeButton.click();  // Simulate a click on the like button
        }, 60000);  // Adjust the interval (in milliseconds) as needed
    }
})();
