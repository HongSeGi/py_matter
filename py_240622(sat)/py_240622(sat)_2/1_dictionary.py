phone_book = {"전민호" : "010-8454-3004"}
phone_book["아무개"] = "010-1234-5678"
phone_book["그사람"] = "010-1478-9632"
# print(phone_book)
# print(phone_book["전민호"])
# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())
# print(type(phone_book.items()))

for name, phone_num in phone_book.items():
    print(name, ":", phone_num)

sorted_phone_book = sorted(phone_book.items())
print(type(phone_book))
print(type(sorted_phone_book))
print("--------------------------------")
sorted_phone_book = dict(sorted(phone_book.items(), key=lambda x: x[0]))
print(type(phone_book))
print(type(sorted_phone_book))

for name, phone_num in sorted_phone_book.items():
    print(name, ":", phone_num)