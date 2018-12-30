ba = int(input(" enter basic salary "))
if ba>5000:
    hra=15/100*ba
    da=150/100*ba
else:
    hra=10/100*ba
    da=110/100*ba
g= ba+hra+da
print("basic salary",ba,"hra is",hra,"da is",da,"gross salary is",g)
