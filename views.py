from route_helper import simple_route
from flask import render_template
import random

@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template('home.html')

@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    """
    Update the player location and encounter a monster, prompting the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """

    if where == "Earth":
        return render_template("Earth.html")

    if where == "Throne":
        return render_template('Throne.html')

    if where == "war":
        x = random.randrange(2, 15)
        y = random.randrange(2, 15)
        z = random.randrange(2, 15)
        return render_template("War.html", header="Playing War") + play_war(x, y, z, world["tasks"])

    if where == "apples":
        return render_template("apples.html", num_of_apples=world["apples"], tasks=world["tasks"], inventory=world["inventory"],
                               enlarge=world['enlarge'], header="Collect the Golden Apples")
    if where == "ladder":
        world["inventory"].append("ladder")
        return render_template("apples.html", num_of_apples=world["apples"], tasks=world["tasks"], inventory=world["inventory"],
                               enlarge=world['enlarge'], header="Collect the Golden Apples")
    if where == "hammer":
        world["inventory"].append("hammer")
        return render_template("apples.html", num_of_apples=world["apples"], tasks=world["tasks"], inventory=world["inventory"],
                               enlarge=world['enlarge'], header="Collect the Golden Apples")
    if where == "magnifier":
        world["inventory"].append("magnifier")
        return render_template("apples.html", num_of_apples=world["apples"], tasks=world["tasks"], inventory=world["inventory"],
                               enlarge=world['enlarge'], header="Collect the Golden Apples")
    if where == "enlarge":
        world['enlarge'] = True
        return render_template("apples.html", num_of_apples=world["apples"], tasks=world["tasks"], inventory=world["inventory"],
                               enlarge=world['enlarge'], header="Collect the Golden Apples")
    if where == "seeds":
        return render_template("seeds.html",num_of_seeds=world["seeds"], tasks=world["tasks"], header="Collect the Seeds")
    if where == "end":
        return render_template("end.html")


@simple_route("/goto/Throne/goto/<where>")
def new_conflict(world: dict, where: str) -> str:
    """
    resolve one of the gods' conflicts from the throne room. Travel to either Ares
    and Athena, Aphrodite and Hera, or Persephone and Hades.

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
    """
    Navigates through the Aphrodite and Hera mini-game based
    on the number of apples that have been collected.

    :param world: the current world
    :param num: the current number of apples collected
    :return: the HTML to show the player
    """
    if int(num) == 4:
        world["tasks"][1] = True
        # signifies completing the Aphrodite and Hera mini-game
    world["apples"] = int(num)
    return render_template("apples.html", num_of_apples=world["apples"], tasks=world["tasks"], inventory=world["inventory"],
                               enlarge=world['enlarge'], header="Collect the Golden Apples")

@simple_route("/goto/seeds/goto/<num>")
def increment_seeds(world: dict, num: str) -> str:
    """
    Navigates through the Persephone and Hades mini-game based
    on the number of seeds that have been collected.
    :param world: the current world
    :param num: the current number of seeds collected
    :return: the HTML to show the player
    """
    if int(num) == 4:
        world["tasks"][2] = True
        # signifies completing the Persephone and Hades mini-game
    if int(num) == 3:
        return render_template("seeds_3.html")
    else:
        world['seeds'] = int(num)
        x = random.randrange(1,1500)
        y = random.randrange(1,500)
        return render_template("seeds.html", num_of_seeds=world['seeds'], tasks=world["tasks"], quiz=world["quiz"], x_pixel=x, y_pixel=y, header="Collect the Seeds")

@simple_route("/goto/seeds/goto/2/<num>")
def new_quiz(world: dict, num: str) -> str:
    """
    Navigates through the quiz section of the Persephone and Hades mini-game based
    on the number of quizzes that have been completed.

    :param world: the current world
    :param num: the current number of quizzes completed
    :return: the HTML to show the player
    """
    world["quiz"] = int(num)
    return render_template("seeds.html", num_of_seeds=world["seeds"], tasks=world["tasks"], quiz=world["quiz"], header="Collect the Seeds")


def play_war(x: int, y: int, z: int, tasks: [bool]) -> str:
    """
    Compares card values in the war mini-game.

    :param x: Player's card value
    :param y: Athena's card value
    :param z: Ares' card value
    :param tasks: Currently completed mini-games
    :return: HTML to show the player
    """
    a = random.randrange(2, 15)
    b = random.randrange(2, 15)
    c = random.randrange(2, 15)
    display = render_template("display_results.html", x=str(x), y=str(y), z=str(z))
    if x == y == z:
        return display + """WAR!!<br>""" + play_war(a, b, c, tasks)
    elif x == y:
        if z > x:
            return display + render_template("/War_Outcomes/Ares_wins.html")
        else:
            return display + """WAR!!<br>""" + play_war(a, b, 0, tasks)
    elif x == z:
        if y > x:
            return display + render_template("/War_Outcomes/Athena_wins.html")
        else:
            return display + """WAR!!<br>""" + play_war(a, 0, c, tasks)
    elif y == z:
        if x > y:
            tasks[0] = True
            # signifies completing the Ares and Athena mini-game
            return display + check_tasks(tasks)
        else:
            return display + render_template("/War_Outcomes/Loss.html")
    elif x > y and x > z:
        tasks[0] = True
        return display + check_tasks(tasks)
    elif y > z and y > x:
        return display + render_template("/War_Outcomes/Athena_wins.html")
    elif z > x and z > y:
        return display + render_template("/War_Outcomes/Ares_wins.html")


def check_tasks(tasks: [bool]) -> str:
    """
    Checks how many mini-games are currently completed
    to determine the links that will appear after completing the war mini-game.

    :param tasks: The currently completed mini-games
    :return: HTML to show the player
    """
    if (not tasks[1]) and (not tasks[2]):
        return render_template("/War_Outcomes/win_options/war_first.html")
    if tasks[1] and (not tasks[2]):
        return render_template("/War_Outcomes/win_options/pageant_war.html")
    if (not tasks[1]) and tasks[2]:
        return render_template("/War_Outcomes/win_options/underworld_war.html")
    if tasks[1] and tasks[2]:
        return render_template("/War_Outcomes/win_options/war_last.html")

