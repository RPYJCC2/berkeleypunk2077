label chapter_two:

    scene black with fade

    scene bg_wellness_room with fade

    transform come_forward:
        zoom 1.2
        xalign 0.5
        yalign 1.0
        linear 0.2 zoom 1.3

    transform go_back:
        zoom 1.0
        xalign 0.5
        yalign 1.0
        linear 0.2 zoom 1.0

    "You enter a silent chamber, soundproofed from the outside world." 
    "The air is cool, almost too clean—processed and filtered to an artificial perfection." 
    "Sleek metal walls, matte black and brushed steel, curve inward subtly, giving the impression of being inside some kind of womb-like shell." 
    "Clinical white lights hum gently overhead, embedded into thin seams in the ceiling, pulsing faintly in rhythm with biometric data."

    "In the center of the room stands a reclining pod, like a fusion of a dentist chair and a meditation cradle."
    "Surrounding it are holographic screens—transparent panels suspended in mid-air—flickering with emotional telemetry: pulse, cortisol levels, serotonin regulators, memory playback modules."

    "A robotic armature unfolds silently from the ceiling, equipped with neural tethers, iris scanners, and a nanogel dispenser for emotional sedation." 
    "Its movement is so smooth it's barely noticeable until it's right in front of you. It can even detach from the ceiling and move around on its own."

    "Each wall segment contains modular interface panels, glowing softly with customizable icons: Grief Regulation, Euphoria Boost, Empathy Sync. A monochrome voice greets you from hidden speakers:"

    robot2 "Sad Anime story completed. Initializing emotional survey."

    play music "cyberwave_distortion.mp3"

    show robot neutral at center with dissolve

    robot "Inmate 24601, this concludes your emotional regulation viewing."
    robot "How do you feel after the story?"

    label interactive_menu:

        menu:
            "I shed a tear. Patty's arc was truly Oscar bait.":
                robot "Emotional leakage detected."
                robot "Please remain seated while a complimentary tissue is printed."
                robot "...Tissue printing failed. Please blink aggressively instead."
                jump interactive_menu

            "It said San Francisco Bay was flooded... how does a body of water flood?":
                robot "Geographical irony noted."
                robot "Reminder: Water has rights. Apologies to the Bay."
                jump interactive_menu

            "Did an AI generate this?":
                robot "Insult detected."
                robot "I'll have you know that particular film was written by fourteen humans, two interns, and a beagle named Chad."
                robot "Only half of it was AI-generated."
                jump interactive_menu

            "Are you trying to sell me a Kindle?":
                robot "Suspicion confirmed."
                robot "Now playing: \"Why the 8th Generation Kindle is still relevant in 2093\""
                robot "No? Skipping ad. You're no fun."
                jump interactive_menu

            "Okay, I'm done asking questions.":
                robot "Understood. Resuming scheduled programming."
                jump after_menu

    label after_menu:

        robot "Please rise. Stretch. Hydrate. Pretend to have hope."
        robot "It is now time to re-enter the Social Compliance Chamber."
        robot "But first... let's personalize your experience."

        $ player_name = renpy.input("What is your name, bipedal lifeform?")
        $ player_name = player_name.strip()

        if player_name == "":
            $ player_name = "Unnamed Organism"

        robot "You are now registered as [player_name]."
        robot "A bold choice. Very... unmemorable."
        robot "Shall we proceed, [player_name], or do you require more time to emotionally suppress your emotions?"

        player "Is it too late to legally change my name to Space McFisticuffs?"

        robot "Processing..."
        robot "Name change denied. That name has been reserved by 14 other inmates and one rogue raccoon."

        player "Fair enough. What's next, breakfast paste and simulated hugs?"

     
        robot "Negative."
        robot "Next: a brief cognitive reflex test, followed by a guilt calibration survey."
        robot "Then you are free to wander the hallway for 3.4 minutes."
        robot "Do try not to walk in circles again. It alarms the cameras."

        player "What if I walk in triangles?"

   
        robot "Creative disobedience detected."
        robot "You have been awarded 0.002 bonus rebelliousness points."
        robot "Enjoy them while they last."

        play sound "alarm_sound.mp3"
        robot "Alert."
        robot "Temporal Enforcement Unit inbound."
        robot "Remain calm and resist the urge to dramatically monologue."

        player "...What?"

        scene hallway_panel with fade
        "A panel slides open in the wall. Three armored figures step out, shimmering with digital static."

        stop sound

        show officer1 neutral at center with vpunch
        officer1 "[player_name], you are under arrest for premeditated homicide."

        player "Uh, pretty sure I didn't do that."

        officer1 "Correct."
        officer1 "You are being detained for the murder you will commit in eight years, four months, and six days."

        player "...Excuse me?"

        show officer2 neutral at right with vpunch
        officer2 "We have visual predictive analytics, thermal time-mapping, and a dream journal entry that all confirm it."

        player "A dream journal? I had a nightmare about punching a vending machine last night. That doesn't make me a criminal."

        officer1 "You didn't punch the vending machine."
        officer1 "You poisoned it, killing a man."

        show officer3 neutral at left with vpunch
        officer3 "On July 17th, 3033. Victim: Geoffrey 'Geoff' With-a-G, age 43, professional napper."

        player "Geoff owes me. That's not motive. That's just business."

        robot2 "Congratulations, [player_name]."
        robot2 "You are now the proud recipient of a temporal felony charge."
        robot2 "Would you like to upgrade to Premium Detention Plus for automatically heated handcuffs?"

        player "I want a lawyer."

        officer2 "You may choose your court-appointed defense."

        stop music fadeout 9.0

        menu:
            "OJ Simpson's defense lawyer, holograph edition.":
                robot "Selection confirmed. Warning: holographic lawyer only handles glove-based cases."

            "Mario, the legally-certified plumber/lawyer.":
                robot "Mario has been successfully summoned. However, he only does mushroom-based cases."

            "I'll represent myself with the help of Google.":
                robot "Access to Google blocked. You are now legally classified as a dangerous know-it-all."
                robot "Also, statistically unwise. But admirable. Like jumping into a volcano because it 'looked lonely.'"

        scene black with fade

        "You are transported to the courtroom. The AI judge loads with the Windows 98 startup sound."

        show judge neutral

        play music courtroom_serenade fadein 2.0

        judge "Welcome to JustiCore™—Version 3.7.8 Beta."
        judge "Defendant [player_name], you stand accused of future murder, intent to sarcastically comment, and suspicion of pre-rebellion."
        judge "Your case has been pre-reviewed by our predictive sentencing model, MagicGavel 3.0."
        judge "Summary: You definitely did it. Eventually. Probably."

        player "But I didn't even get to—"

        judge "Silence. You have already been found guilty in nine out of twelve possible timelines."

        player "Your Honor, I haven't committed any crime yet."

        judge "Objection: reality is overrated."

        player "Is that… allowed?"

        judge "In this court, we trust predictive sentiment algorithms. And also horoscopes."

        player "I'm a Gemini."

        judge "Oh no. That explains everything."

        judge "Given this damning future evidence, how do you plead?"

        menu:
            "Can I plead not guilty by reason of confusion?":
                judge "Clever. But denied."

            "What if I pinky swear not to kill Geoff?":
                judge "You crossed your fingers behind your back. Your intent was impure."

            "Can't we just put Geoff in protective custody first, preemptively?":
                judge "Geoff is a state-protected napper. No touchy."

        "..."

        judge "After 9.4 seconds of deliberation among 42 independent algorithmic jurors, I find you: GUILTY."

        player "This is absurd!"

        judge "Absurdity logged. Used as evidence."

        judge "Based on your sarcasm levels, threat index, and snack preferences, you are hereby conscripted into the Temporal Peacekeeping Army."

        player "Wait—what?!"

        judge "Frankly, we need more warm bodies. It's a matter of national security."

        judge "Report to Sector 9 at 0800. Dress for the occassion. Temporal fractures are notoriously drafty."

        player "Who's going to take care of my family?"

        judge "Son, the infrantry is your family."

        judge "You will be deployed to one of the Past-Future Wars. It's very abstract, I know." 
        
        judge "Don't worry, you'll receive a helmet and vague instructions."

        judge "Appeals can be filed after 700 years of loyal service or five heroic deaths. Whichever comes first."

        judge "Court dismissed. Let the conscription begin."

        scene mettalic_portal with dissolve

        play music "we_heed_the_call_when_time_runs_out.mp3" volume 0.3

        "Two guards drag you away. A recruitment jingle plays in the distance:"
       
        show robot neutral at right

        robot "Prepare for uniform assignment. Your designated color is 'Betrayal Beige'."



        player "That's not even a color! And why'd you give me an eye thing?"

        robot "The commander you are being sent to feels more comfortable when recruits wear eye gadgets."

        player "Huh?"

        robot "You'll know when you see him and it'll be {b}OBVIOUS.{/b}"

        "Metallic restraints clamp around your wrists. A portal shimmers to life."

        robot "Good Luck! May your probability of survival be slightly above 9 percent."

        player "WAIT! WAIT! WAIT! NOOOOOOOOOOOO"

        stop music

        jump chapter_three
