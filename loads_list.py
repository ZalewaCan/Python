print("Enter location"); loc1 = input()
print("Product type"); prod1 = input()
print("Enter start gauge"); loc1sg = int(input())
print("Enter end gauge"); loc1eg = int(input())
tot1 = loc1sg - loc1eg
print("Enter location"); loc2 = input()
print("Product type"); prod2 = input()
print("Enter start gauge"); loc2sg = int(input())
print("Enter end gauge"); loc2eg = int(input())
tot2 = loc2sg - loc2eg
print("Enter location"); loc3 = input()
print("Product type"); prod3 = input()
print("Enter start gauge"); loc3sg = int(input())
print("Enter end gauge"); loc3eg = int(input())

tot3 = loc3sg - loc3eg

wide = 60
print('-' * wide)
print('|    Location    |Gauge start|Gauge end| Total|Product type|')
print('*' * wide)
print('|%16s| %9i | %7i | %4i | %10s |' % (loc1, loc1sg, loc1eg, tot1, prod1))
print('|%16s| %9i | %7i | %4i | %10s |' % (loc2, loc2sg, loc2eg, tot2, prod2))
print('|%16s| %9i | %7i | %4i | %10s |' % (loc3, loc3sg, loc3eg, tot3, prod3))
print('-' * wide)
print()
print('Total hauled today', tot1 + tot2 + tot3, 'm3')
