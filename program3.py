value=input(_)
if value>='a' and value<='z' or value>='A' and value<='Z':
  if value=='a' or value=='e' or value=='i' or value=='o' or value=='u' or value=='A' or value=='E' or value=='I' or value=='O' or value=='U':
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
