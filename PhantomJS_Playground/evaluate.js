/**
 * Created by ertaiduo on 1/25/17.
 */

/*
var page = require('webpage').create();

page.open('http://google.com', function (status) {
    var title = page.evaluate(function () {
        return document.title;
    });

    console.log('Webpage title is ' + title);
    phantom.exit();
});
*/

var page = require('webpage').create();
page.onConsoleMessage = function(msg) {
    console.log('Page title is ' + msg);
};
page.open('http://google.com', function(status) {
    page.evaluate(function() {
        console.log(document.title);
    });
    phantom.exit();
});