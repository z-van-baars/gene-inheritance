import random


def plus1(x):
    return (x + 1)


def plus5(x):
    return (x + 5)


def minus1(x):
    return (x - 1)


def minus5(x):
    return (x - 5)

basepairs = {'A': plus1(1), 'B': plus5(1), 'C': minus1(1), 'D': minus5(1)}
bases = ['A', 'B', 'C', 'D']


def build_strand(l):
    strand = []
    for x in range(l):
        choice = random.choice(bases)
        strand.append(choice)
    return strand

strand1 = build_strand(20)
strand2 = build_strand(200)

print strand1[4]
input("?")

print "none"