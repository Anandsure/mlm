mlm={}
def getNames():
    main=input('Enter boss\'s name: ')
    a=input('Enter first person under him/her: ')
    b=input('Enter second person under him/her: ')
    mlm.update({main:[a,b]})
for i in range(3):
    getNames()
