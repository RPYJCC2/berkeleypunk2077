label show_credits:
    call screen credits_scroll

screen credits_scroll():

    tag menu  # Ensures it replaces other screens like the main menu

    frame:
        style_prefix "credits"
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 20
                text "CREDITS" size 50
                text "Story: Brandon's wild imagination" size 30
                text "Art: ChatGPT 4o Image Generation" size 30
                text "Music: Mostly from Suno AI" size 30
                text "Labor Hours: 50 so far..." size 30
                text "Made with ❤️ using Ren'Py" size 30
                text "\n" * 20  # Forces enough space to scroll

    textbutton "Back" action Return() xalign 0.5 yalign 0.95
