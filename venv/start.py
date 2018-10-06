#!/usr/bin/env python3
# ****************************************
# Site Management
# ****************************************
# Apache 2 site management script
# 2018 (c) Volodymyr Nerovnia
#
# ****************************************

import argparse
import os
import shutil
import re
import zipfile
import tarfile

# Path to sities
apcfgp = os.path.join('/etc', 'apache2', 'sites-available')
wp = os.path.join('/var', 'www')
tavhp = 'tavh'
tvhfn = 'template.vh'

p_dist_cms_dr_8 = 'distros/php/cms/drupal/8/d-8.6.1.tar.gz'
p_dist_cms_wp_4 = 'distros/php/cms/wordpress/4/wp-4.9.8.tar.gz'
p_dist_cms_yii_1 = 'distros/php/cms/yii/1/yii-1.1.20.tar.gz'
p_dist_cms_yii_2b = 'distros/php/cms/yii/2/yii-a-2.0.15.tar.gz'
p_dist_cms_yii_2a = 'distros/php/cms/yii/2/yii-b-2.0.15.tar.gz'
p_dist_forum_BB_3 = 'distros/php/forums/phpBB/phpBB-3.2.3.tar.gz'


def print_decription():
  print( "*********************************************")
  print(" Apache 2 site management script")
  print(" 2018 (c) Volodymyr Nerovnia")
  print("*********************************************")
  print("Usage: cns [action] [cms] domain_name")
  print("Option\t\t\tMeaning")
  print(" Actions:")
  print(" create\t\t\tCreate new site")
  print(" enable\t\t\tEnable exist site")
  print(" disable\t\tDisable exist site")
  print(" drop\t\t\tDrop exist site")
  print(" CMS:")
  print(" d8\t\t\tDrupal 8")
  print(" wp\t\t\tWordPress")
  print(" yii1\t\t\tyii 1")
  print(" yii2b\t\t\tyii 2 basic")
  print(" yii2a\t\t\tyii 2 advanced")
  print(" fbb\t\t\tforum phpBB")

def check_domain(domain):
  if os.path.isfile(os.path.abspath(os.path.join(apcfgp, domain + '.conf'))):
    return True
  return False

def check_source(domain):
  if os.path.isdir(os.path.abspath(os.path.join(wp, domain))):
    return True
  return False

def dec_zip(s_path, d_path):
  zf = zipfile.ZipFile(s_path)
  zf.extractall(d_path)
  zf.close()

def dec_targz(s_path, d_path):
  tar = tarfile.open(s_path)
  tar.extractall(d_path)
  tar.close()

def create_site(args):
  # проверка на существование конфигурации домена и каталога с исходниками
  # выводится подсказка о существовании конфигурации домена или каталога с исходниками
  # и на этом действие программы прекращается
  # создаем конфигурацию домена и копируем исходники в зависимости от указанной CMS
  is_present_domain = False
  is_present_source = False 

  p_dist_arch = ''
  # Определяем требуемый дистрибутив
  if args.cms == 'd8':
    p_dist_arch = p_dist_cms_dr_8
  if args.cms == 'wp':
    p_dist_arch = p_dist_cms_wp_4
  if args.cms == 'yii1':
    p_dist_arch = p_dist_cms_yii_1
  if args.cms == 'yii2b':
    p_dist_arch = p_dist_cms_yii_2b
  if args.cms == 'yii2a':
    p_dist_arch = p_dist_cms_yii_2a
  if args.cms == 'fbb':
    p_dist_arch = p_dist_forum_BB_3

  # Проверка существования настроек домена и установки
  # Если отсутствуют то создаем
  if check_domain(args.domain):
    is_present_domain = True
  if check_source(args.domain):
    is_present_source = True
  if not (is_present_domain and is_present_source):
    if os.access(apcfgp, os.R_OK):
      with open(tavhp + '/' + tvhfn, 'r') as t_file:
        with open(apcfgp + '/' + args.domain + '.conf', 'w') as s_file:
          for strline in t_file.readlines():
            str = re.sub(r'\[domain_name\]', args.domain, strline)
            s_file.write(str)
      dec_targz(p_dist_arch, wp + '/' + args.domain)
      enable_site(args)
    else:
      print("Permission denied to apache2 configuration directory!")
    print("Domain and source is absend!")


def enable_site(args):
  # проверка на существование конфигурации домена
  print("enable")
  print(args.domain)
  os.system('a2ensite ' + args.domain)
  os.system('systemctl reload apache2')

def disable_site(args):
  # проверка на существование конфигурации домена
  print("disable")
  print(args.domain)
  os.system('a2dissite ' + args.domain)
  os.system('systemctl reload apache2')

def drop_site(args):
  # проверка на существование конфигурации домена и каталога с исходниками
  print("drop")
  print(args.domain)


def parse_args():
  """Настройка argparse"""
  parser = argparse.ArgumentParser(description='Apache2 site management utility')
  subparsers = parser.add_subparsers()
  parser_append = subparsers.add_parser('create', help='Create new site')
  parser_append.add_argument('domain', help='Domain name')
  parser_append.add_argument('cms', help='CMS')
  parser_append.set_defaults(func=create_site)


  parser_append = subparsers.add_parser('enable', help='Enable site')
  parser_append.add_argument('domain', help='Domain name')
  parser_append.set_defaults(func=enable_site)

  parser_append = subparsers.add_parser('disable', help='Disable site')
  parser_append.add_argument('domain', help='Domain name')
  parser_append.set_defaults(func=disable_site)

  parser_append = subparsers.add_parser('drop', help='Drop site')
  parser_append.add_argument('domain', help='Domain name')
  parser_append.set_defaults(func=drop_site)

  return parser.parse_args()

def main():
  print_decription()
  args = parse_args()
  args.func(args)


main()
