import socket

def Main():
    host = '127.0.0.1'
    port = 5008

    s = socket.socket()
    s.connect((host, port))

    filename = 'a.md'
    if filename != 'q':
        s.send(filename.encode('utf-8'))
        data = s.recv(1024)
        # dat=str(data)
        # print(data)
        if data[:6] == b'EXISTS':
            filesize = int(data[6:])
            print("File exists, "  +"Bytes, download? (Y/N)? -> ")

            message='Y'
            if message == 'Y':
                s.send("OK".encode("utf-8"))
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print ("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
                print ("Download Complete!")
                f.close()
        else:
            print ("File Does Not Exist!")

    s.close()


if __name__ == '__main__':

    Main()
