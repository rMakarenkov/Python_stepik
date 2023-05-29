# assert abs(-42) == 42, "Указанные в проверке выражения не возвращают значение True"

actual_result = "abrakadabra"
print("Wrong rext, got " + actual_result + ", something wrong")

string = "Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")
print(string)

# Example #1

str1 = "One"
str2 = "Two"
str3 = "Three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

# Example #2
str4 = f"Wrong rext, got {actual_result}, something wrong"
print(str4)

# FALSE
# assert self.catalog_link.text  == "Каталог", \
#    f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'"

#TRUE
# catalog_text = self.catalog_link.text  # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#    f"Wrong language, got {catalog_text} instead of 'Каталог'"
