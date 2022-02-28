# Python Challenge 

##  Observed so Far: 

- [x] Long Methods
- [ ] Many conditionals
- [ ] Repitition
- [ ] Negative Logic
- [ ] Similar Patterns

## Timeline:

### Day01 :

- Install the python and learn basics about how is it working. Then learned about the syntax of python and after that clone a repository and try solving this challenge. well at first it seems pretty ugly code (poorly formatted) but obviously that's what I have solve. 
- Then I spent alot of time just understanding what this is about and finally got to know what I have to do to solve this. well yeah just made my first test running yay!! that doesn't gives any logic to code but still 🎉 So first day was quite rough day for me. 

### Day02 :

- First thing We don't have to change the Item class, Only can make changes in gilded rose class. As we can see in the code we have only one method update quality method and that's generally a long method so can't really see where one concepts ends and different one begins.

#### So Basically gilded rose program is lacking one big thing there is no test around it. Lets create a test for it
- But a good thing in this code is we already have one test which was broken but I can use it to create other test cases.
- So its difficult which test I can do first and one thing which standouts from rest of code is ``` B-Dawg keychain never has to be sold or decrease in quality and also this item always have quality 80 ``` 😳 
- In test I have alwyas have to focus two things first is sellin and second is quality.
- So this test works item doesn't degrade in quality whatever the sellin date is so this test works 

- This test seems pretty easy to write lets do our 2nd test Good wine increase in quality the older it gets.

- Okay I am going to write couple of tests to see if its according to requirements and then refactoring the code would be more easy and alot simpler.✔️

- All tests done and working fine ✔️

### Its time to refactor the code :

- One of strangest item in whole code is B-Dawg keychain so lets refactor it first.
- I am just removing all the negative logics of B-Dawg keychain
``` if item.name == !'B-DAWG Keychain' ```
After removing that I have to test my code if its still working and they are still passing that's great ✅


##### Looking at the code I feel like I should age the good wine the same way. 

- Removed the negative logic ✅
- Remove else block. ✅
- Test Failed it means something went wrong ❌

#### I am going to keep using the same technique I have, this backstage pass.

- But before moving to that part I've seen there is duplication and repetition of code in Good wine so I am going to :
- Extract and create method for that and use in both situations. ✔️

- One thing I've learned so far is formatting the code properly indentation 🙅🏻‍♀️

- So much sneaky code so I am refactoring it.
- Multiple ifs change into if elif else 
- for quality greater than 0 to max(item.quality,0)

- And now test is working 👏🏼

- So refactoring part is almost done we can still avoid repitition of code by extracting method which I am going to do but still its fun part to do.