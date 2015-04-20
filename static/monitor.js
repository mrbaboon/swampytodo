var sent = document.getElementById("sent");
var rcvd = document.getElementById("rcvd");
var cpu = document.getElementById("cpu");
var mem = document.getElementById("mem");

swampdragon.onChannelMessage(function(channels, message){
    sent.innerText = message.data.kb_sent;
    rcvd.innerText = message.data.kb_rcvd;
    cpu.innerText = message.data.cpu + '%';
    mem.innerText = message.data.mem + '%';
});

swampdragon.ready(function(){
    swampdragon.subscribe('sys', 'sysinfo', null);
});