from hashlib import sha256 as sha
import codecs

def mining():
    msg = 'Attack at 9PM!'
    nonce = 0
    difficulty = 5

    while True:
        target = '%s%d' %(msg, nonce)
        hash = sha(target.encode()).digest()
        ret = codecs.encode(hash, 'hex_codec')

        if ret[:difficulty].decode() == '0'*difficulty:
            print('++++Bingo!++++')
            print(ret)
            print(nonce)
            break
        nonce += 1
mining()
