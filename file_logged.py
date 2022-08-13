

# data = [1.6,3.4,5.5,9.4];
# f = open("myfile.txt","x");
# for value in data:
#     record = str(value);
#     f.write(record);
#     f.write("\n");

# f.close();

f = open("myfile.txt","r");

for record in f:
    record = record.replace("\n","");
    print(record);
f.close();