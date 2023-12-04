'''
In theory, this should be a caller.
'''

import socket
from pyVoIP.VoIP import VoIPPhone, InvalidStateError, CallState
import time
import wave

# Meta variables
server_ip: str = '192.168.1.100'

port: int = 5060
username: str = '101'
password: str = 'e2f03a2017220'
my_ip: str = '192.168.1.3'

number: str = '12345'

if __name__ == '__main__':
    # Create phone object
    phone: VoIPPhone = VoIPPhone(my_ip, port, username, password, my_ip)

    # Register phone
    print('Registering w/ VoIP server...')
    phone.start()

    # Call some number
    print('Calling...')
    call = phone.call(number)
    print('Connected!')

    # Sleep for a while
    time.sleep(20)

    # End call
    print('Hanging up.')
    phone.hangup()

    # End phone
    phone.stop()
