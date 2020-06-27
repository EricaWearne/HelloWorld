wizard_list = ['spider leg', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
wizard_list[2]='snail tongue'
wizard_list.append('bear burp')
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
del wizard_list[5]
del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
sorcerer_list = ['amulet', 'jewel', 'figurine', 'decorative piece', 'charcoal inscription', 'skull', 'scarab']
print(wizard_list[0] + " " + sorcerer_list[0])
print(wizard_list[1] + " " + sorcerer_list[1])
print(wizard_list[2] + " " + sorcerer_list[2])
print(wizard_list[3] + " " + sorcerer_list[3])
print(wizard_list[4] + " " + sorcerer_list[4])
magic_tools = wizard_list + sorcerer_list
print(magic_tools*3)
