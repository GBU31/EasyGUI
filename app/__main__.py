import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from core.app import *
from core.start_server import *
from core.settings import *
import multiprocessing


def startServer():
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass


    webServer.server_close()
    print("Server stopped.")

def app():
    app = QApplication(sys.argv)
    QApplication.setApplicationName(title)
    window = MainWindow()
    app.exec_()


if __name__ == '__main__':
    Server = multiprocessing.Process(target=startServer)
    App = multiprocessing.Process(target=app)
    Server.start()
    App.start()
