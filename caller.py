'''
Connects with a VoIP server via login, then makes a call to
a given number.
'''

import socket
from pyVoIP.VoIP import VoIPPhone, InvalidStateError, CallState
import time
import wave

# Meta variables
server_ip: str = '192.168.1.100'    # Server IP address
port: int = 5060                    # Server VoIP port
username: str = '101'               # Username to log into server w/
password: str = 'e2f03a2017220'     # Password for server
my_ip: str = '192.168.1.2'          # Local IP address
number: str = '101'                 # Number to call on soft phone

if __name__ == '__main__':
    try:

        # Create phone object
        print('Instantiating soft phone...')
        phone: VoIPPhone = VoIPPhone(server_ip, port, username, password, my_ip)

        # Register phone
        print('Registering w/ VoIP server...')
        phone.start()

        # Call some number
        print(f'Calling {number}...')
        call = phone.call(number)
        print('Connected! Waiting for 20 seconds, then hanging up.')

        # Sleep for a while
        time.sleep(20)

        # End call
        print('Hanging up.')
        phone.hangup()

        # End phone
        print('De-registering soft phone...')
        phone.stop()

    except Exception as e:
        print(f'Error: {e}')
