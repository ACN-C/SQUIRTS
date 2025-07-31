import socket
import sys


# remember to implement sys.argv for command line arguments

def squirt():
    
    # Need to define those host & port thing
    # Can't decide about port..maybe 69
    # but I think 127.0.0.1 is a good choice for host of "server"
    host = '127.0.0.1'
    port = 69

    # Should this be able to squirt multiple targets?
    # I say, CERTAINLY!
    enjoyers = int(input("How many \"targets\"? "))
    
    # Socket objectifying
    sexy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port, and make it kinky
    sexy.bind((host, port))
    sexy.listen(enjoyers)
    print(f"Listening on {host}:{port} for {enjoyers} connections...") 

    # collecting consent confirmations
    splash_zone = []
    print("Waiting for consent confirmations...")
    for i in range(enjoyers):
        brave = sexy.accept()
        splash_zone.append(brave)
        print(" Rubbing ",i+1," times!")
    
    fileno = 0
    idx = 0

    for brave in splash_zone:
        # Receiving File Data
        idx += 1
        splashed = brave[0].recv(1024).decode()

        if not splashed:
            continue
    # Creating a new file at server end and writing the data
        filename = 'output'+str(fileno)+'.txt'
        fileno = fileno+1
        fo = open(filename, "w")
        while splashed:
            if not splashed:
                break
            else:
                fo.write(splashed)
                splashed = brave[0].recv(1024).decode()

        print()
        print('Receiving file from client', idx)
        print()
        print('Received successfully! New filename is:', filename)
        fo.close()
    # Closing all Connections
    for brave in splash_zone:
        brave[0].close()

squirt()

# naming the client method "taking_it"():
# make it trigger when argument is passed
# still haven't decided how to do this
# as client, perhaps, squirts.py ~~~~ <destination> <file> ???
# with the number of tildes indicating how fast the client should send data? 
# less means short, fast, burst, more means longer but weaker?
def taking_it():
    print("This is the client side, not implemented yet.")
    # Here you would implement the client logic to connect to the server
    # and send data, similar to how the server receives it.
    pass