# client-and-server-communicates-Socket-program
this program demonstrates a simple client-server communication scenario using sockets. The client sends a message to the server, and the server responds with a message.

# Socket Program
A socket program is a type of program thatenables two-way communication between a client and a server. It allows the client to send requests to the server, and the server to respond to the requests.To write a socket program for the above mentioned scenario, the client and serverneed to be coded in two different programs.The client will send the message to the server and the server will respond with the same message.

# Client code
To establish a communication with the server, the client code will first create a socket and connect it to the server. Once the connection is established, the client code will send a message to the server and wait for the server to respond with the same message. However, it is important for the client code to handle any errors that may occur during the communication process, such as disconnection or timeout errors, to ensure a stable and reliable connection.

# Server code
The server code will be responsible for creating a socket and listening for incoming connections. It will then receive the messages sent by the client, and send a message back to the client. 
