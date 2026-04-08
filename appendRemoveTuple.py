# DECLARATIONS

tupleBase = ('chien', 'chat', 'lapin', 'tigre')

tupleInLIst = list(tupleBase)
tupleInLIst.append('souris')
tupleInLIst.remove('chat')
tupleBase = tuple(tupleInLIst)

print(tupleBase)