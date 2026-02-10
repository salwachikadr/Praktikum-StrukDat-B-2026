'''
List digunakan untuk menyimpan banyak item dalam satu variabel.
List dibuat menggunakan tanda kurung siku [ ].
'''
#CHANGE STRING TO LIST
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)     #output akan berupa list dari variabel this list

#ALLOW DUPLICATES
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)     #output akan mencetak variabel thislist

#LIST LENGTH
thislist = ["apple", "banana", "cherry"]
print(len(thislist))        #ouput akan menghasilkan berapa panjang dari variabel thislist

#TYPE
#Akan mencetak tipe data dari list
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

#ACCESS LIST================================================================================
    #negative indeks
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])     #output cherry, karena mundur dari 0 ke -1    
    
    #Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        #output dari indeks 0-4 karena 5 tidak dimasukkan

    #Check if Item Exists


mylist = ["apple", "banana", "cherry"]
print(type(mylist))