import operace_s_ukoly as osu

while osu.user_input != "4":

    osu.hlavni_menu()

    if osu.user_input == "1":
        osu.pridat_ukol()
    elif osu.user_input == "2":
        osu.zobrazit_ukoly()
    elif osu.user_input == "3":
        osu.odstranit_ukol()
    elif osu.user_input not in ["1", "2", "3", "4"]:
        print()
        print("Zadána neplatná volba. Zadejte prosím znovu.")

print()
print("Konec programu.")
print()