def getKeys():
	return ['port', 'flow_up', 'flow_down', 'transfer', 'sspwd', 'enable' ]
	#return ['port', 'u', 'd', 'transfer_enable', 'passwd', 'enable', 'plan' ] # append the column name 'plan'

def isTurnOn(row):
	return True
	#return row['plan'] == 'B' # then judge here

