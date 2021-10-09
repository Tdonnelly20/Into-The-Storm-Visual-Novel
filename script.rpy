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
        scene main_menu
        python:
            protagName = renpy.input("What is your name?", length=32)
            protagName = protagName.strip()

        label Variables:
            $ timer_range = 0
            $ timer_jump = 0
            $ nationalist_points = 0
            $ attendant = 0
            $ friendship = 0
            $ nameKnown =False
            $ helped = 0
            $ nameVesta = 'Passenger'
            $ nameVestaU = 'The passenger'
            $ nameVestaL = 'the passenger'
            $ nameNellU ='The attendant'
            $ nameNellL='the attendant'

        label defineCharacters:
            define Pilot= Character("[protagName]")
            define Radio=Character("Radio")
            define Passenger=DynamicCharacter("nameVesta")
            define Vesta=DynamicCharacter("nameVestaU")
            define vesta=DynamicCharacter("nameVestaL")
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

                    To finish the work that was begun hundreds of years ago to turn these landscapes from harsh to hospitable!

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
                show pass coat i behind cp
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
            with dissolve
            scene rd front
            show doma_station
            show cp back behind doma_station
            show pass qu sit n behind doma_station
            pause 1
            hide doma_station with Dissolve(1.0)
            pause .5

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
                "{i}You reach to turn on the radio, thinking she is finished talking, but [vesta] breaks the awkward silence before you can turn it on.{/i}"
                show pass qu sit i
                Passenger "Is traffic always this bad?"
                Pilot "Not really, I think there’s some event happening tomorrow, but I’m not sure."
                "{i}She looks uncomfortable.{/i}"
                jump choice3_end
            label friendly_small_talk_CS3:
                $ friendship += 1
                Pilot "So why are you heading to Viacaellum? Are you going on vacation?"
                "{i}She pauses for a second, looking out the window.{/i}"
                show pass qu sit t
                Passenger "Sort of, I really just had to get out of town."
                Pilot "That’s fair, it’s good to get out of the city every once and a while."
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
                "{i}She falls silent for a few minutes, watching buildings pass as you snake your way through Domatellium.{/i}"
                show pass qu sit s
                "{i}You reach to turn on the radio, thinking she is finished talking, but [vesta] breaks the awkward silence before you can turn it on.{/i}"
                show pass qu sit i
                Passenger "Is traffic always this bad?"
                Pilot "Not really, I think there’s some event happening tomorrow, but I’m not sure."
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
                "{i}[Vesta] sighs heavily, turning back to the window.{/i}"
                jump choice3_end
            label choice3_end:
                show pass qu sit s
                stop background_music
                play Radio 'audio/amb-sfx_radio-static.mp3'
                play title "audio/mus_title.ogg" fadein 1.0
                "{i}You turn on the radio to listen to some music.{/i}"
                play sound 'audio/sfx_space-engine.mp3'
                "{i}The radio begins to play music and [vesta] seems to relax somewhat as you reach the city walls.{/i}"
                stop background_music fadeout 5.0

        label talking_about_radio_scenes:
            "{i}Passing through the massive gate, you accelerate quickly, the city walls beginning to recede quickly in the background.{/i}"
            stop Radio
            hide black with fade
            stop title
            play background_music "audio/mus_ambient.ogg" fadein 3.0
            show pass qu sit i
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
                Pilot "There's an open bunk for you below the ship"
                hide pass qu sit s with fade
                "{i}Still looking uncomfortable, [vesta] heads down below.{/i}"
                jump choice4_end
            label friendly_4:
                $ friendship += 1;
                Pilot "Once you get out of the domes, you lose reception. Something to do with ambient radiation or something."
                Pilot "There are a few spots where we'll be able to pick it up again, but we won't have it for most of the trip."
                show pass qu sit s
                Passenger "Oh."
                "{i}[Vesta] looks unsettled, shifting in her seat.{/i}"
                Pilot "Have you ever left Domatellium before?"
                show pass qu sit t
                Passenger "No, I never really had any reason to leave."
                Pilot "That explains it then. Most people who never leave the city wouldn't know about it."
                Pilot "You should head down below now and start setting up a bunk, though. There’s an empty wardrobe and a bunk bed, that's yours until we get to Viacaellum."
                "{i}She nods and makes her way down the ladder, clearly shaken, but glad to have a task.{/i}"
                hide pass qu sit n with fade
                "{i}You listen to her footsteps recede until the sound is overcome by the noise of the engines, before turning your focus back to the open road.{/i}"
            jump choice4_end
            label hostile_4:
                $ friendship -= 1;
                Pilot "You didn't know? Really?"
                show pass qu sit i
                Pilot "Is this your first time out of the city or something?"
                "{i}[Passenger] nods, looking uncomfortable.{/i}"
                Pilot "Huh that's weird, I can't imagine staying in the same place my whole life."
                "{i}She glares at you, clearly frustrated.{/i}"
                Pilot "Anyways, there’s an open bunk down below for you. You should go set up."
                hide pass qu sit i with fade
                "{i}[Vesta] gets up and heads down below, clearly happy to get away from your conversation.{/i}"
                "{i}You drive alone for a few hours.{/i}"
                jump choice4_end
            label choice4_end:

            hide pass
            hide cp
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
                xpos .4
                ypos .1
                zoom 1.5
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
                $ timer_jump = 'menu_Storm_Warning'
            show screen countdown
            menu:
                "Do you want to turn back?":
                    hide screen countdown
                    $ friendship += 1
                    Pilot "I think we'll be fine, but do you want to turn back?"
                    if friendship >= 0:
                        "{i}She shakes her head.{/i}"
                        show pass qu sit t at sitAtTable behind table2t
                        Passenger "If you think we'll be fine let's keep going."
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
            show pass std n at bottomRight with fade
            Passenger "I'm going to go get something to eat."
            show pass std i at atDoor with fade
            "{i}You nod, and begin the apparatus’ refueling process. When you turn to head inside the building, you see [vesta] still standing outside.{/i}"
            "{i}She glances back at you before opening the door, the anxiety of entering an unfamiliar place clearly giving her some pause.{/i}"
            label wave:
                $ timer_jump = 'menu_Wave'
                show screen countdown
            menu:
                "{i}Wave to her to go in.{/i}":
                    hide screen countdown
                    $ friendship += 1
                    "{i}You wave at her to enter, and watch reassurance flicker across her face. She squares her shoulders and pushes on the door, crossing the threshold and giving you a glimpse of the empty counter.{/i}"
                    jump enter
                "{i}Look away.{/i}":
                    hide screen countdown
                    jump wave_neutral
            label wave_neutral:
                hide screen countdown
                "{i}You look away, and notice out of the corner of your eye her shoulders sag slightly. Nevertheless, she squares them again, pushing on the door, crossing the threshold and giving you a glimpse of the empty counter.{/i}"
                jump enter
            label enter:
                hide pass with fade
            stop background_music fadeout 2.0

            play background_music 'audio/mus_gas-station.ogg' fadein 3.0
            "{i}A second later you enter the station, greeted by the familiar crackle of the radio.{/i}"
            play sound 'audio/sfx_jingle.mp3'
            scene int_rfstation c
            transform lower:
                xpos 0.2
                ypos 0.3

            transform bottomRight:
                xpos 0.5
                ypos 0.4
            show rs clerk n at lower
            show pass std n at bottomRight
            show ext_rfstation
            hide ext_rfstation with fade

            pause 0.5
            play Radio 'audio/amb-sfx_radio-static.mp3'
            Radio "...as the election of Domatellium’s new governor draws near, gatherings in support of the former mayor’s campaign for the position have popped up across Domatellium!"
            Radio "While this campaign has been somewhat polarizing over the past several weeks, it appears that the mayor’s supporters, or “neighbors,” as they call themselves, are attempting to change that view with citywide celebrations."
            Radio "We go live to one of our reporters on the scene…"
            stop Radio
            label choice5:
                $ timer_jump = 'menu_neutral5'
            show screen countdown
            menu:
                "{i}Listen to the radio.{/i}":
                    hide screen countdown
                    jump Hear_About_Gatherings
                "{i}Talk to refuel station attendant.{/i}":
                    hide screen countdown
                    $ attendant += 1
                    jump conversation_with_attendant
            label menu_neutral5:
                hide screen countdown
                jump Hear_About_Gatherings
            label conversation_with_attendant:
                Passenger "Can you turn that off?"
                Nell "Gladly, I can't stand that crap."
                "{i}[Nell] switches the radio off and looks up as the bell rings with a smile.{/i}"
                Nell "Hey, [Pilot]! Where’ve you been? You haven’t stopped by in a while."
                Pilot "Ah, you know how piloting is, Nell. I don’t exactly get to chose where I go."
                $ nameNellU ='Nell'
                $ nameNellL='Nell'
                Nell "Fair enough, now come take a seat and I’ll make you your usual once I finish up here."
                "{i}As you sit down, Nell turns back to [vesta].{/i}"
                Nell "If they win the election, they’d just have us revert back to how it was when this whole thing fell apart."
                jump Fell_Apart
            label Hear_About_Gatherings:
                "{i}You give [nell] who stands behind the counter a wave as you enter, silently taking a seat and focusing on the radio.{/i}"
                hide pass
                hide rs
                with dissolve
                scene int_rfstation r with Dissolve(1.0)
                pause .5
                "{i}Faint cheering errupts from the radio’s background when the news station switches to the reporter at the gatherings.{/i}"
                Radio "Thanks, Birdy. As you can likely hear, many neighbors have come out to show their support for the former mayor’s campaign."
                Radio "Let’s see if we can ask one of these fine folks some questions."
                Radio "Sir, why have you come out to the gatherings?"
                "{i}There’s some slight fumbling with the microphone right before the interviewee speaks.{/i}"
                Radio "Well, I gotta say that Domatellium--hell, all of Duoterra--ain’t what it used to be anymore. My grandpa told me stories about how it used to be and it’s a real shame how far we’ve fallen."
                "{i}The words become garbled for a moment as the interviewee gets too far from the microphone.{/i}"
                Radio "--but we--Domatellium, that is--used to have aspirations! We used to want progress! And y’know, that’s really all I’m looking for!"
                "{i}The reporter attempts to butt in, but the neighbor quickly speaks over them.{/i}"
                Radio "And why should we settle for stagnation? Duoterra was one of the first colonies, the government should understand that we need to reclaim this planet!"
                "{i}The sounds of a crowd begin to overcome the speaker’s voice, and the reporter jumps at the opportunity to move on to the next person.{/i}"
                Radio "And, what do you have to say, Ma’am?"
                "{i}There’s some more fumbling as the microphone is handed to another neighbor.{/i}"
                Radio "He’s absolutely right. The government has ignored us for too long!"
                Radio "But really we want people to come down and get to know the movement! I promise we’re not all so passionate, we only want to make the world a better place!"
                "{i}The reporter takes the microphone back, and their voice comes through clear once again.{/i}"
                Radio "Well there you have it folks, you’ll find a few lively characters down here, but all in all it seems their message is one of--"
                Nell "With all due respect, I’ve gotta turn this crap off."
                scene int_rfstation c
                show rs clerk n at lower
                show pass std n at bottomRight
                stop Radio
                "{i}[Nell] goes back to cleaning the area behind the counter, and an awkward silence fills the space.{/i}"
                "{i}[Vesta] finishes her meal, pushing her plate away from her.{/i}"
                show pass std i at bottomRight
                Passenger "How much longer will we have to wait?"
                Pilot "It should be done now, actually."
                Passenger "Oh! So we could leave soon?"
                Pilot "I mean, yes."
                show pass std n at bottomRight
                Passenger "So..."
                "{i}You get to your feet, waiving goodbye to [nell] as you exit.{/i}"
                jump choice5_end
            label Fell_Apart:
                $ timer_jump = 'menu_neutral5'
                show screen countdown
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
                    Pilot "What do you mean fell apart"
                    show pass std t at bottomRight
                    Nell "What do you think I mean?"
                    show rs clerk t at lower
                    Nell "Terraforming halted nearly a century ago. Haven’t you looked outside? The roads between our cities are a half day of radiation away from crumbling to dust."
                    Nell "I’ve watched the walls of Domatellium get more cratered every year, and I haven’t seen someone try to repair them since I was a {i}child.{/i}"
                    Nell """
                    My grandmother was one of the head engineers on Domatellium’s terraforming equipment back when it was still functioning, and even then it was failing.

                    They’d been feeding those machines sub-par material for so long that they were beyond salvation.

                    And so people got scared. They got tired of the decline and looked for change, but found it by trying to recreate the past, instead of actually looking toward the future.

                    Damnit, I’m starting to sound as preachy as that awful mayor.
                    """
                    "{i}Nell sets down the glass she had been violently drying.{/i}"
                    Nell """
                    Point being, some pundit got elected that promised change. Tried forcing the engineers to find solutions that didn’t exist, to make the machines work with the wrong materials.

                    My grandma got fired then, so I don’t know what happened. She knew it was fruitless, and I guess now I’m in the same position.
                    """
                    "{i}Nell laughs at herself, picking up another glass and going back to drying.{/i}"
                    Nell "’Cept here I am, drying glasses in a run-down refueling station."
                    show rs clerk n at lower
                    "{i}You look over at [vesta], who’s staring at Nell with a look you can’t quite place.{/i}"
                    show pass std n at bottomRight
                    "{i}[Vesta] finishes her meal, pushing her plate away from her.{/i}"
                    show pass std i at bottomRight
                    Passenger "How much longer will we have to wait?"
                    Pilot "It should be done now, actually."
                    Passenger "Oh! So we could leave soon?"
                    Pilot "I mean, yes."
                    show rs clerk t at lower
                    "{i}Nell watches [vesta] keenly, noting her sudden hurry to leave.{/i}"
                    show pass std n at bottomRight
                    "{i}[Vesta] stands, and makes a motion to begin walking for the exit, but stops herself.{/i}"
                    Passenger "Oh, and also, I wanted to say thanks, I guess. It was…"
                    "{i}She trails off, clearly unable to find the words to express what she means. Turning quickly, [vesta] leaves as if chased by her unfinished sentence.{/i}"
                    hide pass with fade
                    Nell "She’s a weird one, huh?"
                    menu:
                        "I guess.":
                            Pilot "She kinda is. All the way to Viacaellum with no luggage is an interesting choice."
                            Nell "That certainly is. You keep an eye on her though, alright? That’s a lady running from something if I’ve ever seen one."
                            "{i}You shrug, give Nell a final wave, and leave the building.{/i}"
                        "{i}Shrug.{/i}":
                            "{i}You shrug, and Nell nods knowingly.{/i}"
                            Nell "Be safe out there. That storm’s no joke, so drive quick!"
                            "{i}You head out, waving to Nell once more before exiting the building.{/i}"
                    jump choice5_end
                label hopeful_on_nationalism:
                    Pilot "Isn’t it possible that this could head in a good direction? The speeches I’ve heard on the radio seem like they’ve got some good points. I even heard them talk about starting terraforming again."
                    Nell "What are you even talking about?"
                    Pilot "I’m just saying that they’re at least {i}trying{/i} to find solutions."
                    Nell """
                    {i}Solutions?!{/i} They’re just trying to force a fix on something that’s totally broken! This new movement is just repeating the same points that sent Duoterra on the decline a century ago.

                    Ever wonder why the roads between our cities are a half day of radiation away from crumbling to dust?

                    It’s because we wasted our resources trying to fix terraformers so clogged with sub-par material they’d have to be totally rebuilt if they were ever used again, letting everything else fall into disrepair.
                    """
                    Pilot "But that’s exactly what I’m saying! The mayor wants to try and actually fix things! In the speeches--"
                    Nell "In the speeches! Of course! The speeches where they spout rhetoric and empty promises without a single concrete policy to back it up! I swear--"

                    show pass std i at bottomRight
                    "{i}Before Nell can work herself up to a full on rant, [vesta] interrupts her, pushes her plate away from her.{/i}"
                    Passenger "How much longer will we have to wait?"
                    Pilot "It should be done now, actually."
                    Passenger "So we can leave?"
                    Pilot "I mean, yes."
                    show pass std n at bottomRight
                    Passenger "So..."
                    Pilot "Oh, alright."
                    "{i}You get to your feet, waving goodbye to Nell as you exit. Nell simply looks away, shaking her head.{/i}"
                    jump choice5_end
            label choice5_end:
                scene ext_rfstation
                show pass std n at bottomRight
                show int_rfstation c
                hide int_rfstation c with Dissolve(1.0)
                pause 0.7
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
                "What do you think will happen to Domatellium?" if attendant > 0:
                    hide screen countdown
                    jump conversation_about_attendant
                "What do you think about the gatherings?" if attendant < 1:
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
                Pilot "It seems like the current Governor is too busy sending window washers to polish the inside of Domatellium’s walls to try and fix the outside!"
                "{i}Your conversation falls into an awkward silence.{/i}"
                hide pass with fade
                "{i}When you get to the ship, [vesta] heads down to the bunks without saying anything.{/i}"
                jump choice6_end
            label anti_history_conversation:
                Pilot "Yeah, I’ve known Nell for a while now, and she doesn’t make stuff up."
                Passenger "Oh."
                Passenger "That makes sense, I guess. She’s not really the type for that."
                "{i}[Vesta] looks off into the middle distance for a second, collecting her thoughts.{/i}"
                Passenger "I can’t keep myself from thinking that this whole situation is going to get worse, you know?"
                Passenger "I mean people haven’t talked about terraforming in decades, and all of a sudden it’s this huge issue that everyone’s so...{i}angry{/i} about."
                Passenger "I don’t know though. They never seemed that angry to me."
                hide pass with fade
                "{i}Before you can respond however, [vesta] climbs inside your ship, clearly ending the conversation.{/i}"
                jump choice6_end
            label awkward_walk_back:
                "{i}You and [vesta] walk back to the ship in an awkward silence.{/i}"
                hide pass with fade
                "{i}When you reach the entrance of the ship, you open your mouth, unsure of what to say, but [vesta] climbs inside before you can say anything.{/i}"
                jump choice6_end
            label dont_want_to_talk_about_it:
                Pilot "Why do you want to leave so badly?"
                Passenger "Sorry, [protagName]. I just really don’t want to talk about it."
                Pilot "Alright, we don’t have to talk about it then."
                "{i}The two of you walk silently back to the ship.{/i}"
                hide pass with fade
                jump choice6_end
            label dont_need_to_tell_you:
                Pilot "Why do you want to leave so badly?"
                Passenger "I don't need to tell you!"
                "{i}[Vesta] looks angry and a little frightened, clearly unable to talk to you at the moment.{/i}"
                Pilot "Alright, alright."
                "{i}You both walk the rest of the way back to the ship in silence.{/i}"
                hide pass with fade
                "{i}When you reach it, [vesta] stomps below deck without another word to you.{/i}"
                jump choice6_end
            label conversation_about_leaving_station:
                Pilot "Why do you want to leave so badly?"
                Passenger "I’m just worried about the storm."
                Passenger "I want to put as much distance between Domatellium and myself as possible."
                Pilot "Can I ask why you left Domatellium in the first place?"
                Passenger "I made some mistakes, and I didn’t really see another way out of them."
                Passenger "..."
                Passenger "But, I'd rather not talk about it."
                Pilot "Alright, we don’t have to."
                "{i}The two of you silently silently back to the ship.{/i}"
                hide pass with fade
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
                        Passenger "What do you even know? You think you can make a judgment on it based on a couple radio broadcasts?"
                        hide pass with fade
                        "{i}[Vesta] climbs inside the ship before you can respond, her jaw set with frustration.{/i}"
                    "You're right.":
                        $ nationalist_points -= 1
                        Pilot "I suppose you’re right."
                        Passenger "And on top of it all, everyone acts so weird if you try to question the Neighbor’s message. I can’t even tell if they really all believe it, or if people are just too scared of being the odd one out to disagree."
                        Passenger "I remember how weird everyone acted when I started looking into what people were saying back when…"
                        Passenger "Nevermind."
                        hide pass with fade
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

                    "{i}You drive into the night, but eventually you decide to turn in.{/i}"

        label comfort_passenger_scenes:
            transform thru_door:
                xpos .4
                ypos .1
                zoom .75

            transform atChair:
                xpos .27
                ypos .1
                xzoom -1
            hide cp front with Dissolve(1.0)
            show kn table2 with Dissolve(1.0)
            "{i}As you’re walking to the bunks, you hear muffled sobbing.{/i}"
            show kn thru_door
            show pass qu sit a at thru_door
            with Dissolve(1.0)
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
                hide kn thru_door
                hide pass
                with Dissolve(1.0)
                show sit_2chair
                show pass qu sit s at atChair
                with Dissolve(2.0)
                "{i}You knock lightly on the door and step in the room.{/i}"
                Pilot "Hey, are you alright?"
                show pass qu sit s at atChair
                "{i}[Vesta] shakes her head, not looking up at you. Her body shaking as she tries to choke back her sobs.{/i}"
                Pilot "What's wrong?"
                Passenger "What...what if I’m making the wrong choice?"
                Pilot "What do you mean? Wrong choice?"
                Passenger "Leaving! If I go through with this, what if I can’t go back? I can’t make this choice now. I...oh God. How could I be this stupid?"
                "{i}You kneel down next to her, not totally sure what to do.{/i}"
                label convo1:
                    $ timer_jump = 'menu_convo1'
                    show screen countdown
                label menu_convo1:
                    menu:
                        "We all make stupid decisions.":
                            $ friendship -= 1
                            hide screen countdown
                            Pilot "We all make mistakes sometimes. When we get to Viacaellum, I’m sure you’ll be able to find someone who’ll drive you back once the storm has passed."
                            show pass qu sit a
                            Passenger "That’s not, that’s not what I meant!"
                            "{i}She clenches her fists, her whole body tensing with another sob.{/i}"
                            Passenger "I just…"
                            Passenger "What if things go bad? What if I’ve left and something gets instated and it means I can’t go back!"
                            "{i}[Vesta]’s body seems racked with panic for a second, and she lets out a small wail.{/i}"
                            label convo2:
                                $ timer_jump = 'menu_convo2'
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
                                        Passenger "I need to be alone right now. I can’t deal with this."
                                        Pilot "Oh. Yeah, for sure."
                                        "{i}You get up and walk quietly to the door, turning just before you shut it to take another look back at [vesta], wishing you knew how to help her.{/i}"
                                        "{i}Closing the door behind you, you take a seat on your bunk, drained and unsure of what to do next.{/i}"
                                        jump choice7_end
                                    "{i}Reach out to her.{/i}":
                                        $ friendship += 1
                                        hide screen countdown
                                        "{i}You reach out to her, placing your hand in hers.{/i}"
                                        "{i} Letting out another small noise, she grips your hand so tight her knuckles go white, holding on as if for dear life.{/i}"
                                        "{i}A second later, you find your arms wrapped around her as she hangs on to your torso, her sobs shaking both of you.{/i}"
                                        "{i}Moments pass, and [vesta] seems to gain control of herself, pulling back with an ashamed look on her face.{/i}"
                                        Passenger "I..."
                                        Passenger "I’m sorry. That was so inappropriate."
                                        "{i}You sit back, still not totally sure what to say.{/i}"
                                        jump explain_past
                                label convo2_neutral:
                                    hide screen countdown
                                    "{i}You sit back, trying to give her space, but her body just seems to get tighter and tighter, her sobs ever weaker and more desperate.{/i}"
                                    "{i}After what feels like an eternity, her voice, tiny and thin, makes its way out from between her clenched teeth.{/i}"
                                    Passenger "I need you to leave."
                                    Passenger "I’m sorry. I just…"
                                    Passenger "I need to be alone right now. I can’t deal with this."
                                    Pilot "Oh. Yeah, for sure."
                                    "{i}You get up and walk quietly to the door, turning just before you shut it to take another look back at [vesta], wishing you knew how to help her.{/i}"
                                    "{i}Closing the door behind you, you take a seat on your bunk, drained and unsure of what to do next.{/i}"
                                    jump choice7_end
                        "I don’t think that leaving was stupid.":
                            hide screen countdown
                            $ friendship += 2
                            Pilot "I don’t think leaving was stupid."
                            "{i}[Vesta] looks up at you, and she seems to tremble just a little less for a second.{/i}"
                            Pilot "Why... Do you think it was stupid? "
                            "{i}She looks away again, her face contorted into one of anguish.{/i}"
                            Passenger " I...I’ve made mistakes. So, so, so many."
                            "{i}She takes a moment to let the tears in her eyes subside.{/i}"
                            Passenger "And now...I don’t know that I can go back. I’m so...terrified. I’m terrified that by leaving I’ve fucked everything up and…"
                            "{i}Trailing off, [vesta] looks back at you.{/i}"
                            jump explain_past

                    #TODO
                    #Fix this neutral
                    label convo1_neutral:
                        hide screen countdown
                        Pilot "I'm sorry, I don't know what to say."
                        "{i}After what feels like an eternity, her voice, tiny and thin, makes its way out from between her clenched teeth.{/i}"
                        Passenger "I need you to leave."
                        Passenger "I’m sorry. I just…"
                        Passenger "I need to be alone right now. I can’t deal with this."
                        Pilot "Oh. Yeah, for sure."
                        "{i}You get up and walk quietly to the door, turning just before you shut it to take another look back at [vesta], wishing you knew how to help her.{/i}"
                        "{i}Closing the door behind you, you take a seat on your bunk, drained and unsure of what to do next.{/i}"
                        jump choice7_end
                label explain_past:
                    Passenger """
                    Like I said...I haven’t exactly had the best track record my whole life.

                     I used to be one of them. Y’know, believe in the whole terraforming thing, or whatever. A “neighbor,” I guess.
                    """
                    "{i}[Vesta] sniffles, her bottom lip quivering as another tear threatens to roll down her face.{/i}"
                    Passenger """
                    I was so...hungry for change that I just took the first road that presented itself.

                    I used to work as an engineer...and I thought I could try and make things better. I ended up joining some of my coworkers trying to revive some of the old machines, better air filters and stuff.

                    My boss found out...and fired everyone with a connection. Nearly a hundred people, I think.

                    So when I heard about a group that wanted to start terraforming again, I thought they might be good people...
                    """
                    "{i}[Vesta] trails off, wiping at her eyes.{/i}"
                    Pilot "But?"
                    Passenger "But...but I was too blinded by my hope that I missed what was really happening."
                    "{i}She makes direct eye contact with you as if pleading for you to understand.{/i}"
                    Passenger """
                    So many people there just used it...I don’t know. To justify their anger at the world, I guess.

                    One of the rallies...people got violent. They used the belief in a better future to justify hurting people who didn’t join.

                    And the next day I didn’t even hear anything about it. No news. No broadcasts.

                    I…
                    """
                    "{i}Putting her face in her hands, [vesta] lets out another sob, this one deep and guttural.{/i}"
                    Passenger """
                    I don’t even remember what happened, exactly.

                    I don’t think...I don’t think I want to.
                    """
                    "{i}[Vesta] slumps back in her chair, and you watch as silent tears begin to drip down her face.{/i}"
                    Passenger "I’m so sorry, but...I need some time alone."
                    "{i}You nod, stepping out of the small room and closing the door behind you, you take a seat on your bunk, drained and unsure of what to do next.{/i}"
                    jump choice7_end
            label combative_conversation_about_relationship_with_passenger:
                hide kn thru_door
                hide pass
                with Dissolve(1.0)
                show sit_2chair
                show pass cr sit a at atChair
                with Dissolve(2.0)
                "{i}You knock lightly on the door and step in the room.{/i}"
                Pilot "Hey, are you alright?"
                "{i}[Vesta] glares daggers at you, tears streaming down her red face.{/i}"
                Passenger "Get out."
                "{i}She says the words through clenched teeth.{/i}"
                Pilot "Sorry, I was just--"
                Passenger "I said get the fuck out! I don’t want to talk to {i}you!{/i}"
                Pilot "Ok! I’m leaving!"
                hide sit_2chair
                hide pass

                show kn thru_door
                show pass std i
                with fade
                "{i}You go to close the door, but [vesta] gets to her feet.{/i}"
                Passenger "Why did you even come in here? You’ve been nothing but rude to me since we started driving. What did I even do to you?"

                Passenger "I’m {i}sorry{/i} I didn’t think this through, I’m {i}sorry{/i} I inconvenienced you by {i}paying you{/i} to drive me somewhere!"

                Passenger "And then you come in here as if you’re just going to make it better? I’ve been trapped in this god-awful--"

                Passenger "I mean, what even is this thing? Some glorified taxi running on some kind of ancient jet fuel?"

                Passenger "But I’ve been trapped here, with you, regretting every choice I’ve made in my life and trying to keep from losing my mind and your choice, of all the choices you could make, is to try and make this an even {i}greater{/i} hell?"


                #TODO Update when I hear from Nathan
                "{i}She storms towards you, and you take a reflexive step back, removing your hand from the door handle.{/i}"

                show black
                hide pass
                hide kn thru_door
                "{i}She reaches the doorway and slams it shut, causing a bang that echoes around the ship for a few moments.{/i}"
                show cp front behind black
                hide black with fade
                "{i}You return to the cockpit, a little unsure of what to do with yourself.{/i}"
                jump choice7_end
            label choice7_end:

    label Act3:
        label vista_scenes:
            show black with fade
            scene rd front
            show cp back
            show pass qu sit n
            show black
            pause .5
            hide black with fade
            "{i}[Vesta] joins you in the cockpit the next morning, sitting sullenly with dark circles under her eyes.{/i}"
            "{i}She stares out the window absentmindedly, clearly uninterested in maintaining a conversation.{/i}"
            "{i}A few hours later, you break the heavy silence with some trepidation.{/i}"
            Pilot "I’m going to take a break up ahead. There’s an old vista that’s high enough I might be able to catch the storm radio to figure out what's going on with the weather."
            Pilot "It’s a pretty good view, if you want to get a firsthand look you should suit up."
            show pass qu sit s
            Passenger "Why? Do you think the storm will cause trouble after all?"
            "{i}You’re worried about the storm.{/i}"
            "{i}It’s bigger than any you’ve ever driven through before, and even with only a few hundred miles left of the journey, you don’t know if you’ll be able to beat it to Viacaellum like you thought you would.{/i}"
            label weatherLie:
                $ timer_jump = 'menu_neutral9'
            show screen countdown
            menu:
                "No, I don't.":
                    hide screen countdown
                    show pass qu sit n
                    Pilot "Nah, I’ve been in plenty of storms like it before. We really don’t have anything to worry about."
                    Passenger "If there’s nothing to worry about, why do you need to check the radio?"
                    Pilot "I’m just being overly cautious, I guess."
                    "{i}She doesn’t seem entirely convinced, but doesn’t question you further, though you notice her shoulders appear a little less tense.{/i}"
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
            label menu_neutral9:
                hide screen countdown
                Pilot "I don't know."
                jump weatherLie_end
            label weatherLie_end:
                hide pass
                hide cp
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
                    Radio "According to a direct wire we received only minutes ago, it appears that following a call for a recount by the former Governor of the region, riots have broken out--"
                    show pass std i
                    Passenger "What?!"
                    "{i}The reporter starts listing off neighborhoods where the riots have concentrated, and [vesta] listens with bated breath. At one name, a small gasp escapes her lips.{/i}"
                    "{i}[Passenger] seems quite shaken by the news, hastily throwing on her coat and her helmet over her head before rushing outside.{/i}"
                    "{i}You move your hand to change the channel, but she interrupts you.{/i}"
                    Passenger "No, don't!"
                    show pass std s at inDoorway behind table2t
                    Passenger "I’m sorry, I need to hear this."
                    Radio """
                    The riots began last night around eight o’clock, and raged for much of the week. Several fires have been reported throughout the city, most of which appear to have been set by rioters.

                    We cannot be certain, though the message seems to assert that some leaders in these riots have somehow obtained the records of individual citizens’ votes, and are now targeting those who chose not to vote for the former mayor of Domatellium.

                    The homes of several outspoken critics of the former mayor have already burned in incidents that our source referred to as “acts of terror.”

                    We will resume broadcasting as soon as we receive more news of the situation in Domatellium, so in the meantime, please enjoy the newest hit of pop wonder--
                    """
                    "{i}[Vesta] reaches down and turns the dial violently, switching the radio to static.{/i}"
                    "{i}Clearly quite shaken by the news, [vesta] hastily throws her coat on and smashes her helmet on over her head before rushing outside.{/i}"
                    hide pass with fade
            label radioChoice:
                $ timer_jump = 'menu_radioChoice'
                show screen countdown
            menu:
                "{i}Check on [Passenger].{/i}":
                    hide screen countdown
                    jump choice8
                "{i}Keep tuning for the weather channel.{/i}":
                    hide screen countdown
                    jump full_weather_Report
            label radioChoice_neutral:
                hide screen countdown
                jump full_weather_Report
            label full_weather_Report:
                $ friendship -= 2
                play sound 'audio/sfx_weather_jingle.mp3'
                "{i}You continue to tune the radio, attempting to catch Viacaellum’s weather channel. It takes a few times, but you eventually get it.{/i}"
                Radio "--we haven’t seen a storm like this in years. In fact, this may be the largest storm we’ve been able to monitor in almost a century."
                "{i}The tone of the radio is entirely too jovial for the news it delivers.{/i}"
                Radio "Truly a once in a lifetime experience, but not one I’d recommend checkin’ out if you don’t have the proper equipment."
                Radio "The governor recently put out a citywide mandate to stay inside, halting all outbound travel until this truly historic storm has passed through."
                Radio "And for those of you too unlucky to be outside city walls when this things hits…"
                Radio "Well, let’s just say if you ain’t a storm chaser, I {i}do not{/i} envy you."
                Radio "{i}Anyway,{/i} this message should be on repeat until we receive more news, so enjoy my illustrious voice in the meantime."
                "{i}The radio begins to repeat, looping through the same obnoxious message a few times before you shut it off.{/i}"
                "{i}Not long after you do, you hear the sound of the hatch in the sitting room being wrenched open, and a shivering passenger storms inside.{/i}"
                jump radioChoice_end
            label radioChoice_end:
                #TODO Fix transition
                "{i}Eventually, [vesta] comes back onto the ship. She tries to casually hide her face, but you can see her eyes are red and puffy.{/i}"
                Pilot "The storm is getting really bad--"
                "{i}[Vesta] cuts you off.{/i}"
                Passenger "Whatever, let’s keep going. I can’t handle this wasteland much longer."
                jump choice8_end
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
                $ timer_jump = 'menu_neutral8'
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
                    elif friendship >1:
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
                        Passenger "Let’s get going then, my future awaits!"
                        "{i}She turns around, clearly done with the austere view.{/i}"
                        jump choice8_end
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
                        jump choice8_end
                "{i}Stay silent{/i}":
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
                    jump choice8_end
            label apologize:
                menu:
                    "I'm so sorry.":
                        Pilot "I'm so sorry."
                        "{i}You search for more words, but can’t find any.{/i}"
                        "{i}[Vesta] fixes her gaze on the horizon.{/i}"
                        Passenger "I...don’t be. It’s all over now. I can’t dwell on the past."
                        "{i}She squares her shoulders, as if forcing herself to feel sure.{/i}"
                        Passenger "The choices they made are theirs. I’ve just got to make do with mine."
                        Passenger "I’m not going back. Even if I wanted to, everything I know is gone. That part of my life…"
                        Passenger "It’s gone now. Literally."
                        "{i}[Vesta] turns around, clearly done with the austere view.{/i}"
                        Passenger "Can we just get going? I can’t handle this wasteland much longer."
                        jump choice8_end
                    "You can't blame yourself.":
                        $ friendship += 1
                        Pilot "You did the right thing. You tried to warn them and they didn't listen."
                        Pilot "What they chose to do...that’s up to them. Unless you told them to ignore the…"
                        "{i}You search for the right word for a second, but fail to find it.{/i}"
                        Pilot "{i}Bad{/i} things that happened… then that was up to them, ultimately. If they didn’t change their minds, they didn’t want to."
                        Pilot "Staying and risking being caught up in the riots wouldn’t have helped them, or anyone."
                        "{i}You fall silent, letting the stillness of the moment stretch out.{/i}"
                        Passenger "Thank you. I...needed to hear that, I guess."
                        Passenger "I’m not going back. Even if I wanted to, everything I know is gone. That part of my life…"
                        "{i}She squares her shoulders, her voice firm as she comes to this resolution.{/i}"
                        Passenger "It’s gone now. Literally."
                        "{i}[Vesta] turns around, clearly done with the austere view.{/i}"
                        Passenger "Can we just get going? I can’t handle this wasteland much longer."
                        jump choice8_end
            label menu_neutral8:
                hide screen countdown
                jump choice8_end
            label choice8_end:

        label crash_scenes:
            play Wind 'audio/amb-sfx_strong-wind.mp3' fadein 1.0
            scene rd front
            show kn thru_door
            show pass qu sit i at thru_door
            with fade
            Passenger "Can we just get going? I can’t handle this wasteland much longer."
            label checkRadio:
                $ timer_jump = 'menu_checkRadio'
            show screen countdown
            menu:
                "{i}Check radio first.{/i}":
                    hide screen countdown
                    $ friendship -= 1
                    jump checking_Radio
                "{i}Agree and head to cockpit.{/i}":
                    hide screen countdown
                    $friendship+=1
                    jump checkRadio_end
            label checkRadio_neutral:
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
                "{i}Even as the room fills with the whine of the engines, you can still hear her stomps and sniffles from down below.{/i}"
                jump checkRadio_end
            label checkRadio_neu:
                Passenger "Ugh, I don't know why I even bother."
                Passenger "Just be silent and drive."
                Passenger "You're good at that."
                "{i}You nod, and head to the cockpit.{/i}"
                jump checkRadio_end
            label checkRadio_pos:
                Passenger "Could you not, please? I’ve had enough of that damn thing for the rest of my life."
                "{i}You open your mouth to explain that it might offer some information on the duration of the storm and how we might avoid it, but she seems to read my thoughts.{/i}"
                Passenger "Really!? What new information are you going to learn from that thing?"
                Passenger "That storm is headed right towards us, and stretches for as far as I can see. I can’t wait here any longer. Just get me to Viacaellum. Please."
                "{i}You nod, and begin to head to the cockpit.{/i}"
                Pilot "Just brace yourself though. This is going to be a...bumpy ride."
                jump checkRadio_end
            label checkRadio_end:
                play Hail 'audio/sfx_hail.mp3' fadein 1.0
                scene rd front
                hide pass
                hide kn
                with fade
                show cp front with fade
                "{i}You manage to cross nearly half the remaining distance to Viacaellum before the storm hits.{/i}"
                play sound 'audio/sfx_crash.mp3'
                pause .5
                "{i}But when it hits, it hits hard.{/i}"
                scene black with fade
                stop background_music
                pause 1.0
                play sound 'audio/sfx_ear_ringing.mp3'
                pause .5
                #TODO Blurry image of kitchen
                scene rd front
                show black
                show kn table2 behind rd
                show cp crashed behind black
                hide black with Dissolve(3.0)
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
                "{i}Looking around, you realize you are in the kitchen, and must have fallen out of the cockpit and down through the hatch.{/i}"
                if friendship >3:
                    jump pass_helps_outside
                elif friendship<0:
                    jump pass_refuses_to_help
                else:
                    jump pass_helps_inside
            label pass_helps_outside:
                "{i}You call out for [vesta] again, and this time hear a crash in the next room.{/i}"
                "{i}[Vesta] yelps, and you feel yourself twinge with sympathetic pain. Scrambling forward you find her sprawled against the table, surrounded by pieces of broken glass from the mirror that toppled next to her.{/i}"
                "{i}You reach out, managing to pull her into the kitchen, and feel water begin to fill your boots.{/i}"
                "{i}[Vesta] looks around, finally seeming to comprehend that things are not as they should be.{/i}"
                Passenger "What happened?!"
                "{i}She yells this, her voice slightly slurred.{/i}"
                Pilot "We crashed! The ship got hit by one of the largest gusts I’ve ever experienced!"
                "{i}Your voice is nearly drowned out by a peal of thunder, and you find yourself gasping for breath.{/i}"
                Pilot "We need to find our helmets! I think there’s a hole somewhere in the ship, and the air is going to become unbreathable within the next few minutes!"
                "{i}[Vesta] nods, trudging unsteadily through the rising water to the desk in the next room.{/i}"
                "{i}You begin to fumble around in the darkness, searching desperately for your helmet.{/i}"
            label pass_helps_inside:
                "TBD PASSENGER AGREES TO HELP FROM THE INSIDE."
                "TBD YOU BOTH FIX THE SHIP'S LEAK."
            label pass_refuses_to_help:
                "TBD PASSENGER REFUSES TO HELP."
                "TBD YOU FIX THE SHIP'S LEAK."
            stop Wind fadeout 5.0
            stop Hail fadeout 5.0
            if nationalist_points > 1:
                play background_music "audio/mus_ambient-bad.ogg" fadein 5.0
            else:
                play background_music "audio/mus_ambient.ogg" fadein 5.0
            "TBD AFTER THE STORM PASSES YOU'RE ABLE TO RADIO A TRANSPORT TO PICK YOU UP."

        label ending:
            "{i}You go out to where [vesta] is.{/i}"
            scene rd front
            if friendship > 1:
                show pass std t
                with Dissolve(3.0)
                Pilot "The transport will be here soon."

                Pilot "So, what will you do when you get to Viacaellum?"
                if friendship > 7:
                    Passenger "Well, I was thinking that we could find out together."
                    label menu_ending1:
                        menu:
                            "{i}Go with [vesta].{/i}":
                                Pilot "You know what? I'd love to."
                                "{i}[Vesta] smiles.{/i}"
                                jump credits
                            "{i}Say no.{/i}":
                                if nationalist_points >0:
                                    Pilot "Sorry, but I can't."
                                    Pilot "Look, I don't agree with you, but I hope you find what you're looking for."
                                    "{i}[Vesta] nods, but it looks like something inside her just broke.{/i}"
                                    jump credits
                                else:
                                    Pilot "Sorry, I don't think I can."
                                    Pilot "I'm gonna head back to Domatellium. I think some people there could use a ride."
                                    "{i}[Vesta] smiles and nods, but it looks like something inside her just broke.{/i}"
                                    jump credits
                else:
                    Passenger "I don't know."
                    Passenger "What about you?"
                    Pilot "Probably head back to Domatellium. I think some people there could use a ride."
                    "{i}[Vesta] smiles.{/i}"
                    "{i}The transport comes and takes both of you and the ship to Viacaellum.{/i}"
                    jump credits
            else:
                show pass std i
                with Dissolve(3.0)
                "{i}You both stand outside silently, waiting for the transport to arrive.{/i}"
                "{i}The transport comes and takes both of you and the ship to Viacaellum.{/i}"
                "{i}You go back to your job and never see [vesta] again.{/i}"
                if nameKnown<1:
                    "{i}You never even learned her name.{/i}"
                jump credits

    label credits:
        scene black with fade
        pause 0.5
        show text "Thank you for playing a Spaced-Out Studios Original" at truecenter with fade
        pause 2
        hide text with Dissolve(2.0)
        show text "Programming by Tate Donnelly{p}{p}Art by Nathan Booth{p}{p}Original Music and Proofreading by Benny Klaiman{p}{p}Writing by Tate Donnelly and Nathan Booth" at truecenter with fade
        pause 10
        hide text with Dissolve(2.0)
        show text "Jet Take Off and Fly By Sound Effect By SoundEffectsFactry{p}{p}Strong Howling Wind Sound 2 Hours, Swaying Spruce Trees in The Wind By Relaxing Sounds of Nature{p}{p}Heavy Rain Sounds at Night - Sleep, Study, Relax | Ambient Noise Rainstorm, @Ultizzz day#69 by Ultimate Ambient Noise Soundzzz" at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "10 hours of hard rain on a metal roof (Rain Sleep Sounds) Rain Sounds for Sleeping. Rainfall.lluvia by SleepDroid Studios Sleep Sounds{p}{p}Radio Static - Sound Effect By Audio Library - Free Sound Effects"  at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "Ear Ringing Sound Effect - Free Download HD By SFX and GFX{p}{p}Heavy Hail Sound Effects By Free To Use Sounds{p}{p}8 hours of train station sounds | train station sound effect and railway station sound / 8 Hours Of{p}{p}Plane Crash Sound Effect by Sound Effect Database"  at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "Mr.Lucky By Karl Jenkins{p}{p}Tibeauthetraveler By Ember (ft.eleven}"  at truecenter with fade
        pause 3
        hide text with Dissolve(2.0)
        show text "Down to Business (Title/Situational){p}{p}A Bright Future (Good Ending){p}{p}A \"Blight\" Future (Bad Ending){p}{p}by Benny Klaiman"  at truecenter with fade
        pause 3
        hide text with Dissolve(5.0)
        return
