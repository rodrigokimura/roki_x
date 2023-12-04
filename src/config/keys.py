from .models import Key

KEYBOARD_KEYS = [
    Key(name="A", value="A", description="``a`` and ``A``", icon="keyboard"),
    Key(name="B", value="B", description="``b`` and ``B``", icon="keyboard"),
    Key(name="C", value="C", description="``c`` and ``C``", icon="keyboard"),
    Key(name="D", value="D", description="``d`` and ``D``", icon="keyboard"),
    Key(name="E", value="E", description="``e`` and ``E``", icon="keyboard"),
    Key(name="F", value="F", description="``f`` and ``F``", icon="keyboard"),
    Key(name="G", value="G", description="``g`` and ``G``", icon="keyboard"),
    Key(name="H", value="H", description="``h`` and ``H``", icon="keyboard"),
    Key(name="I", value="I", description="``i`` and ``I``", icon="keyboard"),
    Key(name="J", value="J", description="``j`` and ``J``", icon="keyboard"),
    Key(name="K", value="K", description="``k`` and ``K``", icon="keyboard"),
    Key(name="L", value="L", description="``l`` and ``L``", icon="keyboard"),
    Key(name="M", value="M", description="``m`` and ``M``", icon="keyboard"),
    Key(name="N", value="N", description="``n`` and ``N``", icon="keyboard"),
    Key(name="O", value="O", description="``o`` and ``O``", icon="keyboard"),
    Key(name="P", value="P", description="``p`` and ``P``", icon="keyboard"),
    Key(name="Q", value="Q", description="``q`` and ``Q``", icon="keyboard"),
    Key(name="R", value="R", description="``r`` and ``R``", icon="keyboard"),
    Key(name="S", value="S", description="``s`` and ``S``", icon="keyboard"),
    Key(name="T", value="T", description="``t`` and ``T``", icon="keyboard"),
    Key(name="U", value="U", description="``u`` and ``U``", icon="keyboard"),
    Key(name="V", value="V", description="``v`` and ``V``", icon="keyboard"),
    Key(name="W", value="W", description="``w`` and ``W``", icon="keyboard"),
    Key(name="X", value="X", description="``x`` and ``X``", icon="keyboard"),
    Key(name="Y", value="Y", description="``y`` and ``Y``", icon="keyboard"),
    Key(name="Z", value="Z", description="``z`` and ``Z``", icon="keyboard"),
    Key(name="1", value="ONE", description="``1`` and ``!``", icon="keyboard"),
    Key(name="2", value="TWO", description="``2`` and ``@``", icon="keyboard"),
    Key(name="3", value="THREE", description="``3`` and ``#``", icon="keyboard"),
    Key(name="4", value="FOUR", description="``4`` and ``$``", icon="keyboard"),
    Key(name="5", value="FIVE", description="``5`` and ``%``", icon="keyboard"),
    Key(name="6", value="SIX", description="``6`` and ``^``", icon="keyboard"),
    Key(name="7", value="SEVEN", description="``7`` and ``&``", icon="keyboard"),
    Key(name="8", value="EIGHT", description="``8`` and ``*``", icon="keyboard"),
    Key(name="9", value="NINE", description="``9`` and ``(``", icon="keyboard"),
    Key(name="0", value="ZERO", description="``0`` and ``)``", icon="keyboard"),
    Key(name="ENTER", value="ENTER", description="Enter (Return)", icon="keyboard"),
    Key(
        name="RETURN",
        value="RETURN",
        description="Alias for ``ENTER``",
        icon="keyboard",
    ),
    Key(name="ESC", value="ESCAPE", description="Escape", icon="keyboard"),
    Key(
        name="BACKSPACE",
        value="BACKSPACE",
        description="Delete backward (Backspace)",
        icon="keyboard",
    ),
    Key(name="TAB", value="TAB", description="Tab and Backtab", icon="keyboard"),
    Key(name="SPACEBAR", value="SPACEBAR", description="Spacebar", icon="keyboard"),
    Key(name="SPACE", value="SPACE", description="Alias for SPACEBAR", icon="keyboard"),
    Key(name="-", value="MINUS", description="``-` and ``_``", icon="keyboard"),
    Key(name="=", value="EQUALS", description="``=` and ``+``", icon="keyboard"),
    Key(
        name="[",
        value="LEFT_BRACKET",
        description="``[`` and ``{``",
        icon="keyboard",
    ),
    Key(
        name="]",
        value="RIGHT_BRACKET",
        description="``]`` and ``}``",
        icon="keyboard",
    ),
    Key(
        name="\\",
        value="BACKSLASH",
        description=r"``\`` and ``|``",
        icon="keyboard",
    ),
    Key(
        name="#",
        value="POUND",
        description="``#`` and ``~`` (Non-US keyboard)",
        icon="keyboard",
    ),
    Key(
        name=";",
        value="SEMICOLON",
        description="``;`` and ``:``",
        icon="keyboard",
    ),
    Key(name="'", value="QUOTE", description="``'`` and ``\"``", icon="keyboard"),
    Key(
        name="`",
        value="GRAVE_ACCENT",
        description=r"````` and ``~``",
        icon="keyboard",
    ),
    Key(name=",", value="COMMA", description="``,`` and ``<``", icon="keyboard"),
    Key(name=".", value="PERIOD", description="``.`` and ``>``", icon="keyboard"),
    Key(
        name="/",
        value="FORWARD_SLASH",
        description="``/`` and ``?``",
        icon="keyboard",
    ),
    Key(name="CAPS LOCK", value="CAPS_LOCK", description="Caps Lock", icon="keyboard"),
    Key(name="F1", value="F1", description="Function key F1", icon="keyboard"),
    Key(name="F2", value="F2", description="Function key F2", icon="keyboard"),
    Key(name="F3", value="F3", description="Function key F3", icon="keyboard"),
    Key(name="F4", value="F4", description="Function key F4", icon="keyboard"),
    Key(name="F5", value="F5", description="Function key F5", icon="keyboard"),
    Key(name="F6", value="F6", description="Function key F6", icon="keyboard"),
    Key(name="F7", value="F7", description="Function key F7", icon="keyboard"),
    Key(name="F8", value="F8", description="Function key F8", icon="keyboard"),
    Key(name="F9", value="F9", description="Function key F9", icon="keyboard"),
    Key(name="F10", value="F10", description="Function key F10", icon="keyboard"),
    Key(name="F11", value="F11", description="Function key F11", icon="keyboard"),
    Key(name="F12", value="F12", description="Function key F12", icon="keyboard"),
    Key(
        name="PRINT SCREEN",
        value="PRINT_SCREEN",
        description="Print Screen (SysRq)",
        icon="keyboard",
    ),
    Key(
        name="SCROLL LOCK",
        value="SCROLL_LOCK",
        description="Scroll Lock",
        icon="keyboard",
    ),
    Key(name="PAUSE", value="PAUSE", description="Pause (Break)", icon="keyboard"),
    Key(name="INSERT", value="INSERT", description="Insert", icon="keyboard"),
    Key(
        name="HOME",
        value="HOME",
        description="Home (often moves to beginning of line)",
        icon="keyboard",
    ),
    Key(
        name="PAGE UP", value="PAGE_UP", description="Go back one page", icon="keyboard"
    ),
    Key(name="DEL", value="DELETE", description="Delete forward", icon="keyboard"),
    Key(
        name="END",
        value="END",
        description="End (often moves to end of line)",
        icon="keyboard",
    ),
    Key(
        name="PAGE DOWN",
        value="PAGE_DOWN",
        description="Go forward one page",
        icon="keyboard",
    ),
    Key(
        name="RIGHT ARROW",
        value="RIGHT_ARROW",
        description="Move the cursor right",
        icon="keyboard",
    ),
    Key(
        name="LEFT ARROW",
        value="LEFT_ARROW",
        description="Move the cursor left",
        icon="keyboard",
    ),
    Key(
        name="DOWN ARROW",
        value="DOWN_ARROW",
        description="Move the cursor down",
        icon="keyboard",
    ),
    Key(
        name="UP ARROW",
        value="UP_ARROW",
        description="Move the cursor up",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD NUMLOCK",
        value="KEYPAD_NUMLOCK",
        description="Num Lock (Clear on Mac)",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD /",
        value="KEYPAD_FORWARD_SLASH",
        description="Keypad ``/``",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD *",
        value="KEYPAD_ASTERISK",
        description="Keypad ``*``",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD -",
        value="KEYPAD_MINUS",
        description="Keyapd ``-``",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD +",
        value="KEYPAD_PLUS",
        description="Keypad ``+``",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD ENTER",
        value="KEYPAD_ENTER",
        description="Keypad Enter",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 1",
        value="KEYPAD_ONE",
        description="Keypad ``1`` and End",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 2",
        value="KEYPAD_TWO",
        description="Keypad ``2`` and Down Arrow",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 3",
        value="KEYPAD_THREE",
        description="Keypad ``3`` and PgDn",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 4",
        value="KEYPAD_FOUR",
        description="Keypad ``4`` and Left Arrow",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 5",
        value="KEYPAD_FIVE",
        description="Keypad ``5``",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 6",
        value="KEYPAD_SIX",
        description="Keypad ``6`` and Right Arrow",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 7",
        value="KEYPAD_SEVEN",
        description="Keypad ``7`` and Home",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 8",
        value="KEYPAD_EIGHT",
        description="Keypad ``8`` and Up Arrow",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 9",
        value="KEYPAD_NINE",
        description="Keypad ``9`` and PgUp",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD 0",
        value="KEYPAD_ZERO",
        description="Keypad ``0`` and Ins",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD .",
        value="KEYPAD_PERIOD",
        description="Keypad ``.`` and Del",
        icon="keyboard",
    ),
    Key(
        name="KEYPAD \\",
        value="KEYPAD_BACKSLASH",
        description=r"Keypad ``\`` and ``|`` (Non-US)",
        icon="keyboard",
    ),
    Key(
        name="APPLICATION",
        value="APPLICATION",
        description="Application: also known as the Menu key (Windows)",
        icon="keyboard",
    ),
    Key(name="POWER", value="POWER", description="Power (Mac)", icon="keyboard"),
    Key(
        name="KEYPAD EQUALS",
        value="KEYPAD_EQUALS",
        description="Keypad ``=`` (Mac)",
        icon="keyboard",
    ),
    Key(name="F13", value="F13", description="Function key F13 (Mac)", icon="keyboard"),
    Key(name="F14", value="F14", description="Function key F14 (Mac)", icon="keyboard"),
    Key(name="F15", value="F15", description="Function key F15 (Mac)", icon="keyboard"),
    Key(name="F16", value="F16", description="Function key F16 (Mac)", icon="keyboard"),
    Key(name="F17", value="F17", description="Function key F17 (Mac)", icon="keyboard"),
    Key(name="F18", value="F18", description="Function key F18 (Mac)", icon="keyboard"),
    Key(name="F19", value="F19", description="Function key F19 (Mac)", icon="keyboard"),
    Key(name="F20", value="F20", description="Function key F20", icon="keyboard"),
    Key(name="F21", value="F21", description="Function key F21", icon="keyboard"),
    Key(name="F22", value="F22", description="Function key F22", icon="keyboard"),
    Key(name="F23", value="F23", description="Function key F23", icon="keyboard"),
    Key(name="F24", value="F24", description="Function key F24", icon="keyboard"),
    Key(
        name="L CTRL",
        value="LEFT_CONTROL",
        description="Control modifier left of the spacebar",
        icon="keyboard",
    ),
    Key(
        name="CTRL",
        value="CONTROL",
        description="Alias for LEFT_CONTROL",
        icon="keyboard",
    ),
    Key(
        name="L SHIFT",
        value="LEFT_SHIFT",
        description="Shift modifier left of the spacebar",
        icon="keyboard",
    ),
    Key(
        name="SHIFT", value="SHIFT", description="Alias for LEFT_SHIFT", icon="keyboard"
    ),
    Key(
        name="L ALT",
        value="LEFT_ALT",
        description="Alt modifier left of the spacebar",
        icon="keyboard",
    ),
    Key(
        name="ALT",
        value="ALT",
        description="Alias for LEFT_ALT; Alt is also known as Option (Mac)",
        icon="keyboard",
    ),
    Key(
        name="OPT",
        value="OPTION",
        description="Labeled as Option on some Mac keyboards",
        icon="keyboard",
    ),
    Key(
        name="L GUI",
        value="LEFT_GUI",
        description="GUI modifier left of the spacebar",
        icon="keyboard",
    ),
    Key(
        name="GUI",
        value="GUI",
        description="Alias for LEFT_GUI; GUI is also known as the Windows key, Command (Mac), or Meta",
        icon="keyboard",
    ),
    Key(
        name="WIN",
        value="WINDOWS",
        description="Labeled with a Windows logo on Windows keyboards",
        icon="keyboard",
    ),
    Key(
        name="CMD",
        value="COMMAND",
        description="Labeled as Command on Mac keyboards, with a clover glyph",
        icon="keyboard",
    ),
    Key(
        name="R CTRL",
        value="RIGHT_CONTROL",
        description="Control modifier right of the spacebar",
        icon="keyboard",
    ),
    Key(
        name="R SHIFT",
        value="RIGHT_SHIFT",
        description="Shift modifier right of the spacebar",
        icon="keyboard",
    ),
    Key(
        name="R ALT",
        value="RIGHT_ALT",
        description="Alt modifier right of the spacebar",
        icon="keyboard",
    ),
    Key(
        name="R GUI",
        value="RIGHT_GUI",
        description="GUI modifier right of the spacebar",
        icon="keyboard",
    ),
]


