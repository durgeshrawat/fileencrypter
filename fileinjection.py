#file encryptor [* files from folder]
import os,sys
if __name__=='__main__':
    path=os.getcwd()
    files=os.listdir(path)
    _modulepc_=sys.argv[0]
    _modulean_=sys.argv[0]
    key=12
    for i in files:
        _filepc_=path+'\\'+str(i)
        _filean_=path+'/'+str(i)
        try:
            if _modulepc_!=_filepc_:
                with open(_filepc_,'rb') as f:
                    data=f.read()
                image_=bytearray(data)
                for index, values in enumerate(image_):
                    image_[index] = values ^ key
                with open(_filepc_,'wb') as f:
                    f.write(image_)
        except:
            if _modulean_!=_filean_:
                with open(_filean_,'rb') as f:
                    data=f.read()
                image_=bytearray(data)
                for index, values in enumerate(image_):
                    image_[index] = values ^ key
                with open(_filean_,'wb') as f:
                    f.write(image_)
