"""
 Write a Python program for the following requirements.
Read a String statement from the command line
Findout total number of characters present in the statement.
Findout toal number of duplicate Characters in the statement
Findout total number of words present in the statement
Findout toal number of duplicate wordsin the statement
Reverse the characters present in the statement.
Reverse the words present in the statement.
Form a new statement from the reversed words.
Remove the duplicate characters from the latest statement.
Print final latest String statement.

"""
import collections

class String_Task():
    def __init__(self,statement):
        self.statement=statement
    def find_out_number_of_characters_present_in_statement(self):
        #iterate every element from input string(self.statement)
        iter_statment=[i  for i in self.statement]
        return "the number of characters present in statement {}".format(len(iter_statment)),iter_statment
    def Findout_total_number_of_duplicate_Characters_in_the_statement(self):
        #call the function
        iter_statment=self.find_out_number_of_characters_present_in_statement()[1]
        dict_char_count=dict(collections.Counter(iter_statment))

        duplicate_count={i:j for i,j in  dict_char_count.items() if dict_char_count[i]>1}.values()
        return "the dupicate character count in given statement is {}".format(sum(list(duplicate_count)))
    def find_total_words_present_in_given_statement(self):
        split_statemnt=self.statement.split()
        l1=[i for i in enumerate(split_statemnt)]
        return "total words in a given statement: {}".format(l1[-1][0]+1)

    def Find_duplicate_words_from_statement(self):
        statement=self.statement
        data=statement.split()


    def revese_the_character_present_in_the_statement(self):
        reverse_characters=[]
        [reverse_characters.insert(0,i) for i in self.statement]
        revers_the_character="".join(reverse_characters)
        return revers_the_character
    def reverse_the_words_which_are_present_in_the_statement(self):
        reverse_word= []
        [reverse_word.append(j) for i in self.statement.split() for j in [i[::-1]] ]

        revers_the_words= " ".join(reverse_word)
        return revers_the_words


    def Create_or_form_new_statement_from_existing_revese_words(self):
        #call the function which is have revese words
        form_new_statement=self.reverse_the_words_which_are_present_in_the_statement()
        return form_new_statement
    def remove_the_duplicate_chars_from_new_statement(self):
        #call the new form statment function here
        new_statement=self.Create_or_form_new_statement_from_existing_revese_words()
        for i in set(new_statement):
            if new_statement.count(i)>1:
                remove_duplicate_chars=new_statement.replace(i,"")
                new_statement=remove_duplicate_chars
        return remove_duplicate_chars
    def print_final_latest_statement(self):
        return self.remove_the_duplicate_chars_from_new_statement()








string_statemnt=input("enter statement")
string_statemnt1=input("enter statemnt1")
full_statemnt=string_statemnt+" "+string_statemnt1
obj=String_Task(full_statemnt)
find_character_length=obj.find_out_number_of_characters_present_in_statement()
print(find_character_length[0])

#find out duplicate characters present in statement

duplicate_character_in_statement=obj.Findout_total_number_of_duplicate_Characters_in_the_statement()
print(duplicate_character_in_statement)

#find out total words present in the given statement

#otal_words_in_given_statement=obj.find_total_words_present_in_given_statement()

#find out duplicate words from given statement
dupicate_words=obj.Find_duplicate_words_from_statement()
print(dupicate_words)

#print(total_words_in_given_statement)
#reverse the characters present in statement
reverse_the_characters=obj.revese_the_character_present_in_the_statement()
print(reverse_the_characters)
#reverser the words present in statement
reverse_the_words=obj.reverse_the_words_which_are_present_in_the_statement()
print("revese the words present in statement:-----  ",reverse_the_words)

#form a new statement from existing statement which is have reverse words
new_statement_with_rev_words=obj.Create_or_form_new_statement_from_existing_revese_words()
#print(new_statement_with_rev_words)

#Erase or remove duplicates from the new_statement
remove_duplicate_chars_new_statement=obj.remove_the_duplicate_chars_from_new_statement()
print(remove_duplicate_chars_new_statement)
final_statement=obj.print_final_latest_statement()
print("final_statement:",final_statement)

