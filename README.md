API -- Usage:
--------------

ACCOUNTS:
_________
- Verify Account:
      api/user-auth/
      *curl -X GET -d "username=username&password=password" http://127.0.0.1:8000/api/user-auth/

- Create Account:
      api/user-create/
      example:  curl -X POST -d "username=createUser&email=user@example.com&password=password" http://127.0.0.1:8000/api/user-create/
      revert:   curl -X DELETE -d "username=createUser&password=password" http://127.0.0.1:8000/api/user-delete/

- Delete Account:
      api/user-delete/
      example:  curl -X DELETE -d "username=deleteUser&password=password" http://127.0.0.1:8000/api/user-delete/
      revert:   curl -X POST -d "username=deleteUser&email=user@example.com&password=password" http://127.0.0.1:8000/api/user-create/

- Change Account Username:
      api/user-update-username/
      example:  curl -X PUT -d "username=username&new_username=new_username&password=password" http://127.0.0.1:8000/api/user-update-username/
      revert:   curl -X PUT -d "username=new_username&new_username=username&password=password" http://127.0.0.1:8000/api/user-update-username/

- Change Account Email:
      api/user-update-email/
      example:  curl -X PUT -d "username=username&email=new_email@email.com&password=password" http://127.0.0.1:8000/api/user-update-email/
      revert:   curl -X PUT -d "username=username&email=email@email.com&password=password" http://127.0.0.1:8000/api/user-update-email/

- Change Account Password:
      api/user-update-password/
      example:  curl -X PUT -d "username=username&password=password&new_password=new_password" http://127.0.0.1:8000/api/user-update-password/
      revert:   curl -X PUT -d "username=username&password=new_password&new_password=password" http://127.0.0.1:8000/api/user-update-password/

- Get Account Credentials:
      api/get-account/user=<account_id>
      example: curl -X GET http://127.0.0.1:8000/api/user-get/username=a/password=a?format=json


DOCUMENTS:
__________
- Get Documents for Account:
      api/documents-get/username=<username>/password=<password>
      example: curl -X GET http://127.0.0.1:8000/api/documents-get/username=a/password=a?format=json

- Add Document to Account:
      api/document-add/
      example:  curl -X POST -H "Content-Type: application/json" -d '{"username":"username","password":"password","language":"Spanish","title":"My Title","text":"This is my lovely text that I will have to 'remove' double quotations from. :)"}' http://127.0.0.1:8000/api/document-add/

- Remove Document from Account:
      api/document-delete/
      example:  curl -X DELETE -d "username=username&password=password&document_id=1" http://127.0.0.1:8000/api/document-delete/




doc_translator
==============

Allows users to upload documents in a foreign language and click words they don't know to get a translation, powered by Google

Pitch: People who already know a foreign language know that it's not easy keeping up with it. This website will help those who want to practice their foreign language and receive a little help from the internet. 
  - This will facilitate users as they read their documents because they won't have to stop and look up words when they come across one that is unfamiliar. They will simply be able to click on a work and it's translation will quickly popup.

Description: Users will be able to upload documents that they would like to read. While they are reading, practicing, or studying the language they will be able to click on any work in the document. Clicking on a work will make an Ajax request using the google API to get the translation and show it in a modal popup.
  - We will allow for users to translate and use our web app with no account, however, if they wish to store documents they must create accounts to which the documents will be tied.
  - Ideally we would be able to assist in the translation of many documents, however, I'm afraid their may end up being a lot of problems with ASCII characters. So I'll only guarantee that Spanish will be translatable. Time permitting I'll work on getting other languages too.
  - The tranlations that popup will be modal windows that will be implemented using the google closure library.


- This is created to benefit people who are familiar with Spanish, yet would like a little help now and then to increase their comprehension.
- The users will be able to store uploaded documents specific to their accounts. 
    - Accounts and Uploaded files will be stored in a sql-light relational database.
- The front-end will be implemented using the AngularJS framework.
- The back-end will be implemented using Python's DJango framework.
