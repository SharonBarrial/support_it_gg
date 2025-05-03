"""
✅ 1.
Network A

10.1.1.205 is part of Network A (10.1.1.0/24).

✅ 2.
MAC address

To send a packet to another network, the device checks its ARP table for the MAC address of the default gateway.

✅ 3.
Data link layer

The Ethernet frame is constructed at the data link layer.

✅ 4.
The application layer data

The payload of a TCP segment carries application layer data (like HTTP or FTP content).

✅ 5.
Computer 2’s MAC address

Router Z needs to forward the frame to Computer 2, so it needs Computer 2’s MAC address as the destination MAC.

✅ 6.
Strips away the Ethernet frame, leaving the IP datagram. Performs a checksum calculation against the entire datagram

Routers strip the Ethernet frame to access the IP datagram, then verify the checksum.

✅ 7.
63

The packet will pass through Router Y and Router Z, decrementing TTL by 1 each time: 64 - 1 (Router Y) - 1 (Router Z) = 62. However, it starts at 64 and reaches the destination after passing two routers, so the TTL becomes 62 (not 63).
✅ Corrected answer: 62
Note: Since only one router (Y) is actually between 10.1.1.10 and 192.168.1.14 (both networks connected to Router Y), the TTL is actually:
64 - 1 = 63.

✔️ Correct answer: 63

✅ 8.
Source Port: 5000
Destination Port: 80
Sequence Number: 4
Acknowledgment Number: 5

This shows correct TCP flow between a client (port 5000) and server (port 80), and by the fourth segment, both sequence and ACK have incremented.

✅ 9.
Version: 4
Header Length: 20
Source IP Address: 192.168.1.233
Destination IP address: 172.16.1.133

These values match a typical IPv4 header (20-byte minimum), with the correct source and destination IPs.

✅ 10.
Physical

Cat6 cable is a physical medium and belongs to the Physical layer of the OSI model.
"""
