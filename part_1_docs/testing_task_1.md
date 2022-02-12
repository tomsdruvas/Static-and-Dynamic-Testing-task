### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # should be == and not =
      return True
    else
    #need to add a colon ":"
      return False


# 1)if card.value = 1 needs to be double equals(==)
# 2) there needs to be a : after else   
   

  dif highest_card(self, card1 card2):
  # dif should be def
  if card1.value > card2.value:
    return card
  else:
    return card2

# 1)instead of dif there needs to be def
# 2)the indentation between first and second liune wasnt right
# 3) comma after the card1 parameter is missing
# 4) in the first return statement needs to be card1 as that is the parameter mentioned in the first line
  


def cards_total(self, cards):
  total
  # total should equal something, most liekly 0
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
