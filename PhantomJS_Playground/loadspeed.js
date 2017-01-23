/**
 * Created by ertaiduo on 1/22/17.
 */

var page = require('webpage').create(),
    system = require('system'),
    t,
    address;

if(system.args.length === 1){
    console.log('Usage: loadspeed.js http://google.com');
    phantom.exit();
}

t = Date.now();
address = system.args[1];
page.open(address, function (status) {
    if(status !== 'success'){
        console.log('Fail to load the address');
    }
    else{
        t = Date.now() - t;
        console.log('Loading ' + system.args[1]);
        console.log('Loading time ' + t + ' msec');
    }

    phantom.exit();
});