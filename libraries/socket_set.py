from socketIO_client import SocketIO, LoggingNamespace

class socket_set:

    #Initialize the controller when the object is created
    def __init__(self):
        # Connect to the SocketIO Game server
        self.socketIO = SocketIO('localhost', 3000, LoggingNamespace)
        self.socketIO.on('stop', self.on_stop)
        # Listen for game events
        #socketIO.on('connect', on_connect)

        #socketIO.on('reconnect', on_reconnect)
        self.socketIO.on('registered_shot', self.on_registered_shot)
        #socketIO.on('game_halt', on_game_halt)
        #socketIO.on('game_resume', on_game_resume)
        #socketIO.on('game_end', on_game_end)

    def on_connect():
        print('connect')

    def on_stop():
        print('stahp dammit')

    def on_reconnect():
        print('reconnect')

    def on_game_start():
        print('game started')

    def on_game_halt():
        print('game halt')

    def on_game_resume():
        print('game resume')

    def on_game_end():
        print('game has ended')

    def on_registered_shot():
        print('shot registered by server')

    def i_have_been_shot(id):
        print('This bot has been shot by:')
        print(id)
        socketIO.emit('shotBy111')
        # stop the motors, prevent firing
        # report the hit count to the server
        # do a delay?
        # reenable

    def register(self, id):
        print('Attempting registration for: ')
        print(id)
        self.socketIO.emit('register', {'id': id})
        #self.socketIO.wait()

    def ready(self, id):
        print('Reporting ready for: ')
        print(id)
        self.socketIO.emit('ready', {'id': id})
        #self.socketIO.wait()

    def fire(self, id):
        print('This bot has attempted a shot: ')
        print(id)
        self.socketIO.emit('fire', {'botid': id})
        #self.socketIO.wait()

    def hit(self, id):
        print('This bot has been hit: ')
        print(id)
        self.socketIO.emit('hit', {'id': id})
        #self.socketIO.wait()


