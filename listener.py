'''
Links with a VoIP server via login, listens for calls. When a
call is received, it plays a local .wav file on the line, then
hangs up.

Idea from PyVoIP documentation.
'''

import socket
from pyVoIP.VoIP import VoIPPhone, InvalidStateError, CallState
import time
import wave

# Meta variables
server_ip: str = '192.168.1.100'        # Server IP address
port: int = 5060                        # Server port
username: str = '101'                   # Server username
password: str = 'e2f03a2017220'         # Server password
my_ip: str = '192.168.1.3'              # Current IP address    
filepath: str = 'file.wav'              # File to play over call

# Answer an incoming call
def answer(call) -> None:
    try:
        # Get audio
        print('Loading audio...')
        f = wave.open(filepath, 'rb')
        frames = f.getnframes()
        data = f.readframes(frames)
        f.close()

        # Answer call and write audio
        print('Answering call...')
        call.answer()
        call.write_audio(data)
        call.read_audio()

        # Wait for message to be sent
        time.sleep(frames / 8000)

        # Sleep until they hang up
        while call.state == CallState.ANSWERED:
            time.sleep(0.1)

        # End call
        print('Hanging up...')
        call.hangup()
    
    except InvalidStateError:
        print('Exited call with error.')


if __name__ == '__main__':
    try:
        # Create phone object
        print('Instantiating phone...')
        phone: VoIPPhone = VoIPPhone(server_ip,
            port,
            username,
            password,
            my_ip,
            callCallback=answer)

        # Listen for incoming calls
        print('Registering soft phone...')
        phone.start()

        # Delay
        input('Press enter to kill phone')

        # End phone
        print('Deregestering soft phone...')
        phone.stop()

    except Exception as e:
        print(f'Error: {e}')
