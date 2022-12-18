"""Program 5. perform various opetrations on set like
union,insertion,difference etc.
"""


CODE:-
Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}
Days2 = {"Friday","Saturday","Sunday"}
print("set 1 is:-",Days1)
print("set 1 is:-",Days2)
print("\nThe Union is: \n",Days1|Days2) #printing the union of the sets
print("The Union(using .union() ) is: \n",Days1.union(Days2)) #printing
the union of the sets
print("\nThe intersection is: \n",Days1&Days2) #prints the intersection of
the two sets
print("The intersection(using .intersection() ) is: \
n",Days1.intersection(Days2)) #prints the intersection of the two sets
print("\nThe difference is: \n",Days1-Days2) #{"Wednesday", "Thursday"
will be printed}
print("The difference(using .difference() ) is: \n",Days1.difference(Days2))
#{"Wednesday", "Thursday" will be printed}
months1 = set(["January","February", "March", "April", "May", "June"])
months2 = set(["July","August","September","January","March"])
print("\nprinting the original set ... ")
print(months1 ,"\n",months2)
# Adding element in set
print("\nAdding other months to the set months1...");
months1.add("July");
months1.add ("August");
print("\nPrinting the modified set months1...");
print(months1)
# Updating the original set
print("\nupdating the original set months1... ")
months1.update(["July","August","September","October"]);
print("\nprinting the modified set months1... ")print(months1);
# removing elements from month
# 1. using remove function
print("\nRemoving some months from the set months1...(Using remove
function)");
months1.remove("January");
months1.remove("May");
print("\nPrinting the modified set months1...");
print(months1)
# 2. using discard function
print("\nRemoving some months from the set months1...(Using discard
function) ");
months1.discard("January");
months1.discard("May");
print("\nPrinting the modified set months1...");
print(months1)
print("\nThe Union is: \n",months1|months2)
print("The Union(using .union() ) is: \n",months1.union(months2))
print("\nThe intersection is: \n",months1&months2)
print("The intersection(using .intersection() ) is: \
n",months1.intersection(months2))
print("\nThe difference is: \n",months1-months2)
print("The difference(using .difference() ) is: \
n",months1.difference(months2))
