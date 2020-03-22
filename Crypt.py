from random import randint
import json

class encrypted(list):
    def to_bytes(self):
        to_return = b''
        for elem in self:
            to_return += elem.to_bytes(1,'big')
        return to_return

    def hexlify(self):
        to_return = ''
        for elem in self:
            new = hex(elem).replace('0x','')
            if len(new) != 2:
                new = '0'+new
            to_return += new
        return to_return
        

class XOR:
    def __init__(self):
        self.key = {}
        #self.attempts = crypt_attempts
        return None

    def encrypt(self,string:str,binary=False,maxdepth = 0)->encrypted:#depth=0 - random depth(slow but produces very safe encrypted data)
        to_return = []
        for i in range(len(string)):
            str_i = str(i)
            #self.key[str_i] = []
            
            
            
            done = True
            if not binary:
                val = ord(string[i])
            else:
                val = string[i]
            if maxdepth == 0:
                self.key[str_i] = []
                depth = 0
                k = randint(1,254)
                while done:
                    #k = randint(1,254)
                    if i != 0:
                        for n in range(len(self.key)-1):
                            done = False
                        
                            if len(self.key[str(n)])<=depth:
                                continue
                        
                            if k == self.key[str(n)][depth]:
                                done = True
                                val = val^k
                                self.key[str_i].append(k)
                                k = randint(1,254)
                                depth += 1
                        
                    else:
                        done = False                
                        k = randint(1,254)

                    self.key[str_i].append(k)
                    val = val^k
            else:
                self.key[str_i] = [0]*maxdepth
                for depth in range(maxdepth):
                    k = randint(1,254)
                    self.key[str_i][depth] = k
                    val = val^k

            to_return.append(val)
                               

        return encrypted(to_return)
    


    def save_key(self,filename):#closes stream
        file = open(filename,'w')
        json.dump(self.key,file)
        file.close()

    def parse_key(self,filename):
        file = open(filename,'r')
        self.key = json.load(file)
        file.close()

    def decrypt(self,data):
        if len(self.key.keys()) == 0:
            raise Exception('Unparsed Key! Use function parse_key or parse by yourself, before using decryption.')
        to_return = []
        for i in range(len(data)):
            val = data[i]
            for mask in self.key[str(i)][::-1]:
                val = val^mask
            to_return.append(val)
        return encrypted(to_return)



# filename = 'smth.py'


# file = open(filename,'rb')
# data = file.read()
# file.close()


# xor = XOR()
# datae = xor.encrypt(data,True,2)
# xor.save_key('key')

# file = open(f'{filename}.enc','wb')
# file.write(datae.to_bytes())
# file.close()









#file = open('Cryptc.py.enc','rb')
#enc_data = file.read()#file.write(datae.to_bytes())
#file.close()

#xor = XOR()
#xor.parse_key('key')
#data = xor.decrypt(enc_data)

#file = open('Cryptct.py','wb')
#file.write(data.to_bytes())
#file.close()






