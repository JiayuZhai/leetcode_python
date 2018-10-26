import time
import sys
def main():
	n = sys.argv[1]
	t = time.asctime( time.localtime(time.time()) )
	s = '|' + str(n) + '|' + str(t)[:10] + str(t)[19:] + '|\n'
	with open('readme.md','a') as f:
		f.write(s)

if __name__ == '__main__':
	main()