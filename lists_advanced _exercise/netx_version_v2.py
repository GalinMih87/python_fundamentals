version = input()
version = version.replace(".", '')
version = (int(version) + 1)
version = str(version)
print(".".join(version))