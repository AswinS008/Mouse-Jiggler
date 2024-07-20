// ==UserScript==
// @name         Keep Session Active
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Clicks a button every 10 seconds to keep the session active
// @match        https://splunk.fnfis.com/en-US/app/paypal_ist_switch/search
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Function to click the button
    function clickButton() {
        // Change the selector if needed
        const button = document.querySelector('button'); // Update this selector to match the actual button
        if (button) {
            button.click();
            console.log('Button clicked');
        } else {
            console.log('Button not found');
        }
    }

    // Click the button immediately
    clickButton();

    // Set an interval to click the button every 10 seconds
    setInterval(clickButton, 10000); // 10000 milliseconds = 10 seconds
})();
