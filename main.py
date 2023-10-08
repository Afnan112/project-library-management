library = []
wishlist = []

# 1 => Adding Books In List libray
owns_books = input("\nenter the name of a books you won:")
library.append(owns_books)

owns_books = input("enter the name of another book you own(or press'enter' to skip):")

if owns_books:
  library.append(owns_books)
  
print(f"\nYour library: {library}")

# 2 => Adding Books In List Wishlist
wish_book = input("\nenter the name of a book you wish to have in the furure:")
wishlist.append(wish_book)

wish_book = input("enter the name of another book you to have(or press'enter' to skip):")
if wish_book:
  wishlist.append(wish_book)
  
print(f"\nYour wishlist: {wishlist}")

# 3 => Merging Wishlist into Library
acquired_book = input("\nenter the name of a book from your wishlist that you'v acquired(or press'enter'to skip)")
if acquired_book in wishlist:
  library.append(acquired_book)
  wishlist.remove(acquired_book)
  
print(f"\nUpdate library: {library}")
print(f"Updated wishlist: {wishlist}")


# 4 => Donating Books

donation_book = input("\nenter the name of a book your libraty you want tp donated it(or press'enter'to skip):")
if donation_book in library:
  library.remove(donation_book)
  
print(f"\nFinal library after donations: {library}")


