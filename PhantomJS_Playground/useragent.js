/**
 * Created by ertaiduo on 1/26/17.
 */

var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';
page.open('http://www.httpuseragent.org', function (status) {
    if(status !== 'success'){
        console.log('Unable to access network');
    }
    else {
        var ua = page.evaluate(function () {
            return document.getElementById('myagent');
        });
        console.log(ua);
    }

    phantom.exit();
});
