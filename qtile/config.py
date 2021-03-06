"""
    _    _
   | |  | |
   | |__| |_   _  __ _  ___
   |  __  | | | |/ _` |/ _ \
   | |  | | |_| | (_| | (_) |
   |_|__|_|\__,_|\__, |\___/
    / __ \| (_)   __/ | (_)
   | |  | | |___ |___/__ _ _ __ __ _
   | |  | | | \ \ / / _ \ | '__/ _` |
   | |__| | | |\ V /  __/ | | | (_| |
    \____/|_|_| \_/ \___|_|_|  \__,_|
Adapted by Hugo Oliveira.
"""
import os
import re
import socket
import subprocess
from typing import List
from customization import colors, font_size, font_chosen
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

from libqtile.utils import guess_terminal

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

mod = "mod4"
#terminal = guess_terminal()
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
   # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Launch Rofi"),
#    Key([mod], "space", lazy.spawn("rofi -show run -icon-theme 'dracula' -show-icons"), desc="Launch Rofi"),
    Key([mod], "space", lazy.spawn("rofi -combi-modi window,drun,ssh -icon-theme 'dracula' -font 'MesloLGS NF Bold 10' -show combi -show-icons"), desc="Launch Rofi"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Control Volume and Brightness

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

]

#groups=[] # type: ignore
#group_names = ["1", "2", "3", "4", "5", "6",]
#group_labels = ["???", "???", "???", "???", "???", "???",]
#group_layouts = ["columns", "columns", "columns", "columns", "columns", "columns",]

#groups = [Group("???", layout='columns'),
#          Group("???", layout='columns'),
#          Group("???", layout='columns'),
#          Group("???", layout='columns'),
#          Group("???", layout='columns'),
#          Group("???", layout='columns'),
#          Group("???", layout='columns'),
#          ]


#groups = [Group(i) for i in '123456789']

#groups = [Group(group_names[i],group_layouts[i].lower(),group_labels[i]) for i in range(len(group_names))]

#for i in groups:
#    keys.extend(
#        [
#            Key(
#                [mod],
#                i.name,
#                lazy.group[i.name].toscreen(),
#            ),
#
#            Key(
#                [mod, "shift"],
#                i.name,
#                lazy.window.togroup(i.name, switch_group=True),
#            ),
#        ]
#    )

group_names = [("???", {'layout': 'columns',}),
               #("???", {'layout': 'columns', 'matches':[Match(wm_class=["Alacritty"])]}),
               ("???", {'layout': 'columns',}),
               ("???", {'layout': 'columns'}),
               ("???", {'layout': 'columns', 'matches':[Match(wm_class=["libreoffice-writer", "", "", "", ""])]}),
               ("???", {'layout': 'columns', 'matches':[Match(wm_class=["code-oss", "gedit"])]}),
               ("???", {'layout': 'columns', 'matches':[Match(wm_class=["Telegram", "TelegramDesktop"])]}),
               ("???", {'layout': 'columns', 'matches':[Match(wm_class=["viewnior"])]}),
               ("???", {'layout': 'columns'}),
               ("???", {'layout': 'floating', 'matches':[Match(wm_class=["Org.gnome.Nautilus"])]})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layouts = [
    layout.Columns(
        border_focus_stack=["#8befd", "#8be9fd"],
        border_focus=["#83a598", "#83a598"],
        border_width=4,
        fair = False,
        margin_on_single = [5, 5, 5, 5],
        margin = [5,5,5,5],
        ),

    layout.Max(
        border_width=4,
        fair = False,
        margin_on_single = [5, 5, 5, 5],
        margin = [5,5,5,5],
    ),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    layout.MonadTall(
        border_focus_stack=["#5e81ac", "#5e81ac"],
        border_focus=["#8be9fd","#8be9fd"],
        border_width=4,
        fair = False,
        margin_on_single = [7, 7, 7, 7],
        margin = [7,7,7,7],
        ),
    #layout.Floating(),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font=font_chosen,
    fontsize=font_size,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font = font_chosen,
                    fontsize = 15,
                    margin_y = 4,
                    margin_x = 3,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors[2],
                    inactive = colors[7],
                    rounded = True,
                    highlight_color = colors[1],
                    highlight_method = "line",
                    this_current_screen_border = colors[6],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[6],
                    other_screen_border = colors[4],
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.TextBox(
                    text=' | ',
                    foreground = colors[2],
                    background = colors[0],
                    ),
                    
                widget.CurrentLayout(
                    #custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    foreground = colors[2],
                    background = colors[0],
                    fontsize = font_size,
                    padding = 0,
                    scale = 0.7,
                    ),

                widget.TextBox(
                    text=' | ',
                    foreground = colors[2],
                    background = colors[0],
                    ),

                widget.Prompt(
                    foreground = colors[2],
                    background = colors[0],
                    font = font_chosen,
                    ),
                widget.WindowName(
                    foreground = colors[2],
                    background = colors[0],
                    fontsize = font_size,
                    font = font_chosen,
                    ),
                # widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
               # widget.CurrentScreen(
               #     active_color = colors[2],
               #     foreground = colors[2],
               #     background = colors[0]
               #     ),
                widget.TextBox(
                    text='???',
                    foreground = colors[2],
                    background = colors[0],
                    ),
                widget.Wlan(
                    foreground = colors[2],
                    background = colors[0],
                    disconnected_message = 'No Internet',
                    font = font_chosen,
                    update_interval = 5,
                    format='{essid} - {percent:2.0%}',
                ),

                widget.TextBox(
                    text=' | ',
                    foreground = colors[2],
                    background = colors[0],
                    ),

                widget.Systray(
                    foreground = colors[2],
                    background = colors[0],
                    font = font_chosen,
                    ),

                widget.TextBox(
                    text=' | ',
                    foreground = colors[2],
                    background = colors[0],
                    ),

                widget.Battery(
                    battery = 0,
                    charge_char='??? Charging',
                    discharge_char='??? Descharging',
                    #full_char = 'Battery Full',
                    unknown_char='??? --',
                    font=font_chosen,
                    fontsize= font_size,
                    foreground=colors[2],
                    background = colors[0],
                    low_foreground=colors[0],
                    format="{percent:2.0%} {char}",
                    low_percentage=0.2,
                    notify_below=20,
                    update_interval=10,
                ),

                widget.TextBox(
                    text=' | ',
                    foreground = colors[2],
                    background = colors[0],
                    ),

              widget.Volume(
                    foreground = colors[2],
                    background = colors[0],
                    fmt = '??? {}',
                    padding = 5,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                    #emoji = True,
                    ),

                widget.TextBox(
                    text=' | ',
                    foreground = colors[2],
                    background = colors[0],
                    ),

                widget.Clock(
                    format="%d-%m-%Y  %I:%M %p",
                    foreground = colors[2],
                    background = colors[0],
                    fontsize = font_size,
                    font = font_chosen,
                    ),

                widget.TextBox(
                    text=' | ',
                    foreground = colors[2],
                    background = colors[0],
                    ),

                widget.QuickExit(
                    foreground = colors[2],
                    background = colors[0],
                    default_text = '??? ',
                    fontsize = font_size,
                    font = font_chosen
                    ),
            ],
            28,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Volume Control"),  # GPG key password entry
        Match(title="Settings"),  # GPG key password entry
        Match(title="Network Connections"),  # GPG key password entry
        Match(title="Backups"),  # GPG key password entry
        Match(title="Tilda"),  # GPG key password entry
        Match(title="Power Manager"),  # GPG key password entry
        #Match(title="Signal"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
