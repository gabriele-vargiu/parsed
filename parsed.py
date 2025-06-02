

class Parser:
    def __init__(self, path:str) -> None:
        self.data = {}
        with open(path, "r", encoding="UTF-8") as file:
            groupstring = ""
            localestring = ""
            for line in file.readlines():
                line = line.split("#", 1)[0]
                line = line.strip()
                if line == "":
                    continue
                if line[-1] == "]" and line[0] == "[":
                    groupstring = line[1:-1]
                    continue
                if "=" not in line:
                    "=".join([line, ""])
                keywords = line.split("=", 1)
                key = keywords[0].strip()
                if "[" in key and key[-1] == "]":
                    key, localestring = key.split("[")
                    localestring = localestring[0:-1].strip()
                key = key.strip()
                pair = keywords[1].strip()
                self.data[".".join([groupstring, localestring, key])] = pair

    def get_keystring(self,
                      key:str,
                      locale:str|None=None,
                      group:str|None=None
                      ) -> str:
        """ For internal use only """
        localestring = "" if locale is None else locale
        if group is None:
            groupstring = "Desktop Entry"
        elif group[0:2] == "X-":
            groupstring = group
        else:
            groupstring = " ".join(["Desktop", "Action", group])
        keystring = ".".join([groupstring, localestring, key])
        return(keystring)

    def add_key(self,
                key:str,
                pair:str|None,
                locale:str|None=None,
                group:str|None=None
                ) -> None:
        keystring = self.get_keystring(key, locale, group)
        pair = "" if pair is None else pair
        self.data[keystring] = pair

    def rem_key(self,
                key:str,
                locale:str|None=None,
                group:str|None=None
                ) -> None:
        keystring = self.get_keystring(key, locale, group)
        if keystring in self.data:
            self.data.pop(keystring)

    def get_key(self,
                key:str,
                locale:str|None=None,
                group:str|None=None
                ) -> str|None:
        keystring = self.get_keystring(key, locale, group)
        if keystring in self.data:
            return(self.data[keystring])
        return(None)
