The terminal theme took so long... I don't think this was a great use of two hours of my winter break, but I'm counting it as productive because I learned a bit more about powershell.
### Steps
Find the config file (you can do `CTRL + SHIFT + P` and then select `"Open Settings (JSON)"` (there are two things that pop up if you search for it. the one with "default" in the name isn't editable so don't pick that). 
Then you can go to the `"Schemes"` part and paste these colors in between the `"[]"`
```
      {
            "name": "Pinkmint Dark",
            "background": "#12131A",
            "foreground": "#EAEAF0",
            "cursorColor": "#FE97AC",
            "selectionBackground": "#2A2E40",

            "black": "#1A1C26",
            "red": "#FFB7A5",
            "green": "#ACE99C",
            "yellow": "#FFB7A5",
            "blue": "#B48CFF",
            "purple": "#FE97AC",
            "cyan": "#7DF9FF",
            "white": "#EAEAF0",

            "brightBlack": "#3A3F5C",
            "brightRed": "#FFB7A5",
            "brightGreen": "#ACE99C",
            "brightYellow": "#FFB7A5",
            "brightBlue": "#B48CFF",
            "brightPurple": "#FE97AC",
            "brightCyan": "#7DF9FF",
            "brightWhite": "#FFFFFF"
        }

```
You will notice that the yellows are actually pink. I need to do a bit more work on this to figure out how it's actually calling them, because all the themes seem to use roughly the same colors? (If this is some programming equivalent of wire colors that I'm violating, I'm sorry... But at least it's just for me...)

Now just put the line `"colorScheme": "Pinkmint Dark"` in the config file for every profile object, like this:
```
{
    "name": "PowerShell",
    "source": "Windows.Terminal.PowershellCore",
    "colorScheme": "Pinkmint Dark"
}
```
