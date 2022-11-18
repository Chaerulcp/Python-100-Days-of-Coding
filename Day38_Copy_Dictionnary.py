# copy dictionary

teman_teman = {
	"rul":"chaerul cp",
	"win":"darwin kabut",
	"han":"ramadhan loka",
	"raf":"asraf",
	"dar":"masdar"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["rul"]="chaerul cp"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir ajah)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")
