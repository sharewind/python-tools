# -*- coding: utf-8 -*-
import codecs
import os


def convert_file_encoding(filename, src_encoding='GBK',target_encoding = 'UTF-8'):
    f = None
    try:
        # read file by src_encoding
        f = codecs.open(filename, 'r', src_encoding)
        lines = f.readlines()#or use f.read() to fetch the whole file content
        f.close()        
        # write file as target encoding
        f = codecs.open(filename, 'w', target_encoding)
        f.writelines(lines)
        f.close()
    except:
        pass
    finally:
        f.close()

def walk(base_path, patterns="*"):
    patterns = patterns.split(';')
    for root, dirs, files in os.walk(base_path, False):
        for file in files:
             if os.path.splitext(file)[1] == '.ice':
                yield os.path.join(root,file)

def main():
    base_path = "E:\Corporations\Sohu\Projects\cloudatlas\cloudatlas-core"
    for file in walk(base_path,"*.ice"):
        print file
        convert_file_encoding(file)
        print u'文件转换完成',file
    pass

if __name__ == '__main__':
    main()


 