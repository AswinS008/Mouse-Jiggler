event_type	date_time	Connection	port_name	_raw
Issue START time	024.07.14 20:12:59	Disconnected	ChasePNS	2024.07.14 20:12:59 [cmmt:1654127:3674199808]Channel #00020 Link<SSL> Port<ChasePNS> Server<Balancer>: disconnected at <10.18.94.157:43138> from <206.253.180.141:15350>
Issue START time	024.07.14 20:13:00	Disconnected	ChasePNS	2024.07.14 20:13:00 [cmmt:1723266:2273306368]Channel #00020 Link<SSL> Port<ChasePNS> Server<Balancer>: disconnected at <10.18.94.158:35454> from <206.253.180.141:15350>
Issue END time	024.07.14 20:13:02	Connected	ChasePNS	2024.07.14 20:13:02 [cmmt:1723266:2281699072]Channel #00020 Link<SSL> Port<ChasePNS> Server<Balancer>: connected at <10.18.94.158:54950> to <206.253.180.141:15350> Msg<Standard-VISA> Proto<Transparent> LB<> Group<>
Issue END time	024.07.14 20:13:02	Connected	ChasePNS	2024.07.14 20:13:02 [cmmt:1654127:3682592512]Channel #00020 Link<SSL> Port<ChasePNS> Server<Balancer>: connected at <10.18.94.157:37882> to <206.253.180.141:15350> Msg<Standard-VISA> Proto<Transparent> LB<> Group<>


index=chevron_ist_switch_prod host ="vlcvusepistsl70*" sourcetype=prod_chevron_ist_cmmt* ": disconnected at " OR "connected at"
| rex field=_raw ".(?<date_time>\d+.\d+.\d+\s\d+:\d+:\d+)"
| rex field=_raw ".Channel\s(?<channel_id>\S+)" 
| rex field=_raw ".Port\<(?<port_name>\S+)\>" 
| rex field=_raw ".(?<dt>\d+\.\d+\.\d+\s\S+)\>" 
| eval event_type = if(match(_raw, ": disconnected at"),"Issue START time", if(match(_raw,"connected at"),"Issue END time",""))
| eval Connection = if(match(_raw, ": disconnected at"),"Disconnected", if(match(_raw,"connected at"),"Connected",""))
| table event_type, date_time, Connection, port_name, _raw
| sort date_time
