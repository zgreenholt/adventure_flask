from route_helper import simple_route
import random

GAME_HEADER = """
<h1>Welcome to Quest of the Gods</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return GAME_HEADER+"""You woke up confused on Mount Olympus.<br>
    You have been notified of a war between the gods that will <br>
    cause destruction to the human world. If you can solve all the <br>
    gods' conflicts, you can save humanity. Will you save the humans <br>
    or find power for yourself on Mount Olympus?<br>
    <a href="goto/Earth"> Escape back to your home. </a><br>
    <a href="goto/Throne"> Approach Zeus and ask what's wrong. </a><br>
    <a href="goto/Vault Gate"> Sneak into the vault of Olympus. </a>"""



ENCOUNTER_MONSTER = """
<!-- Curly braces let us inject values into the string -->
You are in {}. You found a monster!<br>

<!-- Image taken from site that generates random Corgi pictures-->
<img src="http://placecorgi.com/260/180" /><br>
<img src="/static/Mike_Wazowski.jpg" /><br>   
What is its name?

<!-- Form allows you to have more text entry -->    
<form action="/save/name/">
    <input type="text" name="player"><br>
    <input type="submit" value="Submit"><br>
</form>
"""


@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    """
    Update the player location and encounter a monster, prompting the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player

    world['location'] = where
    return GAME_HEADER+ENCOUNTER_MONSTER.format(where)
    """
    if where == "Earth":
        return GAME_HEADER+"""
        You returned to your home, but then you remembered <br>
        that the doom of humanity was imminent, and Earth is destroyed. <br>
        <h1> GAME OVER <h1>
        
        """
    if where == "Throne":
        return GAME_HEADER+"""
        Zeus tells you about three childish conflicts that the <br>
        gods and goddesses are going through that each much be <br>
        stopped because any god's rage could destroy the planet. <br> <br>
        
        Athena and Ares are arguing over who would win in a battle. <br>
        Aphrodite and Hera each believe they are the more beautiful goddess. <br>
        Persephone is trying to take control of the underworld from Hades. <br>
        
        
        <a href="goto/Battlefield"> Stop Athena and Ares first. </a><br>
        <a href="goto/Pageant"> Stop Aphrodite and Hera first. </a><br>
        <a href="goto/Underworld"> Stop Persephone and Hades first. </a>
        """
    if where == "Vault Gate":
        return GAME_HEADER+"""
        """
    if where == "war":
        x = random.randrange(1, 14)
        y = random.randrange(1, 14)
        z = random.randrange(1, 14)
        play_war(x,y,z)
        return"""
        Testing"""


@simple_route("/goto/Throne/goto/<where>")
def new_conflict(world: dict, where: str) -> str:
    """
    resolve one of the gods' conflicts from the throne room. Travel to either Ares
    and Athena, Aprhodite and Hera, or Persephone and Hades
    :param world: the current world
    :param where: the new place to travel to
    :return: the HTML to show the player
    """
    if where == "Battlefield":
        x = random.randrange(1, 14)
        y = random.randrange(1, 14)
        z = random.randrange(1, 14)
        return GAME_HEADER+ """
           You found the battlefield of Ares and Athena. <br>
           Now you must beat them at a classic game of war <br>
           in order to prove who is stronger. <br>
           <input type ="button" value="Play War" onclick="play_war(x,y,z)"> """

           

    if where == "Pageant":
        return GAME_HEADER + """
        Hera and Aphrodite each believe they are the most beautiful. <br>
        Whoever wins their contest receives a golden apple symbolizing <br>
        their brilliance. <br>
        Collect all the golden apples so you can prove you are the best looking <br>
        and end the goddesses' dispute.
        """
    if where == "Underworld":
        return GAME_HEADER + """
        Hades kidnapped Persephone and forces her to stay in the Underworld <br>
        for four months out of the year, which causes winter. <br>
        She only has to come back because she eats 4 pomegranate <br>
        seeds each time, representing the four months she must stay. <br>
        Find and take Hades' stash of pomegranate seeds so Persephone <br>
        can return to Earth and has no reason to overthrow Hades. <br>
        """


@simple_route("/save/name/")
def save_name(world: dict, monsters_name: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name

    return GAME_HEADER+"""You are in {where}, and you are nearby {monster_name}
    <br><br>
    <a href='/'>Return to the start</a>
    """.format(where=world['location'], monster_name=world['name'])


def play_war (x: int, y: int, z: int) -> str:
    a = random.randrange(1, 14)
    b = random.randrange(1, 14)
    c = random.randrange(1, 14)
    if x == y == z:
        return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""WAR!!<br>
        """

    elif x == y:
        if z > x and z > y:
            return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""<br>
            
            Ares won and now his ego is too big. <br>
            <a href='/goto/Battlefield/'> Try again </a>
            """
        else:
            return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""
            WAR!!<br>""" + play_war(a,b,0)
    elif x == z:
        if y > x and y > z:
            return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""<br>

            Athena won and now her ego is too big. <br>
            <a href='/goto/Battlefield/'> Try again </a>
            """
        else:
            return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""
            <br>WAR!!<br>""" + play_war(a, 0, c)
    elif y == z:
        return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""
        You lost.
        <a href='/goto/Battlefield/'> Try again </a>
        """
    elif x > y and x > z:
        return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""
        <br> You won!! Ares and Athena have been defeated by <br>
        a mere mortal. They don't have the will to keep fighting. <br>
        Now it's time to stop the other gods.
        <a href="/goto/Throne/goto/Pageant/"> Stop Aphrodite and Hera second.</a><br>
        <a href="/goto/Throne/goto/Underworld/"> Stop Persephone and Hades second.</a>"""
    elif y > z and y > x:
        return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""<br>
            
            Ares won and now his ego is too big. <br>
            <a href='/goto/Battlefield/'> Try again </a>
            """
    elif z > x and z > y:
        return"""You: """ + str(x) + """<br>Athena: """ + str(y) + """<br>Ares: """ + str(z) +"""<br>

            Athena won and now her ego is too big. <br>
            <a href='/goto/Battlefield/'> Try again </a>
            """


