### parsed

A desktop file parser for python

### Description

Parsed is a lightweight .desktop file parser I've quickly bodged up for a project of mine. It is optimised at the best of my capabilities to be light on memory and be as quick as possible.

### Usage

`parsed` can be used to import an already existing .desktop file, add, remove and get keys from it and it allows to do such also specifying to perform those actions on the main desktop entry, a desktop action group or on a custom group [as specified by the freedesktop documentation](https://specifications.freedesktop.org/desktop-entry-spec/latest/extending.html) as follow:

```python
from parsed import Parser

file = Parser("path/to/file.desktop")

name_string = file.get_key("Name")
comment_string_it = file.get_key("Comment", "it")
exec_string = file.get_key("Exec")

action_name_string = file.get_key("Name", group="custom_action")
action_comment_string_it = file.get_key("Name", "it", "custom_action")
action_exec_string = file.get_key("Exec", group="custom_action")
```

### License

`parsed` was created by Gabriele Vargiu. It is licensed under the terms of the DWTFYWT public license.
