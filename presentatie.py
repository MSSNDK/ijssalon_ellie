def presenteer(mijn_dict):
        for key, value in mijn_dict.items():
            print(f" {key} : {value} euro")
        print("==========================")
        values = mijn_dict.values()
        totaal = sum(values)
        print(f"Totaal = {totaal}")
mijn_dict = {"Vis": 10, "Vlees": 25, "Overige": 15}
presenteer(mijn_dict)