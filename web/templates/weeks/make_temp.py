import toml
with open("../weeks.toml", 'r') as f:
    weeks_data = toml.load(f)['weeks']

for week in weeks_data:
    out = open(f"{week}.html", 'w') 
    print(f"""{{% extends 'base.html' %}}

{{% block content %}}
<h2>{ weeks_data[week]['title'] }</h2>
<p>
{{% endblock %}}""", file = out)

    

