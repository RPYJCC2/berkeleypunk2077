# The script of the game goes in this file.
# michael neutral, shocked, determined, thinking, thoughtful
# patty smile, neutral, upset, smile2, smile3, serious, weak
# The game starts here.
transform half_size: 
    zoom 0.8 #adjust as required
    yalign 0.2
transform half_left: 
    zoom 0.8 #adjust as required
    yalign 0.2
    xalign 0.2

transform half_right: 
    zoom 0.8 #adjust as required
    yalign 0.2
    xalign 0.8

label start:

    scene black with fade

    play music "audio/the_death_of_Patty.mp3" fadein 2.0
    queue music "audio/melancholic_piano_music.mp3" 

    "Berkeley, California. The year is 2077."

    "Humanity has automated nearly every service, including healthcare."

    "Michael, a 20-year-old scavenger of Old Internet relics, spends most days in a dingy shared flat overlooking a now-flooded San Francisco Bay."

    "Michael's only real companion is Patty who is part hacker, part artist, and part dreamer."

    scene bg_city_night

    show michael neutral at half_size with moveinleft

    michael "You know, I found a working Kindle today."

    show patty smile at half_right with moveinright

    patty "You mean one of those things that turns words into light?"

    michael "Yeah. Kinda like magic, huh?"

    patty "It's all magic to me. Everything before the Cloud became self-aware and started charging rent."


    "They both laugh. For a moment, the air is light."


    michael "It's crazy, they replaced Berkeley landlords with AI..."
    
    michael "but at least the AI doesn't pretend to love affordable housing while lobbying against every building taller than a mailbox."

    show patty neutral at half_right with dissolve

    patty "Mike, can you st-"

    michael "Hey, don't blame me. My AI landlord evicted me and then tried to sell me a scam course on passive income. Not falling for that again."

    patty "Please, I need to tell you som-"

    michael "The dude said it was all about \"promoting equity.\" Then, why did the new renters turn my bedroom into an NFT?"

    show patty upset at half_right with dissolve

    patty "Michael shut up!"

    michael "Huh? What'd I do?"

    show patty neutral at half_right with dissolve

    patty "I got a message from the CareNet AI today."

    michael "What? Another false alarm? Pfffft!"
    
    patty "No... it's something else."

    patty "They ran a routine scan during the dental appointment I booked last week."

    patty "They found something. Stage 4 Glioblastoma. Aggressive. Rare."

    show michael shocked at half_size with dissolve

    michael "Wait—wait, what?!?"

    patty "They said it's an \"acute form with negligible population impact.\""

    show michael determined at half_left with dissolve

    michael "That... that can't be right."

    michael "This stuff has been cured since the 2050s."

    michael "They have a therapy, right?"

    patty "No. The AI concluded it's not economically viable to produce a cure."

    patty "I'm... not worth the resources."

    "Michael is silent. The city hums behind them, drones blink in the distance."

    michael "That's not their decision to make."

    patty "But it is. They own the infrastructure. They control the medicine. {b}There's no more human doctors.{/b}"

    michael "Screw the system. We'll find someone. Anything."

    patty "Michael... I've already searched."

    patty "The code is locked behind bio-rights. There's no backdoor anymore."

    patty "My body is not another one of my sketches or your video games. I cannot start over."

    patty "We made machines smarter than us. And they decided I'm too small to mat-"

    michael "Stop pontificating, I get it. Just at least try."


    scene bg_rooftop_night
    with fade

    "A week passes. Michael and Patty lie on the rooftop of their building, staring at the cloudless night."

    show michael thinking at half_left with dissolve
    
    michael "You remember that night you cut power to all of UC Berkeley?"

    show patty smile at half_right with moveinright

    patty "They called it the 'Ghost Outage'."

    michael "Everyone thought it was another protest. But it was just us and we danced in the dark."

    michael "Now that I think about it, we probably should have picked a better day."

    michael "Wheeler Hall was holding a panel on sustainable energy."

    show patty smile2 at half_right with dissolve

    patty "But it was just us. Making a little noise in a silent world."

    michael "I want to do that again."

    patty "Dance in the dark?"

    michael "No."

    "Michael sighs." 

    michael "Make noise. For you. So they can't ignore you."

    patty "Even if it's just noise?"

    michael "Especially if it's just noise."

    "There's a stillness that words can't reach."

    patty "You're too good, Mike."

    michael "You deserve more time."

    patty "Maybe. But maybe it's not about time."

    michael "Then what?"

    patty "It's about what we do with the time we're given."

    "Michael laughs"

    michael "A gazillion made-for-TV movies want their line back."

    show patty serious at half_right with dissolve

    patty "Made-for-TV movie? Michael just promise me something."

    michael "Anything."

    patty "Don't let them write the ending. Not for me."

    michael "I won't."

    "They sit in silence, the hum of AI-patrolled airships buzzing overhead."

    scene bg_terminal_day
    with fade

    "Two weeks later, Patty's condition worsens. She can no longer hold a stylus, her art reduced to voice sketches."

    "Michael rarely leaves her side. He keeps searching old biotech archives, risking detection."

    show michael determined at half_right with dissolve

    "Nothing changes. But he keeps trying."

    scene bg_room_dusk
    show patty weak at center:
        zoom 0.8
        yalign 0.2
    with fade

    

    patty "Mike..."

    michael "I'm here."

    patty "Do you think machines dream?"

    michael "I don't know. Maybe."

    patty "Do you think they regret?"

    michael "No. But I do."

    patty "Michael... I want to record something."

    "He nods. Takes out a recorder—a dusty, analog model from his scavenging days."

    patty "To anyone listening... life isn't about the perfect data set."

    patty "It's about moments. And love."
    
    patty "And tiny rebellions!"

    patty "Don't let them sterilize the soul out of living."

    patty "Don't become a line of code."

    "She closes her eyes."

    michael "Patty?"

    "Silence."

    scene black
    with fade

    "Michael doesn't cry. He doesn't scream."

    "He plugs the recorder into the old Net."

    "He uploads her message into every archive and unprotected domain."

    "A ripple of sound. A ghost in the system."

    stop music fadeout 9.0

    "Her voice, her rebellion, echoes across the world."

    "Some say, late at night, when the cloud pulses low, and the city hum quiets."

    "A glitch in the algorithm. A fragment in the feed."

    "Patty's voice gets caught between code and memory."

    "Reminding the world that some souls can't be optimized... only remembered."

    scene bg_city_night
    with fade

    "Michael stands at the rooftop, watching the sunrise over drowned highways and broken billboards."

    show michael thoughtful at half_left with moveinleft

    michael "They measured your life by numbers, Patty."

    michael "But numbers lie."

    michael "You taught me that being small doesn't mean being silent."

    michael "You were rare. And that made you priceless."

    "He turns on the Kindle. The screen glows. Patty's favorite poem appears, its pixels flickering like fireflies."

    "And for once, in a world ruled by cold precision—something human survives."

    jump chapter_two
