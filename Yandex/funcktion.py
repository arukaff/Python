
 
s='<table border="1" width="100%">'
l= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
for i in l:
    s+='<tr><td>'
    s+=list(i.values())[0]
    s+='</td><td>'
    s+=list(i.keys())[0]
    s+='</td></tr>'
s+='</table>'
print(s)