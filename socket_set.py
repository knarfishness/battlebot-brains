from socketIO_client import SocketIO, LoggingNamespace

class socket_set:
    def on_connect():
        print('connect')

    def on_disconnect():
        print('disconnect')

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

    def i_have_been_shot(id):
        print('This bot has been shot by:')
        print(id)
        socketIO.emit('shotBy111')
        # stop the motors, prevent firing
        # report the hit count to the server
        # do a delay?
        # reenable

    def attempted_shot(self, id):
        print('This bot has attempted a shot: ')
        print(id)
        self.socketIO.emit('fire', {'id': 123, 'test':'value'})
        self.socketIO.wait()

    #Initialize the controller when the object is created
    def __init__(self):
        # Connect to the SocketIO Game server
        self.socketIO = SocketIO('10.5.65.45', 3000, LoggingNamespace)
        #socketIO.on('connect', on_connect)
        #socketIO.on('disconnect', on_disconnect)
        #socketIO.on('reconnect', on_reconnect)

        # Listen for game events
        #socketIO.on('game_start', on_game_start)
        #socketIO.on('game_halt', on_game_halt)
        #socketIO.on('game_resume', on_game_resume)
        #socketIO.on('game_end', on_game_end)
