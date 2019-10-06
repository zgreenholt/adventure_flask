from route_helper import simple_route

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
    if where == "Battlefield":
        return GAME_HEADER+"""
        """
    if where == "Pageant":
        return GAME_HEADER+"""
        """
    if where == "Underworld":
        return GAME_HEADER+"""
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


