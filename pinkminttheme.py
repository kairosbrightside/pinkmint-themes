from thonny import get_workbench
from thonny.workbench import SyntaxThemeSettings


def pinkmint_dark() -> SyntaxThemeSettings:
    # Core palette (your pinkmint)
    pink = "#FE97AC"
    mint = "#ACE99C"
    soft_fg = "#E8ECEF"

    bg_main = "#15171C"
    bg_gutter = "#1C1F26"
    bg_line = "#20242C"
    bg_sel = "#2B2F36"

    comment_fg = "#7F8A8A"
    accent = "#9B8CFF"   # gentle violet for structure

    return {
        # Main editor
        "TEXT": {
            "background": bg_main,
            "foreground": soft_fg,
            "insertbackground": pink,
        },

        # Line numbers
        "GUTTER": {
            "background": bg_gutter,
            "foreground": comment_fg,
        },

        "current_line": {"background": bg_line},
        "sel": {"background": bg_sel, "foreground": soft_fg},

        # Syntax roles
        "keyword": {"foreground": pink, "font": "BoldEditorFont"},
        "definition": {"foreground": accent, "font": "BoldEditorFont"},
        "builtin": {"foreground": accent},

        "string": {"foreground": mint},
        "string3": {"foreground": mint},
        "open_string": {"foreground": mint},
        "open_string3": {"foreground": mint},

        "number": {"foreground": "#7DFFD4"},
        "comment": {"foreground": comment_fg},

        # Parenthesis matching
        "surrounding_parens": {
            "background": bg_sel,
            "foreground": pink,
            "font": "BoldEditorFont",
        },
    }


def load_plugin() -> None:
    get_workbench().add_syntax_theme(
        "Pinkmint Dark",
        "Default Dark",
        pinkmint_dark,
    )
