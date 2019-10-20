from route_helper import simple_route
from flask import render_template
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
    for task in tasks:
        tasks[tasks.index(task)] = False
    if "hammer" in inventory:
        inventory.remove("hammer")
    if "ladder" in inventory:
        inventory.remove("ladder")
    if "magnifier" in inventory:
        inventory.remove("magnifier")
    apples[0] = 0
    seeds[0] = 0
    quiz[0] = 0
    enlarge[0] = False
    return render_template('home.html')


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
        return render_template("Earth.html", )
    if where == "Throne":
        return render_template('Throne.html')
    if where == "Vault Gate":
        return GAME_HEADER + """
        """
    if where == "war":
        tasks[0] = True
        x = random.randrange(2, 15)
        y = random.randrange(2, 15)
        z = random.randrange(2, 15)
        return render_template("war.html",header="Playing War") + play_war(x, y, z)
    if where == "apples":
        tasks[1] = True
        return render_template("apples.html", num_of_apples=apples[0], tasks=tasks, inventory=inventory,
                               enlarge=enlarge[0], header="Collect the Golden Apples")
    if where == "ladder":
        inventory.append("ladder")
        return render_template("apples.html", num_of_apples=apples[0], tasks=tasks, inventory=inventory,
                               enlarge=enlarge[0], header="Collect the Golden Apples")
    if where == "hammer":
        inventory.append("hammer")
        return render_template("apples.html", num_of_apples=apples[0], tasks=tasks, inventory=inventory,
                               enlarge=enlarge[0], header="Collect the Golden Apples")
    if where == "magnifier":
        inventory.append("magnifier")
        return render_template("apples.html", num_of_apples=apples[0], tasks=tasks, inventory=inventory,
                               enlarge=enlarge[0], header="Collect the Golden Apples")
    if where == "enlarge":
        enlarge[0] = True
        return render_template("apples.html", num_of_apples=apples[0], tasks=tasks, inventory=inventory,
                               enlarge=enlarge[0], header="Collect the Golden Apples")
    if where == "seeds":
        tasks[2] = True
        return render_template("seeds.html",num_of_seeds=seeds[0],tasks=tasks, header="Collect the Seeds")
    if where == "end":
        return render_template("end.html")


@simple_route("/goto/Throne/goto/<where>")
def new_conflict(world: dict, where: str) -> str:
    """
    resolve one of the gods' conflicts from the throne room. Travel to either Ares
    and Athena, Aphrodite and Hera, or Persephone and Hades
    :param world: the current world
    :param where: the new place to travel to
    :return: the HTML to show the player
    """
    if where == "Battlefield":
        return render_template("Battlefield.html")
    if where == "Pageant":
        return render_template("Pageant.html")
    if where == "Underworld":
        return render_template("Underworld.html")

@simple_route("/goto/apples/<num>")
def increment_apples(world: dict, num: str) -> str:
    apples[0] = int(num)
    return render_template("apples.html", num_of_apples=apples[0], tasks=tasks, inventory=inventory,
                               enlarge=enlarge[0], header="Collect the Golden Apples")

@simple_route("/goto/seeds/goto/<num>")
def increment_seeds(world: dict, num: str) -> str:
    if int(num) == 3:
        return render_template("seeds_3.html")
    else:
        seeds[0] = int(num)
        x = random.randrange(1,1500)
        y = random.randrange(1,500)
        return render_template("seeds.html", num_of_seeds=seeds[0], tasks=tasks, quiz=quiz[0], x_pixel=x, y_pixel=y, header="Collect the Seeds")

@simple_route("/goto/seeds/goto/2/<num>")
def new_quiz(world: dict, num: str) -> str:
    quiz[0] = int(num)
    return render_template("seeds.html", num_of_seeds=seeds[0], tasks=tasks, quiz=quiz[0], header="Collect the Seeds")






