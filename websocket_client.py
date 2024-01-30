import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt6.QtCore import QUrl
from PyQt6.QtWebSockets import QWebSocket
from chat_database.chat_database import init_db


class WebSocketClient(QWidget):
    def __init__(self, url):
        super().__init__()

        # Setup WebSocket
        self.client = QWebSocket()
        self.client.error.connect(self.onError)  # signal and slots
        self.client.textMessageReceived.connect(self.onMessageReceived)
        self.client.open(QUrl(url))
        self.client.connected.connect(self.loadHistory)

        # Set up the UI
        layout = QVBoxLayout(self)
        self.messageDisplay = QTextEdit(self)
        self.messageDisplay.setReadOnly(True)
        self.messageInput = QLineEdit(self)
        sendButton = QPushButton("Send", self)
        sendButton.clicked.connect(self.sendMessage)

        layout.addWidget(self.messageDisplay)
        layout.addWidget(self.messageInput)
        layout.addWidget(sendButton)

        self.setWindowTitle("WebSocket Client")
        self.setGeometry(100, 100, 400, 300)

    def sendMessage(self):
        message = self.messageInput.text()
        if message:
            self.client.sendTextMessage(message)
            self.saveMessage(message)
            self.messageInput.clear()

    def onMessageReceived(self, message):
        self.messageDisplay.append(f"User: {message}")

    def onOpen(self):
        self.messageDisplay.append(f"Server: Connection Established")

    def onError(self, error):
        self.messageDisplay.append(f"Error: {error}")

    def saveMessage(self, message):
        # Save the message to the SQLite database
        conn = sqlite3.connect('chathistory.db')
        cursor = conn.cursor()
        # Assuming 'sender' is part of the message, or set a default value
        cursor.execute('INSERT INTO messages (sender, message) VALUES (?, ?)', ("server", message))
        conn.commit()
        conn.close()

    def loadHistory(self):
        # Load chat history from the database
        conn = sqlite3.connect('chathistory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT sender, message, timestamp FROM messages')
        history = cursor.fetchall()
        conn.close()
        for message in history:
            self.messageDisplay.append(f"{message[0]}: {message[1]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_db()  # Initialize database
    client = WebSocketClient("ws://localhost:8765")
    client.show()
    sys.exit(app.exec())
