## 代码可从官网复制
## 建议复制时用:set paste 和 :set no paste
from match_client.match import Match
from match_client.match.ttypes import User
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()

    ##接下来写你的代码：

    user = User(1,'glk',1500)
    client.add_user(user,"")

    # Close!
    transport.close()



if __name__ == "__main__" :
    main()