@simple_route("/save/name/")
def save_name(world: dict, monsters_name: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name

    return GAME_HEADER + """You are in {where}, and you are nearby {monster_name}
    <br><br>
    <a href='/'>Return to the start</a>
    """.format(where=world['location'], monster_name=world['name'])


def play_war(x: int, y: int, z: int) -> str:
    a = random.randrange(2, 15)
    b = random.randrange(2, 15)
    c = random.randrange(2, 15)
    if x == y == z:
        return display_results(x, y, z) + """
        
        WAR!!<br>
        """ + play_war(a, b, c)

    elif x == y:
        if z > x:
            return display_results(x, y, z) + """
            
            Ares won and now his ego is too big. <br><br>
            <input type ="button" class="btn btn-outline-danger" value="Try Again" onclick=window.location.href=window.location.href>
            """
        else:
            return display_results(x, y, z) + """
            WAR!!<br>""" + play_war(a, b, 0)
    elif x == z:
        if y > x:
            return display_results(x, y, z) + """

            Athena won and now her ego is too big. <br><br>
            <input type ="button" class="btn btn-outline-danger" value="Try Again" onclick=window.location.href=window.location.href>
            """
        else:
            return display_results(x, y, z) + """
            WAR!!<br>""" + play_war(a, 0, c)
    elif y == z:
        return display_results(x, y, z) + """
        You lost.<br><br>
        <input type ="button" class="btn btn-outline-danger" value="Try Again" onclick=window.location.href=window.location.href>
        """
    elif x > y and x > z:
        if not tasks[1] and not tasks[2]:
            return display_results(x, y, z) + """
        
            You won!! Ares and Athena have been defeated by <br>
            a mere mortal. They don't have the will to keep fighting. <br>
            Now it's time to stop the other gods.<br><br>
            <div class = "btn-group-vertical">
                <a class="btn btn-outline-primary" role="button" href="/goto/Throne/goto/Pageant"> Stop Aphrodite and Hera second.</a>
                <a class="btn btn-outline-primary" role="button" href="/goto/Throne/goto/Underworld"> Stop Persephone and Hades second.</a>
            </div>"""
        if tasks[1] and not tasks[2]:
            return display_results(x, y, z) + """

            You won!! Ares and Athena have been defeated by <br>
            a mere mortal. They don't have the will to keep fighting. <br>
            Now it's time to stop the other gods.<br><br>
            <a class="btn btn-outline-primary" role="button" href="/goto/Throne/goto/Underworld"> Stop Persephone and Hades third.</a>"""
        if not tasks[1] and tasks[2]:
            return display_results(x, y, z) + """

            You won!! Ares and Athena have been defeated by <br>
            a mere mortal. They don't have the will to keep fighting. <br>
            Now it's time to stop the other gods.<br><br>
            <a class="btn btn-outline-primary" role="button" href="/goto/Throne/goto/Pageant"> Stop Aphrodite and Hera third.</a>"""
        if tasks[1] and tasks[2]:
            return display_results(x, y, z) + """

            You won!! Ares and Athena have been defeated by <br>
            a mere mortal. They don't have the will to keep fighting. <br><br>
            You have resolved all conflicts. Report to Zeus. <br><br>
            <a class="btn btn-outline-primary" role="button" href="/goto/end">Go home</a>"""
    elif y > z and y > x:
        return display_results(x, y, z) + """
            
        Athena won and now her ego is too big. <br>
        <input type ="button" class="btn btn-outline-danger" value="Try Again" onclick=window.location.href=window.location.href>
        """
    elif z > x and z > y:
        return display_results(x, y, z) + """

        Ares won and now his ego is too big. <br>
        <input type ="button" class="btn btn-outline-danger" value="Try Again" onclick=window.location.href=window.location.href>
        """


def display_results(x: int, y: int, z: int) -> str:
    return """
            <table class="table table-dark">
                <tbody>
                    <tr> 
                        <td><img class="rounded" src="/static/images/""" + str(x) + """.png" height="200" width="150"><br></td>
                        <td><img class="rounded" src="/static/images/""" + str(y) + """.png" height="200" width="150"><br></td>
                        <td><img class="rounded" src="/static/images/""" + str(z) + """.png" height="200" width="150"><br></td>
                    </tr>    
                </tbody>    
            </table>        
            """

seeds = [0]
apples = [0]
quiz = [0]
tasks = [False, False, False]
enlarge = [False]
inventory = []
