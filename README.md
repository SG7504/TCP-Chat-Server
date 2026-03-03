
# TCP Chat Server

A simple multi-client TCP chat server built using Python standard libraries.  
The server allows multiple users to connect over TCP, log in with a username, and chat with each other in real time.

This project is built without HTTP, databases, or external libraries, and focuses on low-level socket programming and concurrency.

---

## Features

### Core Features
- Multi-client TCP server (threaded)
- Username-based login with collision handling
- Public message broadcasting
- Graceful client disconnect handling with notifications

### Bonus Features
- List active users (`WHO`)
- Private messaging (`DM <username> <text>`)
- Heartbeat support (`PING` → `PONG`)
- Idle timeout (clients disconnected after 60 seconds of inactivity)

---

## Requirements
- Python 3.x
- No external dependencies (standard library only)

---

## How to Run the Server

Run on default port **4000**:
```bash
python server.py
````

Run on a custom port:

```bash
PORT=5000 python server.py
```

---

## How to Connect (Client)

Clients can connect using tools like `netcat` or `telnet`.

Using netcat:

```bash
nc localhost 4000
```

---

## Supported Commands

```text
LOGIN <username>
MSG <text>
WHO
DM <username> <text>
PING
```

---

## Example Interaction

### Client 1

```text
LOGIN Naman
OK
MSG hi everyone!
```

### Client 2

```text
LOGIN Yudi
OK
MSG hello Naman!
```

### Client 1 receives

```text
MSG Yudi hello Naman!
```

### On client disconnect

```text
INFO Naman disconnected
```

---

## Bonus Feature Details

* **WHO**
  Lists all currently connected users.
  Response format:

  ```text
  USER <username>
  ```

* **DM `<username> <text>`**
  Sends a private message to a specific user. Only the recipient receives the message.

* **PING / PONG**
  Clients can send `PING` to verify connection liveness. The server responds with `PONG`.

* **Idle Timeout**
  Clients are automatically disconnected after **60 seconds of inactivity**, implemented using socket-level timeouts.

---

## Screen Recording (Demo)

A short screen recording demonstrating:

* Server startup
* Multiple clients connecting
* Login flow
* Public messaging
* Disconnect handling

📹 **Demo Video:**
[https://drive.google.com/file/d/1MbDtlM6n3qjRjcVqIqOqr1r3tTZSpuSU/view?usp=sharing](https://drive.google.com/file/d/1MbDtlM6n3qjRjcVqIqOqr1r3tTZSpuSU/view?usp=sharing)

---

## Deployment

This TCP server can be deployed on any virtual machine (e.g., AWS EC2 or DigitalOcean) by opening the required TCP port and running:

```bash
python server.py
```

For this submission, functionality is demonstrated via local execution and screen recording, as per the assignment instructions.

---

## Author

**Sparsh Guha**

* GitHub: [https://github.com/SG7504](https://github.com/SG7504)
* LinkedIn: [https://www.linkedin.com/in/sparshguha75/](https://www.linkedin.com/in/sparshguha75/)
