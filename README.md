# tcp-chat-server
# TCP Chat Server

A simple multi-client TCP chat server built using Python standard libraries.

## Features
- Multiple clients (threaded)
- Username login
- Public chat
- Private messaging (DM)
- List active users (WHO)
- Heartbeat support (PING/PONG)
- Idle timeout (60 seconds)

---

## Requirements
- Python 3.x
- No external dependencies

---

## How to Run

```bash
python server.py
Or with a custom port:

PORT=5000 python server.py
How to Connect (Client)
Using netcat:

nc localhost 4000
Commands
LOGIN <username>
MSG <text>
WHO
DM <username> <text>
PING
Example Session
Client 1
LOGIN Naman
OK
MSG hi everyone!
Client 2
LOGIN Yudi
OK
MSG hello Naman!
Client 1 sees
MSG Yudi hello Naman!
On disconnect
INFO Naman disconnected
