from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

class SABHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        super().end_headers()

if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), SABHandler)
    print("Serving with SharedArrayBuffer support on http://localhost:8000")
    server.serve_forever()
