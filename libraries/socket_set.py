from socketIO_client import SocketIO, LoggingNamespace

class socket_set:

    #Initialize the controller when the object is created
    def __init__(self):
        # Connect to the SocketIO Game server
        self.socketIO = SocketIO('192.168.1.10', 3000, LoggingNamespace)
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

    def register(self):
        print('Attempting registration')
        self.socketIO.emit('register')
        #self.socketIO.wait()

    def ready(self):
        print('Reporting ready')
        self.socketIO.emit('ready')
        #self.socketIO.wait()

    def fire(self):
        print('This bot has attempted a shot')
        self.socketIO.emit('fire')
        #self.socketIO.wait()

    def hit(self):
        print('This bot has been hit')
        self.socketIO.emit('hit')
        #self.socketIO.wait()


