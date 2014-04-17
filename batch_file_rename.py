# -*- coding: utf-8 -*-
import codecs
import fnmatch
import os
import string

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
                    

def rename_file(dir, file_extensions, src_part, target_part):
    
    file_count = 0
    
    for file in walk(dir, file_extensions):
        src_file_name = str(file).decode("GBK")
        print src_file_name
        target_file_name = src_file_name.replace(src_part, target_part)
        print u'重命名文件',target_file_name
        os.rename(file, target_file_name)
        file_count += 1
        
    print u"共重命名文件 %d 个" % file_count
    return file_count

def main():
    dir = "F:\TDDOWNLOAD"
    file_extensions = "*.wmv"
    rename_file(dir, file_extensions, u"", '')

if __name__ == '__main__':
    main()


 