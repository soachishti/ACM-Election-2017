import random

data = [('acm100', '@tji13'), ('acm101', '@biq88'), ('acm102', '@zpr14'), ('acm103', '@znd80'), ('acm104', '@crj41'), ('acm105', '@lfq65'), ('acm106', '@fiv72'), ('acm107', '@njp63'), ('acm108', '@jum93'), ('acm109', '@ple68'), ('acm110', '@jzp85'), ('acm111', '@imi42'), ('acm112', '@urv59'), ('acm113', '@emf98'), ('acm114', '@stp21'), ('acm115', '@pmz17'), ('acm116', '@wje24'), ('acm117', '@ojn48'), ('acm118', '@whn24'), ('acm119', '@vsi10'), ('acm120', '@kup88'), ('acm121', '@gak71'), ('acm122', '@mfe50'), ('acm123', '@psw45'), ('acm124', '@idc88'), ('acm125', '@jpa71'), ('acm126', '@qpl83'), ('acm127', '@ovq97'), ('acm128', '@kqx84'), ('acm129', '@iul82'), ('acm130', '@xkz67'), ('acm131', '@grs45'), ('acm132', '@tcz37'), ('acm133', '@lkt36'), ('acm134', '@bjz61'), ('acm135', '@zlz85'), ('acm136', '@pia40'), ('acm137', '@jdr88'), ('acm138', '@fbx86'), ('acm139', '@gmd44'), ('acm140', '@ees46'), ('acm141', '@sim46'), ('acm142', '@ldg39'), ('acm143', '@dxr35'), ('acm144', '@dqj68'), ('acm145', '@iox49'), ('acm146', '@acp90'), ('acm147', '@epn78'), ('acm148', '@kfp92'), ('acm149', '@fov59')];

for i in data:
	print "U: " + i[0] + "\tP: " + i[1]

"""
az = "abcdefghijklmnopqrstuvwxz"
result = []
for i in range(100, 150):
	username = "acm" + str(i)
	password = "@" + random.choice(az) + random.choice(az) + random.choice(az) + str(random.randint(10,99))
	
	result.append((username, password))

print result
"""