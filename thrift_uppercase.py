# -*- coding: utf-8 -*-
import codecs
import fnmatch
import os
import sys

def convert_file_encoding(filename, src_encoding='UTF-8',target_encoding = 'UTF-8'):
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
    except Exception as e:
        print "exception: ",e
    finally:
        if f: f.close()

def walk(dir, file_extensions="*"):
    # short name
    path = os.path

    patterns = file_extensions.split(';')
    for root, dirs, files in os.walk(dir, False):
        for file in files:
            #print "check file ", file
            for pattern in patterns:
                if fnmatch.fnmatch(file, pattern):
                    yield path.join(root,file)


def convert_files(dir, file_extensions, src_encoding='GBK',target_encoding = 'UTF-8'):
    file_count = 0
    for file in walk(dir, file_extensions):
        print file
        convert_file_encoding(file, src_encoding, target_encoding)
        print u'文件转换完成',file
        file_count += 1
    print u"共转换文件 %d 个" % file_count
    return file_count

def main():
    
    #base_path = "E:\Corporations\Sohu\Projects\cloudatlas\cloudatlas-core\src"
    #file_extensions = "*.java;*.ice;*.thrift"
    
    if (len(sys.argv) < 1) : 
        print "argv error "
        return 
    
    dir = sys.argv[1]
    file_extensions = sys.argv[2]
    src_encoding = sys.argv[3]
    target_encoding = sys.argv[4]
    
    if not dir:
        print "please enter the dir "
        return
    
    if not os.path.exists(dir):
        print "error: dir %s doesn't exist!" % dir
        return 
    
    if not file_extensions: file_extensions = "*.java"    
    if not src_encoding: src_encoding = 'GBK'
    if not target_encoding: target_encoding = 'UTF-8'
    
    print "start convert file encoding, path = %s , file extension match = %s " % (dir, file_extensions)
    convert_files(dir, file_extensions, src_encoding, target_encoding)
    
    # todo  print help 


if __name__ == '__main__':
    main()


 