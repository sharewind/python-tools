# -*- coding: utf-8 -*-
import codecs
import fnmatch
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
    except Exception as e:
        print "exception: ",e
    finally:
        if f: f.close()

def walk(base_path, file_extensions="*"):
    # short name
    path = os.path

    patterns = file_extensions.split(';')
    for root, dirs, files in os.walk(base_path, False):
        for file in files:
            #print "check file ", file
            for pattern in patterns:
                if fnmatch.fnmatch(file, pattern):
                    yield path.join(root,file)

def main():
    base_path = "E:\Corporations\Sohu\Projects\cloudatlas\cloudatlas-core\src"
    file_extensions = "*.java;*.ice;*.thrift"

    if not os.path.exists(base_path):
        print "error: dir %s doesn't exist!" % base_path
    else:
        print "start convert file encoding, path = %s , file extension match = %s " % (base_path, file_extensions)

    file_count = 0
    for file in walk(base_path, file_extensions):
        print file
        convert_file_encoding(file)
        print u'文件转换完成',file
        file_count += 1
    print u"共转换文件 %d 个" % file_count


if __name__ == '__main__':
    main()


 