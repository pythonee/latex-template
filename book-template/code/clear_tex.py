import os,sys

from itertools import chain

paths = ['D:\\Dropbox\\Document\\Latex',
         'D:\\Dropbox\\Document\\xeLate',
         'D:\\Dropbox\\Document\\Resume',
         'D:\\Dropbox\\Document\\Master Project']

suffixs = ['.log','.aux','.bbl','.blg','.ilg','.toc',
           '.lof','.lot','.idx','.ind','.out','.brf',
           '.glo','.gls']

for root,dirs,files in chain.from_iterable(os.walk(path) for path in paths):
    for file in files:
        pathtofile = os.path.join(root,file)
        filename, ext = os.path.splitext(file)

        if ext in suffixs:
            print filename,ext
            try:
                os.remove(pathtofile)
            except IOError:
                print 'error'

