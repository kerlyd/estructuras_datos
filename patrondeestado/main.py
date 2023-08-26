class TCPConnection:
    def __init__(self):
        self.state = ClosedState()  # Inicialmente, la conexión está cerrada

    def change_state(self, new_state):
        self.state = new_state

    def open(self):
        self.state.open(self)

    def close(self):
        self.state.close(self)

    def send_data(self, data):
        self.state.send_data(self, data)


class TCPState:
    def open(self, connection):
        pass

    def close(self, connection):
        pass

    def send_data(self, connection, data):
        pass


class ClosedState(TCPState):
    def open(self, connection):
        print("Opening the connection")
        connection.change_state(OpenedState())

    def close(self, connection):
        print("Connection is already closed")

    def send_data(self, connection, data):
        print("Cannot send data, the connection is closed")


class OpenedState(TCPState):
    def open(self, connection):
        print("Connection is already open")

    def close(self, connection):
        print("Closing the connection")
        connection.change_state(ClosedState())

    def send_data(self, connection, data):
        print(f"Sending data: {data}")


# Uso del código
connection = TCPConnection()

connection.open()
connection.send_data("Hello, world!")

connection.close()
connection.send_data("This won't be sent")