MEDIA_KEYS = [
    Key(name="RECORD", value="RECORD", description="Record", icon="play circle"),
    Key(
        name="FAST FORWARD",
        value="FAST_FORWARD",
        description="Fast Forward",
        icon="play circle",
    ),
    Key(name="REWIND", value="REWIND", description="Rewind", icon="play circle"),
    Key(
        name="SCAN NEXT TRACK",
        value="SCAN_NEXT_TRACK",
        description="Skip to next track",
        icon="play circle",
    ),
    Key(
        name="SCAN PREVIOUS TRACK",
        value="SCAN_PREVIOUS_TRACK",
        description="Go back to previous track",
        icon="play circle",
    ),
    Key(name="STOP", value="STOP", description="Stop", icon="play circle"),
    Key(name="EJECT", value="EJECT", description="Eject", icon="play circle"),
    Key(
        name="PLAY PAUSE",
        value="PLAY_PAUSE",
        description="Play/Pause toggle",
        icon="play circle",
    ),
    Key(name="MUTE", value="MUTE", description="Mute", icon="play circle"),
    Key(
        name="VOLUME DECREMENT",
        value="VOLUME_DECREMENT",
        description="Decrease volume",
        icon="play circle",
    ),
    Key(
        name="VOLUME INCREMENT",
        value="VOLUME_INCREMENT",
        description="Increase volume",
        icon="play circle",
    ),
    Key(
        name="BRIGHTNESS DECREMENT",
        value="BRIGHTNESS_DECREMENT",
        description="Decrease Brightness",
        icon="play circle",
    ),
    Key(
        name="BRIGHTNESS INCREMENT",
        value="BRIGHTNESS_INCREMENT",
        description="Increase Brightness",
        icon="play circle",
    ),
]


MOUSE_KEYS = [
    Key(
        name="LEFT BUTTON",
        value="LEFT_BUTTON",
        description="Left mouse button.",
        icon="mouse",
    ),
    Key(
        name="RIGHT BUTTON",
        value="RIGHT_BUTTON",
        description="Right mouse button.",
        icon="mouse",
    ),
    Key(
        name="MIDDLE BUTTON",
        value="MIDDLE_BUTTON",
        description="Middle mouse button.",
        icon="mouse",
    ),
]

KEYS = KEYBOARD_KEYS + MEDIA_KEYS + MOUSE_KEYS
