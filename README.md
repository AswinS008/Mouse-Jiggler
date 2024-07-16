2024.07.14 20:13:08.838736184 [cmmt:98444:4118783744]Channel #00020 Link<TCP> Port<IntChasUsW> Server<Balancer>: connected at <10.18.103.29:55558> to <206.253.180.113:4558> Msg<Standard-TEXTCR> Proto<Transparent> LB<> Group<>	1
2024.07.14 20:13:08.843736704 [cmmt:98444:3623876352]Channel #00020 Link<TCP> Port<IntChasUsW> Server<Balancer>: Reader successfully waited for CONNECTED state after 1 wait(s)
index=intuit_ist_switch host ="vlinusepistsl70*" sourcetype=prod_intuit_ist_switch_cmmt_int_chas_**.log "connected at" OR "Port<IntChasCaE> 
Server<Balancer>: reader - started" OR "Port<IntChasCaE> Server<Balancer>: writer - started" OR "Reader successfully waited for CONNECTED state"|stats count by host,_raw
