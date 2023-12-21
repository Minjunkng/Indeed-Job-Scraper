import grabdata as g

job = "engineer"
g1 = g.Main(job)
data = g1.run_playwright()
print(data)