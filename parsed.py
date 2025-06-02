

class Parser:
    def __init__(self, path:str) -> None:
        """
    A class used to store and manipulate the action groups and key-pairs from
    the given desktop file.

    Attributes
    ----------
    path:str
      the location of the desktop file to open and parse its content

    Methods
    -------
    add_key(key, pair, locale=None, group=None)
      adds a key to parsed desktop file
    rem_key(key, locale=None, group=None)
      removes a key from parsed desktop file
    get_key(key, locale=None, group=None)
      gets the value of a key from parsed desktop file
        """
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
        """
    Adds a key to the currently parsed desktop file or changes its value if key
    already exists.

    If the `locale` argument is not specified or given `None` then it'll assume
    the unlocalised key is requested.

    If the `group` argument is not specified or given `None` then it'll assume
    the key from the "Desktop Entry" group is requested; if it is a string
    starting with "X-" then the group from which the key is requested will be
    left untouched from the given argument, otherwise the key from the
    corresponding "Desktop Action" group will be requested.

    Parameters
    ----------
    key : str, mandatory
      the name of the key itself to be added or changed
    pair : str | None, mandatory
      the value of the key to be added or changed
    locale : str | None = None, optional
      the locale of the key to be added or changed
    group : str | None = None, optional
      the group to which add or change the key value
        """
        keystring = self.get_keystring(key, locale, group)
        pair = "" if pair is None else pair
        self.data[keystring] = pair

    def rem_key(self,
                key:str,
                locale:str|None=None,
                group:str|None=None
                ) -> None:
        """
    Removes a key to the currently parsed desktop file.

    If the `locale` argument is not specified or given `None` then it'll assume
    the unlocalised key is to be removed.

    If the `group` argument is not specified or given `None` then it'll assume
    the key from the "Desktop Entry" group is to be removed; if it is a string
    starting with "X-" then the group from which the key is removed will be
    left untouched from the given argument, otherwise the key from the
    corresponding "Desktop Action" group will be removed.

    Parameters
    ----------
    key : str, mandatory
      the name of the key itself to be removed
    locale : str | None = None, optional
      the locale of the key to be removed
    group : str | None = None, optional
      the group to which remove the key
        """
        keystring = self.get_keystring(key, locale, group)
        if keystring in self.data:
            self.data.pop(keystring)

    def get_key(self,
                key:str,
                locale:str|None=None,
                group:str|None=None
                ) -> str|None:
        """
    Gets a key from the currently parsed desktop file.

    If the `locale` argument is not specified or given `None` then it'll assume
    the unlocalised key is to be retrieved.

    If the `group` argument is not specified or given `None` then it'll assume
    the key from the "Desktop Entry" group is to be retrieved; if it is a
    string starting with "X-" then the group from which the key is to be
    retrieved will be left untouched from the given argument, otherwise the key
    from the corresponding "Desktop Action" group will be retrieved.

    Parameters
    ----------
    key : str, mandatory
      the name of the key itself to be retrieved
    locale : str | None = None, optional
      the locale of the key to be retrieved
    group : str | None = None, optional
      the group from which retrieve the key
        """
        keystring = self.get_keystring(key, locale, group)
        if keystring in self.data:
            return(self.data[keystring])
        return(None)
