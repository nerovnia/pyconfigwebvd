#!/usr/bin/env python3

import os, re
import tarfile, zipfile, lzma

def extract(arch_file_url, extract_path='.'):
  extRegexZIP = re.compile(r'.+\.zip$')
# https://docs.python.org/3.5/library/lzma.html
# https://docs.python.org/3.5/library/lzma.html#module-lzma
  extRegexXZ = re.compile(r'.+\.xz$')
# https://docs.python.org/3.5/library/lzma.html
# https://docs.python.org/3.5/library/lzma.html#module-lzma
# https://docs.python.org/3.5/library/tarfile.html
  extRegexLZMA = re.compile(r'.+\.lzma$')
# https://docs.python.org/3.5/library/tarfile.html
  extRegexGZIP = re.compile(r'.+\.gzip$')
# https://docs.python.org/3.5/library/tarfile.html
  extRegexBZ2 = re.compile(r'.+\.bz2$')
# https://docs.python.org/3.5/library/zlib.html#module-zlib
# https://docs.python.org/3.5/library/tarfile.html
  extRegexGZ = re.compile(r'.+\.gz$') 
# https://docs.python.org/3.5/library/tarfile.html
  extRegexTARGZ = re.compile(r'.+\.tar.gz$') 
# https://docs.python.org/3.5/library/tarfile.html
  extRegexTAR = re.compile(r'.+\.tar$') 
 
  options = { extRegexTAR : print('tar')
              extRegexZIP : print('zip')
  }


def zip(arch_file_url, extract_path='.'):

def xz(arch_file_url, extract_path='.'):

def lzma(arch_file_url, extract_path='.'):

def gzip(arch_file_url, extract_path='.'):

def bz2(arch_file_url, extract_path='.'):

def gz(arch_file_url, extract_path='.'):

def targz(arch_file_url, extract_path='.'):

def tar(arch_file_url, extract_path='.'):

#  print arch_file_url
#  if arch_file_url
#  tar = tarfile.open(arch_file_url, 'r')
#  for item in tar:
#    tar.extract(item, extract_path)
#    if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
#        extract(item.name, "./" + item.name[:item.name.rfind('/')])
#try:
#
#    extract(sys.argv[1] + '.tgz')
#    print 'Done.'
#except:
#    name = os.path.basename(sys.argv[0])
#    print name[:name.rfind('.')], '<filename>'
