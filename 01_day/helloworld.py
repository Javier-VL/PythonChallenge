#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme.md

from sys import version

# 1 checar la version de python
print(version)

# 4 Check the data types of the following data:
list = [10,9.8,3.14,(4-4j),(['Asabeneh', 'Python', 'Finland']),"LO SIENTO BB"]

for x in range(len(list)):
    print(f"el tipo {type(list[x])} corresponde al elemento {list[x]}")

# find an eucliidan distance betwe (2,3) and (10,8)
# implementado con decoradores
def euclidian(two_points):
    def wraper(*args,**kwargs):
        print("achi es")
        res = two_points(*args,**kwargs)
        return res
    return wraper


@euclidian
def resta(p,q):
    return abs(p-q)

one_dimension = resta(10,17)

print(f"la distancia eucladiana en 1 dimension es de: {one_dimension}")