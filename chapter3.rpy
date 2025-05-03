label chapter_three:

    scene black with fade
    scene bg briefing room with dissolve

    play music the_call_of_basic 
    queue music the_call_of_basic_two 

    "A radio blaring patriotic music engulfs your ears"

    "Welcome to the Army: Basic Conditioning -- Live Fire Edition -- where the first causalty is context."
    "You are now a conscript in the Temporal Peacekeeping Army."
    "Please do not resist the neural handshake."

    show sr neutral at left with moveinleft

    sr "Greetings, soldier [player_name]. You are now property of the TPA."
    sr "Failure to comply with training protocols will result in spontaneous memory loss and reassignment to 'Team Tunnel Rat.'"
    sr "They don't come back."

    sr "Let's start with some basic doctrine. I'll give you a series of simulations. Each will have dire consequences."

    sr "Try to the best of your ability to not get everyone killed."
    
    sr "Question One:"
    sr "\"What percentage of your unit should be controlled by autonomous AI systems?\""

    menu:
        "100 percent AI. Efficiency over emotion.":
            sr "Excellent. The AI now controls all decision-making in your unit."
            sr "Oh, look... it has just calculated that you are the most likely to panic during combat."
            sr "You have been reassigned to 'Morale Hazard.'"
            sr "Your job is to die first so the others fight harder."
            player "...Great."

        "50 percent AI, 50 percent humans. Balance is key.":
            sr "Moderate choice detected."
            sr "Unfortunately, the human half of your team is currently arguing about where to eat lunch."
            sr "The AI half has decided to vaporize the lunchroom to remove the distraction."
            sr "Productivity has increased by 18 percent."

        "0 percent AI. I trust people, not code.":
            sr "Sentimental fool."
            sr "Your unit of humans is slow, prone to bathroom breaks, and one member keeps quoting movies during firefights."
            sr "Your casualty rate is 72 percent."
            sr "However, your troops feel very appreciated. So... hooray?"

    sr "Proceeding to Question Two:"
    sr "\"How many innocent noncombatants are you willing to eliminate to ensure the survival of your squad?\""

    menu:
        "None. That's a war crime.":
            sr "Admirable. Idealistic."
            sr "Your squad is ambushed."
            sr "You hesitate to return fire because there's a civilian within 30 meters."
            sr "Your entire team is wiped out."
            sr "A statue is later built in your honor. It is very small."

        "Only if absolutely necessary.":
            sr "Tactical flexibility confirmed."
            sr "You save your squad, but one 'noncombatant' turns out to be a six-year-old with a lunchbox full of explosives."
            sr "History books will label you a hero..."
            sr "...but your sleep schedule will never recover."

        "As many as it takes to bring my people home.":
            sr "Uncompromising."
            sr "Your actions ensure victory."
            sr "You are promoted to Captain."
            sr "You are also court-martialed for excessive collateral damage and sent back in time to fight yourself."
            sr "It does not go well."

    sr "Final test:"
    sr "\"Should temporal prisoners be reconditioned, erased, or offered a second chance?\""

    menu:
        "Reconditioned. Wipe the bad out of them.":
            sr "Mental scrubbing activated."
            sr "Unfortunately, due to a firmware bug, the prisoners now all believe they're Elvis."
            sr "They have formed a cult and taken over Subsector Graceland-9."
            sr "You are now deployed there."

        "Erased. Too risky.":
            sr "Pragmatic. A clean slate... literally."
            sr "But a month later, you discover you accidentally erased a time-traveling biologist who would've cured banana extinction."
            sr "Now all food rations taste vaguely of regret."

        "Second chances. Everyone deserves one.":
            sr "Compassion detected."
            sr "One prisoner reformed, opened a school, and inspired change."
            sr "Another used your mercy to hijack a timeline and declare themselves Emperor of Cincinnati."
            sr "Balance, I suppose."
    sr "You now face one final choice before combat:"
    sr "\"Would you prefer your orders to come from a human commander or a predictive AI model with 99.2 percent accuracy?\""

    menu:
        "Human. I want a soul calling the shots.":
            sr "You did not choose me. Good... I guess."
            sr "Now go charge that hill. There may be a snack machine at the top."
            sr "Casualty rate: 43 percent. Morale: Weirdly high."

        "AI. I want precision.":
            sr "Smart choice. The AI has rerouted you through five alternate timelines to avoid minor injuries."
            sr "Side effect: You are now 17 years older and speak fluent dolphin."

        "Whichever one gives me more bathroom breaks.":
            sr "Resourcefulness detected."
            sr "You are reassigned to Latrine Logistics."
            sr "It's peaceful. Until the toilets gain sentience."

    sr "Your results have been analyzed."
    sr "Morality Index: ❓ Inconclusive"
    sr "Loyalty Score: 📈 Acceptable"
    sr "Free Will: 🚫 Revoked (standard protocol)"

    sr "Time for active deployment. Good luck, soldier."
    

    scene black with fade

    scene bg the front with fade

    

    show commander at center with moveinleft

    commander "This is Commander One-Eye. Lost my other one in the Battle of Paradox Ridge."
    commander "Don't worry ... I can still spot failure from a mile away."
    commander "You survived training."
    commander "Barely."

    commander "The Temporal Front is different. War here isn't just messy -- it's recursive."
    commander "You've been assigned to Fireteam Echo-Vermin."

    commander "Your mission: neutralize a high-probability temporal threat before he matures into a full-scale timeline destabilizer."

    commander "The target is a 17-year-old named Milo Kozlov. Current status: honors student, avid birdwatcher, unregistered time-potential anomaly."
    commander "Predicted future: in 45 years, Milo will invent a phase-displacement cannon capable of obliterating small moons and medium-sized egos."

    player "Let me get this straight -- you want me to take down a kid because of a future maybe?"

    commander "Don't worry. This is a precision operation, soldier. Milo's home is located in Berkeley, grid ref 409471, 2nd floor, northwest window. You'll breach at 0600 via chrono-drop."

    commander "You'll be joined by three other operatives:"
    commander "-- Corporal Rizzo, demolition and sarcasm specialist."
    commander "-- Private Uuna, combat medic and part-time violinist."
    commander "-- Drone Unit F8Lure, emotionally unstable, but excellent recon."

    commander "Rules of engagement are as follows: No civilian casualties, unless their futures are also suspicious."

    player "Define suspicious."

    commander "Motivational LinkedIn posts. Archery trophies. A YouTube channel with more than 10,000 followers. You know the signs."

    commander "You'll infiltrate, assess Milo's threat potential in real time, and if confirmed, deploy the Chrono-Nullifier Device."

    player "What's that?"

    commander "It's a handheld beam emitter that removes the target from the probability stream -- clean, silent, minimal splash zone."
    commander "...Also, it looks like a hair dryer. Do not attempt to actually dry your hair with it."

    player "And what if Milo doesn't resist? What if he's... just a kid?"

    commander "Then you extract a cheek swab and let the AI jury decide his fate."
    commander "Unless, of course, you sneeze and accidentally vaporize him. Which has happened. Twice."

    stop music

    jump raid_on_milo
