import pandas as pd

class Table:
    def __init__(self):
        self.table = {1:"-", 2:"-", 3:"-", 4:"-", 5:"-", 6:"-", 7:"-", 8:"-", 9:"-"}
        self.x = "x"
        self.o = "o"
        self.used = []
        self.available = list(self.table.keys())
        
    def show_table(self):
        return self.table.values()

    def show_used(self):
        return self.used()

    def is_number(self):
        num = True
        while num:
            try:
                insert = int(input("Number: "))
                print()
                num = False
                return insert
            except:
                print("wrong!")
                print(f"To be used: {self.available}")
                print(f"Used already: {self.used}")
                print()

    def change_table(self, user, available_list, used_list):
        print(f"Available moves: {self.available}")
        insert = self.is_number()
        if insert in available_list:
            if insert not in used_list:
                self.table[insert] = user
                self.used.append(insert)
                self.available.remove(insert)
                print(f"Used moves: {pd.Series(self.used).unique()}.")

        else: 
            print("again")
            print(f"To be used: {self.available}")
            print(f"Used already: {self.used}")
            return self.change_table(user, available_list, used_list)

    def run_table(self, change_table):
        change_table
        return self.show_table()



if __name__ == "__main__":
    t = Table()
    start = True
    while start:
        change = t.change_table("l", available_list= t.available, used_list= t.used)
        print(t.run_table(change))
