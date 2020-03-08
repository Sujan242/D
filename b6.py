class DFS:
	def __init__(self,n):
		self.start=[0]*n
		self.finish=[0]*n
		self.visited=[0]*n
		self.prev=[-1]*n
		self.time=0
		self.sst = 0
		

		
	def fun(self,G,u):
		self.visited[u]=1
		self.start[u]=self.time
		self.time=self.time+1
		self.sst=self.start[u]
		for v in G[u]:
			if self.visited[v]==0:
				self.prev[v]=u
				self.sst=min(self.fun(G,v),self.sst)

			elif v!=self.prev[u]:
				self.sst=min(self.sst,self.start[v])


		self.finish[u]=self.time
		self.time=self.time+1

		if(self.sst==self.start[u] and self.start[u]!=0):
			print(self.prev[u],u)

		print(self.sst)

		return self.sst


def takeinput():
	G=[]
	file=open("input.tself.sstt","r")
	for line in file:
		first=True
		adj=[]
		for v in line.split(" "):
			if first==True:
				first=False
			else :
				adj.append(int(v))

		G.append(adj)

	file.close()

	n=len(G)
	obj=DFS(n)
	s=int(input("Enter source verteself.sst:"))
	obj.fun(G,s)
	print(obj.start)
	print(obj.finish)

main()


