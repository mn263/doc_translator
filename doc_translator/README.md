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
