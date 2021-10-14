label start:

    label setup:
        init python:
            renpy.music.set_volume(0, 0, channel="background_music")
            renpy.music.register_channel("background_music", "music", True)
        init python:
            renpy.music.set_volume(0, 0, channel="title")
            renpy.music.register_channel("title", "music", True)
        init python:
            renpy.music.set_volume(0, 0, channel="bg_noise")
            renpy.music.register_channel("bg_noise", "music", True)
        init python:
            renpy.music.register_channel("Radio", "music", True)
        init python:
            renpy.music.register_channel("Wind", "music", True)
        init python:
            renpy.music.register_channel("Hail", "music", True)
        init python:
            renpy.music.register_channel("Rain", "music", True)
        scene main_menu
        python:
            protagName = renpy.input("What is your name?", length=32)
            protagName = protagName.strip()
        transform cpSit:
            xpos 0.2
            ypos 0.1
        transform flip:
            xzoom -1
        transform thru_door:
            xpos .4
            ypos .1
            zoom .75
            xzoom 1

        label Variables:
            $ timer_range = 0
            $ timer_jump = 0
            $ nationalist_points = 0
            $ attendantConvo = 0
            $ friendship = 0
            $ nameKnown =False
            $ helped = 0
            $ nameVesta = 'Passenger'
            $ nameVestaU = 'The passenger'
            $ nameVestaL = 'the passenger'
            $ nameNell = 'Attendant'
            $ nameNellU ='The attendant'
            $ nameNellL='the attendant'

        label defineCharacters:
            define Pilot= Character("[protagName]")
            define Radio=Character("Radio")
            define Passenger=DynamicCharacter("nameVesta")
            define Vesta=DynamicCharacter("nameVestaU")
            define vesta=DynamicCharacter("nameVestaL")
            define Attendant=DynamicCharacter("nameNell")
            define Nell = DynamicCharacter("nameNellU")
            define nell = DynamicCharacter("nameNellL")


        """This game relies heavily on all the choices you make and don't make.

        This game will ask you to make certain decisions within a short time limit. In an effort to be more accommodating, you can choose how long you have to make a decision.

        Please choose a duration now."""

        menu:
            "5 seconds.":
                $ timeLimit=5
            "15 seconds.":
                $ timeLimit=15
            "30 seconds.":
                $ timeLimit=30

        transform alpha_dissolve:
            alpha 0.0
            linear 0.1 alpha 1.0
            on hide:
                linear 0.5 alpha 0
            # This is to fade the bar in and out, and is only required once in your script

        screen countdown():

            timer time repeat False action [ Hide('countdown'), Jump(timer_jump) ]
            bar value AnimatedValue(0, timeLimit, timeLimit, timeLimit) xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

    label Act1:
        label station_scenes:
            scene doma_station
            show main_menu
            show cp front behind main_menu
            stop music fadeout 3.0
            hide main_menu with fade
            play bg_noise 'audio/amb-sfx_train-station.mp3'
            play Radio 'audio/amb-sfx_radio-static.mp3'
            play background_music "audio/mus_ambient.ogg" fadein 3.0
            Radio """
            My friends, compatriots, and neighbors, do you feel it in the air? The buzz of excitement, the thrill of chance? The lust, no, love for justice that swirls through the streets?

            I do.

            That, my friends, is the feeling of a just democracy about to change course! The feeling of a movement about to make history!

            For those listeners who might not have picked up upon my meaning, I refer, of course, to the most pivotal election of the era.

            A chance for those who wish to see real change, real justice, real solutions!

            For far too long, we’ve allowed ourselves to become entrenched in our glorious past, too afraid of marring the legacy of our great city.

            We’ve polished the portraits of long-dead heroes while the walls we hide behind became too tarnished to recognize!

            But we have had enough! Yes, my neighbors, now is the time for change!
            """

            label choice1:
                $ time = timeLimit
                $ timer_range = timeLimit
                $ timer_jump = 'menu_neutral'
            show screen countdown
            menu:
                "{i}Keep listening to the radio.{/i}":
                    hide screen countdown
                    Radio """
                    I have promised you for many months that one day, we would rise from the pitted remains of this legendary city to claim the wastelands of Duoterra!

                    To finish the work that began hundreds of years ago to turn these landscapes from harsh to hospitable!

                    And now, after all of these promises, our movement is large enough to take the reigns of this city from the senile politicians who would wish to sink slowly into obscurity without protest!"""

                    menu:
                        "This is bullshit.":
                            $ nationalist_points -= 1
                        "This is pretty interesting.":
                            $ nationalist_points += 1
                    Radio """
                    I call on you, my friends, my fellow citizens of Domatellium, to take action, for tomorrow is the day we claim this city!

                    The day we may finally reignite the fire forgotten for too many years!

                    The day we refuse to let our--
                    """
                    stop Radio

                    jump choice1_end
                "{i}Turn off the radio.{/i}":
                    stop Radio
                    hide screen countdown
                    "{i}You turn the radio off.{/i}"
                    jump choice1_end
            label menu_neutral:#If the Player doesn't make a choice
                hide screen countdown
                stop Radio
                "You know, in times like these, if you’re always this indecisive, you’ll probably end up regretting it later."
            label choice1_end:
                show pass coat i at flip behind cp
            Passenger "Taxi!"
            Passenger "Can you take me to Viacaellum?"

            label choice2:
                $ timer_jump = 'menu_neutral2'
            show screen countdown
            menu:
                "Really? Wouldn't a transport be faster?":
                    hide screen countdown
                    $friendship -= 1
                    Pilot "Really? Wouldn't a transport be faster?"
                    Passenger "Please, can you just take me?"
                    Pilot "Fine. Do you have any bags?"
                    jump choice2_end
                "Yeah, of course.":
                    hide screen countdown
                    Pilot "Yeah, of course. Do you have any bags?."
                    show pass coat r
                    jump choice2_end
            label menu_neutral2:#If the Player doesn't make a choice
                hide screen countdown
                Pilot "Sure. Do you have any bags?"
                jump choice2_end
            label choice2_end:
                show pass coat r
                "{i}She looks down and shakes her head.{/i}"
                show pass coat
                Pilot "Alright, hop in."
            stop bg_noise
            hide pass
            hide cp
            with fade
            scene rd front
            show pass qu sit n at cpSit behind cp_backt
            show cp_backt
            show cp back behind pass
            with fade

        label small_talk_scenes:
            label choice3:
                $ timer_jump = 'menu_neutral3'
            show screen countdown
            menu:
                "So why are you heading to Viacaellum?":
                    hide screen countdown
                    jump friendly_small_talk_CS3
                "Why don't you have any luggage?":
                    hide screen countdown
                    jump hostile_small_talk_CS3
            label menu_neutral3:
                hide screen countdown
                show pass qu sit n
                "{i}[Vesta] looks out the window silently.{/i}"
                "{i}You reach to turn on the radio, but [vesta] breaks the awkward silence before you can turn it on.{/i}"
                show pass qu sit i
                Passenger "Is traffic always this bad?"
                show pass qu sit s
                Pilot "Not really, I think there’s some event happening tomorrow, but I’m not sure."
                "{i}She looks uncomfortable.{/i}"
                jump choice3_end
            label friendly_small_talk_CS3:
                $ friendship += 1
                Pilot "So why are you heading to Viacaellum? Are you going on vacation?"
                show pass qu sit t
                "{i}She pauses for a second, looking out the window.{/i}"
                show pass qu sit n
                Passenger "Sort of, I really just had to get out of town."
                Pilot "That’s fair. It’s good to get out of the city every once and a while."
                "{i}A slightly awkward silence falls between you two.{/i}"
                Pilot "I'm [protagName], by the way."
                Passenger "Oh, I'm Vesta."
                $ nameKnown=1
                $ nameVesta = 'Vesta'
                $ nameVestaU = 'Vesta'
                $ nameVestaL = 'Vesta'

                Passenger "So, how long have you been a pilot?"
                Pilot "It feels like I’ve been doing this forever."
                Passenger "Do you like being a pilot?"
                menu:
                    "It's my life's purpose.":
                        Pilot "Yeah, I love being able to travel around the planet, getting a break from it all."
                        jump job_talk_end
                    "It's alright, I guess.":
                        Pilot "Ah, you know, it’s alright, I guess. It’s what I know how to do, so I don’t really get the luxury of a choice."
                        jump job_talk_end
            label job_talk_end:
                show pass qu sit t
                "{i}She falls silent for a few minutes, watching buildings pass as you snake your way through Domatellium.{/i}"
                show pass qu sit i
                "{i}You reach to turn on the radio, thinking she is finished talking, but [vesta] breaks the awkward silence before you can turn it on.{/i}"
                Passenger "Is traffic always this bad?"
                Pilot "Not really, I think there’s some event happening tomorrow, but I’m not sure."
                show pass sit s
                "{i}She looks uncomfortable.{/i}"
                jump choice3_end
            label hostile_small_talk_CS3:
                $friendship -= 1
                Pilot "Why are you heading all the way to Viacaellum without any luggage? It’s a pretty long trip for a spur-of-the-moment decision."
                show pass qu sit i
                Passenger "What do you mean, a pretty long trip? All the advertisements say it’s only a few hours!"
                Pilot "Yeah, by transport. It’s nearly a week if I take you. What, did you think I can get to sub-orbit with this thing? Viacaellum is a quarter of the way across this planet!"
                show pass qu s
                Passenger "Fine. I don't care how long it takes."
                "{i}[Vesta] crosses her arms and stares out the window, glaring at the buildings slowly inching past.{/i}"
                show pass qu sit i
                Passenger "Is traffic always this bad?"
                Pilot "Not really, I think there’s some event happening tomorrow, but I’m not sure."
                show pass qu sit t
                "{i}[Vesta] sighs heavily, turning back to the window.{/i}"
                jump choice3_end
            label choice3_end:
                show pass qu sit s
                stop background_music
                play Radio 'audio/amb-sfx_radio-static.mp3'
                play title "audio/mus_title.ogg" fadein 1.0
                "{i}You turn on the radio to listen to some music.{/i}"
                play sound 'audio/sfx_space-engine.mp3'
                show pass qu sit n
                "{i}The radio begins to play music and [vesta] seems to relax somewhat as you reach the city walls.{/i}"
                stop background_music fadeout 5.0

        label talking_about_radio_scenes:
            "{i}Passing through the massive gate, you accelerate quickly, the city walls beginning to recede quickly in the background.{/i}"
            stop Radio
            stop title
            play background_music "audio/mus_ambient.ogg" fadein 3.0
            show pass qu sit s
            stop sound fadeout 1.0
            "{i}The radio shuts off abruptly, startling [vesta].{/i}"
            Passenger "Why did the radio just shut off?"

            label choice4:
                $ timer_jump = 'menu_neutral4'
                show screen countdown
            menu:
                "We lost reception.":
                    hide screen countdown
                    jump friendly_4
                "You didn't know? Really?":
                    hide screen countdown
                    jump hostile_4
            label menu_neutral4:
                hide screen countdown
                show pass qu sit n
                Passenger "Oh, it just does that sometimes."
                "{i}She shifts in her seat.{/i}"
                Pilot "There's an open bunk for you below the ship."
                hide pass qu sit s with dissolve
                "{i}Still looking uncomfortable, [vesta] heads down below.{/i}"
                jump choice4_end
            label friendly_4:
                $ friendship += 1;
                Pilot "Once you get out of the domes, you lose reception-something to do with ambient radiation or something."
                Pilot "There are a few spots where we'll be able to pick it up again, but we won't have it for most of the trip."
                show pass qu sit s
                Passenger "Oh."
                "{i}[Vesta] looks unsettled, shifting in her seat.{/i}"
                Pilot "Have you ever left Domatellium before?"
                show pass qu sit t
                Passenger "No, I never really had any reason to leave."
                Pilot "That explains it then. Most people who never leave the city wouldn't know about it."
                Pilot "You should head down below now and start setting up a bunk, though. There’s an empty wardrobe and a bunk bed that's yours until we get to Viacaellum."
                "{i}She nods and makes her way down the ladder, clearly shaken but glad to have a task.{/i}"
                hide pass qu sit n with dissolve
                "{i}You listen to her footsteps recede until the sound is overcome by the noise of the engines before turning your focus back to the open road.{/i}"
            jump choice4_end
            label hostile_4:
                $ friendship -= 1;
                Pilot "You didn't know? Really?"
                show pass qu sit i
                Pilot "Is this your first time out of the city or something?"
                "{i}[Passenger] nods, looking uncomfortable.{/i}"
                Pilot "Huh, that's weird. I can't imagine staying in the same place my whole life."
                "{i}She glares at you, clearly frustrated.{/i}"
                Pilot "Anyways, there’s an open bunk down below for you. You should go set up."
                hide pass qu sit i with dissolve
                "{i}[Vesta] gets up and heads down below, clearly happy to get away from your conversation.{/i}"
                "{i}You drive alone for a few hours.{/i}"
                jump choice4_end
            label choice4_end:

            hide pass
            hide cp
            hide cp_backt
            with dissolve
            scene black
            show pass qu sit n at sitAtTable
            show kn table2 behind pass
            show table2t
            show rd front
            pause 1
            hide rd front with Dissolve(1.0)
            pause .5

    label Act2:
        label Storm_Waring_Scene:
            transform sitAtTable:
                xpos .26
                ypos -.05
                zoom 2
                xzoom -1.0
            "{i}[Vesta] looks to you nervously, picking absentmindedly at the seat of her chair. The radio comes back on, startling her.{/i}"
            play Radio 'audio/amb-sfx_radio-static.mp3'
            play sound 'audio/sfx_weather_jingle.mp3'
            Radio "Attention all pilots, forecasters are warning everyone to take shelter in a dome or station for the time being."
            show pass qu sit s at sitAtTable behind table2t
            Radio "Storm Mutatio is predicted to hit within the week and will be one of the worst storms Duoterra will encounter this year."
            stop Radio
            Passenger "Do you think the storm will hit us before we reach Viacaellum?"
            label Storm_Warning:
                $ timer_jump = 'menu_neutral_Storm_Warning'
            show screen countdown
            menu:
                "Do you want to turn back?":
                    hide screen countdown
                    $ friendship += 1
                    Pilot "I think we'll be fine, but do you want to turn back?"
                    if friendship >= 0:
                        "{i}She shakes her head.{/i}"
                        show pass qu sit n at sitAtTable behind table2t
                        Passenger "If you think we'll be fine, let's keep going."
                        Pilot "Sounds good, but I will have to refuel if we’re gonna make it to Viacaellum."
                        Pilot "It’ll take an hour or so, but there’s a counter there if you’d like to grab a bite."
                    else:
                        show pass qu sit s at sitAtTable behind table2t
                        Passenger "No."
                        Pilot "I was just checking--"
                        Passenger "It's {i}fine.{/i}"
                        Passenger "..."
                        Passenger "Thank you, though."
                        show pass qu sit n at sitAtTable behind table2t
                        "{i}A few more minutes pass before you break the silence.{/i}"
                        Pilot "We’re going to have to stop soon to refuel and reach Viacaellum."
                        Pilot "It’ll take about an hour, but there’s a counter there if you’d like to grab a bite."
                    jump Storm_Warning_end
                "Too late to turn back now.":
                    hide screen countdown
                    $ friendship -= 1
                    Pilot "We’ll be fine. Besides, it’s too late to turn back now."
                    show pass qu sit i at sitAtTable behind table2t
                    "{i}[Vesta] narrows her eyes at this, clearly unsettled by your statement.{/i}"
                    Pilot "Also, I will have to refuel if we’re gonna make it to Viacaellum."
                    Pilot "It’ll take an hour or so, but there’s a counter there if you’d like to grab a bite."
                    jump Storm_Warning_end
            label menu_neutral_Storm_Warning:
                hide screen countdown
                Pilot "Nah, the forecasters always make the storms a bigger deal than they are."
                Passenger "Okay, if you're sure."
                show pass qu sit n at sitAtTable behind table2t
                Pilot "We’ll be fine, but I will need to refuel if we’re gonna make it to Viacaellum."
                Pilot "It’ll take an hour or so, but there’s a counter there if you’d like to grab a bite."
                jump Storm_Warning_end
            label Storm_Warning_end:
            scene ext_rfstation
            play bg_noise 'audio/amb-sfx_train-station.mp3'
            "{i}You pilot the ship through the gates of the refueling station’s small dome, bringing it to a stop next to the refueling apparatus.{/i}"

        label refuel_station_scenes:
            transform atDoor:
                zoom .35
                ypos .7
            show pass std n at bottomRight with dissolve
            Passenger "I'm going to go get something to eat."
            show pass std i at atDoor with dissolve
            "{i}You nod and begin the apparatus’ refueling process. When you turn to head inside the building, you see [vesta] still standing outside.{/i}"
            "{i}She glances back at you before opening the door, the anxiety of entering an unfamiliar place clearly giving her some pause.{/i}"
            label wave:
                $ timer_jump = 'menu_Wave_neutral'
                show screen countdown
            menu:
                "{i}Wave to her to go in.{/i}":
                    hide screen countdown
                    $ friendship += 1
                    "{i}You wave at her to enter and watch reassurance flicker across her face. She squares her shoulders and pushes on the door, crossing the threshold and giving you a glimpse of the empty counter.{/i}"
                    jump enter
                "{i}Look away.{/i}":
                    hide screen countdown
                    jump menu_Wave_neutral
            label menu_Wave_neutral:
                hide screen countdown
                "{i}You look away and notice out of the corner of your eye her shoulders sag slightly.{/i}"
                "{i}Nevertheless, she squares them again, pushing on the door, crossing the threshold, and giving you a glimpse of the empty counter.{/i}"
                jump enter
            label enter:
                hide pass with dissolve
            stop background_music fadeout 2.0

            play background_music 'audio/mus_gas-station.ogg' fadein 3.0
            "{i}A second later, you enter the station, greeted by the familiar crackle of the radio.{/i}"
            play sound 'audio/sfx_jingle.mp3'

            transform lower:
                xpos 0.1
                ypos 0.3

            transform bottomRight:
                xpos 0.4
                ypos 0.4
            transform sitAtBar:
                xpos 0.4
                ypos 0.32
                xzoom -1

            scene int_rfstation c
            show rs clerk n at lower
            show pass qu sit t at sitAtBar
            show bartop
            with dissolve

            pause 0.5
            play Radio 'audio/amb-sfx_radio-static.mp3'
            Radio "...as the election of Domatellium’s new governor draws near, gatherings in support of the former mayor’s campaign for the position have popped up across Domatellium!"
            Radio "While this campaign has been somewhat polarizing over the past several weeks, it appears that the mayor’s supporters, or “neighbors,” as they call themselves, are attempting to change that view with citywide celebrations."
            Radio "We go live to one of our reporters on the scene…"
            stop Radio
            transform stand:
                xpos .55
                xzoom 1
            label choice5:
                $ timer_jump = 'menu_neutral5'
            show screen countdown
            menu:
                "{i}Listen to the radio.{/i}":
                    hide screen countdown
                    jump Hear_About_Gatherings
                "{i}Talk to refuel station attendant.{/i}":
                    hide screen countdown
                    $ attendantConvo += 1
                    jump conversation_with_attendant
            label menu_neutral5:
                hide screen countdown
                jump Hear_About_Gatherings
            label conversation_with_attendant:
                Passenger "Can you turn that off?"
                show rs clerk t
                Attendant "Gladly, I can't stand that crap."
                show rs clerk n
                "{i}[Nell] switches the radio off and looks up as the bell rings with a smile.{/i}"
                Attendant "Hey, [Pilot]! Where’ve you been? You haven’t stopped by in a while."
                Pilot "Ah, you know how piloting is, Nell. I don’t exactly get to choose where I go."
                $ nameNell ='Nell'
                $ nameNellU ='Nell'
                $ nameNellL='Nell'
                Attendant "Fair enough, now come take a seat, and I’ll make you your usual once I finish up here."
                "{i}As you sit down, Nell turns back to [vesta].{/i}"
                Attendant "If they win the election, they’d just have us revert back to how it was when this whole thing fell apart."
                jump Fell_Apart
            label Hear_About_Gatherings:
                "{i}You give [nell] who stands behind the counter a wave as you enter silently taking a seat and focusing on the radio.{/i}"
                scene int_rfstation r with Dissolve(1.0)
                pause .5
                "{i}Faint cheering erupts from the radio’s background when the news station switches to the reporter at the gatherings.{/i}"
                Radio "Thanks, Birdy. As you can likely hear, many neighbors have come out to show their support for the former mayor’s campaign."
                Radio "Let’s see if we can ask one of these fine folks some questions."
                Radio "Sir, why have you come out to the gatherings?"
                "{i}There’s some slight fumbling with the microphone right before the interviewee speaks.{/i}"
                Radio "Well, I gotta say that Domatellium--hell, all of Duoterra--ain’t what it used to be anymore. My grandpa told me stories about how it used to be, and it’s a real shame how far we’ve fallen."
                "{i}The words become garbled for a moment as the interviewee gets too far from the microphone.{/i}"
                Radio "--but we--Domatellium, that is--used to have aspirations! We used to want progress! And y’know, that’s really all I’m looking for!"
                "{i}The reporter attempts to butt in, but the neighbor quickly speaks over them.{/i}"
                Radio "And why should we settle for stagnation? Duoterra was one of the first colonies, and the government should understand that we need to reclaim this planet!"
                "{i}The sounds of a crowd begin to overcome the speaker’s voice, and the reporter jumps at the opportunity to move on to the next person.{/i}"
                Radio "And, what do you have to say, Ma’am?"
                "{i}There’s some more fumbling as the microphone is handed to another neighbor.{/i}"
                Radio "He’s absolutely right. The government has ignored us for too long!"
                Radio "But really, we want people to come down and get to know the movement! I promise we’re not all so passionate; we only want to make the world a better place!"
                "{i}The reporter takes the microphone back, and their voice comes through clear once again.{/i}"
                Radio "Well, there you have it, folks, you’ll find a few lively characters down here, but all in all, it seems their message is one of--"
                Nell "With all due respect, I’ve gotta turn this crap off."
                scene int_rfstation c
                show rs clerk n at lower behind bartop
                show pass qu sit t at bottomRight, flip
                show bartop

                stop Radio
                "{i}[Nell] goes back to cleaning the area behind the counter, and an awkward silence fills the space.{/i}"
                "{i}[Vesta] finishes her meal, pushing her plate away from her.{/i}"
                show bartop behind pass
                show pass std i at bottomRight
                Passenger "How much longer will we have to wait?"
                Pilot "It should be done now, actually."
                Passenger "Oh! So we could leave soon?"
                Pilot "I mean, yes."
                show pass std n at bottomRight
                Passenger "So..."
                "{i}You get to your feet, waving goodbye to [nell] as you exit.{/i}"
                jump choice5_end
            label Fell_Apart:
                menu:
                    "What do you mean fell apart?":
                        hide screen countdown
                        jump attendant_monologue
                    "Maybe it's gonna head in a good direction.":
                        hide screen countdown
                        $ nationalist_points += 1
                        jump hopeful_on_nationalism
                label Fell_Apart_Neutral:
                    "{i}You stay silent.{/i}"
                    jump choice5_end
                label attendant_monologue:
                    Pilot "What do you mean fell apart?"
                    Attendant "What do you think I mean?"
                    show rs clerk t at lower
                    Attendant "Terraforming halted nearly a century ago. Haven’t you looked outside? The roads between our cities are a half-day of radiation away from crumbling to dust."
                    Attendant "I’ve watched the walls of Domatellium get more cratered every year, and I haven’t seen someone try to repair them since I was a {i}child.{/i}"
                    Attendant """
                    My grandmother was one of the head engineers on Domatellium’s terraforming equipment back when it was still functioning, and even then, it was failing.

                    They’d been feeding those machines subpar material for so long that they were beyond salvation.

                    And so people got scared. They got tired of the decline and looked for change but found it by trying to recreate the past instead of actually looking toward the future.

                    Damnit, I’m starting to sound as preachy as that awful mayor.
                    """
                    show rs clerk n at lower
                    "{i}Nell sets down the glass she had been violently drying.{/i}"
                    Attendant """
                    Point being, some pundit got elected that promised change. Tried forcing the engineers to find solutions that didn’t exist, to make the machines work with the wrong materials.

                    My grandma got fired then, so I don’t know what happened. She knew it was fruitless, and I guess now I’m in the same position.
                    """
                    show rs clerk t at lower
                    "{i}Nell laughs at herself, picking up another glass and going back to drying.{/i}"
                    Attendant "’Cept here I am, drying glasses in a run-down refueling station."
                    show rs clerk n at lower
                    "{i}You look over at [vesta], who’s staring at Nell with a look you can’t quite place.{/i}"


                    show pass std n at bottomRight, stand
                    "{i}[Vesta] finishes her meal, pushing her plate away from her.{/i}"
                    show pass std i at bottomRight, stand
                    Passenger "How much longer will we have to wait?"
                    Pilot "It should be done now, actually."
                    Passenger "Oh! So we could leave soon?"
                    Pilot "I mean, yes."
                    show rs clerk n at lower
                    "{i}Nell watches [vesta] keenly, noting her sudden hurry to leave.{/i}"

                    show pass std n at bottomRight, stand
                    "{i}[Vesta] stands and makes a motion to begin walking for the exit but stops herself.{/i}"
                    Passenger "Oh, and also, I wanted to say thanks, I guess. It was…"
                    "{i}She trails off, clearly unable to find the words to express what she means. Turning quickly, [vesta] leaves as if chased by her unfinished sentence.{/i}"
                    hide pass with dissolve
                    Attendant "She’s a weird one, huh?"
                    menu:
                        "I guess.":
                            Pilot "She kinda is. All the way to Viacaellum with no luggage is an interesting choice."
                            Nell "That certainly is. You keep an eye on her, though, alright? That’s a lady running from something if I’ve ever seen one."
                            "{i}You shrug, give Nell a final wave, and leave the building.{/i}"
                        "{i}Shrug.{/i}":
                            "{i}You shrug, and Nell nods knowingly.{/i}"
                            Nell "Be safe out there. That storm’s no joke, so drive quick!"
                            "{i}You head out, waving to Nell once more before exiting the building.{/i}"
                    jump choice5_end
                label hopeful_on_nationalism:
                    Pilot "Isn’t it possible that this could head in a good direction? The speeches I’ve heard on the radio seem like they’ve got some good points. I even heard them talk about starting terraforming again."
                    show rs clerk t
                    Nell "What are you even talking about?"
                    Pilot "I’m just saying that they’re at least {i}trying{/i} to find solutions."
                    Attendant """
                    {i}Solutions?!{/i} They’re just trying to force a fix on something that’s totally broken! This new movement is just repeating the same points that sent Duoterra on the decline a century ago.

                    Ever wonder why the roads between our cities are a half-day of radiation away from crumbling to dust?

                    It’s because we wasted our resources trying to fix terraformers so clogged with sub-par material they’d have to be totally rebuilt if they were ever used again, letting everything else fall into disrepair.
                    """
                    Pilot "But that’s exactly what I’m saying! The mayor wants to try and actually fix things! In the speeches--"
                    Attendant "In the speeches! Of course! The speeches where they spout rhetoric and empty promises without a single concrete policy to back it up! I swear--"

                    show pass std i at bottomRight, stand
                    "{i}Before Nell can work herself up to a full-on rant, [vesta] interupts her, pushes her plate away from her.{/i}"
                    Passenger "How much longer will we have to wait?"
                    show rs clerk n
                    Pilot "It should be done now, actually."
                    Passenger "So we can leave?"
                    Pilot "I mean, yes."
                    show pass std n at bottomRight, stand
                    Passenger "So..."
                    Pilot "Oh, alright."
                    "{i}You get to your feet, waving goodbye to Nell as you exit. Nell simply looks away, shaking her head.{/i}"
                    jump choice5_end
            label choice5_end:
                scene ext_rfstation
                show pass std n at bottomRight, stand
                with dissolve
                stop music fadeout 1.0
                "{i}You follow [vesta] as she walks hurriedly to the ship, needing to jog a few steps to catch up to her.{/i}"
                #Max nationalist_points is 3
                if nationalist_points > 1:
                    play background_music "audio/mus_ambient-bad.ogg" fadein 3.0
                else:
                    play background_music "audio/mus_ambient.ogg" fadein 3.0
            label choice6:
                $ timer_jump = 'menu_neutral6'
            show screen countdown
            menu:
                "What do you think will happen to Domatellium?" if attendantConvo > 0:
                    hide screen countdown
                    jump conversation_about_attendant
                "What do you think about the gatherings?" if attendantConvo < 1:
                    hide screen countdown
                    jump conversation_about_gatherings
                "Why do you wanna leave so badly?":
                    hide screen countdown
                    if friendship > 1:
                        jump conversation_about_leaving_station
                    if friendship == 0:
                        jump dont_want_to_talk_about_it
                    if friendship < 0:
                        jump dont_need_to_tell_you
            label menu_neutral6:
                hide screen countdown
                jump awkward_walk_back
            label conversation_about_attendant:
                "{i}You begin to ask a question, but [vesta] beats you to it, shaking her head and stopping suddenly.{/i}"
                Passenger "Do you think all that stuff she said was really true?"
                if nationalist_points > 0:
                    jump nationalist_history_conversation
                if nationalist_points <= 0:
                    jump anti_history_conversation
            label nationalist_history_conversation:
                Pilot "No, I think it’ll be different this time, y’know? We’ve learned since then, so we have to have a better chance of terraforming Duoterra than we did before."
                Passenger "That’s what everyone says, but I’m not sure if I believe it anymore."
                Passenger "What about what Nell said about the last time we tried to terraform Duoterra..."
                Passenger "It seems like it just made everything worse."
                Pilot "Well, we need to try something! It’s not like the alternative is going to try and make things better."
                Pilot "It seems like the current governor is too busy sending window washers to polish the inside of Domatellium’s walls to try and fix the outside!"
                "{i}Your conversation falls into an awkward silence.{/i}"
                hide pass with dissolve
                "{i}When you get to the ship, [vesta] heads down to the bunks without saying anything.{/i}"
                jump choice6_end
            label anti_history_conversation:
                Pilot "Yeah, I’ve known Nell for a while now, and she doesn’t make stuff up."
                Passenger "Oh."
                Passenger "That makes sense, I guess. She’s not really the type for that."
                "{i}[Vesta] looks off into the middle distance for a second, collecting her thoughts.{/i}"
                Passenger "I can’t keep myself from thinking that this whole situation is going to get worse, you know?"
                Passenger "I mean, people haven’t talked about terraforming in decades, and all of a sudden, it’s this huge issue that everyone’s so...{i}angry{/i} about."
                Passenger "I don’t know, though. They never seemed that angry to me."
                hide pass with dissolve
                "{i}Before you can respond, however, [vesta] climbs inside your ship, clearly ending the conversation.{/i}"
                jump choice6_end
            label awkward_walk_back:
                "{i}You and [vesta] walk back to the ship in awkward silence.{/i}"
                hide pass with dissolve
                "{i}When you reach the entrance of the ship, you open your mouth, unsure of what to say, but [vesta] climbs inside before you can say anything.{/i}"
                jump choice6_end
            label dont_want_to_talk_about_it:
                Pilot "Why do you want to leave so badly?"
                Passenger "Sorry, [protagName]. I just really don’t want to talk about it."
                Pilot "Alright, we don’t have to talk about it then."
                "{i}The two of you walk silently back to the ship.{/i}"
                hide pass with dissolve
                jump choice6_end
            label dont_need_to_tell_you:
                Pilot "Why do you want to leave so badly?"
                Passenger "I don't need to tell you!"
                "{i}[Vesta] looks angry and a little frightened, clearly unable to talk to you at the moment.{/i}"
                Pilot "Alright, alright."
                "{i}You both walk the rest of the way back to the ship in silence.{/i}"
                hide pass with dissolve
                "{i}When you reach it, [vesta] stomps below deck without another word to you.{/i}"
                jump choice6_end
            label conversation_about_leaving_station:
                Pilot "Why do you want to leave so badly?"
                Passenger "I’m just worried about the storm."
                Passenger "I want to put as much distance between Domatellium and myself as possible."
                Pilot "Can I ask why you left Domatellium in the first place?"
                Passenger "I made some mistakes, and I didn’t really see another way out of them."
                Passenger "..."
                Passenger "But I'd rather not talk about it."
                Pilot "Alright, we don’t have to."
                "{i}The two of you walk silently back to the ship.{/i}"
                hide pass with dissolve
                jump choice6_end
            label conversation_about_gatherings:
                Pilot "What do you think about the gatherings?"
                "{i}[Vesta] visibly stiffens.{/i}"
                Passenger "Why do you ask?"
                Pilot "Just curious, I guess. I heard about them on the radio while you were inside."
                Passenger "Well, I think they’re weird. Everyone is obsessed with putting this nice image over the real points. A real movement wouldn’t feel the need to manipulate people into siding with them."
                menu:
                    "I don't think that's what they’re trying to do.":
                        $ nationalist_points += 1
                        Pilot "I don’t think that’s true. I’m sure there are a couple who are like that, but it really just seems like a group passionate about change for the better."
                        Passenger "What do you even know? You think you can make a judgment on it based on a couple of radio broadcasts."
                        hide pass with dissolve
                        "{i}[Vesta] climbs inside the ship before you can respond, her jaw set with frustration.{/i}"
                    "You're right.":
                        $ nationalist_points -= 1
                        Pilot "I suppose you’re right."
                        Passenger "And on top of it all, everyone acts so weird if you try to question the neighbor’s message. I can’t even tell if they really all believe it or if people are just too scared of being the odd one out to disagree."
                        Passenger "I remember how weird everyone acted when I started looking into what people were saying back when…"
                        Passenger "Nevermind."
                        hide pass with dissolve
                        "{i}[Vesta] climbs into your ship before you can ask what she meant, clearly done with the conversation.{/i}"
                jump choice6_end
            label choice6_end:
                scene rd front
                show cp front
                show ext_rfstation
                hide ext_rfstation with Dissolve(1.0)
                pause .5
                stop bg_noise
                "{i}As you climb into the pilot’s seat, you can’t stop thinking about what you heard earlier.{/i}"

                "{i}You drive into the night, but eventually, you decide to turn in.{/i}"

        label comfort_passenger_scenes:
            hide cp front with Dissolve(1.0)
            show kn table2 with Dissolve(1.0)
            "{i}As you’re walking to the bunks, you hear muffled sobbing.{/i}"
            transform atChair:
                xpos .27
                ypos .14
                xzoom -1.00
            show sit_2chair
            transform crySit:
                xpos .05

                zoom 1.5
            show pass cr sit s at crySit behind chairArm
            show chairarm
            with Dissolve(2.0)
            pause
            pause .5
            "{i}You poke your head in the doorway of the sitting room and see [vesta]. She’s curled up in one of the chairs with her head in her hands, apparently not having noticed you yet.{/i}"
            label choice7:
                $ timer_jump = 'menu_neutral7'
                show screen countdown
            menu:
                "Are you ok?":
                    hide screen countdown
                    if friendship > 0:
                        $ helped=1
                        jump meaningful_conversation_about_past
                    if friendship <= 0:
                        $ helped=-1
                        jump combative_conversation_about_relationship_with_passenger
                "{i}Ignore Passenger.{/i}":
                    hide screen countdown
                    "{i}You ignore [vesta].{/i}"
                    show black with Dissolve(2.0)
                    jump choice7_end
            label menu_neutral7:
                hide screen countdown
                "{i}You ignore [vesta].{/i}"
                show black with Dissolve(2.0)
                jump choice7_end
            label meaningful_conversation_about_past:
                "{i}You knock lightly on the door and step into the room.{/i}"
                Pilot "Hey, are you alright?"
                "{i}[Vesta] shakes her head, not looking up at you. Her body is shaking as she tries to choke back her sobs.{/i}"
                Pilot "What's wrong?"
                Passenger "What...what if I’m making the wrong choice?"
                Pilot "What do you mean? Wrong choice?"
                transform scared:
                    xpos .13
                    ypos .24
                    zoom 1.2
                transform oops:
                    xpos 0.05
                    ypos .02
                    zoom 1.5
                show pass qu sit s at scared
                pause
                Passenger "Leaving! If I go through with this, what if I can’t go back? I can’t make this choice now. I...oh God. How could I be this stupid?"
                "{i}You kneel down next to her, not totally sure what to do.{/i}"
                label convo1:
                    $ timer_jump = 'convo1_neutral'
                    show screen countdown
                label menu_convo1:
                    menu:
                        "We all make stupid decisions.":
                            $ friendship -= 1
                            hide screen countdown
                            Pilot "We all make mistakes sometimes. When we get to Viacaellum, I’m sure you’ll be able to find someone who’ll drive you back once the storm has passed."
                            Passenger "That’s not- that’s not what I meant!"
                            show pass cr sit s at oops behind chairArm
                            "{i}She clenches her fists, her whole body tensing with another sob.{/i}"
                            Passenger "I just…"
                            Passenger "What if things go bad? What if I’ve left and something gets instated, and it means I can’t go back!"
                            "{i}[Vesta]’s body seems racked with panic for a second, and she lets out a small wail.{/i}"
                            label convo2:
                                $ timer_jump = 'menu_convo2_neutral'
                                show screen countdown
                            label menu_convo2:
                                menu:
                                    "{i}Draw back and wait.{/i}":
                                        hide screen countdown
                                        $ friendship -= 1
                                        "{i}You sit back, trying to give her space, but her body just seems to get tighter and tighter, her sobs ever weaker and more desperate.{/i}"
                                        "{i}After what feels like an eternity, her voice, tiny and thin, makes its way out from between her clenched teeth.{/i}"
                                        Passenger "I need you to leave."
                                        Passenger "I’m sorry. I just…"
                                        show pass qu sit s at scared
                                        Passenger "I need to be alone right now. I can’t deal with this."
                                        Pilot "Oh. Yeah, for sure."
                                        "{i}You get up and walk quietly to the door, turning just before you shut it to take another look back at [vesta], wishing you knew how to help her.{/i}"
                                        "{i}Closing the door behind you. You take a seat on your bunk, drained and unsure of what to do next.{/i}"
                                        jump choice7_end
                                    "{i}Reach out to her.{/i}":
                                        $ friendship += 1
                                        hide screen countdown
                                        "{i}You reach out to her, placing your hand in hers.{/i}"
                                        "{i}Letting out another small noise, she grips your hand so tight her knuckles go white, holding on as if for dear life.{/i}"
                                        "{i}A second later, you find your arms wrapped around her as she hangs on to your torso, her sobs shaking both of you.{/i}"
                                        "{i}Moments pass, and [vesta] seems to gain control of herself, pulling back with an ashamed look on her face.{/i}"
                                        Passenger "I..."
                                        show pass qu sit s at scared
                                        Passenger "I’m sorry. That was so inappropriate."
                                        "{i}You sit back, still not totally sure what to say.{/i}"
                                        jump explain_past
                                label menu_convo2_neutral:
                                    hide screen countdown
                                    "{i}You sit back, trying to give her space, but her body just seems to get tighter and tighter, her sobs ever weaker and more desperate.{/i}"
                                    "{i}After what feels like an eternity, her voice, tiny and thin, makes its way out from between her clenched teeth.{/i}"
                                    Passenger "I need you to leave."
                                    Passenger "I’m sorry. I just…"
                                    show pass qu sit s at scared
                                    Passenger "I need to be alone right now. I can’t deal with this."
                                    Pilot "Oh. Yeah, for sure."
                                    "{i}You get up and walk quietly to the door, turning just before you shut it to take another look back at [vesta], wishing you knew how to help her.{/i}"
                                    "{i}Closing the door behind you, you take a seat on your bunk, drained and unsure of what to do next.{/i}"
                                    jump choice7_end
                        "I don’t think that leaving was stupid.":
                            hide screen countdown
                            $ friendship += 2
                            Pilot "I don’t think leaving was stupid."
                            show pass qu sit s at scared
                            "{i}[Vesta] looks up at you, and she seems to tremble just a little less for a second.{/i}"
                            Pilot "Why... Do you think it was stupid? "
                            show pass cr sit s  at oops behind chairArm
                            "{i}She looks away again, her face contorted into one of anguish.{/i}"

                            Passenger " I...I’ve made mistakes. So, so, so many."
                            "{i}She takes a moment to let the tears in her eyes subsided.{/i}"
                            Passenger "And now...I don’t know that I can go back. I’m so...terrified. I’m terrified that, by leaving, I’ve fucked everything up and…"
                            show pass qu sit s at scared
                            "{i}Trailing off, [vesta] looks back at you.{/i}"
                            jump explain_past
                    label convo1_neutral:
                        hide screen countdown
                        Pilot "I'm sorry, I don't know what to say."
                        "{i}After what feels like an eternity, her voice, tiny and thin, makes its way out from between her clenched teeth.{/i}"
                        Passenger "I need you to leave."
                        Passenger "I’m sorry. I just…"
                        show pass qu sit s at scared
                        Passenger "I need to be alone right now. I can’t deal with this."
                        Pilot "Oh. Yeah, for sure."
                        #TODO show doorway
                        with Dissolve(1.0)
                        "{i}You get up and walk quietly to the door, turning just before you shut it to take another look back at [vesta], wishing you knew how to help her.{/i}"
                        "{i}Closing the door behind you, you take a seat on your bunk, drained and unsure of what to do next.{/i}"
                        jump choice7_end
                label explain_past:
                    Passenger """
                    I haven’t exactly had the best track record my whole life.

                     I used to be one of them. Y’know, believe in the whole terraforming thing, or whatever. A “neighbor,” I guess.
                    """
                    "{i}[Vesta] sniffles, her bottom lip quivering as another tear threatens to roll down her face.{/i}"
                    Passenger """
                    I was so...hungry for change that I just took the first road that presented itself.

                    I used to work as an engineer...and I thought I could try and make things better. I ended up joining some of my coworkers trying to revive some of the old machines, better air filters, and stuff.

                    My boss found out...and fired everyone with a connection. Nearly a hundred people, I think.

                    So when I heard about a group that wanted to start terraforming again, I thought they might be good people...
                    """
                    show pass cr sit s at oops behind chairArm
                    "{i}[Vesta] trails off, wiping at her eyes.{/i}"
                    Pilot "But?"
                    show pass qu sit s at scared
                    Passenger "But...but I was too blinded by my hope that I missed what was really happening."
                    "{i}She makes direct eye contact with you as if pleading for you to understand.{/i}"
                    Passenger """
                    So many people there just used it...I don’t know. To justify their anger at the world, I guess.

                    One of the rallies...people got violent. They used the belief in a better future to justify hurting people who didn’t join.

                    And the next day, I didn’t even hear anything about it. No news. No broadcasts.

                    I…
                    """
                    show pass cr sit s at oops behind chairArm
                    "{i}Putting her face in her hands, [vesta] lets out another sob, this one deep and guttural.{/i}"
                    Passenger """
                    I don’t even remember what happened, exactly.

                    I don’t think...I don’t think I want to.
                    """
                    "{i}[Vesta] slumps back in her chair, and you watch as silent tears begin to drip down her face.{/i}"
                    Passenger "I’m so sorry, but...I need some time alone."
                    "{i}You nod stepping out of the small room and closing the door behind you, you take a seat on your bunk, drained and unsure of what to do next.{/i}"
                    jump choice7_end
            label combative_conversation_about_relationship_with_passenger:
                #TODO Hide doorway
                show pass std i
                with Dissolve(2.0)
                "{i}You knock lightly on the door and step into the room.{/i}"
                Pilot "Hey, are you alright?"
                show pass qu sit i at scared
                "{i}[Vesta] glares daggers at you, tears streaming down her red face.{/i}"
                Passenger "Get out."
                "{i}She says the words through clenched teeth.{/i}"
                Pilot "Sorry, I was just--"
                Passenger "I said, get the fuck out! I don’t want to talk to {i}you!{/i}"
                Pilot "Ok! I’m leaving!"
                #TODO Show doorway
                "{i}You go to close the door, but [vesta] gets to her feet.{/i}"
                Passenger "Why did you even come in here? You’ve been nothing but rude to me since we started driving. What did I even do to you?"

                Passenger "I’m {i}sorry{/i} I didn’t think this through. I’m {i}sorry{/i} I inconvenienced you by {i}paying you{/i} to drive me somewhere!"

                Passenger "And then you come in here as if you’re just going to make it better? I’ve been trapped in this god-awful--"

                Passenger "I mean, what even is this thing? Some glorified taxi running on some kind of ancient jet fuel?"

                Passenger "But I’ve been trapped here, with you, regretting every choice I’ve made in my life and trying to keep from losing my mind and your choice, of all the choices you could make, is to try and make this an even {i}greater{/i} hell?"


                #TODO Update when I hear from Nathan
                "{i}She storms towards you, and you take a reflexive step back, removing your hand from the door handle.{/i}"

                show black
                "{i}She reaches the doorway and slams it shut, causing a bang that echoes around the ship for a few moments.{/i}"

                scene rd front
                show cp front behind black
                hide black
                with fade
                "{i}You return to the cockpit, a little unsure of what to do with yourself.{/i}"
                jump choice7_end
            label choice7_end:

    label Act3:
        label vista_scenes:
            show black with fade
            scene rd front
            show cp back
            show pass qu sit n at cpSit
            show cp_backt
            show black
            pause .5
            hide black with fade

            "{i}[Vesta] joins you in the cockpit the next morning, sitting sullenly with dark circles under her eyes.{/i}"
            "{i}She stares out the window absentmindedly, clearly uninterested in maintaining a conversation.{/i}"
            "{i}A few hours later, you break the heavy silence with some trepidation.{/i}"
            Pilot "I’m going to take a break up ahead. There’s an old vista that’s high enough I might be able to catch the storm radio to figure out what's going on with the weather."
            Pilot "It’s a pretty good view. If you want to get a firsthand look, you should suit up."
            show pass qu sit s
            Passenger "Why? Do you think the storm will cause trouble after all?"
            "{i}You’re worried about the storm.{/i}"
            "{i}It’s bigger than any you’ve ever driven through before, and even with only a few hundred miles left of the journey, you don’t know if you’ll be able to beat it to Viacaellum like you thought you would.{/i}"
            label weatherLie:
                $ timer_jump = 'menu_weatherLie_neutral'
            show screen countdown
            menu:
                "No, I don't.":
                    hide screen countdown
                    show pass qu sit n
                    Pilot "Nah, I’ve been in plenty of storms like it before. We really don’t have anything to worry about."
                    Passenger "If there’s nothing to worry about, why do you need to check the radio?"
                    Pilot "I’m just being overly cautious, I guess."
                    "{i}She doesn’t seem entirely convinced but doesn’t question you further, though you notice her shoulders appear a little less tense.{/i}"
                    $ friendship += 1
                    jump weatherLie_end
                "Yes, probably.":
                    hide screen countdown
                    $ friendship -= 1
                    Pilot "Yeah, I’m worried it might hit us right before we reach Viacaellum."
                    show pass qu sit i
                    Passenger "What does that mean? We won’t have to stop, though, will we?"
                    "{i}You shrug.{/i}"
                    Pilot "There’s not anything I can do except try to beat it to Viacaellum. It’s big enough that even if we stop now, it’ll still hit us eventually. All we can do is hope that we won’t get the worst of it."
                    show pass qu sit s
                    "{i}[Vesta] bites her lip nervously, twisting her hands in her lap. She doesn’t seem in the mood to say anymore, fixated on the dark clouds barely visible on the horizon.{/i}"
                    jump weatherLie_end
            label menu_weatherLie_neutral:
                hide screen countdown
                Pilot "I don't know."
                jump weatherLie_end
            label weatherLie_end:
                hide pass
                hide cp
                hide cp_backt
                with fade

            show kn table2 with fade
            transform inDoorway:
                ypos .15

            pause 1.0
            show table2t
            menu:
                "{i}Fiddle with radio.{/i}":
                    "{i}You begin fiddling with the radio and accidentally tune it to the news station.{/i}"
                    Radio "--thank you, Doctor. Now we’ve got some breaking news here, folks, and I’m afraid it could be somewhat distressing to those following the ongoing elections over in Domatellium."
                    show pass std n at inDoorway behind table2t with fade
                    "{i}[Vesta] appears in the doorway.{/i}"
                    Passenger "Oh, you got the radio to work."
                    Radio "According to a direct wire we received only minutes ago, it appears that following a call for a recount by the former governor of the region, riots have broken out--"
                    show pass std i
                    Passenger "What?!"
                    "{i}The reporter starts listing off neighborhoods where the riots have concentrated, and [vesta] listens with bated breath. At one name, a small gasp escapes her lips.{/i}"
                    "{i}[Passenger] seems quite shaken by the news, hastily throwing on her coat and her helmet over her head before rushing outside.{/i}"
                    "{i}You move your hand to change the channel, but she interupts you.{/i}"
                    Passenger "No, don't!"
                    show pass std s at inDoorway behind table2t
                    Passenger "I’m sorry, I need to hear this."
                    Radio """
                    The riots began last night around eight o’clock and raged for much of the week. Several fires have been reported throughout the city, most of which appear to have been set by rioters.

                    We cannot be certain, though the message seems to assert that some leaders in these riots have somehow obtained the records of individual citizens’ votes and are now targeting those who chose not to vote for the former mayor of Domatellium.

                    The homes of several outspoken critics of the former mayor have already burned in incidents that our source referred to as “acts of terror.”

                    We will resume broadcasting as soon as we receive more news of the situation in Domatellium, so in the meantime, please enjoy the newest hit of pop wonder--
                    """
                    "{i}[Vesta] reaches down and turns the dial violently, switching the radio to static.{/i}"
                    "{i}Clearly quite shaken by the news, [vesta] hastily throws her coat on and smashes her helmet on over her head before rushing outside.{/i}"
                    hide pass with dissolve
            label radioChoice:
                $ timer_jump = 'menu_radioChoice_neutral'
                show screen countdown
            menu:
                "{i}Check on [Passenger].{/i}":
                    hide screen countdown
                    jump choice8
                "{i}Keep tuning for the weather channel.{/i}":
                    hide screen countdown
                    jump full_weather_Report
            label menu_radioChoice_neutral:
                hide screen countdown
                jump full_weather_Report
            label full_weather_Report:
                $ friendship -= 2
                play sound 'audio/sfx_weather_jingle.mp3'
                "{i}You continue to tune the radio, attempting to catch Viacaellum’s weather channel. It takes a few times, but you eventually get it.{/i}"
                Radio "--we haven’t seen a storm like this in years. In fact, this may be the largest storm we’ve been able to monitor in almost a century."
                "{i}The tone of the radio is entirely too jovial for the news it delivers.{/i}"
                Radio "Truly a once-in-a-lifetime experience, but not one I’d recommend checkin’ out if you don’t have the proper equipment."
                Radio "The governor recently put out a citywide mandate to stay inside, halting all outbound travel until this truly historic storm has passed through."
                Radio "And for those of you too unlucky to be outside city walls when this thing hits…"
                Radio "Well, let’s just say if you ain’t a storm chaser, I {i}do not{/i} envy you."
                Radio "{i}Anyway,{/i} this message should be on repeat until we receive more news, so enjoy my illustrious voice in the meantime."
                "{i}The radio begins to repeat, looping through the same obnoxious message a few times before you shut it off.{/i}"
                "{i}Not long after you do, you hear the sound of the hatch in the sitting room being wrenched open, and a shivering passenger storms inside.{/i}"
                jump radioChoice_end
            label radioChoice_end:
                jump menu_neutral8
            transform Vista:
                xzoom -1
            label choice8:
                scene close_vista
                show pass std i at Vista
                with fade
                pause 1.0
                "{i}You step out of the ship, making your way to where [vesta] stands overlooking the vista.{/i}"
                "{i}When you arrive, you find her staring out over the vast expanse of lifeless terrain, shivering even through her thick coat.{/i}"
                "{i}You stop next to her, contemplating the empty valley for a second. Wind howls past you, knocking dust and small rocks off the cliff. In the far distance, you watch storm clouds creep slowly over the horizon.{/i}"
                "{i}[Vesta] looks over at you, finally acknowledging your presence.{/i}"
                $ timer_jump = 'silent8_neutral'
                show screen countdown
            menu:
                "What's wrong?":
                    hide screen countdown
                    Pilot "What's wrong?"
                    if helped>0:
                        Passenger "I live--"
                        "{i}She catches herself.{/i}"
                        Passenger "{i}Used to{/i} live in one of the neighborhoods they mentioned."
                        Passenger "Everyone I know lives there."
                        "{i}She looks back off the cliff, shivering a little more than before.{/i}"
                        Passenger "I talked to my friends, my family after I saw...what I saw. They were all part of the...movement, too. I thought I could...I don’t know."
                        Passenger "Maybe if I’d stayed longer..."
                        Pilot "You could've convinced them to come with you."
                        "{i}[Vesta] nods, looking down.{/i}"
                        Passenger "I still feel like it’s my fault, you know. All of them joining. I told them about what happened when I got fired, and I can’t help but think that if I hadn’t done that...maybe they would’ve listened."
                        Passenger "It was like they didn’t care. At all. I was so scared…I thought someone would tell other neighbors that I wanted to leave."
                        Passenger "The next morning, I didn’t even pack. And now we’re here, I guess."
                        "{i}She looks back at you, though you can’t tell what her expression might be behind the mask.{/i}"
                        jump apologize
                    elif friendship > 2:
                        Passenger "I live--"
                        "{i}She catches herself.{/i}"
                        Passenger "{i}Used to{/i} live in one of the neighborhoods they mentioned."
                        Passenger "Everyone I know lives there."
                        "{i}She looks back off the cliff, shivering a little more than before.{/i}"
                        Passenger "I was ready to leave. I wanted to go and never look back."
                        "{i}She shakes her head, eyes fixated on her shoes.{/i}"
                        Passenger "But now it’s really gone. For good. I couldn’t go back if I wanted to."
                        "{i}Her hands form fists for a second, but she opens them again with a forceful sigh, squaring her shoulders.{/i}"
                        Passenger " I guess I’ve just got the future to look forward to."
                        "{i}She laughs dryly.{/i}"
                        Passenger "Showing up in a city all alone, with no belongings, references, or purpose. The world truly is my oyster. I can do nothing but watch the paths unfold in front of me!"
                        "{i}The desperation in her voice is evident.{/i}"
                        Passenger "I’m sorry. I shouldn’t get so nihilistic."
                        "{i}She turns her gaze back to the horizon.{/i}"
                        Passenger "I guess we should leave now, huh? Those storm clouds look mighty nasty."
                        Pilot "Probably."
                        "{i}You open your mouth to say something, but no words come.{/i}"
                        Passenger "Let’s get going then. My future awaits!"
                        "{i}She turns around, clearly done with the austere view.{/i}"
                        jump return_to_ship
                    else:
                        "{i}[Vesta] contemplates her response for a second, as if deciding if it’s worth answering the question.{/i}"
                        Passenger"""
                        I {i}used{/i} to live in one of those neighborhoods. So did basically everyone else I knew.

                        I thought I’d be able to go back, maybe. But I guess my choice is made for me now.

                        I don’t even...I don’t know.
                        """
                        "{i}She turns her gaze back to the horizon.{/i}"
                        Passenger "I don’t really want to talk about it."
                        "{i}Silence descends between the two of you, the wind howling even louder.{/i}"
                        Pilot "You should head back to the ship now. We want to make it to Viacaellum before the storm hits, and it’s going to be closer than I’d like."
                        "{i}She nods silently, turning around, clearly done with the austere view.{/i}"
                        jump return_to_ship
                "{i}Stay silent{/i}":
                    jump silent8_neutral
            label silent8_neutral:
                hide screen countdown
                """
                {i}You say nothing, simply standing with her in silence.{/i}

                {i}[Vesta] turns her eyes back to the horizon, watching the dark storm clouds grow slowly closer.{/i}

                {i}After a few moments, the silence seems to settle in, the anticipation of a conversation fading, and the two of you stand together in a kind of camaraderie, taking solace in watching the storm swallow the world.{/i}

                {i}A tiny streak of sheet lightning ripples across the clouds, traveling for what you know to by miles across the storm front, startling both you and [vesta].{/i}
                """
                Pilot "It might be time to head back to the ship. The storm is only going to get closer, and we don’t want to get caught in it."
                "{i}Shaking herself, [vesta] starts as if coming out of a trance.{/i}"
                Passenger "...Yeah. Of course."
                "{i}She takes one last glance out over the landscape before beginning to walk silently back to the ship.{/i}"
                jump return_to_ship
            label apologize:
                menu:
                    "I'm so sorry.":
                        Pilot "I'm so sorry."
                        "{i}You search for more words but can’t find any.{/i}"
                        "{i}[Vesta] fixes her gaze on the horizon.{/i}"
                        Passenger "I...don’t be. It’s all over now. I can’t dwell on the past."
                        "{i}She squares her shoulders as if forcing herself to feel sure.{/i}"
                        Passenger "The choices they made are theirs. I’ve just got to make do with mine."
                        Passenger "I’m not going back. Even if I wanted to, everything I know is gone. That part of my life…"
                        Passenger "It’s gone now. Literally."
                        "{i}[Vesta] turns around, clearly done with the austere view.{/i}"
                        Passenger "Can we just get going? I can’t handle this wasteland much longer."
                        jump return_to_ship
                    "You can't blame yourself.":
                        $ friendship += 1
                        Pilot "You did the right thing. You tried to warn them, and they didn't listen."
                        Pilot "What they chose to do...that’s up to them. Unless you told them to ignore the…"
                        "{i}You search for the right word for a second but fail to find it.{/i}"
                        Pilot "{i}Bad{/i} things that happened… then that was up to them, ultimately. If they didn’t change their minds, they didn’t want to."
                        Pilot "Staying and risking being caught up in the riots wouldn’t have helped them or anyone."
                        "{i}You fall silent, letting the stillness of the moment stretch out.{/i}"
                        Passenger "Thank you. I...needed to hear that, I guess."
                        Passenger "I’m not going back. Even if I wanted to, everything I know is gone. That part of my life…"
                        "{i}She squares her shoulders, her voice firm as she comes to this resolution.{/i}"
                        Passenger "It’s gone now. Literally."
                        "{i}[Vesta] turns around, clearly done with the austere view.{/i}"
                        Passenger "Can we just get going? I can’t handle this wasteland much longer."
                        jump return_to_ship
            label menu_neutral8:
                hide screen countdown
                scene rd front
                show kn table2

                show pass qu sit n at sitAtTable
                show table2t
                with fade
                "{i}Eventually, [vesta] comes back onto the ship. She tries to casually hide her face, but you can see her eyes are red and puffy.{/i}"
                Pilot "The storm is getting really bad--"
                "{i}[Vesta] cuts you off.{/i}"
                Passenger "Whatever, let’s keep going. I can’t handle this wasteland much longer."
                jump pre_crash_radio_scenes
            label return_to_ship:
                scene rd front
                show kn table2
                show pass qu sit s at sitAtTable
                show table2t
                with fade
                "{i}The two of you enter the ship, and [vesta] immediately takes a seat at the kitchen table.{/i}"

        label pre_crash_radio_scenes:
            play Wind 'audio/amb-sfx_strong-wind.mp3' fadein 10.0
            play Rain 'audio/amb-sfx_rain-on-metal-roof.mp3' fadein 10.0
            label checkRadio:
                $ timer_jump = 'menu_checkRadio_neutral'
            show screen countdown
            menu:
                "{i}Check radio.{/i}":
                    hide screen countdown
                    $ friendship -= 1
                    jump checking_Radio
                "{i}Head to cockpit.{/i}":
                    hide screen countdown
                    $friendship+=1
                    jump checkRadio_end
            label menu_checkRadio_neutral:
                hide screen countdown
                jump checking_Radio
            label checking_Radio:
                if friendship<0:
                    jump checkRadio_neg
                if friendship>0:
                    jump checkRadio_pos
                else:
                    jump checkRadio_neu
            label checkRadio_neg:
                Passenger "Seriously?"
                "{i}She gets to her feet angrily, standing with a childish look of fury on her face.{/i}"
                Passenger "Just DRIVE, damnit!"
                "{i}You agree begrudgingly, entering the cockpit and starting the craft.{/i}"
                "{i}Even as the room fills with the whine of the engines you can still hear her stomps and sniffles from down below.{/i}"
                jump checkRadio_end
            label checkRadio_neu:
                Passenger "Ugh, I don't know why I even bother."
                Passenger "Just be silent and drive."
                Passenger "You're good at that."
                "{i}You nod and head to the cockpit.{/i}"
                jump checkRadio_end
            label checkRadio_pos:
                Passenger "Could you not, please? I’ve had enough of that damn thing for the rest of my life."
                "{i}You open your mouth to explain that it might offer some information on the duration of the storm and how we might avoid it, but she seems to read my thoughts.{/i}"
                Passenger "Really!? What new information are you going to learn from that thing?"
                Passenger "That storm is headed right towards us and stretches for as far as I can see. I can’t wait here any longer. Just get me to Viacaellum. Please."
                "{i}You nod and begin to head to the cockpit.{/i}"
                Pilot "Just brace yourself, though. This is going to be a...bumpy ride."
                jump checkRadio_end
            label checkRadio_end:

        label crash_scenes:
            label actual_crash:
                play Hail 'audio/sfx_hail.mp3' fadein 5.0
                scene rd storm
                show cp front
                with fade
                "{i}You manage to cross nearly half the remaining distance to Viacaellum before the storm hits.{/i}"
                play sound 'audio/sfx_crash.mp3'
                pause .5
                "{i}But when it hits, it hits hard.{/i}"
                scene black with fade
                stop background_music
                pause 1.0
                play sound 'audio/sfx_ear_ringing.mp3' fadeout 1.0
                pause 1.5
                #TODO Blurry image of kitchen
                scene rd storm
                show black
                show kn crashed behind black
                hide black with Dissolve(3.0)
                pause
                play sound 'audio/sfx_creak.mp3'
                "{i}The ship groans as you get up.{/i}"
                hide cp
                hide rd
                with fade
                "{i}You look around, but you can't see [vesta].{/i}"
                if nameKnown>0:
                    Pilot "[Vesta]! Can you hear me?! Are you ok?!"
                else:
                    Pilot "Hey! Can you hear me?! Are you ok?!"
                "{i}You step forward, trying to regain your footing on the slanted floor.{/i}"
                "{i}Grasping for one of the walls, you lose your balance, sliding down until you hit the wall hard, sending shocks up your legs.{/i}"
                "{i}Water laps around the ankles of your boots, and you realize the level has already begun to rise.{/i}"
                "{i}Looking around, you realize you are in the kitchen and must have fallen out of the cockpit and down through the hatch.{/i}"
                if friendship<=0:
                    jump pass_refuses_to_help
                else:
                    jump pass_helps

            label pass_helps:
                play sound 'audio/sfx_table_broken.mp3'
                "{i}You call out for [vesta] again, and this time hear a crash in the next room.{/i}"
                "{i}[Vesta] yelps, and you feel yourself twinge with sympathetic pain. Scrambling forward, you find her sprawled against the table, surrounded by pieces of broken glass from the mirror that toppled next to her.{/i}"
                show pass fall 1
                "{i}You reach out, managing to pull her into the kitchen and feel the pressure of the water around your knees, lapping at the tops of your boots as if desperate to poor in.{/i}"
                "{i}[Vesta] looks around, finally seeming to comprehend that things are not as they should be.{/i}"
                Passenger "What happened?!"
                "{i}She yells this, her voice slightly slurred.{/i}"
                play sound 'audio/sfx_thunder.mp3'
                Pilot "We crashed! The ship got hit by one of the largest gusts I’ve ever experienced!"
                "{i}Your voice is nearly drowned out by a peal of thunder, and you find yourself gasping for breath, creating a cloud of mist in the freezing air.{/i}"
                Pilot "We need to find our helmets! I think there’s a hole somewhere in the ship, and the air is going to become unbreathable within the next few minutes!"
                "{i}[Vesta] nods, trudging unsteadily through the rising water to the desk in the next room.{/i}"
                hide pass with dissolve
                "{i}You begin to fumble around in the darkness, searching desperately for your helmet.{/i}"
                Passenger "I found it!"
                show pass fall h1 with fade
                "{i}[Vesta] stumbles back, pulling her helmet over her disheveled hair.{/i}"
                "{i}You nod at her, giving a shaky thumbs-up before going back to searching.{/i}"
                "{i}Minutes pass, and you find yourself beginning to cough, the air growing steadily thicker as your search becomes more frantic.{/i}"
                "{i}[Vesta] joins you, throwing open the doors of cabinets and plunging her hands into the ever-rising water.{/i}"
                Passenger "I do-d-don’t think it’s h-here!"
                "{i}You look over and realize that she’s shivering hard, her fingers faintly blue in the dim emergency lights.{/i}"
                Pilot "We’re going to have to stop searching! Is your coat dry?"
                Passenger "I...I think so."
                "{i}[Vesta] looks around, confused as if trying to remember where she put it.{/i}"
                Passenger "It...it’s on-n t-t-top of my bunk!"
                hide pass with dissolve
                "{i}Without you saying anything, [vesta] clambers into the next room, doing her best to avoid the nearly mid-thigh high water despite her violent shivering.{/i}"
                "{i}You reach out for the ladder to the cockpit, clambering shakily up its rungs to the dry safety.{/i}"
                scene rd storm
                show cp crashed behind pass
                with fade
                Pilot "Come up to the cockpit! We should be able to seal it off long enough to make it through the storm!"
                show pass fall h1 with fade
                "{i}[Vesta] struggles up the ladder a second later, her coat grasped in one arm. You reach over and pull the hatch down behind her, sealing off the cockpit.{/i}"
                "{i}You breathe deeply, savoring the recycled air as Duoterra’s atmosphere is filtered out.{/i}"
                Passenger "So...what now?"
                Pilot "I...don’t know."
                "{i}You shake your head, trying to gain some semblance of your bearings back.{/i}"
                Pilot "We have to call for help. The emergency power still works, so I’ll be able to send a direct distress transmission to Viacaellum."
                "{i}[Vesta] looks relieved, and she seems to relax slightly. She removes her helmet, revealing a face far paler than what you’ve become accustomed to.{/i}"
                "{i}Suddenly, her body is wracked with convulsions, her teeth chattering so hard you can easily hear it from across the cockpit.{/i}"
                "{i}She reaches for her coat, attempting to put it on, but [vesta] struggles to maintain a grip.{/i}"
                "{i}You reach out, helping her slide her shaking arms through the sleeves and feet into the rubber bottoms.{/i}"
                "{i}Even after a few minutes, [vesta] continues to shudder, and you notice her lips remain slightly blue, her skin still pale in the faint light.{/i}"
                "{i}She looks off to one side when she notices your worried look, staring out of the windscreen.{/i}"
                "{i}Her eyes widen suddenly, and she points a shaking finger out at the storm.{/i}"
                "{i}You follow her gaze and see the cause of the leak: a gash a few feet long that rain is pouring into.{/i}"
                Passenger "C-can we f-f-fix that?"
                if friendship > 3:
                    jump pass_helps_outside
                else:
                    jump pass_helps_inside
                label pass_helps_outside:
                    Pilot "I...maybe. If we could, it would let us divert heat to the cockpit as it wouldn’t be immediately lost trying to keep the engine from entirely freezing over."
                    Pilot "There’s an emergency welder and scrap metal down below, but going out in this storm is too dangerous. And besides--"
                    hide pass with dissolve
                    "{i}Before you can finish, [vesta] is gone, climbing down the ladder.{/i}"
                    Passenger "Where is it-t?"
                    menu:
                        "{i}Tell her where it is.{/i}":
                            Pilot "Look on the wall behind the ladder. There should be a compartment."
                            "{i}You hear a clunking noise as the compartment is opened, and moments later, the pilot reemerges.{/i}"
                            show pass fall h1
                            "{i}Without hesitation, she reaches up to the emergency release on the hatch on the ceiling of the cockpit, only glancing back at you for a second.{/i}"
                            Passenger "B-b-brace y-yourself!"
                            "{i}[Vesta] is imbued with a calm you’ve never seen before, and despite her constant shivering, she seems almost ready.{/i}"
                            "{i}Hoisting herself into the storm, the hatch slams shut behind her, the blast of air covering the windshield instantly in frost.{/i}"
                            "{i}You leap forward, attempting to wipe the glass clean, but your arm feels weak, and you lose your balance on the suddenly icy floor.{/i}"
                            "{i}Collapsing against the dashboard, you feel your skin stick to the metal, the pain so sharp it cuts through the numbness in your fingers.{/i}"
                            "{i}Outside, [vesta] is blown against the ship, falling hard on the deck of the ship.{/i}"
                            "{i}She struggles to her feet, however, sliding her pieces of metal across the gash wielding the welder with ease only granted by experience.{/i}"
                            "{i}Before you know it, she finishes and begins to stumble back toward you, her feet sinking into the wet sand that surrounds the ship.{/i}"
                            "{i}A gust catches her from behind, throwing [vesta] to the ground and sending the emergency welder flying.{/i}"
                            "{i}You hear yourself cry out, and you rip your hands from the dashboard, grasping at nothing. Your breath fogs up the windshield, obscuring your view.{/i}"
                            "{i}For a second, you can hear nothing by the howling of the wind and the deafening sound of hail hitting the ship.{/i}"
                            "{i}Then, just as you are about to give up hope, a bang startles you overhead as the hatch is wrenched open, and hail rains through, accompanied by wind that blows your hair back and causes ice to crust across your skin.{/i}"
                            Passenger "Y-y-you n-n-n-need y-your c-c-coat!"
                            "{i}[Vesta] shakes so hard she can barely get the words out, but her blur of a finger points you to where it lies crumpled in a corner.{/i}"
                            "{i}You crawl across the ground, feeling the face on your skin crack as you attempt to form words.{/i}"
                            Pilot "Heat-t-ting c-controls are on the f-far l-left-t. If-f y-you’ve s-s-sealed th-the hole, you sh-sh-should be able to switch it-t to only the c-c-cockp-pit."
                            "{i}You pull your coat on, wishing your body could generate enough heat to warm it up.{/i}"
                            "{i}Following your commands, [vesta] redirects the heat, and you feel warm air fill the room as the atmosphere is filtered out, your breathing slowly becoming less shaky and strained.{/i}"
                            "{i}As the heat washes over you, you feel yourself begin to fall into unconsciousness, your body struggling to maintain heat.{/i}"
                            "{i}As your eyes close, you see [vesta] sink to the floor as well, unable to continue to function.{/i}"
                            jump aftermath
                        "{i}Tell her to come back.{/i}":
                            Pilot "It’s not worth it! You’re more likely to be killed by the storm than waiting for help."
                            "{i}[vesta] climbs back up the ladder.{/i}"
                            Passenger "You’re sure we can’t fix it? I know how to use these tools!"
                            jump pass_helps_inside
                label pass_helps_inside:
                    Pilot "I...I don’t think so. At this point, the only thing we can do is call for help."
                    "{i}[vesta]’s face pales even more, but she nods.{/i}"
                    Passenger "Ok, how do we do that?"
                    "{i}You scan the cockpit, and your eyes land on the emergency radio. You grab it, clutching it to your chest like it’s your lifeline.{/i}"
                    Pilot "We’re going to have to stay here. It’s the highest part of the ship, and we should be able to seal it off from the rest of the ship."
                    Pilot "Unfortunately, the heating probably won’t function while we’re up here. It’s designed to heat the coldest place, and provided another hole doesn’t get put in the cockpit, it should stay at least a little warmer."
                    "{i}[vesta] nods, shivering hard. She pulls her coat tighter around herself, leaning against the wall for support.{/i}"
                    Passenger "S-s-o what next?"
                    "{i}You look down at the radio, checking it for damage.{/i}"
                    Pilot "Shit!"
                    Passenger "What is it? Is it broken?"
                    "{i}You shake your head, having noticed the power cable, which should have attached to a spool inside the cockpit, had been severed, the wires frayed and ripped.{/i}"
                    Pilot "The power cable is severed, which means we won’t be able to send or receive messages without manual power."
                    Passenger "M-manual p-p-power?"
                    "{i}You gesture to the crank built onto the side of the radio.{/i}"
                    Pilot "It’s incredibly archaic, but it should work."
                    play Radio 'audio/amb-sfx_radio-static.mp3'
                    "{i}You spin the crank, the muscles in your arm protesting with every rotation. After a few seconds, lights begin to glow dimly, and a faint crackle emanates from the speakers.{/i}"
                    Pilot "Mayday! Mayday! [protagName] to Viacaellum, come in Viacaellum!"
                    Pilot "My ship crashed right outside of your city."
                    "{i}You rattle off your last known coordinates.{/i}"
                    Pilot "Please send help! The ship’s flooding fast and we’ve lost heat. "
                    "{i}You feel yourself begin to fall into unconsciousness, your body struggling to maintain heat. {/i}"
                    Pilot "P-please! Viacaellum come in!"
                    "{i}You continue to repeat the message, desperate for a reply.{/i}"
                    "{i}Just as your body feels ready to give out, the crackle spikes, and you hear garbled words over the whir of the crank.{/i}"
                    Radio "We copy [protagName], we will send a rescue vehicle to those coordinates once the storm has cleared enough to ensure safe travel. Over."
                    "{i}As your eyes close, you see [vesta] sink to the floor as well, unable to continue to function.{/i}"

                    jump aftermath
            label pass_refuses_to_help:
                "{i}You call out for [vesta] again, and this time hear a crash in the next room.{/i}"
                "{i}[Vesta] yelps, and you feel yourself twinge with sympathetic pain. Scrambling forward, you find her sprawled against the table, surrounded by pieces of broken glass from the mirror that toppled next to her.{/i}"
                show pass fall 1
                "{i}You reach out, managing to pull her into the kitchen and feel the pressure of the water around your knees, lapping at the tops of your boots as if desperate to poor in.{/i}"
                "{i}[Vesta] looks around, finally seeming to comprehend that things are not as they should be.{/i}"
                Passenger "What the hell happened?!"
                "{i}She yells this, her eyes frantic as she attempts to make anything out in the dim emergency lights{/i}"
                play sound 'audio/sfx_thunder.mp3'
                Pilot "We crashed! The ship got hit by one of the largest gusts I’ve ever experienced!"
                "{i}Your voice is nearly drowned out by a peal of thunder, and you find yourself gasping for breath, creating a cloud of mist in the freezing air.{/i}"
                Passenger "You said we could make it to Viacaellum before the storm hits!"
                "{i}[vesta] is glaring at you, her face tinged with red, whether from anger or cold you aren’t sure.{/i}"
                Pilot "Look, we have bigger things to deal with here!"
                Pilot "We need to find our helmets! I think there’s a hole somewhere in the ship, and the air is going to become unbreathable within the next few minutes!"
                "{i}[Vesta] nods, stomping through the rising water to the desk in the next room.{/i}"
                hide pass with dissolve
                "{i}You begin to fumble around in the darkness, searching desperately for your helmet.{/i}"
                Passenger "I found it!"
                "{i}Minutes pass, and you find yourself beginning to cough, the air growing steadily thicker as your search becomes more frantic.{/i}"
                "{i}You look down and realize that your fingers are faintly blue in the dim emergency lights.{/i}"
                "{i}As you search, you realize you’re shaking, water having seeped under the coat and pants of your suit while you were unconscious.{/i}"
                "{i}After what feels like a lifetime, you find your helmet and stuff it on.{/i}"
                "{i}It takes a few minutes, but your head begins to clear, and you frantically start to look for the source of the leak.{/i}"
                "{i}Your heart sinks when you see a gash a few feet long that rain is pouring into. You know your hands are too numb and shaking too hard to weld that gash shut.{/i}"
                "{i}You give up on fixing the leak, and instead make your way to the cockpit of the ship.{/i}"
                "{i}Searching desperately for the emergency radio, you find it on the ground in the corner of the cockpit, its power cable severed.{/i}"
                "{i}Looking it over desperately for any other signs of damage, you find none, and hastily fold out the hand crank, your hands shaking as you attempt to grasp the handle.{/i}"
                "{i}You spin the crank, the muscles in your arm protesting with every rotation. After a few seconds, lights begin to glow dimly, and a faint crackle emanates from the speakers.{/i}"
                Pilot "Mayday! Mayday! [protagName] to Viacaellum, come in Viacaellum!"
                "{i}The storm is so loud that you can barely hear the radio static, but in the back of your mind you think you could hear a soft click on the other end.{/i}"
                Pilot "SOS! I repeat, SOS! My ship has crash-landed outside of your city, please send help!"
                "{i}You hurriedly look over to your coord system, but the screen is dark and cracked, the emergency power too weak to keep it operational.{/i}"
                "{i}You feel your eyes beginning to get heavy, and you clutch the radio to your chest as you crawl to the hatch of the cockpit, calling down into the rest of the ship.{/i}"
                Pilot "Come to the cockpit! It’s the only place we have a chance of surviving the storm!"
                "{i}You yell to [vesta].{/i}"
                "{i}You lose your footing and crash into the floor, sliding down to the opposite end of the cockpit.{/i}"
                "{i}Dazed and freezing against the cold metal, you wrap your coat tighter around yourself, hoping your body heat will be enough to warm the sodden clothes underneath.{/i}"
                show pass std i with dissolve
                "{i}After what feels like an eternity, you see [vesta] struggle up the tilted ladder in the cockpit, wincing with every rung.{/i}"
                Passenger "How could you do this?"
                "{i}She seems delirious, but the anger in her voice is palpable.{/i}"
                Passenger "You said we’d make it. You risked not just your life, but also mine!"
                Passenger "What were you thinking? Why did you let this happen?"
                "{i}You open your mouth to protest.{/i}"
                Passenger "You were supposed to know what was safe! You were supposed to know when we had to turn around."
                Passenger "I couldn’t have known what was safe! I didn’t even know the journey would take longer using this {i}awful{/i} thing rather than a transport!"
                "{i}She kicks the wall of the cockpit weakly, sinking to the floor with a look of despair.{/i}"
                Passenger "I...{i}trusted{/i} you to do this right. We should’ve just turned back."
                "{i}She hugs her torso, reflexively trying to keep from losing more heat.{/i}"
                Passenger "And you knew that this wouldn’t work, didn’t you! You were checking that weather station at the vista."
                "{i}She seems to have come to her final conclusion, all of your actions lining up into an arching conspiracy that lead to this crash.{/i}"
                "{i}She opens her mouth as if to say more, but nothing comes out, her anger and paranoia too strong to manifest into words.{/i}"
                "{i}Unable to protest, you feel your body give up, and you collapse on the floor.{/i}"
                "{i}As you close your eyes, the last thing you see is the radio.{/i}"
                jump aftermath
            label aftermath:
                show black with fade
                hide pass
                stop Wind fadeout 5.0
                stop Hail fadeout 5.0
                stop Rain fadeout 5.0
                if nationalist_points > 1:
                    play background_music "audio/mus_ambient-bad.ogg" fadein 5.0
                else:
                    play background_music "audio/mus_ambient.ogg" fadein 5.0
                hide black with fade
                "{i}You wake up to a looping radio message.{/i}"
                Radio "Distress call heard. Please evacuate the vehicle."
                "{i}After a few loops, the sounds begin to distort, the message slowing down as the radio loses power.{/i}"
                "{i}Looking around, you don't see [vesta], but notice that the emergency hatch on the ceiling of the cockpit is lined with frost, unlocked but closed.{/i}"
                "{i}Eventually, you manage to drag yourself to your feet, your limbs feeling too frozen to move. Straining to reach the hatch, you open it and make your way outside and find [vesta].{/i}"
        label ending:
            scene rd front
            if friendship > 1:
                show pass std t
                with Dissolve(3.0)
                if friendship > 7:
                    "{i}You slide down the roof of the cockpit, stumbling slightly as your feet sink into the wet sand that buries your ship.{/i}"
                    "{i}Making your way gingerly along the unstable surface, you climb onto the road, limping across the cracked and pitted expanse to [vesta], who sits on a rock, observing the striking view of Viacaellum.{/i}"
                    Passenger "We almost made it."
                    "{i}She gestures at the city, which stands only a few miles away, a looming dome bursting from a crater.{/i}"
                    Pilot "Yeah. Crazy to think we were that close and still almost died."
                    "{i}[Vesta] laughs weakly, which transforms into a cough that racks her whole body.{/i}"
                    Passenger "Do you have any idea how long it’ll take for the rescue vehicle to get here?"
                    "{i}You shrug, pointing at the road leading into the city, which appears to be largely submerged in water.{/i}"
                    Pilot "Until they finish clearing that, it’s gonna be awhile. The roads used to have good drainage systems, but they stopped functioning properly years ago."
                    Passenger "Huh."
                    "{i}Glancing over at your ruined ship for a second, [vesta] winces, putting a hand up to her neck.{/i}"
                    Passenger "So what happens next for you? I know just enough about how vehicles work to say that yours is trashed."
                    "{i}You follow her gaze, taking in the wreckage. Engine parts and body panels litter the road as far back as you can see, and though [vesta] fixed the largest hole, it doesn’t take much observation to know that it is beyond repair.{/i}"
                    Pilot "I...don't know."
                    Pilot "I guess I’d never really thought about the next thing. Not like I’ve got much choice now."

                    "{i}You and [vesta] sigh in union, and she makes a noise of agreement.{/i}"
                    Passenger "I guess it’s kinda a fresh start for both of us. Or the sudden and brutal end to your old way of life, whichever way you choose to see it."
                    "{i}She laughs again, and the coughs soon follow.{/i}"
                    "{i}The two of you sit in silence with that statement for a while, until [vesta] gets up suddenly.{/i}"
                    Passenger "Do you see that!"
                    "{i}You squint at the gate to the city, and notice a tiny trail of water and steam rising on the road just in front of the gate.{/i}"
                    Pilot "I guess our rescue is close at hand."
                    Passenger "Does that mean our journey together is over?"
                    "{i}You look over at her, surprised by the question.{/i}"
                    Pilot "I mean...I guess?"
                    "{i}[Vesta] watches the trail slowly grow closer for a few moments.{/i}"
                    Passenger "I guess I don’t want to never see you again."
                    "{i}She looks away, her posture one of embarrassment.{/i}"
                    Passenger "I’m sorry, I just--we almost died a bit ago! And both of our old lives are kinda gone now."
                    Passenger "I guess I’d like to hear from you once you’ve got a grasp on what’s happening again. I can’t help but blame myself for your livelihood getting destroyed."
                    "{i}She goes silent, and when you try to answer, she interrupts you.{/i}"
                    Passenger "I don’t need a resolved response. Just...here."
                    "{i}She rummages around in the pockets of her coat until she finds what she’s looking for: a personal card.{/i}"
                    Passenger "If you’re ever in Viacaellum again, or that’s where you end up, look me up in a directory."
                    "{i}The two of you sit for the rest of the time in silence, the card weighing slightly in your pocket.{/i}"
                    "{i}You don’t know what’s next for you. You might go back to Viacaellum, you might not. Your livelihood, as she put it, is gone.{/i}"
                    "{i}Whatever the future holds is too foggy for you to know, so you sit and stare at this strange city, waiting for your new life to start.{/i}"
            elif friendship<-1:
                "{i}You slide down the roof of the cockpit, stumbling slightly as your feet sink into the wet sand that buries your ship.{/i}"
                "{i}Making your way gingerly along the unstable surface, you climb onto the road, limping across the cracked and pitted expanse to [vesta], who sits on a rock, observing the striking view of Viacaellum.{/i}"
                Passenger "I can't believe I almost made it."
                "{i}She gestures at the city, which stands only a few miles away, a looming dome bursting from a crater.{/i}"
                Pilot "It’s not too far now. And you heard the message, rescue will be here soon."
                "{i}[Vesta] laughs weakly, which transforms into a cough that racks her whole body.{/i}"
                Passenger "Yeah. And not a moment too soon. Do you think it’ll be much longer? The storm has passed for some time now."
                "{i}You shrug, pointing at the road leading into the city, which appears to be largely submerged in water.{/i}"
                Pilot "Until they finish clearing that, it’s gonna be awhile. The roads used to have good drainage systems, but they stopped functioning properly years ago."
                Passenger "I guess [nameNellL] was right about that."
                "{i}You think back to that time in the refueling station, wondering what else [nameNellL] had told [vesta] before you entered the building.{/i}"
                "{i}Glancing over at your ruined ship for a second, [vesta] winces, putting a hand up to her neck.{/i}"
                Passenger "So what happens next for you? I know just enough about how vehicles work to say that yours is trashed."
                "{i}You follow her gaze, taking in the wreckage. Engine parts and body panels litter the road as far back as you can see, and though [vesta] fixed the largest hole, it doesn’t take much observation to know that it is beyond repair.{/i}"
                Pilot "I...don't know."
                Pilot "I guess I’d never really thought about the next thing. Not like I’ve got much choice now."
                "{i}You sigh, and [vesta] looks over at you, as if unsure of what to say.{/i}"
                Passenger "I’m sorry about that, I guess. It’s a nasty way to lose a ship."
                "{i}You snort at this.{/i}"
                Pilot "I don’t think I’ve ever heard a larger understatement."
                Passenger "Do you see that!"
                "{i}You squint at the gate to the city, and notice a tiny trail of water and steam rising on the road just in front of the gate.{/i}"
                Pilot "I guess our rescue is close at hand."
                "{i}You squint at the gate to the city, and notice a tiny trail of water and steam rising on the road just in front of the gate.{/i}"
                Pilot "I guess our rescue is close at hand."
                Passenger "I guess it is."
                "{i}She picks herself up from the rock she was leaning against, though still maintaining a hold for support.{/i}"
                Passenger "I...thank you."
                "{i}She glances over at you for a moment before turning her eyes back to the road in the distance. She doesn’t quite seem to know what else to say.{/i}"
                "{i}You let the thanks linger in the air, knowing that there isn’t really any response. Instead, the two of you watch the cloud slowly grow, taking comfort in the end of this arduous journey.{/i}"
                "{i}[Vesta] is right, however. Your old life, whether you like it or not, isn’t something you’ll ever be able to get back again. Not in the same way, at least.{/i}"
                "{i}You don’t know what’s next for you. You might go back to Viacaellum, you might not.  You couldn’t have ever foreseen this happening in the future, but there wasn’t really any way to stop it either.{/i}"
                "{i}Whatever the future holds is too foggy for you to know, so you sit and stare at this strange city, waiting for your new life to start.{/i}"
                jump credits
            else:
                "{i}You slide down the roof of the cockpit, stumbling slightly as your feet sink into the wet sand that buries your ship.{/i}"
                "{i}Making your way gingerly along the unstable surface, you climb onto the road, limping across the cracked and pitted expanse to [vesta], who sits on a rock, observing the striking view of Viacaellum.{/i}"
                "{i}[Vesta] sits against a rock on the far side, staring out at Viacaellum. She glances over at you, catching your eye for a split second, but her gaze doesn’t linger.{/i}"
                "{i}You turn away from her, staring out at the city as well, and let your thoughts run wild.{/i}"
                "{i}You know your ship is broken. Truly, fully broken.{/i}"
                "{i}Even the brief glimpse you got of the engine, and trail of debris that stretches back as far as you can see, was enough to know it was far beyond repair.{/i}"
                "{i}Your life, at least as you knew it, is over. Whatever’s next for you is too unknowable to contemplate at the moment, so instead you focus on the gates of the city.{/i}"
                "{i}After some time, you catch a glimpse of a miniscule cloud arising from the horizon.{/i}"
                "{i}It seems as though this terrible journey is finally coming to an end, and you have almost nothing to show for it.{/i}"
                "{i}You don’t know what’s next for you. You might go back to Viacaellum, you might not.  You couldn’t have ever foreseen this happening in the future, but there wasn’t really any way to stop it either.{/i}"
                "{i}These thoughts are heavy in your mind, you sit and watch the strange city, waiting for your new life to start. {/i}"

    label credits:
        scene black with fade
        pause 0.5
        show text "Thank you for playing a Spaced-Out Studios Original" at truecenter with fade
        pause 2
        hide text with Dissolve(2.0)
        show text "Programming by Tate Donnelly{p}{p}Art by Nathan Booth{p}{p}Original Music and Proofreading by Benny Klaiman{p}{p}Writing by Tate Donnelly and Nathan Booth" at truecenter with fade
        pause 10
        hide text with Dissolve(2.0)
        show text "Radio Static - Sound Effect. YouTube, uploaded by Audio Library - Free Sound Effects, 1 Feb. 2016, https://www.youtube.com/watch?v=fo0G59aygu8.{p}{p}10 hours of hard rain on a metal roof (Rain Sleep Sounds) Rain Sounds for Sleeping. Rainfall.lluvia. YouTube, uploaded by SleepDroid Studios Sleep Sounds, 26 Mar. 2015, https://www.youtube.com/watch?v=s61TmfE3zY4.{p}{p}8 hours of train station sounds | train station sound effect and railway station sound. YouTube, uploaded by 8 Hours of, 6 Apr. 2015, https://www.youtube.com/watch?v=GRZ6rrpMoHs." at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "Heavy Rain Sounds at Night - Sleep, Study, Relax | Ambient Noise Rainstorm, @Ultizzz day#69. YouTube, uploaded by Ultimate Ambient Noise Soundzzz, 2 Jun. 2018, https://www.youtube.com/watch?v=XSL1HbrE3DE.{p}{p}Tibeauthetraveler - Ember (ft.eleven). YouTube, uploaded by Tibeauthetraveler, 6 Mar. 2021, https://www.youtube.com/watch?v=_libcjgqnog.{p}{p}Sounds For The Supermarket 1 (1975) - Grocery Store Music. YouTube, uploaded by TiHKAL MooN DWeLLeR, 20 Oct. 2020, https://www.youtube.com/watch?v=U-WzMovyzUA.{p}{p}Plane Crash - @Sound Effect. YouTube, uploaded by Sound Effect, 2 May 2020, https://www.youtube.com/watch?v=oEMUjsw2S74."  at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "Low Pitched Metal creaks and stress Groans. YouTube, uploaded by OroBolide8755, 6 Nov. 2018, https://www.youtube.com/watch?v=EWmuR-IDSi4.{p}{p}Ear Ringing Sound Effect - Free Download HD. YouTube, uploaded by SFX and GFX, 22 Aug. 2015, https://www.youtube.com/watch?v=rHTinEcgLn0.{p}{p}Heavy Hail Sound Effects. YouTube, uploaded by Free To Use Sounds, 17 Jun. 2020, https://www.youtube.com/watch?v=E0ArjfkbLLY."  at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "Shop Door Bell. YouTube, uploaded by Sound FX Tracks, 20 Aug. 2020, https://www.youtube.com/watch?v=8yXqrRwkar8.{p}{p}Jet Take Off and Fly By Sound Effect. YouTube, uploaded by SoundEffectsFactory, 17 Jan. 2012, https://www.youtube.com/watch?v=OUNwFrt5IEQ.{p}{p}Oh no our table it's broken. YouTube, uploaded by luke2587I, 24 Apr. 2019, https://www.youtube.com/watch?v=pK4x9jIh5rA.{p}{p}Thunder Sound Effect. YouTube, uploaded by arival0, 8 Apr. 2017, https://www.youtube.com/watch?v=vJ08fwaLXwg."  at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "Down to Business (Title/Situational){p}{p}A Bright Future (Good Ending){p}{p}A \"Blight\" Future (Bad Ending){p}{p}by Benny Klaiman"  at truecenter with fade
        pause 3
        hide text with Dissolve(5.0)
        return
