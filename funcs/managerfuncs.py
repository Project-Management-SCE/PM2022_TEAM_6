import sys
sys.path.append('../')


def get_data():
  f=open('manger/auth_data/authdata.txt')
  data=f.readlines()
  username=data[0].strip().split(':')[1]
  psw=data[1].strip().split(':')[1]

  return (username,psw)
