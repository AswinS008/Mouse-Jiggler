index=chevron_ist_switch_prod host="vlcvusepistsl70*" sourcetype=prod_chevron_ist_cmmt* ("disconnected at" OR "connected at")
| rex field=_raw "(?<event_type>disconnected at|connected at)" 
| rex field=_raw ".(?<date_time>\d+\.\d+\.\d+\s\d+:\d+:\d+)"
| rex field=_raw "Channel\s#(?<channel_id>\d+)" 
| rex field=_raw "Port\<(?<port_name>[^>]+)\>" 
| rex field=_raw "Server\<(?<server_name>[^>]+)\>"
| rex field=_raw "connected at \<(?<connect_ip>\d+\.\d+\.\d+\.\d+:\d+)\> to \<(?<server_ip>\d+\.\d+\.\d+\.\d+:\d+)\> Msg\<(?<message>[^>]+)\> Proto\<(?<protocol>[^>]+)\> LB\<(?<lb>[^>]+)\> Group\<(?<group>[^>]+)\>"
| eval date_time_epoch = strptime(date_time, "%Y.%m.%d %H:%M:%S")
| stats min(date_time_epoch) as min_time max(date_time_epoch) as max_time by event_type
| eval ISSUE_START_TIME = if(event_type == "disconnected at", strftime(min_time, "%Y.%m.%d %H:%M:%S"), null())
| eval ISSUE_END_TIME = if(event_type == "connected at", strftime(max_time, "%Y.%m.%d %H:%M:%S"), null())
| fields - min_time max_time event_type date_time_epoch


index=chevron_ist_switch_prod host="vlcvusepistsl70*" sourcetype=prod_chevron_ist_cmmt* ("connected at" OR "disconnected at")
| rex field=_raw ".(?<date_time>\d+\.\d+\.\d+\s\d+:\d+:\d+)"  # Extract date_time
| rex field=_raw ".Port<(?<port_name>\S+)>"  # Extract port_name
| eval event_type=if(match(_raw, "connected at"), "connected", "disconnected")  # Determine event type
| stats min(date_time) as date_time, values(_raw) as _raw by event_type  # Find earliest and latest events
| table event_type, date_time, _raw
| rename COMMENT as "Filtering to show specific outputs:"
| search event_type="connected" OR event_type="disconnected"
