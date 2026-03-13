#!/usr/bin/env python3

import objc
from AppKit import (
    NSApplication,
    NSApplicationActivationPolicyAccessory,
    NSStatusBar,
    NSVariableStatusItemLength,
    NSMenu,
    NSMenuItem,
    NSObject,
)
from Foundation import NSLog


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        self._status_item = (
            NSStatusBar.systemStatusBar()
            .statusItemWithLength_(NSVariableStatusItemLength)
        )
        self._status_item.setTitle_("telakka")   

        #Menu
        menu = NSMenu.alloc().init()

        quit_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Quit Telakka", "terminate:", "q"
        )
        menu.addItem_(quit_item)

        self._status_item.setMenu_(menu)

        NSLog("started — running as background process.")


def main():
    app = NSApplication.sharedApplication()

    # Hide from dock
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)

    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)

    app.run()


if __name__ == "__main__":
    main()

