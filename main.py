def HelloWorld(a):
    print(a);



HelloWorld("print");


nameOfFile = input();
extention = "";
flag = 0;
for c in nameOfFile:
    if c == '.':
        flag = 1;
    if flag:
        extention+=c;

if extention in [".txt", ".json", ".cvs", ".html", ".xml"]:
    HelloWorld("Все окей");
else:
    HelloWorld("Ты долбоеб");