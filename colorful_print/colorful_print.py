def print_format_table():
  """prints table fo format options.
  """
  for style in range(8):
    for fg in range(30, 38):
      s1 = ''
      for bg in range(40, 48):
        fmt = ';'.join([str(style), str(fg), str(bg)])
        s1 += u'\x1b[%sm %s \x1b[0m' % (fmt, fmt)
        print(s1)
    print('\n')


print('Before')
print_format_table()
print('After')
