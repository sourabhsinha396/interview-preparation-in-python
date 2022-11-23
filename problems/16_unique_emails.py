import sqlite3
from typing import List


class Solution:
    def __init__(self):
            self.db = sqlite3.connect(':memory:')
            self.cursor = self.db.cursor()
            self.cursor.execute("""
            CREATE TABLE emailstore (
            email TEXT NOT NULL
            )
            """)
            
    def validate_if_email(self,email)->bool:
        #handle more than 1 @
        local_name,domain = email.split("@")
        if domain:
            return True
    
    def process_email(self,email:str)->str:
        """processes the '.' and '+' sign"""
        local_name,domain = email.split("@")
        new_email = ""
        for character in email:
            if character == "+":
                return new_email + "@" + domain
            elif character == ".":
                continue
            elif character == "@":
                return new_email + "@" + domain
            else:
                new_email+= character
        return new_email + "@" + domain
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        validated_emails = [] 
        for email in emails:
            validated_email = self.validate_if_email(email)
            validated_emails.append(validated_email)
        
        processed_emails = []
        for email in emails:
            processed_email = self.process_email(email)
            processed_emails.append(processed_email)
        
        print("processed_emails are",processed_emails)
        for email in processed_emails:
            print("inserting ",email)
            self.cursor.execute("INSERT INTO emailstore VALUES (?)", (email,))
            
        data = self.cursor.execute('''
        SELECT count(distinct(email)) from emailstore;
        ''')
        
        data = self.cursor.fetchall()
        
        return (data[0][0])
            
        
            
            
import pytest

iterable = (
    (["a@leetcode.com","b@leetcode.com","c@leetcode.com"],3),
    (["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],2)
)


@pytest.mark.parametrize("input,output",iterable)
def test_should_find_dictinct_emails_count(input,output):
    assert Solution().numUniqueEmails(input)==output