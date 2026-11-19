books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {"Programming", "AI", "Software Engineering"}
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("==================================================")
print("         LIBRARY BOOK & CATEGORY MANAGER          ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\n--- Current Library Catalog (Fixed Records) ---")
        count = 1
        for book in books:
            title, author, year, category = book
            print(str(count) + '. "' + title + '" by ' + author + ' (' + year + ') | Genre: ' + category)
            count = count + 1
        print("Total Books:", len(books))

    elif choice == "2":
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        if title != "" and author != "" and year != "" and category != "":
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)
            print('\n[SUCCESS] "' + title + '" added as an immutable catalog record.')
            print('[INFO] Category set updated with: "' + category + '"')
        else:
            print("\n[ERROR] All fields are required.")

    elif choice == "3":
        print("\n--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print("- " + cat)
        print("Total Unique Genres:", len(library_categories))

    elif choice == "4":
        print("\n--- Add to Student Wishlist ---")
        req_cat = input("Enter requested category: ")
        if req_cat != "":
            student_wishlist.add(req_cat)
            print('[SUCCESS] "' + req_cat + '" added to student wishlist.')
        else:
            print("[ERROR] Please enter a valid category.")

    elif choice == "5":
        print("\n================= CATEGORY GAP ANALYSIS =================")
        print("Library Holdings (Set):", sorted(library_categories))
        print("Student Wishlist (Set):", sorted(student_wishlist))

        in_stock = library_categories & student_wishlist
        needed = student_wishlist - library_categories
        all_genres = library_categories | student_wishlist

        print("\n1. Already in Stock (Intersection &):")
        print("  ", sorted(in_stock))

        print("\n2. Purchase Order Needed (Difference -):")
        print("  ", sorted(needed))

        print("\n3. Full Combined Genre Coverage (Union |):")
        print("  ", sorted(all_genres))
        print("=========================================================")

    elif choice == "6":
        print("\nThank you for using the Library Manager. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please select from 1 to 6.")