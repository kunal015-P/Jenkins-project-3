from http.server import BaseHTTPRequestHandler, HTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello from Kubernetes Python App 🚀".encode())


def run():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, AppHandler)
    print("Server running on port 5000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
