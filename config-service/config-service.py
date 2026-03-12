"""Minimal TCP server that accepts connections but never sends a response.

This simulates a hung/overloaded service — it completes the TCP handshake
so the client gets a successful connection, but then never writes any data,
causing blocking reads on the client side to hang indefinitely.
"""
import socket
import threading


def _handle(conn):
    """Hold the connection open forever without sending data."""
    try:
        while True:
            # Read and discard any data the client sends
            data = conn.recv(4096)
            if not data:
                break
    except OSError:
        pass
    finally:
        conn.close()


def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("0.0.0.0", 8888))
    srv.listen(128)
    print("config-service listening on :8888 (slow-drain mode)")
    while True:
        conn, addr = srv.accept()
        threading.Thread(target=_handle, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    main()
