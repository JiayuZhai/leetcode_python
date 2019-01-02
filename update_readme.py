#coding:utf-8
import os
import time
	
path = '.'
l = []
for root, dir, files in os.walk(path):
	for file in files:
		full_path = os.path.join(root, file)
		#print(full_path)
		if (file.endswith('.py')or file.endswith('.sql')or file.endswith('.sh')) and file.split('.')[0].isdigit():
			t = os.path.getctime(file)
			l.append([t,file.split('.')[0]])
l.sort()
i = 0
with open('README.md','w') as f:
	f.write('# leetcode_python\n刷题记录\n\n\n| Problem  |      Date     | Problem  |      Date     | Problem  |      Date     |\n|----------|:-------------:|----------|:-------------:|----------|:-------------:|\n')
	for ll in l:
		file_modify_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(ll[0]))
		f.write('|')
		f.write(ll[1] + '|' + file_modify_time)
		if i==2:
			f.write('|\n')
			i=0
		else:
			i+=1