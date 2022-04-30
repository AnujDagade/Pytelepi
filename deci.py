class GPIO_Handler:
    def match(msg):
        if(msg.lower() == 'pratik'):
            print('HI',msg)
            s = 'HI '+msg
            return s
        else:
            print('Wrong Command')
            return 'Wrong Command'
