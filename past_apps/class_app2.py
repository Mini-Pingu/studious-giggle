class TagCloud:
    def __init__(self):
        self.__tags = {}
        # self.tags = {} # 在變量前加上 __ 可以改爲私人變量，不被外部訪問

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
# print(cloud.__tags)
cloud["python3"] = 10
cloud["python3"] = 20

print(cloud["p1ython"])
print(cloud["python3"])
print(cloud.__dict__)
# print(cloud.__tags["PYTHON"])
