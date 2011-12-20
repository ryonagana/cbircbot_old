

class moduloteste():
	def __init__(self, moduleargs, config, engine):
		
		self.args = moduleargs()
		self.conf =  config
		self.client = engine
		self.args.cmdname = "nick"
		
		
		
		
		
		
		#src.Modules.IModule.__init__(self)
		
	def Execute(self, sender, channel):
		
		if(self.client.isConnected and self.client.isJoined):

			if( len(self.args.args) == 0):
				pass
			
			
			try:
			
				if(self.args.args[0].find(self.conf.nick) != -1 and self.args.args[1] == self.args.args.cmdname and self.args.args[2] != None or self.args.args[2] != ""):
					
					self.client.ChangeNick(self.conf.nick, self.args[2])
			
			except Exception:
				raise Exception
				
				
			


	
		
		
		

if __name__ == "__main__":
	moduloteste.__doc__