# Networking

## Finding Servers

1. multicast used to keep network aware of servers
    - new services must register
    - exiting services must re-register periodically (~5 mins?)
1. new clients can ping multicast server to find services
    - server returns message: `{ip, port, service, requester}`
1. client connects to service via udp or tcp
