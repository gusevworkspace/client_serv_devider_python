#!/usr/bin/python

def parser(num):
	str_ans=''
	if num < 0:
		num *= -1
		end_num=-1
	else: 
		end_num=1
	if num==1:
		return 1
	
	
	contunue = True
	last = num
	while contunue:
		ret = devider(last)
		if ret !=1:
			last /= ret
			str_ans += "%s, " % (ret)
		else:
			str_ans += "%s, %s;" % (last,end_num)
			return str_ans

def devider(step):
	dev_flag = False
	for i in range(2,step):
		if step % i == 0:
			def_flag = True
			return i
	return 1


print "input a number"
ans = int(raw_input())

print parser(ans)
