# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label start:

    label point_system:
        $ nationalist_points = 0
        $ anti_points = 0
        $ attendant = 0
        $ friendship = 0
        $ nameKnown = 0
    define Passenger=Character("Passenger")
    init python:
        renpy.music.set_volume(0, 0, channel="background_music")
        renpy.music.register_channel("background_music", "music", True)
    define Nationalist=Character("Radio")
    define Radio=Character("Radio")
    scene main_menu
    python:
        protagName = renpy.input("What is your name?", length=32)
        protagName = protagName.strip()
    define pov= Character("[protagName]")

    """This game relies heavily on every choice you make and don't make.

    This game will ask you to make certain decisions within a short time limit. In an effort to be more accommodating, you can choose how long you have to make a decision.

    Please choose a duration now."""

    menu:
        "5 seconds":
            $ timeLimit=5
        "15 seconds":
            $ timeLimit=15
        "30 seconds":
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

    scene doma_station
    show main_menu
    show cp front behind main_menu
    stop music fadeout 3.0
    hide main_menu with fade
    init:
        $ timer_range = 0
        $ timer_jump = 0
    init python:
        renpy.music.register_channel("Radio", "sfx", True)
    play Radio 'audio/mus_Radio-static.mp3'
    Radio """
    My friends, compatriots, and neighbors, do you feel it in the air? The buzz of excitement, the thrill of chance? The lust, no, love for justice that swirls through the streets?

    I do.

    That, my friends, is the feeling of a just democracy about to change course! The feeling of a movement about to make history!

    For those listeners who might not have picked up upon my meaning, I refer of course to the most pivotal election of the era.

    A chance for those who wish to see real change, real justice, real solutions!

    For far too long we’ve allowed ourselves to become entrenched in our glorious past, too afraid of marring the legacy of our great city.

    We’ve polished the portraits of long-dead heroes while the walls we hide behind became too tarnished to recognize!

    But we have had enough! Yes, my neighbors, now is the time for change!
    """

    label choice1:
        $ time = timeLimit
        $ timer_range = timeLimit
        $ timer_jump = 'menu_neutral'
    show screen countdown
    menu:
        "{i}Keep listening to the radio.{\i}":
            hide screen countdown
            Radio """
            I have promised you for many months that one day, we would rise from the pitted remains of this legendary city to claim the wastelands of Duoterra!

            To finish the work that was begun hundreds of years ago to turn these landscapes from harsh to hospitable!

            And now, after all of these promises, our movement is large enough to take the reigns of this city from the senile politicians who would wish to sink slowly into obscurity without protest!

            I call on you, my friends, my fellow citizens of Domatellium, to take action, for tomorrow is the day we claim this city!

            The day we may finally reignite the fire forgotten for too many years!

            The day we refuse to let our--
            """
            stop Radio
            play background_music "audio/mus_ambient.mp3" fadein 1.0
            jump choice1_end
        "{i}Turn off the radio.{\i}":
            stop Radio
            hide screen countdown
            play background_music "audio/mus_ambient.mp3" fadein 1.0
            "{i}You turn the Radio off.{\i}"
            jump choice1_end

    label menu_neutral:#If the Player doesn't make a choice
        hide screen countdown
        stop Radio
        play background_music "audio/mus_ambient.mp3" fadein 1.0
        "You know, in times like these, if you’re always this indecisive you’ll probably end up regretting it later."
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
            pov "Really? Wouldn't a transport be faster?"
            Passenger "Please, can you just take me?"
            pov "Fine. Do you have any bags?"
            jump choice2_end
        "Yeah, of course.":
            hide screen countdown
            pov "Yeah, of course. Do you have any bags?."
            show pass coat r
            jump choice2_end
    label menu_neutral2:#If the Player doesn't make a choice
        hide screen countdown
        pov "Sure."
        jump choice2_end
    label choice2_end:
        show pass coat i
        "{i}The passenger looks down and shakes her head.{\i}"
        show pass coat
        pov "Alright, hop in."

    hide pass
    hide cp
    with dissolve
    scene rd front
    show doma_station
    show cp back behind doma_station
    show pass qu sit s behind doma_station
    pause 1
    hide doma_station with Dissolve(1.0)
    pause .5

    define Passenger=Character("Vesta")
    show pass qu sit s
    pov "I'm [protagname], by the way."
    show pass qu sit t
    Passenger "Oh, nice to meet you, [protagname]. I'm Vesta."
    label choice3:
        $ timer_jump = 'menu_neutral3'
    show screen countdown
    menu:
        "So why are you heading to Viacaellum?":
            hide screen countdown
            $ friendship += 1
            jump friendly_small_talk_CS3
        "{i}Make small talk (hostile).{\i}":
            hide screen countdown
            $friendship -= 1
            jump hostile_small_talk_CS3
    label menu_neutral3:
        hide screen countdown
        show pass qu sit n
        "{i}The awkward silence is, unsurprisingly, awkward.{\i}"
        jump choice3_end
    label friendly_small_talk_CS3:
        pov "So why are you heading to Viacaellum? Are you going on vacation?"
        show pass qu sit t
        Passenger "Sort of, I really just had to get out of town."
        show pass qu sit s
        "{i}TBD You and the passenger have a friendly conversation about traveling.{\i}"
        jump choice3_end
    label hostile_small_talk_CS3:
        show pass qu sit i
        "{i}Hostile small talk ensues.{\i}"
        jump choice3_end
    label choice3_end:
        show pass qu sit n
        stop background_music fadeout 1.0
        play Radio 'audio/mus_Radio-static.mp3'
        play background_music "audio/main-menu-theme.mp3" fadein 1.0
        "{i}You turn on the radio to listen to some music{\i}."
        stop Radio fadeout 1.0
        stop background_music fadeout 1.0
        play background_music "audio/mus_ambient.mp3" fadein 3.0
        show pass qu sit s
        "{i}The radio shuts off abruptly, startling the passenger.{\i}"
        Passenger "Why did the radio just shut off?"
    label choice4:
        $ timer_jump = 'menu_neutral4'
    show screen countdown
    menu:
        "{i}Explain radio disturbance.{\i}":
            hide screen countdown
            $ friendship += 1;
            jump friendly_4
        "You didn't know? Really?":
            hide screen countdown
            $ friendship -= 1;
            jump hostile_4
    label menu_neutral4:
        hide screen countdown
        show pass qu sit n
        Passenger "Don't worry, it does that sometimes."
        jump choice4_end
    label friendly_4:
        show pass qu sit s
        pov "Oh yeah, once you get close enough to the edge of the cities you lose reception."
        pov "There are a few spots outside the domes where we'll be able to pick up reception, but we won't have it for most of the trip."
        show pass qu sit t
        Passenger "Huh, I never knew that."
        pov "Have you ever left Domatellium before?"
        show pass qu sit n
        Passenger "No, I never really saw any reason to leave."
        pov "That explains it then. Most people who never leave the city wouldn't know about it."
    jump choice4_end
    label hostile_4:
        show pass qu sit s
        pov "You didn't know? Really?"
        pov "Is this your first time out of the city or something?"
        "{i}[Passenger] nods.{\i}"
        show pass qu sit i
        pov "Huh. That's weird, I can't imagine never leaving the cities."
        jump choice4_end
    label choice4_end:
        play sound 'audio/sfx_space-engine.mp3'
        scene leaving_doma_still with Dissolve(2.0)

        stop background_music fadeout 5.0

        "{i}Ship leaves doma{/i}"
        stop sound
        play background_music "audio/mus_ambient.mp3"


    ###Act 2
    scene ext_rfstation
    show cp back
    show pass qu sit n
    play Radio 'audio/mus_Radio-static.mp3'
    Radio "Attention all pilots, forecasters are warning everyone to take shelter in a dome or station for the time being."
    show pass qu sit s
    Radio "Storm Mutatio is predicted to hit within the week and will be one of the worst storms Duoterra will encounter this year."
    stop Radio
    Passenger "Do you think the storm will hit us before we reach Viacaellium?"
    label Storm_Warning:
        $ timer_jump = 'menu_Storm_Warning'
    show screen countdown
    menu:
        "Do you want to turn back?":
            hide screen countdown
            show pass qu sit t
            Passenger "{i}She shakes her head.{\i} If you think we'll be fine let's keep moving."
            show pass qu sit t
            pov "Sounds good, but we’re gonna need to refuel if we’re gonna make it to Viacalleum."
            jump Storm_Warning_end
        "No, we'll be fine.":
            hide screen countdown
            show pass qu sit s
            pov "Nah, the forecastors always make the storms a bigger deal than they are."
            Passenger "Ok, if you're sure."
            pov "We’ll be fine, but we’ll need to refuel if we’re gonna make it to Viacalleum."
            jump Storm_Warning_end
    label menu_neutral_Storm_Warning:
        hide screen countdown
        show pass qu sit s
        pov "Too late to turn back now."
        pov "Also, we’ll need to refuel if we’re gonna make it to Viacalleum."
        jump choice7_end
    label Storm_Warning_end:
    scene ext_rfstation
    play sound 'audio/sfx_space-engine.mp3'
    "{i}Ship lands{\i}"
    scene rf_station_still
    show rs clerk n
    play sound 'audio/sfx_jingle.mp3'
    pause 0.5
    play Radio 'audio/mus_Radio-static.mp3'
    Radio "Gatherings in support of Domatellium's mayor have popped up all across Duoterra!"
    Radio "Many gatherers are excited about Domatellium's mayor running for Governor."
    stop Radio
    define clerk = Character("Attendant")
    label choice5:
        $ timer_jump = 'menu_neutral5'
    show screen countdown
    menu:
        "{i}Talk to refuel station attendant.{\i}":
            hide screen countdown
            "TBD political discussion"
            $ attendant += 1
            jump conversation_with_attendant
        "{i}Ignore the refuel station attendant.{\i}":
            hide screen countdown
            "{i}You ignore refuel station attendant.{\i}"
            "{i}You get fuel.{\i}"
            jump Hear_About_Gatherings
    label menu_neutral5:
        hide screen countdown
        "{i}You ignore refuel station attendant.{\i}"
        "{i}You get fuel.{\i}"
        jump Hear_About_Gatherings
    label conversation_with_attendant:
        clerk "Ugh, this crap."
        "{i}Attendant switches the radio off.{\i}"
        "TBD CONVERSATION BETWEEN REFUEL ATTENDANT AND PASSENGER ABOUT GATHERINGS."
        clerk "We’re just reverting back to how it was when this whole thing fell apart."
        jump Fell_Apart
    label Hear_About_Gatherings:
        Radio "TBD Radio goes on about gatherings"
        jump choice5_end
    label Fell_Apart:
        $ timer_jump = 'menu_neutral5'
        show screen countdown
        menu:
            "What do you mean fell apart?":
                hide screen countdown
                jump attendant_monologue
            "Maybe it's gonna head in a good direction":
                hide screen countdown
                $ nationalist_points += 1
                jump hopeful_on_nationalism
        label Fell_Apart_Neutral:
            "{i}You stay silent{\i}"
            jump choice5_end
        label attendant_monologue:
            "TBD Attendant explains history"
            jump choice5_end
        label hopeful_on_nationalism:
            clerk "You don’t know what you’re talking about."
            "TBD ARGUMENT ABOUT CURRENT POLITICS RELATING TO PAST POLITICS"
            jump choice5_end
    label choice5_end:
        "TBD FINISH FOOD AND WALK BACK DESCRIPTION"
        hide clerk

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
        "Why do you wanna leave so bad?":
            hide screen countdown
            if friendship >= 1:
                jump passenger_monologue
            if friendship == 0:
                jump dont_want_to_talk_about_it
            if friendship < 0:
                jump dont_need_to_tell_you
    label menu_neutral6:
        hide screen countdown
        "{i}You both walk back in silence{\i}"
        jump choice6_end
    label conversation_about_attendant:
        Passenger "I honestly don’t know anymore. Do you think all that stuff she said was really true?"
        if nationalist_points > anti_points:
            jump nationalist_history_conversation
        if nationalist_points <= anti_points:
            jump anti_history_conversation
    label nationalist_history_conversation:
        pov "No, I think it’ll be different."
        "TBD CONVERSATION ABOUT WHAT REFUELING ATTENDANT SAID"
        jump choice6_end
    label anti_history_conversation:
        pov "Yeah, I don’t see a point in repeating history that's been proven not to work."
        "TBD CONVERSATION ABOUT WHAT REFUELING ATTENDANT SAID"
        jump choice6_end
    label passenger_monologue:
        "TBD Passenger monologues about past"
        jump choice6_end
    label dont_want_to_talk_about_it:
        Passenger "I don't want to talk about it!"
        jump choice6_end
    label dont_need_to_tell_you:
        Passenger "I don't need to tell you!"
        jump choice6_end
    label conversation_about_gatherings:
        "TBD Conversation about gatherings"
        jump choice6_end
    label choice6_end:
        "TBD DESCRIPTION INTRODUCES NEW DAY"
        "TBD INTERNAL DIALOGUE ON POINTS (INFLUENCED BY POLITICAL POINTS), THEN DESCRIBES FINDING PASSENGER UPSET"


    label choice7:
        $ timer_jump = 'menu_neutral7'
    show screen countdown
    menu:
        "Are you ok?":
            hide screen countdown
            if friendship > 0:
                jump meaningful_conversation_about_past
            if friendship <= 0:
                jump combative_conversation_about_relationship_with_passenger
        "{i}Ignore Passenger{\i}":
            hide screen countdown
            "{i}You ignore the passenger.{\i}"
            jump choice7_end
    label menu_neutral7:
        hide screen countdown
        "{i}You ignore the passenger.{\i}"
        jump choice7_end
    label meaningful_conversation_about_past:
        "TBD PASSENGER EXPLAINS WHAT HAPPENED AND PART OF WHY THEY’RE LEAVING"
        jump choice7_end
    label combative_conversation_about_relationship_with_passenger:
        "TBD PASSENGER: DON’T TALK TO ME"
        jump choice7_end
    label choice7_end:
    #Act 3
    scene rd front
    show cp back
    show pass gr sit n
    pov "I’m going to take a break up ahead. There’s an old vista that’s high enough to catch the storm radio to figure out what's going on with the weather."
    pov "It’s a pretty good view. But if you want to get a firsthand look, you should suit up."
    show pass gr sit s
    Passenger "Why? Do you think the storm will cause trouble after all?"
    "{i}You are worried about the storm.{\i}"
    "{i}It’s bigger than any you’ve ever driven through before, and even with only a few hundred miles left of our journey, you don’t know if you’ll be able to beat it to Viacelleum like you thought you would."
    label weatherLie:
        $ timer_jump = 'menu_neutral9'
    show screen countdown
    menu:
        "No, I don't.":
            hide screen countdown
            show pass gr sit i
            "TBD LIE ABOUT WEATHER, PASSENGER SEES THROUGH IT"
            $ friendship -=1
            jump weatherLie_end
        "Yes, probably":
            hide screen countdown
            $ friendship +=1
            show pass gr sit s
            "TBD TELL PASSENGER TRUTH, THIS SCARES HER"
            jump weatherLie_end
    label menu_neutral9:
        hide screen countdown
        pov "It could be."
        show pass gr sit s
        jump weatherLie_end
    label weatherLie_end:
    scene bed_desk
    menu:
        "{i}Fiddle with radio{\i}":
            "{i}You accidentally tune the radio to the news station.{\i}"
            Radio "--thank you, Doctor. Now we’ve got some breaking news here, folks, and I’m afraid it could be somewhat distressing to those following the ongoing elections over in Domatellium."
            "{i}PASSENGER APPEARS IN DOORWAY{\i}"
            Passenger "Oh, you got the radio to work."
            Radio "According to a direct wire we received only minutes ago, it appears that following a call for a recount by the former Governor of the region, riots have broken out--"
            Passenger "What?!"
            "TBD PASSENGER HEARS ABOUT RIOTS IN HER OLD NEIGHBOURHOOD IN DOMATELLIUM."
            "{i}[Passenger] seems quite shaken by the news, hastily throwing her coat on and throwing her helmet on over her head before rushing outside.{\i}"
    label radioChoice:
        $ timer_jump = 'menu_radioChoice'
    show screen countdown
    menu:
        "Check on [Passenger].":
            hide screen countdown
            jump choice8
        "{i}Keep tuning for the weather channel.{\i}":
            hide screen countdown
            jump full_weather_Report
    label radioChoice_neutral:
        hide screen countdown
        "{i}You keep tuning for the weather channel.{\i}"
        jump full_weather_Report
    label full_weather_Report:
        "TBD RADIO EXPLAINS STORM IS REACHING RECORD LEVELS AND TRAVEL IS NOT RECOMMENDED"
        $ friendship -=2
        jump radioChoice_end
    label radioChoice_end:
        jump choice8_end

    label choice8:
        $ timer_jump = 'menu_neutral8'
        scene close_vista
        "TBD PILOT CHECKS IN ON PASSENGER, FINDS OUT ABOUT HER FAMILY BACK IN DOMATELLIUM"
    show screen countdown
    menu:
        "TBD Choice 1":
            hide screen countdown
            jump choice8_end
        "TBD Choice 2":
            hide screen countdown
            jump choice8_end
    label menu_neutral8:
        hide screen countdown
        jump choice8_end
    label choice8_end:

    scene kn thru_door
    Passenger "Can we just get going? I can’t handle this wasteland much longer."

    label checkRadio:
        $ timer_jump = 'menu_checkRadio'
    show screen countdown
    menu:
        "{i}Check radio first.{\i}":
            hide screen countdown
            jump checking_Radio
        "{i}Agree and head to cockpit{\i}":
            hide screen countdown
            $friendship-=1
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
        "{i}She gets to her feet angrily, standing with a childish look of fury on her face.{\i}"
        Passenger "Just DRIVE, damnit!"
        "{i}You agree begrudgingly, entering the cockpit and starting the craft.{\i}"
        "{i}Even as the room fills with the whine of the engines, you can still hear her stomps and sniffles from down below.{\i}"
        jump checkRadio_end
    label checkRadio_neu:
        Passenger "Ugh, I don't know why I even bother."
        Passenger "Just be silent and drive."
        Passenger "You're good at that."
        "{i}You nod, and head to the cockpit.{\i}"
        jump checkRadio_end
    label checkRadio_pos:
        Passenger "Could you not, please? I’ve had enough of that damn thing for the rest of my life."
        "{i}You open your mouth to explain that it might offer some information on the duration of the storm and how we might avoid it, but she seems to read my thoughts.{\i}"
        Passenger "Really!? What new information are you going to learn from that thing?"
        Passenger "That storm is headed right towards us, and stretches for as far as I can see. I can’t wait here any longer. Just get me to Viacalleum. Please."
        "{i}You nod, and begin to head to the cockpit{\i}"
        pov "Just brace yourself though. This is going to be a...bumpy ride."
        jump checkRadio_end
    label checkRadio_end:
        "{i}You manage to cross nearly half the remaining distance to Viacelleum before the storm hits.{\i}"
        "{i}But when it hits, it hits hard.{\i}"
        "{i}Hailstones the size of your hand slam against the craft, scratching paint and causing the entire chassis to shake, pushing the craft further and further to one side of the road.{\i}"
        "{i}Then, without warning, a rock nearly the size of your head comes flying out of nowhere. It crashes into the right side thruster, gouging the windshield with paneling and bits of metal dispersed by the collision.{\i}"
        "{i}The crash is quick.{\i}"
        "{i}As soon as it loses a thruster, the craft dives for the ground, burying its nose as it slices a deep trench into the mud.{\i}"
        "{i}The force of the impact knocks you out immediately, bucking you violently from your seat.{\i}"

        #"{i}{\i}"
    scene rd_storm
    show cp crashed
    "TBD CONVERSATION BETWEEN PASSENGER AND PILOT AS THEY TRY TO FIGURE OUT WHAT TO DO"
    if friendship>3:
        jump ext_pass_helps
    if friendship<0:
        jump pass_refuses_to_help
    else:
        jump int_pass_helps
    label ext_pass_helps:
        "TBD Passenger helps repair ship outside"
        jump ship_fixed
    label pass_refuses_to_help:
        "TBD Passenger refuses to help"
        jump ship_fixed
    label int_pass_helps:
        "Passenger helps repair ship inside"
        jump ship_fixed
    label ship_fixed:
        "Ending times"

    if nationalist_points < -2:
        "You return to Domatellium to support the new government."
    if anti_points >2:
        if friendship > 3:
            "You stay in Viacelleum with Passenger"
        else:
            "You return to Domatellium to help others leave."
    else:
        "You return to Domatellium to continue your job."
    # label choice11:
    #     $ timer_jump = 'menu_neutral11'
    # show screen countdown
    # menu:
    #     "":
    #         hide screen countdown
    #         jump choice11_end
    #     "":
    #         hide screen countdown
    #         jump choice11_end
    # label menu_neutral11:
    #     hide screen countdown
    #     jump choice11_end
    # label choice11_end:
    #     ""
    # label choice11:
    #     $ timer_jump = 'menu_neutral11'
    # show screen countdown
    # menu:
    #     "":
    #         hide screen countdown
    #         jump choice11_end
    #     "":
    #         hide screen countdown
    #         jump choice11_end
    # label menu_neutral11:
    #     hide screen countdown
    #     jump choice11_end
    # label choice11_end:
    #     ""
    # label choice11:
    #     $ timer_jump = 'menu_neutral11'
    # show screen countdown
    # menu:
    #     "":
    #         hide screen countdown
    #         jump choice11_end
    #     "":
    #         hide screen countdown
    #         jump choice11_end
    # label menu_neutral11:
    #     hide screen countdown
    #     jump choice11_end
    # label choice11_end:
    #     ""

    # label choice12:
    #     $ timer_jump = 'menu_neutral12'
    # show screen countdown
    # menu:
    #     "":
    #         hide screen countdown
    #         jump choice12_end
    #     "":
    #         hide screen countdown
    #         jump choice12_end
    # label menu_neutral12:
    #     hide screen countdown
    #     jump choice12_end
    # label choice12_end:
    #     ""


    # Credit Sequence
    scene credits with fade
    pause 0.5
    show text "Thank you for playing a Spaced-Out Studios Original" at truecenter with fade
    pause 2
    hide text with Dissolve(2.0)
    show text "Programming by Tate Donnelly{p}{p}Art by Nathan Booth{p}{p}Original Music/Proofreading/Tech Support by Benny Klaiman{p}{p}Writing by Tate Donnelly and Nathan Booth" at truecenter with fade
    pause 10
    hide text with Dissolve(2.0)
    show text "Jet Take Off and Fly By Sound Effect By SoundEffectsFactry{p}{p}Strong Howling Wind Sound 2 Hours, Swaying Spruce Trees in The Wind By Relaxing Sounds of Nature{p}{p}Heavy Rain Sounds at Night - Sleep, Study, Relax | Ambient Noise Rainstorm, @Ultizzz day#69 By Ultimate Ambient Noise Soundzzz" at truecenter with fade
    pause 3
    hide text with Dissolve(2.0)
    show text "10 hours of hard rain on a metal roof (Rain Sleep Sounds) Rain Sounds for Sleeping. Rainfall.lluvia By SleepDroid Studios Sleep Sounds{p}{p}Radio Static - Sound Effect By Audio Library - Free Sound Effects"  at truecenter with fade
    pause 3
    hide text with Dissolve(2.0)
    show text "Mr.Lucky By Karl Jenkins{p}{p}Tibeauthetraveler By Ember (ft.eleven}"  at truecenter with fade
    pause 3
    hide text with Dissolve(5.0)
    return
