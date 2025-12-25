from thonny import get_workbench
from thonny.workbench import SyntaxThemeSettings


def pastel_cyberpunk() -> SyntaxThemeSettings:
    pink = "#FE97AC"
    mint = "#ACE99C"
    violet = "#B48CFF"
    cyan = "#7DF9FF"
    peach = "#FFB7A5"

    fg = "#EAEAF0"
    bg = "#12131A"
    bg_gutter = "#1A1C26"
    bg_line = "#1E2130"
    bg_sel = "#2A2E40"

    comment = "#7B8199"

    return {
        "TEXT": {
            "background": bg,
            "foreground": fg,
            "insertbackground": cyan,
        },

        "GUTTER": {
            "background": bg_gutter,
            "foreground": comment,
        },

        "current_line": {"background": bg_line},
        "sel": {"background": bg_sel, "foreground": fg},

        # Syntax
        "keyword": {"foreground": pink, "font": "BoldEditorFont"},
        "definition": {"foreground": violet, "font": "BoldEditorFont"},
        "builtin": {"foreground": violet},

        "string": {"foreground": mint},
        "string3": {"foreground": mint},
        "open_string": {"foreground": mint},
        "open_string3": {"foreground": mint},

        "number": {"foreground": cyan},
        "operator": {"foreground": peach},

        "comment": {"foreground": comment},

        "surrounding_parens": {
            "background": bg_sel,
            "foreground": peach,
            "font": "BoldEditorFont",
        },
    }


def load_plugin() -> None:
    get_workbench().add_syntax_theme(
        "Pastel Cyber",
        "Default Dark",
        pastel_cyberpunk,
    )
